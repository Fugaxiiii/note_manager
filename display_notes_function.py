def display_notes(notes):
    if not notes:
        print("У вас нет сохранённых заметок.")
        return

    print("Список заметок:")
    print("-" * 35)

    for index, note in enumerate(notes, start=1):
        print(f"Заметка №{index}:")
        print(f"Имя пользователя: {note.get('username', 'Не указано')}")
        print(f"Заголовок: {note.get('title', 'Не указан')}")
        print(f"Описание: {note.get('content', 'Не указано')}")
        print(f"Статус: {note.get('status', 'Не указан')}")
        print(f"Дата создания: {note.get('creation_date', 'Не указана')}")
        print(f"Дедлайн: {note.get('issue_date', 'Не указан')}")
        print("-" * 35)

if __name__ == "__main__":
    notes = [{'username': 'Максим', 'title': 'экзамен', 'content': '32 билета', 'status': 'в процессе',
                      'creation_date': '12-01-2025', 'issue_date': '12-02-2025' },
             {'username': 'Алексей', 'title': 'список покупок', 'content': 'хлеб', 'status': 'закончена',
                      'creation_date': '12-01-2025', 'issue_date': '12-02-2025' }]

    display_notes(notes)
