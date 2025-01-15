from datetime import datetime

def create_note():
    # Получаем текущую дату
    current_date = datetime.now()
    print("Текущая дата:", current_date.strftime("%d-%m-%Y"))

    while True:
        try:
            # Запрашиваем у пользователя данные для заметки
            name = input("Введите имя пользователя: ")
            title = input("Введите заголовок заметки: ")
            description = input("Введите описание заметки: ")

            status_list = ["новая", "в процессе", "выполнено"]
            status = ""
            while status not in status_list:
                status = input(f"Введите статус заметки ({', '.join(status_list)}): ")
                if status not in status_list:
                    print('Пожалуйста, введите статус заметки из перечисленных (новая, в процессе, выполнено)')

            creation_date = input("Введите дату создания (день-месяц-год): ")
            try:
                # Проверка формата даты создания
                datetime.strptime(creation_date, "%d-%m-%Y")
            except ValueError:
                print("Некорректный формат даты создания. Пожалуйста, введите дату в формате день-месяц-год.")
                continue

            issue_date = input("Введите дату дедлайна (день-месяц-год): ")
            try:
                # Проверяем формат даты дедлайна
                datetime.strptime(issue_date, "%d-%m-%Y")
            except ValueError:
                print("Некорректный формат даты дедлайна. Пожалуйста, введите дату в формате день-месяц-год.")
                break

            except ValueError:
                print("Некорректный формат даты. Пожалуйста, введите дату в формате день-месяц-год.")

            note = {
                "Имя": name,
                "Заголовок": title,
                "Описание": description,
                "Статус": status,
                "Дата создания": creation_date,
                "Дата дедлайна": issue_date
            }
            return note

        except Exception as e:
            print(f"Произошла ошибка: {e}")

# Вызов функции для проверки дедлайна
if __name__ == "__main__":
    note = create_note()
    print("Заметка создана:", note)