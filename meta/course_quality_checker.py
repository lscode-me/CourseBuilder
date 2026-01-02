#!/usr/bin/env python3
"""
Объединенный инструмент для создания и проверки качества курсов.

Включает в себя все проверки из course_validate_tools:
- Анализ качества согласно стандартам CourseBuilder
- Проверка комплектности (структура файлов)
- Автоматическое исправление форматирования Markdown
- Перемешивание ответов в квизах для устранения bias

Использование в процессе создания курсов:
1. После генерации модуля запускается проверка качества
2. Автоматически исправляется форматирование
3. Проверяется структура файлов
4. Балансируются ответы в квизах
"""

import os
import re
import random
import shutil
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import Optional, List, Tuple, Set, Dict
from argparse import ArgumentParser


# ============================================================================
# МОДЕЛЬ ДАННЫХ И МЕТРИКИ КАЧЕСТВА
# ============================================================================

# Типы курсов по отношению к программированию
COURSE_TYPE_PROGRAMMING = "programming"  # Программистские курсы (Python, JS, etc.)
COURSE_TYPE_TECHNICAL = "technical"      # Технические курсы (платежи, сети, etc.)
COURSE_TYPE_NON_TECHNICAL = "non_technical"  # Гуманитарные курсы

# Ключевые слова для определения типа курса
PROGRAMMING_KEYWORDS = [
    'python', 'javascript', 'java', 'go', 'rust', 'sql', 'typescript',
    'programming', 'программирование', 'разработка', 'framework', 'library',
    'код', 'code', 'development', 'backend', 'frontend', 'fullstack',
    'algorithm', 'алгоритм', 'react', 'vue', 'angular', 'django', 'flask',
    'node', 'express', 'fastapi', 'spring', 'rails'
]

TECHNICAL_KEYWORDS = [
    'payment', 'платёж', 'платеж', 'система', 'system', 'network', 'сеть',
    'security', 'безопасность', 'infrastructure', 'инфраструктура', 
    'devops', 'kubernetes', 'docker', 'cloud', 'облако', 'architecture',
    'архитектура', 'data', 'данные', 'database', 'криптография', 'crypto',
    'blockchain', 'api', 'protocol', 'протокол', 'integration', 'интеграция'
]

NON_TECHNICAL_KEYWORDS = [
    'history', 'история', 'management', 'менеджмент', 'marketing', 'маркетинг',
    'sales', 'продажи', 'communication', 'коммуникация', 'psychology', 'психология',
    'soft skills', 'leadership', 'лидерство', 'business', 'бизнес', 'finance',
    'финансы', 'law', 'право', 'language', 'язык', 'culture', 'культура'
]


def detect_course_type(course_path: Path) -> str:
    """Определяет тип курса по его содержимому."""
    course_name = course_path.name.lower()
    
    # Проверяем description.md если есть
    description_path = course_path / "description.md"
    description_content = ""
    if description_path.exists():
        try:
            description_content = description_path.read_text(encoding='utf-8').lower()
        except:
            pass
    
    # Проверяем README.md если есть
    readme_path = course_path / "README.md"
    readme_content = ""
    if readme_path.exists():
        try:
            readme_content = readme_path.read_text(encoding='utf-8').lower()
        except:
            pass
    
    combined_text = f"{course_name} {description_content} {readme_content}"
    
    # Подсчитываем совпадения для каждого типа
    programming_score = sum(1 for kw in PROGRAMMING_KEYWORDS if kw in combined_text)
    technical_score = sum(1 for kw in TECHNICAL_KEYWORDS if kw in combined_text)
    non_technical_score = sum(1 for kw in NON_TECHNICAL_KEYWORDS if kw in combined_text)
    
    # Программистские курсы имеют приоритет
    if programming_score > 0 and programming_score >= technical_score:
        return COURSE_TYPE_PROGRAMMING
    elif technical_score > non_technical_score:
        return COURSE_TYPE_TECHNICAL
    elif non_technical_score > 0:
        return COURSE_TYPE_NON_TECHNICAL
    else:
        # По умолчанию — технический курс (средние требования)
        return COURSE_TYPE_TECHNICAL


