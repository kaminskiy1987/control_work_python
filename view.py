import model


def create_note(number):
    title = check_text(
        input('Введите Название заметки: '), number)

    body = check_text(
        input('Введите Описание заметки: '), number)

    return model.Note(title=title, body=body)


def menu():
    print(
        "\nЭто программа 'Заметки'. Имеются следующие функции:\n\n1 - вывод всех заметок из файла\n2 - добавление "
        "заметки\n3 - удаление заметки\n4 - редактирование заметки\n5 - выборка заметок по дате\n6 - показать заметку "
        "по id\n7 - выход\n\nВведите номер функции: ")


def check_text(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text


def finishing():
    print("До свидания!")
