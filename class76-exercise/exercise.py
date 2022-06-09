
'''SOMANDO NUMEROS DE LISTAS'''

list1 = [1,2,3,4,5,6,7]
list2 = [1,2,3,4]

'''1° MANEIRA'''

sum_list = []

for i in range(len(list2)):
    sum_list.append(list1[i] + list2[i])
print(sum_list)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

'''2° MANEIRA'''

sum_list2 = []

for i, _ in enumerate(list2):
    sum_list2.append(list1[i] + list2[i])
print(sum_list2)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

'''2° MANEIRA'''

sum_list3 = [x+y for x, y in zip(list1, list2)]
print(sum_list3)

