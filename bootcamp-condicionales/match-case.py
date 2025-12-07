
def provide_access(user):
    return {
        'username': user,
        'password': 'admin'
    }

user = input('Digite su usuario: ')
#
# match user.lower():
#     case 'ana':
#         print('Ana no tiene acceso a la Base de Datos, solo tiene acceso al Backend.')
#     case 'carlos':
#         print('Carlos no tiene acceso a la base de datos, solo tiene acceso al Frontend.')
#     case 'caro':
#         print('Caro tiene acceso a la Base de Datos.')
#         print(provide_access(user))
#     case _:
#         print('No tiene acceso al sistema.')


# match user:
#    case 'ana' | 'carlos':
#       print('no tienen acceso a la base de datos')


allowed_user = ['caro', 'ana']

match user:
    case user if user in allowed_user:
        print(f'{user} tiene acceso a la Base de Datos.')
        print(provide_access(user))
    case _:
        print(f'{user} no tiene acceso al sistema.')
