def save_notes_to_file(notes, filename):
    try:
        with open(filename, 'w') as file:
            for note in notes:
                file.write(f"Имя пользователя: {note['username']}\n")
                file.write(f"Заголовок: {note['title']}\n")
                file.write(f"Описание: {note['content']}\n")
                file.write(f"Статус: {note['status']}\n")
                file.write(f"Дата создания: {note['created_date']}\n")
                file.write(f"Дедлайн: {note['issue_date']}\n")
                file.write("---\n")
    except Exception as e:
        print(f"Ошибка при записи в файл {filename}: {e}")


def load_notes_from_file(filename):
    notes = []

    try:
        with open(filename, 'r') as file:
            content = file.read().strip()
            if content:
                entries = content.split('---\n')
                for entry in entries:
                    lines = entry.strip().split('\n')
                    if len(lines) >= 6:
                        note = {
                            'username': lines[0].split(': ')[1],
                            'title': lines[1].split(': ')[1],
                            'content': lines[2].split(': ')[1],
                            'status': lines[3].split(': ')[1],
                            'created_date': lines[4].split(': ')[1],
                            'issue_date': lines[5].split(': ')[1],
                        }
                        notes.append(note)
                    else:
                        print(f"Ошибка при чтении файла {filename}. Проверьте его содержимое.")
            else:
                print(f"Файл {filename} пуст.")
    except FileNotFoundError:
        print(f"Файл {filename} не найден. Создан новый файл.")
        open(filename, 'w').close()  # Создание нового файла
    except Exception as e:
        print(f"Ошибка при чтении файла {filename}: {e}")

    return notes