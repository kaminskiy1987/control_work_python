import read_write_operation
import model
import view

number = 10


def add():
    note = view.create_note(number)
    array = read_write_operation.read_file()

    for notes in array:
        if model.Note.get_id(note) == model.Note.get_id(notes):
            model.Note.set_id(note)

    array.append(note)
    read_write_operation.write_file(array, 'a')

    print('Заметка добавлена...')


def show(text):
    is_choice = True
    array = read_write_operation.read_file()

    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')

    for notes in array:
        if text == 'all':
            is_choice = False
            print(model.Note.map_note(notes))
        if text == 'id':
            is_choice = False
            print('ID: ' + model.Note.get_id(notes))
        if text == 'date':
            is_choice = False
            if date in model.Note.get_date(notes):
                print(model.Note.map_note(notes))

    if is_choice:
        print('Нет ни одной заметки...')


def id_operation(text):
    id_input = input('Введите id необходимой заметки: ')
    array = read_write_operation.read_file()
    is_choice = True

    for notes in array:
        if id_input == model.Note.get_id(notes):
            is_choice = False
            if text == 'edit':
                note = view.create_note(number)
                model.Note.set_title(notes, note.get_title())
                model.Note.set_body(notes, note.get_body())
                model.Note.set_date(notes)
                print('Заметка изменена...')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена...')
            if text == 'show':
                print(model.Note.map_note(notes))

    if is_choice:
        print('Такой заметки нет, возможно, вы ввели неверный id')

    read_write_operation.write_file(array, 'a')
