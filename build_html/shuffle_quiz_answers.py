#!/usr/bin/env python3
"""
Shuffle quiz answer options to eliminate answer position bias.

This script randomizes the order of answer options (A, B, C, D) in quiz.md files
while updating the Answer Key to reflect the new correct answer positions.

Supports two Answer Key formats:
1. Table format: | 1 | B | explanation |
2. List format: 1. **B** - explanation
"""

import re
import random
from pathlib import Path


def parse_quiz(content: str) -> tuple[list[dict], dict, str, str, str, str]:
    """
    Parse quiz content and return:
    - questions: list of question dicts with options
    - answer_key: dict mapping question_num -> (correct_letter, explanation)
    - before_questions: content before first question
    - answer_key_format: 'table' or 'list'
    - answer_key_header: header lines of answer key section
    - after_answer_key: content after answer key
    """
    lines = content.split('\n')
    
    questions = []
    current_question = None
    answer_key = {}
    answer_key_format = 'table'  # default
    
    before_questions = []
    after_answer_key = []
    in_questions = False
    in_answer_key = False
    after_answer_key_done = False
    answer_key_header = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check for question start
        question_match = re.match(r'^## Question (\d+):\s*(.*)$', line)
        if question_match:
            in_questions = True
            if current_question:
                questions.append(current_question)
            
            current_question = {
                'num': int(question_match.group(1)),
                'title': question_match.group(2),
                'content_lines': [],
                'options': {},
                'options_order': [],
            }
            i += 1
            continue
        
        # Check for answer key header
        if '## Answer Key' in line:
            if current_question:
                questions.append(current_question)
                current_question = None
            in_answer_key = True
            answer_key_header.append(line)
            i += 1
            continue
        
        # Parse answer key rows
        if in_answer_key and not after_answer_key_done:
            # Table header/separator lines
            if line.startswith('|') and ('---' in line or '# ' in line.lower() or 'answer' in line.lower()):
                answer_key_header.append(line)
                i += 1
                continue
            
            # Answer row format 1 (table): | 1 | B | explanation |
            answer_match = re.match(r'^\|\s*(\d+)\s*\|\s*([A-D])\s*\|\s*(.+?)\s*\|?\s*$', line)
            if answer_match:
                answer_key_format = 'table'
                q_num = int(answer_match.group(1))
                letter = answer_match.group(2)
                explanation = answer_match.group(3)
                answer_key[q_num] = (letter, explanation)
                i += 1
                continue
            
            # Answer row format 2 (list): 1. **B** - explanation
            answer_match2 = re.match(r'^(\d+)\.\s*\*\*([A-D])\*\*\s*[-–—]\s*(.+)$', line)
            if answer_match2:
                answer_key_format = 'list'
                q_num = int(answer_match2.group(1))
                letter = answer_match2.group(2)
                explanation = answer_match2.group(3)
                answer_key[q_num] = (letter, explanation)
                i += 1
                continue
            
            # Check if we're done with answer key
            if answer_key and line.strip() == '---':
                after_answer_key_done = True
                after_answer_key.append(line)
                i += 1
                continue
            
            # Empty lines in answer key
            if line.strip() == '':
                if answer_key:
                    # Check if more answer rows follow
                    has_more = False
                    for j in range(i+1, min(i+5, len(lines))):
                        if re.match(r'^\|\s*\d+\s*\|', lines[j]) or re.match(r'^\d+\.\s*\*\*[A-D]\*\*', lines[j]):
                            has_more = True
                            break
                    if not has_more:
                        after_answer_key_done = True
                        after_answer_key.append(line)
                        i += 1
                        continue
                i += 1
                continue
        
        if after_answer_key_done:
            after_answer_key.append(line)
            i += 1
            continue
        
        # Before questions section
        if not in_questions and not in_answer_key:
            before_questions.append(line)
            i += 1
            continue
        
        # Inside a question - parse options or content
        if current_question:
            option_match = re.match(r'^([A-D])\)\s*(.*)$', line)
            if option_match:
                letter = option_match.group(1)
                text = option_match.group(2)
                current_question['options'][letter] = text
                current_question['options_order'].append(letter)
            else:
                if line.strip() == '---':
                    pass
                elif not current_question['options']:
                    current_question['content_lines'].append(line)
        
        i += 1
    
    return (questions, answer_key, '\n'.join(before_questions), 
            answer_key_format, '\n'.join(answer_key_header), '\n'.join(after_answer_key))


def shuffle_question_options(question: dict, correct_letter: str) -> tuple[dict, str]:
    """Shuffle options for a question and return new correct letter."""
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


