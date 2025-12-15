#!/usr/bin/env python3
"""
Проверка форматирования Markdown файлов.

Проверяет типичные ошибки:
- Отсутствие пустых строк перед/после заголовков
- Отсутствие пустых строк перед/после блоков кода
- Отсутствие пустых строк между пунктами списка с **bold**
- Отсутствие пустых строк между текстом и списком (списки склеиваются в строку)
- Слипшиеся секции
"""

import os
import re
import sys
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FormatIssue:
    """Проблема форматирования."""
    line_num: int
    issue_type: str
    description: str
    context: str = ""


@dataclass
class FileReport:
    """Отчёт по файлу."""
    filepath: Path
    issues: list[FormatIssue] = field(default_factory=list)
    
    @property
    def has_issues(self) -> bool:
        return len(self.issues) > 0


def get_code_block_ranges(lines: list[str]) -> list[tuple[int, int]]:
    """Находит диапазоны строк внутри блоков кода.
    
    Поддерживает вложенные блоки: ```` может содержать ``` внутри.
    """
    ranges = []
    in_code_block = False
    start = 0
    opening_backticks = 0
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Считаем количество бэктиков в начале строки
        backtick_count = 0
        for char in stripped:
            if char == '`':
                backtick_count += 1
            else:
                break
        
        # Должно быть минимум 3 бэктика
        if backtick_count >= 3:
            if not in_code_block:
                # Открываем блок кода
                in_code_block = True
                start = i
                opening_backticks = backtick_count
            else:
                # Закрываем блок только если количество бэктиков >= opening
                if backtick_count >= opening_backticks:
                    in_code_block = False
                    ranges.append((start, i))
                    opening_backticks = 0
    
    return ranges


def is_in_code_block(line_num: int, ranges: list[tuple[int, int]]) -> bool:
    """Проверяет, находится ли строка внутри блока кода."""
    for start, end in ranges:
        if start < line_num < end:
            return True
    return False


def check_blank_lines_around_headers(lines: list[str], code_ranges: list[tuple[int, int]]) -> list[FormatIssue]:
    """Проверка пустых строк вокруг заголовков."""
    issues = []
    
    for i, line in enumerate(lines):
        # Пропускаем первую строку и строки внутри блоков кода
        if i == 0 or is_in_code_block(i, code_ranges):
            continue
            
        # Если это заголовок (не внутри кода)
        if re.match(r'^#{1,6}\s+', line):
            # Проверяем предыдущую строку (должна быть пустой или начало файла)
            prev_line = lines[i - 1].strip() if i > 0 else ""
            
            # Исключения: начало файла, после ---, после другого заголовка
            if prev_line and prev_line != "---" and not prev_line.startswith('#'):
                issues.append(FormatIssue(
                    line_num=i + 1,
                    issue_type="header_no_blank_before",
                    description="Нет пустой строки ПЕРЕД заголовком",
                    context=f"  {i}: {lines[i-1][:50]}...\n→ {i+1}: {line[:50]}"
                ))
            
            # Проверяем следующую строку (должна быть пустой)
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                # После заголовка должна быть пустая строка ИЛИ другой заголовок ИЛИ ---
                if next_line and not next_line.startswith('#') and next_line != "---":
                    issues.append(FormatIssue(
                        line_num=i + 1,
                        issue_type="header_no_blank_after",
                        description="Нет пустой строки ПОСЛЕ заголовка",
                        context=f"→ {i+1}: {line[:50]}\n  {i+2}: {lines[i+1][:50]}..."
                    ))
    
    return issues


def ends_with_colon(text: str) -> bool:
    """Проверяет, заканчивается ли текст двоеточием (учитывая markdown)."""
    # Убираем trailing markdown форматирование
    text = text.rstrip('*_`')
    return text.endswith(':')


def check_blank_lines_around_code_blocks(lines: list[str]) -> list[FormatIssue]:
    """Проверка пустых строк вокруг блоков кода.
    
    Учитывает вложенные блоки: ```` содержащие ```.
    """
    issues = []
    in_code_block = False
    opening_backticks = 0
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Считаем количество бэктиков в начале строки
        backtick_count = 0
        for char in stripped:
            if char == '`':
                backtick_count += 1
            else:
                break
        
        # Должно быть минимум 3 бэктика
        if backtick_count >= 3:
            if not in_code_block:
                # Открываем блок кода
                in_code_block = True
                opening_backticks = backtick_count
                
                # Проверяем предыдущую строку
                if i > 0:
                    prev_line = lines[i - 1].strip()
                    # Исключения: пустая строка, заголовок, ---, текст с двоеточием на конце
                    if prev_line and not prev_line.startswith('#') and prev_line != "---" and not ends_with_colon(prev_line):
                        issues.append(FormatIssue(
                            line_num=i + 1,
                            issue_type="code_no_blank_before",
                            description="Нет пустой строки ПЕРЕД блоком кода",
                            context=f"  {i}: {lines[i-1][:50]}...\n→ {i+1}: {line[:50]}"
                        ))
            else:
                # Закрываем блок только если количество бэктиков >= opening
                if backtick_count >= opening_backticks:
                    in_code_block = False
                    opening_backticks = 0
                    
                    # Проверяем следующую строку
                    if i + 1 < len(lines):
                        next_line = lines[i + 1].strip()
                        # Исключения: пустая строка, заголовок, ---, **Output:**
                        if next_line and not next_line.startswith('#') and next_line != "---" and not next_line.startswith('**'):
                            issues.append(FormatIssue(
                                line_num=i + 1,
                                issue_type="code_no_blank_after",
                                description="Нет пустой строки ПОСЛЕ блока кода",
                                context=f"→ {i+1}: {line[:50]}\n  {i+2}: {lines[i+1][:50]}..."
                            ))
    
    return issues


