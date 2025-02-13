#variables

my_variable='My String variable'
my_bool_variable=True

print(my_bool_variable)

print(my_variable)


print(my_variable, my_bool_variable, 'holi')

print(len(my_variable))

print(len('andres'))




#variables de una sola linea
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS' , 'JS', 'React', 'Python' ]
person_info = ['Name:', first_name, 
               'Last Name:', last_name,
               'Country:', country, 
               'City:', city, 
               'Age:', age, 
               'Married?', is_married, 
               'Skills:', skills]

print(person_info)

first_name=input('Cual es tu nombre?')
age=input('Cual es tu edad?')

print('Hola', first_name, 'tu edad es', age)