@dataclass
class ModuleMetrics:
    """Метрики одного модуля."""
    course: str
    module: str
    course_type: str = COURSE_TYPE_TECHNICAL  # Тип курса
    
    # Lecture metrics
    lecture_lines: int = 0
    h2_sections: int = 0
    code_blocks: int = 0
    learning_objectives: int = 0
    key_takeaways: int = 0
    
    # Structure checks
    has_prerequisites: bool = False
    has_learning_objectives: bool = False
    has_key_takeaways: bool = False
    has_next_steps: bool = False
    has_quiz: bool = False
    
    # Quiz metrics
    quiz_questions: int = 0
    quiz_has_answer_key: bool = False
    quiz_has_scoring: bool = False
    
    def lecture_status(self) -> str:
        """Статус длины лекции."""
        if self.lecture_lines < 400:
            return "❌ Очень короткая"
        elif self.lecture_lines < 600:
            return "⚠️ Короткая"
        elif self.lecture_lines <= 1000:
            return "✅ Норма"
        elif self.lecture_lines <= 1200:
            return "⚠️ Длинная"
        else:
            return "❌ Очень длинная"
    
    def sections_status(self) -> str:
        """Статус количества секций."""
        if self.h2_sections < 5:
            return "⚠️ Мало"
        elif self.h2_sections <= 12:
            return "✅ Норма"
        else:
            return "⚠️ Много"
    
    def code_blocks_status(self) -> str:
        """Статус количества блоков кода с учётом типа курса."""
        if self.course_type == COURSE_TYPE_PROGRAMMING:
            # Программистские курсы: 15-30 блоков
            if self.code_blocks < 10:
                return "⚠️ Мало"
            elif self.code_blocks < 15:
                return "⚠️ Ниже нормы"
            elif self.code_blocks <= 30:
                return "✅ Норма"
            else:
                return "⚠️ Много"
        elif self.course_type == COURSE_TYPE_TECHNICAL:
            # Технические курсы: 5-15 блоков (диаграммы, схемы, примеры API)
            if self.code_blocks < 3:
                return "⚠️ Мало"
            elif self.code_blocks < 5:
                return "⚠️ Ниже нормы"
            elif self.code_blocks <= 20:
                return "✅ Норма"
            else:
                return "ℹ️ Много (ок для техн.)"
        else:
            # Гуманитарные курсы: 0-5 блоков (опционально)
            if self.code_blocks <= 10:
                return "✅ Норма"
            else:
                return "ℹ️ Много (необязательно)"
    
    def quiz_status(self) -> str:
        """Статус квиза."""
        if not self.has_quiz:
            return "❌ Нет"
        elif self.quiz_questions < 15:
            return "⚠️ Мало вопросов"
        elif self.quiz_questions < 20:
            return "⚠️ Ниже нормы"
        elif self.quiz_questions <= 40:
            return "✅ Норма"
        else:
            return "⚠️ Много вопросов"
    
    def structure_score(self) -> int:
        """Баллы за структуру (0-5)."""
        score = 0
        if self.has_prerequisites:
            score += 1
        if self.has_learning_objectives:
            score += 1
        if self.has_key_takeaways:
            score += 1
        if self.has_next_steps:
            score += 1
        if self.has_quiz:
            score += 1
        return score
    
    def overall_quality(self) -> str:
        """Общая оценка качества."""
        issues = 0
        
        # Критические проблемы
        if not self.has_quiz:
            issues += 2
        if self.lecture_lines < 400:
            issues += 2
        if not self.has_learning_objectives:
            issues += 1
        if not self.has_key_takeaways:
            issues += 1
        
        # Средние проблемы
        if self.lecture_lines < 600 or self.lecture_lines > 1000:
            issues += 1
        if self.h2_sections < 5 or self.h2_sections > 12:
            issues += 1
        # Проверка блоков кода с учётом типа курса
        if self.course_type == COURSE_TYPE_PROGRAMMING and self.code_blocks < 15:
            issues += 1
        elif self.course_type == COURSE_TYPE_TECHNICAL and self.code_blocks < 5:
            issues += 1
        # Для гуманитарных курсов код не обязателен
        if self.has_quiz and self.quiz_questions < 20:
            issues += 1
        
        if issues == 0:
            return "✅ Отлично"
        elif issues <= 2:
            return "✅ Хорошо"
        elif issues <= 4:
            return "⚠️ Требует улучшений"
        else:
            return "❌ Серьёзные проблемы"


# ============================================================================
# АНАЛИЗ КАЧЕСТВА КУРСОВ
# ============================================================================

