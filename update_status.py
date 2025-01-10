# Запрашиваем текущий статус заметки
current_status = input('Текущий статус заметки: ')
print(current_status)

# Запрашиваем новый статус заметки и проверяем его корректность
print('Выберете новый статус заметки:')
note_status = {
    1: 'Выполнено',
    2: 'В процессе',
    3: 'Отложено'
}

# Отображаем доступные статусы
for number, status in note_status.items():
    print(f'{number} - {status}')

while True:
    try:
        choice = int(input("Ваш выбор: "))
        if choice in note_status:
            # Получаем новый статус
            new_status = note_status[choice]
            # Выходим из цикла, так как выбор корректен
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите номер из списка.")
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите число.")

# Обновляем статус
current_status = new_status

# Отображаем обновленный статус
print(f'\nСтатус заметки успешно обновлён на: "{current_status}"')