from datetime import datetime

def update_note(note):
    # Получаем текущую дату
    current_date = datetime.now()
    print("Текущая дата:", current_date.strftime("%d-%m-%Y"))

    print('-----Обновление заметки-----')
    print('Текущая заметка:')
    for key, value in note.items():
        print(f'{key} : {value}')

    updatable_data = ['username', 'title', 'content', 'status',
                      'creation_date', 'issue_date']

    while True:
        note_changer = input('Какие данные вы хотите обновить?'
                             '(username, title, content, status,'
                             'creation_date, issue_date): ')
        if note_changer not in updatable_data:
            print('Ошибка, пожалуйста, выберете поле из списка.')
            continue

        new_value = input('Введите новое значение: ')

        if note_changer in ['creation_date', 'issue_date']:
            try:
                # Пробуем преобразовать строку в дату
                new_value = datetime.strptime(new_value, "%d-%m-%Y").strftime("%d-%m-%Y")
            except ValueError:
                print("Некорректный формат даты. Пожалуйста, введите дату в формате день-месяц-год.")
                continue

        note[note_changer] = new_value
        print(f'Значение {note_changer} обновлено на: {new_value}')

        # Спрашиваем, хочет ли пользователь продолжить обновление
        continue_update = input('Хотите ли вы обновить еще что-то? (да/нет): ')
        if continue_update.lower() != 'да':
            break

    return note

if __name__ == "__main__":
    note = {
        "username": "Ангелина",
        "title": "Список покупок",
        "content": "Лимоны",
        "status": "новая",
        "creation_date": "16-01-2025",
        "issue_date": "19-01-2025"
    }
    updated_note = update_note(note)
    print('Обновленная заметка:', updated_note)