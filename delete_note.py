from datetime import datetime

def get_date_from_user(prompt):
    #Запрашиваем у пользователя дату в формате день-месяц-год
    # и возвращаем её в формате datetime
    while True:
        try:
            date_str = input(prompt)
            date = datetime.strptime(date_str, "%d-%m-%Y")
            return date.strftime("%d-%m-%Y")
        except ValueError:
            print("Неверный формат даты. Пожалуйста, введите дату в формате день-месяц-год.")

def add_note():
    #Запрашиваем у пользователя данные для новой заметки
    # и возвращаем её в виде словаря
    name = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    description = input("Введите описание заметки: ")
    status = input("Введите статус заметки (новая, в процессе, выполнено): ")
    creation_date = get_date_from_user("Введите дату создания (день-месяц-год): ")
    deadline = get_date_from_user("Введите дедлайн (день-месяц-год): ")

    note = {
        "Имя": name,
        "Заголовок": title,
        "Описание": description,
        "Статус": status,
        "Дата создания": creation_date,
        "Дедлайн": deadline
    }
    return note

def display_notes(notes):
    #Выводит список всех заметок
    print("\nСписок заметок:")
    for index, note in enumerate(notes, start=1):
        print(f"{index}. Имя: {note['Имя']}")
        print(f"   Заголовок: {note['Заголовок']}")
        print(f"   Описание: {note['Описание']}")
        print(f"   Статус: {note['Статус']}")
        print(f"   Дата создания: {note['Дата создания']}")
        print(f"   Дедлайн: {note['Дедлайн']}\n")

def delete_note(notes):
    #Удаляет заметку по имени пользователя или заголовку
    search_term = input("Введите имя пользователя или заголовок для удаления заметки: ").strip().lower()

    # Была ли найдена заметка
    note_found = False

    # Создаем новый список заметок, исключая удаляемую
    updated_notes = []

    for note in notes:
        if note['Имя'].lower() == search_term or note['Заголовок'].lower() == search_term:
            # Заметка найдена
            note_found = True
            print("Успешно удалено.")
        else:
            # Сохраняем заметку в новом списке
            updated_notes.append(note)

    if not note_found:
        print("Заметка не найдена.")

    return updated_notes

def main():
    #Основная функция программы
    print("Добро пожаловать в 'Менеджер заметок'! Вы можете добавить новую заметку.")

    notes = []

    while True:
        note = add_note()
        notes.append(note)

        another = input("Хотите добавить ещё одну заметку? (да/нет): ").strip().lower()
        if another != 'да':
            break

    display_notes(notes)

    # Удаление заметки
    notes = delete_note(notes)

    # Вывод обновленного списка заметок
    display_notes(notes)

if __name__ == "__main__":
    main()