#creating an empty list
my_list =[]

#appending 10, 20, 30, 40
for i in range (10,50,10):
	my_list.append(i)
print(my_list)

#inserting 15 in second position 
my_list.insert(1, 15)
print (my_list)

#extending list with another list
second_list =[50,60,70]
my_list.extend(second_list)
print(my_list)

#removing last number 70
my_list.pop()
print(my_list)
#sorting list in ascending order
my_list.sort()
print(my_list)

# find and print 30 and it's index
while 30 in my_list:
	print(my_list.index(30))
	break