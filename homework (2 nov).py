fruit = {"orange","mango","watermelon","grapes","blueberry"}
print (fruit)


colors = ['red','blue','green','yellow','purple']
print ("first color:",colors[0])
print ("third color:",colors[2]) 
print ("last color:",colors[-1])


numbers =[10,20,30,40,50]
#change the 10 into 25
numbers[1] = 25
#add 60 to end of the list
numbers.append(60)
#print the modifies list
print ("modified list:",numbers)


names = ['alice', 'bob', 'charlie', 'david', 'emma']
#creating a new list subset containing only the first three names.
subset = names[:3]
print ("subset:",subset)



numbers = list(range(1,11))
print(f"{numbers} squared is: {numbers * 2}")




#list
shopping_cart =[]
shopping_cart.append('milk')
shopping_cart.append('bread')
shopping_cart.append('eggs')
shopping_cart.extend( ['butter', 'cheese'] )
print("shopping_cart:", shopping_cart)


numbers = [45,22,88,56,92,33]
max_value = max(numbers)
min_value = min(numbers)
print("list of numbers:",numbers)
print("maximum value:",max_value)
print("minimum value:",min_value)


letters = ['a','b','a','c','b','a','d']
count_a = letters.count('a')
print("print list of letters:", letters)
print("occurence of'a':",count_a)


squares_of_evens = [x**2 for x in range(11) if x % 2 == 0]
print(squares_of_evens)




numbers =[1,2,2,3,4,4,5,6,6,7]
unique_numbers_set= set(numbers)
print("unique elements(set()):", unique_numbers_set)