def check_bold_list_items(lines: list[str]) -> list[FormatIssue]:
    """Проверка пустых строк между пунктами списка с **bold**."""
    issues = []
    
    for i, line in enumerate(lines):
        # Если это пункт списка с bold: - **Something:**
        if re.match(r'^[-*]\s+\*\*[^*]+\*\*', line) or re.match(r'^[-*]\s+\*\*[^*]+:', line):
            # Проверяем следующую строку
            if i + 1 < len(lines):
                next_line = lines[i + 1]
                # Если следующая строка тоже bold-пункт — нужна пустая строка между ними
                if re.match(r'^[-*]\s+\*\*[^*]+\*\*', next_line) or re.match(r'^[-*]\s+\*\*[^*]+:', next_line):
                    issues.append(FormatIssue(
                        line_num=i + 1,
                        issue_type="bold_list_no_blank",
                        description="Нет пустой строки между bold-пунктами (могут слипнуться)",
                        context=f"→ {i+1}: {line[:50]}...\n  {i+2}: {next_line[:50]}..."
                    ))
    
    return issues


def check_bold_heading_before_list(lines: list[str], code_ranges: list[tuple[int, int]]) -> list[FormatIssue]:
    """Проверка пустой строки между **Bold:** и последующим списком."""
    issues = []
    
    for i, line in enumerate(lines):
        # Пропускаем строки внутри блоков кода
        if is_in_code_block(i, code_ranges):
            continue
        
        stripped = line.strip()
        
        # Паттерн: строка вида **Something:** (bold заголовок)
        if re.match(r'^\*\*[^*]+:\*\*$', stripped):
            # Проверяем следующую строку
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                # Если следующая строка — пункт списка, нужна пустая строка
                if next_line.startswith('-') or next_line.startswith('*') or re.match(r'^\d+\.', next_line):
                    issues.append(FormatIssue(
                        line_num=i + 1,
                        issue_type="bold_heading_no_blank_before_list",
                        description="Нет пустой строки между **Bold:** и списком (список не отрендерится)",
                        context=f"→ {i+1}: {line.strip()}\n  {i+2}: {next_line[:50]}..."
                    ))
    
    return issues


def check_text_colon_before_list(lines: list[str], code_ranges: list[tuple[int, int]]) -> list[FormatIssue]:
    """Проверка пустой строки между обычным текстом и последующим списком."""
    issues = []
    
    for i, line in enumerate(lines):
        # Пропускаем строки внутри блоков кода
        if is_in_code_block(i, code_ranges):
            continue
        
        stripped = line.strip()
        
        # Пропускаем пустые строки, заголовки, списки, блоки кода, разделители
        if (not stripped or 
            stripped.startswith('#') or 
            stripped.startswith('-') or 
            stripped.startswith('*') or 
            stripped.startswith('`') or 
            stripped == "---" or
            re.match(r'^\d+\.', stripped) or
            stripped.startswith('**') and stripped.endswith('**')):
            continue
        
        # Проверяем следующую строку - если это список, нужна пустая строка
        if i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            # Если следующая строка — пункт списка, нужна пустая строка
            if next_line.startswith('-') or next_line.startswith('*') or re.match(r'^\d+\.', next_line):
                issues.append(FormatIssue(
                    line_num=i + 1,
                    issue_type="text_no_blank_before_list",
                    description="Нет пустой строки между текстом и списком (список склеится в строку при сборке HTML)",
                    context=f"→ {i+1}: {line.strip()}\n  {i+2}: {next_line[:50]}..."
                ))
    
    return issues


