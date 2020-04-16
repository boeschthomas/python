#1
def  countDown(num):   # Function with variable num
    newList = []       # Empty list to accept integers
    for i in range(num, -1, -1):  # For loop to loop through range
        newList.append(i)    # instruction to add each looped num to the newList
    return newList           # Returns newList
print(countDown(5))          # calls function and prints result

#2
def print_and_return(list):
    print (list[0])
    return [1]
print (print_and_return([1,2]))  # Got the result but not sure how to tell in the terminal if a value is returned or printed

#3
def first_plus_length(num_list):
    return num_list[0] + len(num_list)
print (first_plus_length([1,2,3,4,5]))

#4
def values_greater_than_second(orig_list):
    new_list = []
    second_val = orig_list[1]
    for idx in range(len(orig_list)):
        if orig_list[idx] > second_val:
            new_list.append(orig_list[idx])

    print(len(new_list))
    return new_list

print(values_greater_than_second([5,2,3,2,1,4]))  # Definitely needed help from the solution for this one. If you just look at the sudo code
                                                  # line by line, it really helps figure it out.

#5
def this_length_that_value(size,value):
    new_list = []
    for num_times in range(size):
        new_list.append(value)
    return new_list

print(this_length_that_value(4,7)) # Needed help with this also but getting a better grip on the proccess.
