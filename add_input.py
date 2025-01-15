from datetime import datetime

created_date_input = input('Введите дату создания заметки: ')
issue_date_input = input ('Введите дату изменения заметки: ')

created_date = datetime.strptime(created_date_input, "%d.%m.%y")
issue_date = datetime.strptime(issue_date_input, "%d.%m.%y")

temp_created_date = created_date.strftime("%d.%m")
temp_issue_date = issue_date.strftime("%d.%m")

title=input('Введите заголовок заметки: ')

content=input('Введите содержание заметки: ')

print("\nИнформация о заметке:")
print(f"Заголовок: {title}")
print(f"Содержание: {content}")
print(f"Дата создания: {temp_created_date}")
print(f"Дата изменения: {temp_issue_date}")
