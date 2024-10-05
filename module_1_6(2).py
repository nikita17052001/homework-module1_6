my_dict = {'Nikita': 2001, 'Alex': 1996}
print(my_dict)
print(my_dict.get('Alex'))
print(my_dict.get('Olga'))
my_dict.update({'Asya': 2000, 'Denis': 1995})
print(my_dict)
a = my_dict.pop('Nikita')
print(a)
print(my_dict)
my_set = {1, 2, 3, False, 17.15, 'I like to learn Python', 1, 2, 3, 17.15}
print(my_set)
my_set.add(5)
my_set.update((5, 9, 4, 5.6))
my_set.discard(False)
print(my_set)