def check_section_separators(lines: list[str], code_ranges: list[tuple[int, int]]) -> list[FormatIssue]:
    """Проверка пустых строк вокруг --- разделителей."""
    issues = []
    
    for i, line in enumerate(lines):
        # Пропускаем --- внутри блоков кода (YAML document separators и т.п.)
        if is_in_code_block(i, code_ranges):
            continue
            
        if line.strip() == "---":
            # Проверяем предыдущую строку
            if i > 0:
                prev_line = lines[i - 1].strip()
                if prev_line and prev_line != "---":
                    issues.append(FormatIssue(
                        line_num=i + 1,
                        issue_type="separator_no_blank_before",
                        description="Нет пустой строки ПЕРЕД ---",
                        context=f"  {i}: {lines[i-1][:50]}...\n→ {i+1}: ---"
                    ))
            
            # Проверяем следующую строку
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if next_line and next_line != "---":
                    issues.append(FormatIssue(
                        line_num=i + 1,
                        issue_type="separator_no_blank_after",
                        description="Нет пустой строки ПОСЛЕ ---",
                        context=f"→ {i+1}: ---\n  {i+2}: {lines[i+1][:50]}..."
                    ))
    
    return issues


def check_file(filepath: Path) -> FileReport:
    """Проверка одного файла."""
    report = FileReport(filepath=filepath)
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        lines = content.split('\n')
    except Exception as e:
        report.issues.append(FormatIssue(
            line_num=0,
            issue_type="read_error",
            description=f"Ошибка чтения файла: {e}"
        ))
        return report
    
    # Находим диапазоны блоков кода (чтобы игнорировать их содержимое)
    code_ranges = get_code_block_ranges(lines)
    
    # Запускаем все проверки
    report.issues.extend(check_blank_lines_around_headers(lines, code_ranges))
    report.issues.extend(check_blank_lines_around_code_blocks(lines))
    report.issues.extend(check_bold_list_items(lines))
    report.issues.extend(check_bold_heading_before_list(lines, code_ranges))
    report.issues.extend(check_text_colon_before_list(lines, code_ranges))
    report.issues.extend(check_section_separators(lines, code_ranges))
    
    # Сортируем по номеру строки
    report.issues.sort(key=lambda x: x.line_num)
    
    return report


def print_report(report: FileReport, verbose: bool = False):
    """Вывод отчёта по файлу."""
    if not report.has_issues:
        if verbose:
            print(f"✅ {report.filepath}: OK")
        return
    
    print(f"\n❌ {report.filepath}: {len(report.issues)} проблем(а)")
    print("-" * 60)
    
    for issue in report.issues:
        print(f"  Строка {issue.line_num}: {issue.description}")
        if issue.context and verbose:
            for ctx_line in issue.context.split('\n'):
                print(f"    {ctx_line}")
    
    print()


def check_module(module_path: Path, verbose: bool = False) -> int:
    """Проверка модуля (lecture.md и quiz.md)."""
    total_issues = 0
    
    for filename in ['lecture.md', 'quiz.md']:
        filepath = module_path / filename
        if filepath.exists():
            report = check_file(filepath)
            print_report(report, verbose)
            total_issues += len(report.issues)
    
    return total_issues


def check_course(course_path: Path, verbose: bool = False) -> int:
    """Проверка всего курса."""
    total_issues = 0
    
    for item in sorted(course_path.iterdir()):
        if item.is_dir() and item.name[0].isdigit():
            total_issues += check_module(item, verbose)
    
    return total_issues


def main():
    """Главная функция."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Проверка форматирования Markdown')
    parser.add_argument('path', nargs='?', help='Путь к файлу, модулю или курсу')
    parser.add_argument('-v', '--verbose', action='store_true', help='Подробный вывод')
    parser.add_argument('-a', '--all', action='store_true', help='Проверить все курсы')
    
    args = parser.parse_args()
    
    # Определяем путь к курсам
    script_dir = Path(__file__).parent
    courses_path = script_dir.parent / 'Courses'
    
    total_issues = 0
    
    if args.all:
        # Проверяем все курсы
        print("=" * 60)
        print("🔍 Проверка форматирования всех курсов")
        print("=" * 60)
        
        for course_dir in sorted(courses_path.iterdir()):
            if course_dir.is_dir():
                print(f"\n📚 {course_dir.name}")
                total_issues += check_course(course_dir, args.verbose)
    
    elif args.path:
        path = Path(args.path)
        
        if path.is_file():
            # Проверяем один файл
            report = check_file(path)
            print_report(report, args.verbose)
            total_issues = len(report.issues)
        
        elif path.is_dir():
            # Проверяем директорию
            if (path / 'lecture.md').exists():
                # Это модуль
                total_issues = check_module(path, args.verbose)
            else:
                # Это курс
                total_issues = check_course(path, args.verbose)
    
    else:
        parser.print_help()
        return
    
    # Итог
    print("=" * 60)
    if total_issues == 0:
        print("✅ Проблем форматирования не найдено!")
    else:
        print(f"⚠️ Найдено проблем: {total_issues}")
    print("=" * 60)
    
    sys.exit(1 if total_issues > 0 else 0)


if __name__ == '__main__':
    main()

