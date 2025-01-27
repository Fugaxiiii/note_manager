def save_notes_to_file(notes, filename):
    with open(filename, 'w') as file:
        for note in notes:
            file.write(f"Имя пользователя: {note['username']}\n")
            file.write(f"Заголовок: {note['title']}\n")
            file.write(f"Описание: {note['content']}\n")
            file.write(f"Статус: {note['status']}\n")
            file.write(f"Дата создания: {note['created_date']}\n")
            file.write(f"Дедлайн: {note['issue_date']}\n")
            file.write("---\n")