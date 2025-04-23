lst = ['Apple','guava','banana','orange','kiwi']        

print("leangh of list is: ",len(lst)) 
print("first element of list is: ",lst[0])
print("last element of list is: ",lst[-1])

lst.append('mango')
print("updated list is: ",lst)

lst.remove('banana')
print("updated list is: ",lst)

lst.sort()
print("sorted list is: ",lst)

lst.pop(1)
print("updated list is: ",lst)

lst.reverse()
print("reversed list is: ",lst)             


print("multiplication of list is: ",lst*2)          

lst = lst[:4]
print("sliced list is: ",lst)

lst.clear()
print("Updated list is: ",lst)                                  
