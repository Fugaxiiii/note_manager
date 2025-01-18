def search_notes(notes, keyword=None, status=None):

    # Проверка на пустой список заметок
    if not notes:
        print("Список заметок пуст.")
        return []

    # Список для хранения найденных заметок
    filtered_notes = []

    for note in notes:
        # Проверка на наличие ключевого слова в заголовке, содержимом или имени пользователя
        match_keyword = (keyword.lower() in note['title'].lower() or
                         keyword.lower() in note['content'].lower() or
                         keyword.lower() in note['username'].lower()) if keyword else True

        # Проверка на совпадение статуса
        match_status = (note['status'] == status) if status else True

        # Если оба условия совпадают, добавляем заметку в список
        if match_keyword and match_status:
            filtered_notes.append(note)

    # Вывод результатов
    if not filtered_notes:
        print("Заметки, соответствующие запросу, не найдены.")
    else:
        print("Найдены заметки:")
        for index, note in enumerate(filtered_notes, start=1):
            print(f"Заметка №{index}:")
            print(f"Имя пользователя: {note.get('username', 'Не указано')}")
            print(f"Заголовок: {note.get('title', 'Не указан')}")
            print(f"Описание: {note.get('content', 'Не указано')}")
            print(f"Статус: {note.get('status', 'Не указан')}")
            print("------------------------------")


# Пример работы функции
if __name__ == "__main__":
    notes = [
        {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая',
         'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
        {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе',
         'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
        {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено',
         'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
    ]

    # 1. Поиск по ключевому слову
    print("Поиск по ключевому слову:")
    search_notes(notes, keyword='покупок')

    # 2. Поиск по статусу
    print("\nПоиск по статусу:")
    search_notes(notes, status='в процессе')

    # 3. Поиск по ключевому слову и статусу
    print("\nПоиск по ключевому слову и статусу:")
    search_notes(notes, keyword='работы', status='выполнено')

    # 4. Проверка на пустой список заметок
    print("\nПроверка на пустой список:")
    search_notes([], keyword='покупок')
