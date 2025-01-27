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
    except FileNotFoundError:
        pass  # Файл не найден, возвращаем пустой список

    return notes