def rebuild_quiz(questions: list[dict], answer_key: dict, before: str, 
                 answer_format: str, answer_header: str, after: str) -> str:
    """Rebuild quiz content from parsed components."""
    lines = []
    
    # Before questions
    lines.append(before)
    
    # Questions
    for q in questions:
        lines.append(f"## Question {q['num']}: {q['title']}")
        lines.append('')
        
        for content_line in q['content_lines']:
            lines.append(content_line)
        
        for letter in ['A', 'B', 'C', 'D']:
            if letter in q['options']:
                lines.append(f"{letter}) {q['options'][letter]}")
                lines.append('')
        
        lines.append('---')
        lines.append('')
    
    # Answer Key
    lines.append('---')
    lines.append('')
    lines.append('## Answer Key')
    lines.append('')
    
    if answer_format == 'table':
        lines.append('| # | Answer | Explanation |')
        lines.append('|---|--------|-------------|')
        for q_num in sorted(answer_key.keys()):
            letter, explanation = answer_key[q_num]
            lines.append(f'| {q_num} | {letter} | {explanation} |')
    else:  # list format
        for q_num in sorted(answer_key.keys()):
            letter, explanation = answer_key[q_num]
            lines.append(f'{q_num}. **{letter}** - {explanation}')
    
    lines.append('')
    lines.append(after.lstrip('\n'))
    
    return '\n'.join(lines)


def process_quiz_file(filepath: Path) -> bool:
    """Process a single quiz file and shuffle answers."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    questions, answer_key, before, answer_format, answer_header, after = parse_quiz(content)
    
    if not questions:
        print(f"  ⚠️  No questions found")
        return False
    
    if not answer_key:
        print(f"  ⚠️  No answer key found")
        return False
    
    new_answer_key = {}
    for q in questions:
        if q['num'] not in answer_key:
            print(f"  ⚠️  Question {q['num']} not in answer key")
            continue
        
        correct_letter, explanation = answer_key[q['num']]
        
        if len(q['options']) != 4:
            print(f"  ⚠️  Question {q['num']} has {len(q['options'])} options, skipping")
            new_answer_key[q['num']] = (correct_letter, explanation)
            continue
        
        new_options, new_correct = shuffle_question_options(q, correct_letter)
        q['options'] = new_options
        new_answer_key[q['num']] = (new_correct, explanation)
    
    new_content = rebuild_quiz(questions, new_answer_key, before, answer_format, answer_header, after)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True


def get_answer_distribution(directory: Path) -> dict:
    """Get distribution of correct answers across all quizzes."""
    distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    
    for quiz_file in directory.rglob('quiz.md'):
        with open(quiz_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Table format
        matches = re.findall(r'\|\s*\d+\s*\|\s*([A-D])\s*\|', content)
        for letter in matches:
            distribution[letter] += 1
        
        # List format
        matches = re.findall(r'^\d+\.\s*\*\*([A-D])\*\*\s*[-–—]', content, re.MULTILINE)
        for letter in matches:
            distribution[letter] += 1
    
    return distribution


def main():
    import sys
    random.seed(42)
    
    workspace = Path('/Users/rasul/workspace/ls/CourseBuilder')
    
    # Allow specifying a target directory as argument
    if len(sys.argv) > 1:
        target_dir = Path(sys.argv[1])
        if not target_dir.is_absolute():
            target_dir = workspace / sys.argv[1]
        if not target_dir.exists():
            print(f"❌ Directory not found: {target_dir}")
            sys.exit(1)
        print(f"🎯 Target: {target_dir}")
    else:
        target_dir = workspace
    
    print("📊 Before shuffle:")
    before = get_answer_distribution(target_dir)
    total_before = sum(before.values())
    for letter, count in sorted(before.items()):
        pct = count / total_before * 100 if total_before > 0 else 0
        print(f"   {letter}: {count:4d} ({pct:5.1f}%)")
    
    print("\n🔀 Shuffling quizzes...")
    
    quiz_files = list(target_dir.rglob('quiz.md'))
    processed = 0
    
    for quiz_file in sorted(quiz_files):
        relative_path = quiz_file.relative_to(workspace) if str(quiz_file).startswith(str(workspace)) else quiz_file
        print(f"   Processing {relative_path}...", end='')
        if process_quiz_file(quiz_file):
            processed += 1
            print(" ✓")
        else:
            print()
    
    print(f"\n✅ Processed {processed}/{len(quiz_files)} quiz files")
    
    print("\n📊 After shuffle:")
    after = get_answer_distribution(target_dir)
    total_after = sum(after.values())
    for letter, count in sorted(after.items()):
        pct = count / total_after * 100 if total_after > 0 else 0
        print(f"   {letter}: {count:4d} ({pct:5.1f}%)")


if __name__ == '__main__':
    main()
