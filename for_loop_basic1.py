
# I had to use the solution code to help me with some of these

def basic():
  for x in range(151):
    print(x)

basic()

def multiples_of_five():
  for x in range(5,5005,5):
    print(x)

multiples_of_five()


def the_doj0_way():
  for x in range(1, 101):
    if x % 10 == 0:
      print("Coding Dojo")
    elif x % 5 == 0:
      print("Coding")
    else:
      print(x)

the_dojo_way()

def woah_huge():
   final_sum = 0
   for x in range(1, 5000000, 2):
      final_sum += x
   print(final_sum)

woah_huge()

def countdown_by_fours():
  for x in range(2018, 0, -4):
    print(x)

countdown_by_fours()

def flexible_counter(low_num, high_num, mult):
  for x in range(low_num, high_num + 1):
    if x % mult == 0:
      print(x)

flexible_counter(2, 9, 3)