#1
x = [ [5,2,3], [10,8,9] ]
x[1][0] = 15     # Index 0 of index 1 in the string
print(x)


students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
students[0]['last_name'] = 'Bryant'   # [0] is the first index in the string
print(students)


sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andfres'
print(sports_directory)


z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)

#2 I could not get this one to work because I was not in the python shell and did not use python3 to run it in the terminal
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterate_dictionary(some_list):
  for curr_dict in some_list:
    display_str = ""
    for curr_key in curr_dict.keys():
        display_str += f"{curr_key} - {curr_dict[curr_key]}"
    display_str = display_str[:len(display_str) - 2]
    print(display_str)   


iterate_dictionary(students)

#3  Figuring these out with the help of the solution code and backing into how the output was derrived.
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterate_dictionary2(key, some_list):
  for curr_dict in some_list:
    print(curr_dict[key])

iterate_dictionary2('first_name', students)
iterate_dictionary2('last_name', students)

#4

# I can not get this one to print out the list of locations
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for key in some_dict.key():
      print(f"{len(some_dict[key])} {key.upper()}")
    for item in some_dict[key]:
      print(item)
    print('\n')

printInfo(dojo)