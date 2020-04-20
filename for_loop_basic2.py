#1 Some of these proved to be challenging and I had to reffer to the solution to work some of them out.
def big_size(list):
    for num in range(len(list)):
        if list[num] > 0: 
            list[num] = "Big"
    return list

print(big_size([-1,3,5,-5]))

#2
def count_pos(list):
    count = 0
    for val in list:
        if val > 0:
             count += 1
    list[len(list) - 1] = count
    return list

print(count_pos([-1,1,1,1]))
print(count_pos([1,6,-4,-2,-7,-2]))

#3
def sum_total(list):
    total = 0
    for val in list:
        total += val
    return total

print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))

#4
def average(list):
    total = 0
    for val in list:
        total += val
    return float(total) / float(len(list))

print(average([1,2,3,4]))

#5
def length(list):
        count = 0
        for val in list:
            count += 1
        return count

print(length([4,3,19,24]))
print(length([]))

#6
def minimum(list):
    if len(list) == 0:
        return False
    result = list[0]
    for val in list:
        if val < result:
            result = val
    return result

print(minimum([24,12,6,3,-3]))

#7
def maximun(list):
    if len(list)== 0:
          return False
    result = list[0]
    for val in list:
        if val > result:
            result = val
    return result

print(maximun([24,12,6,3,-3]))
print(maximun([0]))

#8
def ultimate_analysis(list):
    result = {
        'sum_total': None,
        'maximunm': None,
        'minimum': None,
        'average': None,
        'length': 0
    }
    if len(list) == 0:
        return result
    else:
        result['sum_total'] = 0
        result['maximum'] = list[0]
        result['minimum'] = list[0]
    for val in list:
        if val > result['maximum']:
            result['maximum'] = val
        elif val < result['minimum']:
            result['minimum'] = val

        result['sum_total'] += val
        result['length'] += 1
    result['average'] = result['sum_total'] / len(list)

    return result

print(ultimate_analysis([24,12,6,3,-3]))
print(ultimate_analysis([]))


    