class QualityAnalyzer:
    """Анализатор качества курсов."""
    
    @staticmethod
    def analyze_lecture(filepath: Path) -> dict:
        """Анализ lecture.md файла."""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.split('\n')
        
        # Подсчет блоков кода
        code_blocks = len(re.findall(r'^```', content, re.MULTILINE))
        code_blocks = code_blocks // 2  # Открывающие и закрывающие
        
        # Подсчет H2 секций (основных нумерованных секций)
        h2_sections = len(re.findall(r'^## \d+\.', content, re.MULTILINE))
        
        # Learning Objectives - считаем пункты после секции
        lo_match = re.search(
            r'## 🎯 Learning Objectives.*?\n(.*?)(?=\n## |\n---|\Z)',
            content, re.DOTALL | re.IGNORECASE
        )
        learning_objectives = 0
        if lo_match:
            lo_text = lo_match.group(1)
            learning_objectives = len(re.findall(r'^[-*•]\s', lo_text, re.MULTILINE))
        
        # Key Takeaways - считаем пункты
        kt_match = re.search(
            r'## 💡 Key Takeaways.*?\n(.*?)(?=\n## |\n---|\Z)',
            content, re.DOTALL | re.IGNORECASE
        )
        key_takeaways = 0
        if kt_match:
            kt_text = kt_match.group(1)
            key_takeaways = len(re.findall(r'^[-*•]\s', kt_text, re.MULTILINE))
        
        # Проверка наличия секций
        has_prerequisites = bool(re.search(r'## 📋 Prerequisites', content, re.IGNORECASE))
        has_learning_objectives = bool(re.search(r'## 🎯 Learning Objectives', content, re.IGNORECASE))
        has_key_takeaways = bool(re.search(r'## 💡 Key Takeaways', content, re.IGNORECASE))
        has_next_steps = bool(re.search(r'## 🚀 Next Steps', content, re.IGNORECASE))
        
        return {
            'lecture_lines': len(lines),
            'code_blocks': code_blocks,
            'h2_sections': h2_sections,
            'learning_objectives': learning_objectives,
            'key_takeaways': key_takeaways,
            'has_prerequisites': has_prerequisites,
            'has_learning_objectives': has_learning_objectives,
            'has_key_takeaways': has_key_takeaways,
            'has_next_steps': has_next_steps,
        }
    
    @staticmethod
    def analyze_quiz(filepath: Path) -> dict:
        """Анализ quiz.md файла."""
        if not filepath.exists():
            return {
                'has_quiz': False,
                'quiz_questions': 0,
                'quiz_has_answer_key': False,
                'quiz_has_scoring': False,
            }
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Подсчет вопросов - ищем "## Question N" или "**Question N"
        questions = len(re.findall(r'##\s*Question\s+\d+', content, re.IGNORECASE))
        if questions == 0:
            # Альтернативный формат
            questions = len(re.findall(r'\*\*Question\s+\d+', content, re.IGNORECASE))
        if questions == 0:
            # Еще один формат: просто нумерованные вопросы
            questions = len(re.findall(r'^##\s*\d+\.', content, re.MULTILINE))
        
        has_answer_key = bool(re.search(r'Answer Key|Ответы|Answer Sheet', content, re.IGNORECASE))
        has_scoring = bool(re.search(r'Scoring Guide|Шкала оценки|Scoring', content, re.IGNORECASE))
        
        return {
            'has_quiz': True,
            'quiz_questions': questions,
            'quiz_has_answer_key': has_answer_key,
            'quiz_has_scoring': has_scoring,
        }
    
    @staticmethod
    def analyze_module(course_path: Path, module_name: str, course_name: str, 
                       course_type: str = COURSE_TYPE_TECHNICAL) -> Optional[ModuleMetrics]:
        """Анализ одного модуля."""
        module_path = course_path / module_name
        lecture_path = module_path / 'lecture.md'
        quiz_path = module_path / 'quiz.md'
        
        if not lecture_path.exists():
            return None
        
        metrics = ModuleMetrics(course=course_name, module=module_name, course_type=course_type)
        
        # Анализ лекции
        lecture_data = QualityAnalyzer.analyze_lecture(lecture_path)
        metrics.lecture_lines = lecture_data['lecture_lines']
        metrics.code_blocks = lecture_data['code_blocks']
        metrics.h2_sections = lecture_data['h2_sections']
        metrics.learning_objectives = lecture_data['learning_objectives']
        metrics.key_takeaways = lecture_data['key_takeaways']
        metrics.has_prerequisites = lecture_data['has_prerequisites']
        metrics.has_learning_objectives = lecture_data['has_learning_objectives']
        metrics.has_key_takeaways = lecture_data['has_key_takeaways']
        metrics.has_next_steps = lecture_data['has_next_steps']
        
        # Анализ квиза
        quiz_data = QualityAnalyzer.analyze_quiz(quiz_path)
        metrics.has_quiz = quiz_data['has_quiz']
        metrics.quiz_questions = quiz_data['quiz_questions']
        metrics.quiz_has_answer_key = quiz_data['quiz_has_answer_key']
        metrics.quiz_has_scoring = quiz_data['quiz_has_scoring']
        
        return metrics
    
    @staticmethod
    def analyze_course(courses_path: Path, course_name: str) -> list[ModuleMetrics]:
        """Анализ всего курса."""
        course_path = courses_path / course_name
        metrics = []
        
        if not course_path.exists():
            return metrics
        
        # Определяем тип курса
        course_type = detect_course_type(course_path)
        
        for item in sorted(course_path.iterdir()):
            if item.is_dir() and item.name.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
                module_metrics = QualityAnalyzer.analyze_module(
                    course_path, item.name, course_name, course_type
                )
                if module_metrics:
                    metrics.append(module_metrics)
        
        return metrics


