note = []

name = input('Имя пользователя: ')
content = input('Содержание заметки: ')
status = input('Статус: ')
created_date = input('Дата создания заметки: ')
change_date = input('Дата изменения заметки: ')

titles_list = []
for i in range(2):
       title_list = input(f'Заголовок  {i + 1}: ')
       titles_list.append(title_list)

note.append(name)
note.append(content)
note.append(status)
note.append(created_date)
note.append(change_date)
note.append(titles_list)

print("\nДанные о заметке:")
print("Имя пользователя:", note[0])
print("Содержание заметки:", note[1])
print("Статус:", note[2])
print("Дата создания заметки:", note[3])
print("Дата изменения заметки:", note[4])
print("Заголовки:", note[5])