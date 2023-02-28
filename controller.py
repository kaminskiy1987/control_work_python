import function
import view


def runProgram():
    choice_user = ''

    while choice_user != '7':
        view.menu()
        choice_user = input().strip()

        if choice_user == '1':
            function.show('all')
        if choice_user == '2':
            function.add()
        if choice_user == '3':
            function.show('all')
            function.id_operation('del')
        if choice_user == '4':
            function.show('all')
            function.id_operation('edit')
        if choice_user == '5':
            function.show('date')
        if choice_user == '6':
            function.show('id')
            function.id_operation('show')
        if choice_user == '7':
            view.finishing()

            break
