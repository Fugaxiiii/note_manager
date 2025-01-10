from datetime import datetime

def check_deadline():
        # Получаем текущую дату
        current_date = datetime.now()
        print("Текущая дата:", current_date.strftime("%d-%m-%Y"))

        while True:
            try:
                # Запрашиваем дату дедлайна у пользователя
                deadline_str = input("Введите дату дедлайна (в формате день-месяц-год): ")

                # Преобразуем строку с датой в объект datetime
                deadline_date = datetime.strptime(deadline_str, "%d-%m-%Y")
                # Вычисляем разницу между текущей датой и дедлайном
                time_difference = deadline_date - current_date
                days_difference = time_difference.days

                # Сравниваем даты
                if deadline_date < current_date:
                    # Если дедлайн истёк
                    days_overdue = (current_date - deadline_date).days
                    print(f"Внимание! Дедлайн истёк {days_overdue} дней назад.")
                elif deadline_date > current_date:
                    # Если дедлайн ещё не истёк
                    days_remaining = (deadline_date - current_date).days
                    print(f"До дедлайна осталось {days_remaining} дней.")
                else:
                    # Если дедлайн сегодня
                    print("Дедлайн истекает сегодня!")

                # Прерываем цикл после успешной обработки даты
                break

            except ValueError:
                # Обработка ошибки при неправильном формате даты
                print("Неверный формат даты. "
                      "Пожалуйста, введите дату в формате день-месяц-год.")
            except Exception as e:
                # Обработка прочих ошибок
                print(f"Произошла непредвиденная ошибка: {str(e)}")
                print("Пожалуйста, попробуйте снова.")

# Вызов функции для проверки дедлайна
if __name__ == "__main__":
    check_deadline()