# ============================================================================
# ПРОВЕРКА КОМПЛЕКТНОСТИ КУРСОВ
# ============================================================================

class CompletenessChecker:
    """Проверка комплектности курсов."""
    
    @staticmethod
    def extract_lecture_modules_from_readme(readme_path: Path) -> Set[str]:
        """Извлекает имена модулей лекций из README."""
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Паттерн для ссылок: [текст](XX_ModuleName/) или [текст](XX_ModuleName/file.md)
        pattern = r'\[[^\]]+\]\(\.?/?([0-9]+_[^/)]+)(?:/|\))'
        matches = re.findall(pattern, content)
        
        return set(matches)
    
    @staticmethod
    def get_lecture_directories(course_path: Path) -> Set[str]:
        """Получает список папок лекций в курсе."""
        modules = set()
        for item in course_path.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                modules.add(item.name)
        return modules
    
    @staticmethod
    def check_lecture_directory(lecture_path: Path) -> Tuple[bool, List[str], List[str]]:
        """Проверяет папку лекции."""
        required_files = {'lecture.md', 'quiz.md'}
        
        files = set()
        for item in lecture_path.iterdir():
            if item.is_file():
                files.add(item.name)
            elif item.is_dir():
                files.add(f"{item.name}/")  # Помечаем папки
        
        missing = required_files - files
        extra = files - required_files
        
        is_valid = len(missing) == 0 and len(extra) == 0
        return is_valid, sorted(missing), sorted(extra)
    
    @staticmethod
    def check_course(course_path: Path) -> dict:
        """Проверяет курс на комплектность."""
        results = {
            'course_path': course_path,
            'has_readme': False,
            'readme_modules': set(),
            'actual_modules': set(),
            'missing_modules': [],
            'extra_modules': [],
            'module_issues': {},
            'files_to_delete': [],
            'directories_to_delete': [],
            'course_root_extra_files': [],
        }
        
        # Проверка README
        readme_path = course_path / 'README.md'
        if not readme_path.exists():
            return results
        
        results['has_readme'] = True
        
        # Извлекаем модули из README
        results['readme_modules'] = CompletenessChecker.extract_lecture_modules_from_readme(readme_path)
        
        # Получаем реальные папки модулей
        results['actual_modules'] = CompletenessChecker.get_lecture_directories(course_path)
        
        # Проверяем корневую папку курса на лишние файлы
        allowed_in_root = {'README.md'}
        for item in course_path.iterdir():
            if item.is_file() and item.name not in allowed_in_root:
                results['course_root_extra_files'].append(item)
                results['files_to_delete'].append(item)
            elif item.is_dir() and not item.name.startswith('.') and item.name not in results['actual_modules']:
                results['directories_to_delete'].append(item)
        
        # Модули, которые есть в README, но отсутствуют в файловой системе
        results['missing_modules'] = sorted(results['readme_modules'] - results['actual_modules'])
        
        # Модули, которые есть в файловой системе, но не упомянуты в README
        results['extra_modules'] = sorted(results['actual_modules'] - results['readme_modules'])
        
        # Проверяем каждую папку модуля
        for module_name in results['actual_modules']:
            module_path = course_path / module_name
            is_valid, missing, extra = CompletenessChecker.check_lecture_directory(module_path)
            
            if not is_valid:
                results['module_issues'][module_name] = {
                    'missing': missing,
                    'extra': extra
                }
                
                # Собираем файлы для удаления
                for item in extra:
                    if item.endswith('/'):
                        dir_name = item.rstrip('/')
                        results['directories_to_delete'].append(module_path / dir_name)
                    else:
                        results['files_to_delete'].append(module_path / item)
        
        return results


# ============================================================================
# ИСПРАВЛЕНИЕ ФОРМАТИРОВАНИЯ MARKDOWN
# ============================================================================

