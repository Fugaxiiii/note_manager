# Создание списка для заголовков
list_titles = []

# Цикл по заголовкам
while True:
    # Запрос заголовка
    title = input("Введите заголовок "
                  "(или оставьте пустым для завершения): ")
    # Проверка на пустой ввод
    if title == "":
        # Завершение ввода, если строка пустая
        break

    # Добавление заголовка в список
    list_titles.append(title)

# Вывод списка заголовков заметок
print("\nЗаголовки заметки:")
# Использую enumerate для получения индекса
for idx, title in enumerate(list_titles):
    print(f"- {title}")