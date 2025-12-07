def show_info(*args, **kwargs):
    print('>>> Info')
    for value in args:
        print(value)

    print('\n')
    print('>>> Detail')
    for key, values in kwargs.items():
        print(key, values)


show_info(
    'Cody', 'Facilito', 12, 'cody@codigofacilito.com',
    courses= ['Python', 'Django', 'Flask'],
    score= 10,
    active=True,
    is_super_admin=True
)