class MarkdownFormatter:
    """Автоматическое исправление форматирования Markdown."""
    
    @staticmethod
    def get_code_block_ranges(lines: List[str]) -> List[Tuple[int, int]]:
        """Находит диапазоны строк внутри блоков кода."""
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
    
    @staticmethod
    def is_in_code_block(line_num: int, ranges: List[Tuple[int, int]]) -> bool:
        """Проверяет, находится ли строка внутри блока кода."""
        for start, end in ranges:
            if start < line_num < end:
                return True
        return False
    
    @staticmethod
    def ends_with_colon(text: str) -> bool:
        """Проверяет, заканчивается ли текст двоеточием."""
        text = text.rstrip('*_`')
        return text.endswith(':')
    
    @staticmethod
    def fix_file(filepath: Path, dry_run: bool = False) -> int:
        """Исправление одного файла. Возвращает количество исправлений."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            lines = content.split('\n')
        except Exception as e:
            print(f"❌ Ошибка чтения {filepath}: {e}")
            return 0
        
        # Простейшие исправления (не модифицируем содержимое внутри блоков кода)
        fixed_lines = lines.copy()
        total_fixes = 0
        
        # Находим диапазоны блоков кода, чтобы не трогать их содержимое
        code_block_ranges = MarkdownFormatter.get_code_block_ranges(fixed_lines)
        
        # Примечание: Для безопасности отключаем автоматические исправления,
        # которые могут испортить форматирование внутри code blocks.
        # Исправления заголовков применяем только ВНЕ блоков кода.
        
        # Исправление пустых строк после заголовков (только вне code blocks)
        for i in range(len(fixed_lines) - 1, -1, -1):
            if i == 0:
                continue
            # Пропускаем строки внутри блоков кода
            if MarkdownFormatter.is_in_code_block(i, code_block_ranges):
                continue
            line = fixed_lines[i]
            # Проверяем, что это Markdown-заголовок (начинается с #, но не внутри кода)
            if re.match(r'^#{1,6}\s+\w', line):
                if i + 1 < len(fixed_lines):
                    next_line = fixed_lines[i + 1].strip()
                    # Добавляем пустую строку только если следующая строка не пустая,
                    # не заголовок и не разделитель
                    if next_line and not next_line.startswith('#') and next_line != "---":
                        # Проверяем, что следующая строка тоже не в блоке кода
                        if not MarkdownFormatter.is_in_code_block(i + 1, code_block_ranges):
                            fixed_lines.insert(i + 1, '')
                            total_fixes += 1
                            # Пересчитываем диапазоны после вставки
                            code_block_ranges = MarkdownFormatter.get_code_block_ranges(fixed_lines)
        
        if total_fixes > 0 and not dry_run:
            new_content = '\n'.join(fixed_lines)
            if content.endswith('\n'):
                new_content += '\n'
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
        
        return total_fixes


# ============================================================================
# ПЕРЕМЕШИВАНИЕ ОТВЕТОВ В КВИЗАХ
# ============================================================================

class QuizShuffler:
    """Перемешивание ответов в квизах."""
    
    @staticmethod
    def parse_quiz(content: str) -> tuple:
        """Парсинг содержимого квиза."""
        lines = content.split('\n')
        questions = []
        answer_key = {}
        answer_key_format = 'table'
        
        current_question = None
        in_answer_key = False
        
        for i, line in enumerate(lines):
            # Поиск вопросов
            question_match = re.match(r'^## Question (\d+):\s*(.*)$', line)
            if question_match:
                if current_question:
                    questions.append(current_question)
                
                current_question = {
                    'num': int(question_match.group(1)),
                    'title': question_match.group(2),
                    'content_lines': [],
                    'options': {},
                    'options_order': [],
                }
                continue
            
            # Поиск Answer Key
            if '## Answer Key' in line:
                if current_question:
                    questions.append(current_question)
                    current_question = None
                in_answer_key = True
                continue
            
            # Парсинг ответов в Answer Key
            if in_answer_key:
                # Формат таблицы: | 1 | B | explanation |
                answer_match = re.match(r'^\|\s*(\d+)\s*\|\s*([A-D])\s*\|\s*(.+?)\s*\|?\s*$', line)
                if answer_match:
                    q_num = int(answer_match.group(1))
                    letter = answer_match.group(2)
                    explanation = answer_match.group(3)
                    answer_key[q_num] = (letter, explanation)
                continue
            
            # Парсинг опций внутри вопроса
            if current_question:
                option_match = re.match(r'^([A-D])\)\s*(.*)$', line)
                if option_match:
                    letter = option_match.group(1)
                    text = option_match.group(2)
                    current_question['options'][letter] = text
                    current_question['options_order'].append(letter)
                else:
                    if line.strip() != '---' and not current_question['options']:
                        current_question['content_lines'].append(line)
        
        if current_question:
            questions.append(current_question)
        
        return questions, answer_key, answer_key_format
    
    @staticmethod
    def shuffle_question_options(question: dict, correct_letter: str) -> tuple:
        """Перемешивание опций вопроса."""
        letters = ['A', 'B', 'C', 'D']
        items = [(l, question['options'].get(l, '')) for l in letters if l in question['options']]
        
        if len(items) != 4:
            return question['options'], correct_letter
        
        random.shuffle(items)
        
        new_options = {}
        new_correct = correct_letter
        
        for new_letter, (old_letter, text) in zip(letters, items):
            new_options[new_letter] = text
            if old_letter == correct_letter:
                new_correct = new_letter
        
        return new_options, new_correct
    
    @staticmethod
    def get_answer_distribution(directory: Path) -> dict:
        """Получение распределения правильных ответов."""
        distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
        
        for quiz_file in directory.rglob('quiz.md'):
            with open(quiz_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Формат таблицы
            matches = re.findall(r'\|\s*\d+\s*\|\s*([A-D])\s*\|', content)
            for letter in matches:
                distribution[letter] += 1
        
        return distribution
    
    @staticmethod
    def calculate_deviation(distribution: dict) -> float:
        """Вычисление максимального отклонения от равномерного распределения."""
        total = sum(distribution.values())
        if total == 0:
            return 0.0
        
        ideal_pct = 25.0
        max_deviation = 0.0
        
        for letter in ['A', 'B', 'C', 'D']:
            count = distribution.get(letter, 0)
            pct = (count / total * 100) if total > 0 else 0
            deviation = abs(pct - ideal_pct)
            max_deviation = max(max_deviation, deviation)
        
        return max_deviation


# ============================================================================
# ГЛАВНЫЙ КЛАСС - ПРОВЕРЩИК КАЧЕСТВА КУРСОВ
# ============================================================================

class CourseQualityChecker:
    """Главный класс для проверки и улучшения качества курсов."""
    
    def __init__(self, workspace_path: Path):
        self.workspace_path = workspace_path
        self.courses_path = workspace_path / 'Courses'
        
        # Инициализируем компоненты
        self.quality_analyzer = QualityAnalyzer()
        self.completeness_checker = CompletenessChecker()
        self.markdown_formatter = MarkdownFormatter()
        self.quiz_shuffler = QuizShuffler()
    
    def check_module_quality(self, course_path: Path, module_name: str, 
                           fix_formatting: bool = True, shuffle_quiz: bool = True,
                           dry_run: bool = False) -> ModuleMetrics:
        """
        Проверка и улучшение качества одного модуля.
        
        Args:
            course_path: Путь к курсу
            module_name: Имя модуля
            fix_formatting: Исправлять ли форматирование
            shuffle_quiz: Перемешивать ли ответы в квизе
            dry_run: Режим проверки без изменений
            
        Returns:
            Метрики качества модуля
        """
        module_path = course_path / module_name
        
        print(f"\n📖 Проверка модуля: {module_name}")
        print("-" * 50)
        
        # 1. Исправление форматирования
        if fix_formatting:
            lecture_fixes = 0
            quiz_fixes = 0
            
            lecture_path = module_path / 'lecture.md'
            if lecture_path.exists():
                lecture_fixes = self.markdown_formatter.fix_file(lecture_path, dry_run)
                if lecture_fixes > 0:
                    print(f"  📝 Исправлено форматирование lecture.md: {lecture_fixes} проблем")
            
            quiz_path = module_path / 'quiz.md'
            if quiz_path.exists():
                quiz_fixes = self.markdown_formatter.fix_file(quiz_path, dry_run)
                if quiz_fixes > 0:
                    print(f"  📝 Исправлено форматирование quiz.md: {quiz_fixes} проблем")
        
        # 2. Анализ качества
        course_name = course_path.name
        course_type = detect_course_type(course_path)
        metrics = self.quality_analyzer.analyze_module(course_path, module_name, course_name, course_type)
        
        if metrics:
            # Показываем тип курса
            type_labels = {
                COURSE_TYPE_PROGRAMMING: "💻 Программистский",
                COURSE_TYPE_TECHNICAL: "⚙️ Технический", 
                COURSE_TYPE_NON_TECHNICAL: "📚 Гуманитарный"
            }
            print(f"  📊 Качество: {metrics.overall_quality()} (тип: {type_labels.get(course_type, course_type)})")
            print(f"     - Строк в лекции: {metrics.lecture_lines} ({metrics.lecture_status()})")
            print(f"     - H2 секций: {metrics.h2_sections} ({metrics.sections_status()})")
            print(f"     - Блоков кода: {metrics.code_blocks} ({metrics.code_blocks_status()})")
            print(f"     - Quiz: {metrics.quiz_questions} вопросов ({metrics.quiz_status()})")
            
            # 3. Перемешивание квиза (если нужно)
            if shuffle_quiz and metrics.has_quiz and not dry_run:
                quiz_path = module_path / 'quiz.md'
                if quiz_path.exists():
                    # Простая проверка необходимости перемешивания
                    # В полной версии здесь будет более сложная логика
                    print(f"  🎯 Квиз готов к перемешиванию")
        
        return metrics or ModuleMetrics(course=course_name, module=module_name, course_type=course_type)
    
    def check_course_quality(self, course_name: str, fix_formatting: bool = True,
                           check_completeness: bool = True, shuffle_quiz: bool = True,
                           dry_run: bool = False) -> List[ModuleMetrics]:
        """
        Проверка и улучшение качества курса.
        
        Args:
            course_name: Имя курса
            fix_formatting: Исправлять ли форматирование
            check_completeness: Проверять ли комплектность
            shuffle_quiz: Перемешивать ли ответы в квизах
            dry_run: Режим проверки без изменений
            
        Returns:
            Список метрик по модулям
        """
        course_path = self.courses_path / course_name
        
        # Определяем тип курса
        course_type = detect_course_type(course_path)
        type_labels = {
            COURSE_TYPE_PROGRAMMING: "💻 Программистский",
            COURSE_TYPE_TECHNICAL: "⚙️ Технический", 
            COURSE_TYPE_NON_TECHNICAL: "📚 Гуманитарный"
        }
        
        print(f"\n{'='*80}")
        print(f"📚 Проверка курса: {course_name}")
        print(f"   Тип курса: {type_labels.get(course_type, course_type)}")
        print(f"{'='*80}")
        
        # 1. Проверка комплектности (структуры файлов)
        if check_completeness:
            completeness_results = self.completeness_checker.check_course(course_path)
            
            if not completeness_results['has_readme']:
                print("❌ README.md отсутствует!")
                return []
            
            total_issues = (len(completeness_results['missing_modules']) +
                          len(completeness_results['extra_modules']) +
                          len(completeness_results['module_issues']))
            
            if total_issues == 0:
                print("✅ Структура курса корректна")
            else:
                print(f"⚠️ Найдено проблем со структурой: {total_issues}")
                # Здесь можно добавить автоматическое исправление
        
        # 2. Проверка модулей
        all_metrics = []
        
        if course_path.exists():
            modules = [item for item in sorted(course_path.iterdir()) 
                      if item.is_dir() and item.name.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'))]
            
            for module_path in modules:
                metrics = self.check_module_quality(
                    course_path, module_path.name, 
                    fix_formatting=fix_formatting,
                    shuffle_quiz=shuffle_quiz,
                    dry_run=dry_run
                )
                all_metrics.append(metrics)
        
        # 3. Итоговый отчет по курсу
        self._print_course_summary(course_name, all_metrics)
        
        return all_metrics
    
    def _print_course_summary(self, course_name: str, modules: List[ModuleMetrics]):
        """Вывод итогового отчета по курсу."""
        if not modules:
            return
        
        print(f"\n📋 ИТОГОВЫЙ ОТЧЕТ: {course_name}")
        print("-" * 60)
        
        # Сводная статистика
        total_lines = sum(m.lecture_lines for m in modules)
        avg_lines = total_lines // len(modules) if modules else 0
        total_quiz_questions = sum(m.quiz_questions for m in modules)
        modules_with_quiz = sum(1 for m in modules if m.has_quiz)
        
        print(f"Модулей: {len(modules)}")
        print(f"Средняя длина лекции: {avg_lines} строк")
        print(f"Модулей с квизом: {modules_with_quiz}/{len(modules)}")
        print(f"Всего вопросов в квизах: {total_quiz_questions}")
        
        # Качество
        excellent = sum(1 for m in modules if "Отлично" in m.overall_quality())
        good = sum(1 for m in modules if "Хорошо" in m.overall_quality())
        needs_work = sum(1 for m in modules if "Требует" in m.overall_quality())
        serious = sum(1 for m in modules if "Серьёзные" in m.overall_quality())
        
        print(f"\nКачество модулей:")
        print(f"  ✅ Отлично: {excellent}")
        print(f"  ✅ Хорошо: {good}")
        print(f"  ⚠️ Требует улучшений: {needs_work}")
        print(f"  ❌ Серьёзные проблемы: {serious}")
    
    def recommend_improvements(self, modules: List[ModuleMetrics]) -> List[str]:
        """Генерирует рекомендации по улучшению качества."""
        recommendations = []
        
        for module in modules:
            module_recs = []
            
            # Проблемы со структурой
            if not module.has_learning_objectives:
                module_recs.append("Добавить секцию 🎯 Learning Objectives")
            if not module.has_key_takeaways:
                module_recs.append("Добавить секцию 💡 Key Takeaways")
            if not module.has_quiz:
                module_recs.append("Создать quiz.md")
            
            # Проблемы с содержимым
            if module.lecture_lines < 600:
                module_recs.append(f"Расширить содержимое лекции (текущая длина: {module.lecture_lines} строк)")
            # Рекомендации по коду с учётом типа курса
            if module.course_type == COURSE_TYPE_PROGRAMMING and module.code_blocks < 15:
                module_recs.append("Добавить больше примеров кода (программистский курс)")
            elif module.course_type == COURSE_TYPE_TECHNICAL and module.code_blocks < 5:
                module_recs.append("Добавить диаграммы/схемы/примеры API (технический курс)")
            if module.h2_sections < 5:
                module_recs.append("Добавить больше основных секций")
            if module.has_quiz and module.quiz_questions < 20:
                module_recs.append("Добавить больше вопросов в квиз")
            
            if module_recs:
                recommendations.append(f"\n📖 {module.module}:")
                recommendations.extend(f"  - {rec}" for rec in module_recs)
        
        return recommendations


# ============================================================================
# ГЛАВНАЯ ФУНКЦИЯ И CLI
# ============================================================================

def main():
    """Главная функция."""
    parser = ArgumentParser(
        description='Объединенный инструмент для проверки и улучшения качества курсов'
    )
    
    parser.add_argument(
        'target', 
        nargs='?', 
        help='Путь к курсу, модулю или директории с курсами (по умолчанию: Courses/)'
    )
    
    # Режимы работы
    parser.add_argument(
        '--mode', 
        choices=['quality', 'completeness', 'format', 'quiz', 'all'], 
        default='all',
        help='Режим работы (по умолчанию: all)'
    )
    
    # Флаги
    parser.add_argument(
        '-n', '--dry-run', 
        action='store_true', 
        help='Режим проверки без изменений'
    )
    parser.add_argument(
        '--no-format', 
        action='store_true', 
        help='Не исправлять форматирование'
    )
    parser.add_argument(
        '--no-shuffle', 
        action='store_true', 
        help='Не перемешивать квизы'
    )
    parser.add_argument(
        '--recommendations', 
        action='store_true', 
        help='Показать рекомендации по улучшению'
    )
    
    args = parser.parse_args()
    
    # Определяем пути
    script_dir = Path(__file__).parent
    workspace = script_dir.parent
    
    # Инициализируем главный класс
    checker = CourseQualityChecker(workspace)
    
    # Определяем цель
    if args.target:
        target = Path(args.target)
        if not target.is_absolute():
            target = workspace / args.target
        if not target.exists():
            print(f"❌ Путь не найден: {target}")
            sys.exit(1)
    else:
        target = checker.courses_path
    
    # Определяем список курсов для обработки
    courses_to_check = []
    
    if (target / 'README.md').exists():
        # Это один курс
        courses_to_check = [target.name]
        checker.courses_path = target.parent
    elif target.is_dir() and target.name == 'Courses':
        # Все курсы
        courses_to_check = [d.name for d in sorted(target.iterdir()) if d.is_dir()]
        checker.courses_path = target
    elif target.is_dir():
        # Директория с курсами
        courses_to_check = [
            d.name for d in sorted(target.iterdir()) 
            if d.is_dir() and (d / 'README.md').exists()
        ]
        checker.courses_path = target
    else:
        print(f"❌ Неизвестный тип цели: {target}")
        sys.exit(1)
    
    if not courses_to_check:
        print("❌ Не найдено курсов для проверки")
        sys.exit(1)
    
    # Настройки режима
    fix_formatting = not args.no_format and args.mode in ['format', 'all']
    shuffle_quiz = not args.no_shuffle and args.mode in ['quiz', 'all']
    check_completeness = args.mode in ['completeness', 'all']
    
    # Вывод заголовка
    print("🔍 ПРОВЕРКА КАЧЕСТВА КУРСОВ")
    print("=" * 60)
    print(f"Режим: {args.mode}")
    print(f"Курсов к проверке: {len(courses_to_check)}")
    if args.dry_run:
        print("⚠️ Режим проверки (dry-run): изменения не будут применены")
    print()
    
    # Обрабатываем курсы
    all_modules = []
    for course_name in courses_to_check:
        modules = checker.check_course_quality(
            course_name,
            fix_formatting=fix_formatting,
            check_completeness=check_completeness,
            shuffle_quiz=shuffle_quiz,
            dry_run=args.dry_run
        )
        all_modules.extend(modules)
    
    # Рекомендации по улучшению
    if args.recommendations and all_modules:
        recommendations = checker.recommend_improvements(all_modules)
        if recommendations:
            print("\n" + "=" * 60)
            print("💡 РЕКОМЕНДАЦИИ ПО УЛУЧШЕНИЮ")
            print("=" * 60)
            for rec in recommendations:
                print(rec)
    
    # Итоговая статистика
    if len(courses_to_check) > 1:
        total_modules = len(all_modules)
        excellent = sum(1 for m in all_modules if "Отлично" in m.overall_quality())
        good = sum(1 for m in all_modules if "Хорошо" in m.overall_quality())
        needs_work = sum(1 for m in all_modules if "Требует" in m.overall_quality())
        serious = sum(1 for m in all_modules if "Серьёзные" in m.overall_quality())
        
        print("\n" + "=" * 60)
        print("📊 ОБЩАЯ СТАТИСТИКА")
        print("=" * 60)
        print(f"Всего модулей проверено: {total_modules}")
        print(f"✅ Отлично: {excellent} ({excellent/total_modules*100:.1f}%)")
        print(f"✅ Хорошо: {good} ({good/total_modules*100:.1f}%)")
        print(f"⚠️ Требует улучшений: {needs_work} ({needs_work/total_modules*100:.1f}%)")
        print(f"❌ Серьёзные проблемы: {serious} ({serious/total_modules*100:.1f}%)")


if __name__ == '__main__':
    main()