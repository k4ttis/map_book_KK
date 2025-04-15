# moja_lista_na_sok:list = ['banan']
# print(moja_lista_na_sok)
# moja_lista_na_sok.append('marchew')
# print(moja_lista_na_sok)

users: list = [
    {'name': 'Maciej', 'location': 'Łódź', 'posts': 100},

]

print(users)
def add_user(users_data:list)->None:
    new_name:str=input('podaj imię nowego znajomego: ')
    new_location:str=input('podaj lokalizację: ')
    new_posts:str=input('podaj liczbę postów: ')
    users.append({'name': new_name, 'location': new_location, 'posts': new_posts},)



add_user(users)
print(users)
