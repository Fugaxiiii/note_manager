import json

def save_notes_json(notes, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:

            json.dump(notes, file, ensure_ascii=False, indent=4)
    except PermissionError:
        print(f"Ошибка: Нет прав для записи в файл '{filename}'.")
    except Exception as e:
        print(f"Произошла ошибка при записи в файл '{filename}': {e}")

if __name__ == '__main__':
    notes_to_save = [
        {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая',
         'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
        {'username': 'Максим', 'title': 'экзамен', 'content': '32 билета', 'status': 'в процессе',
                      'creation_date': '12-01-2025', 'issue_date': '12-02-2025' }
    ]

    save_notes_json(notes_to_save, 'notes.json')