#List Comprehension - Numbers
numbers = [1,2,3,4]
#new_list = [new_item for item in list]
new_list = [n+1 for n in numbers]
print(new_list)

#List Comprehension - Alphabets / Strings
alpha = "Angela"
#new_list = [new_item for item in list]
new_alpha = [n for n in alpha]
print(new_alpha)

#List Comprehension Challenge - Double (*2)
#new_list = [new_item for item in list]
new_lists = [num*2 for num in range(1,5)]
print(new_lists)

#Conditional List Comprehension Challenge
names_list = ["Javed","Sajid","Naveed","Shafi","Saba","Faizan","Junaid","Danish","Rehan","Akshay"]
#new_list = [new_item for item in list if test]
#Should contain Names only if len(name) is < 5
new_names1 = [n for n in names_list if len(n) < 5]
print(new_names1)


#Conditional List Comprehension Challenge - Lower Case
names_list = ["Javed","Sajid","Naveed","Shafi","Saba","Faizan","Junaid","Danish","Rehan","Akshay"]
#new_list = [new_item for item in list if test]
#Should contain Names only if len(name) is > 5
new_names2 = [n.lower() for n in names_list if len(n) > 5]
print(new_names2)
