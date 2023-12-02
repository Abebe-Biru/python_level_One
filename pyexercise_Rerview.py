# Commented tasks for you to complete
#################################
####### Problem 1 ######
# given the string
s = 'distributed-systems'

# use the indexing to print out the following

print(s[11])  # '-'

print(s)  # 's'

print(s[:12])  # 'distributed-'
print(s[0:12])  # 'distributed-'

print(s[:4])  # 'dist'
print(s[0:4])  # 'dist'

print(s[11:16])  # '-syst'

# Bonus : Use indexing to reverse the string
print(s[::-1])  # 'smetsys-detubirtsid'

#########################
##### Problem 2 #########
#########################
# given this nested list
list = [4, 5, [1, 4, 'hello']]

# reassign "hello" to be "goodbye"
list[2][2] = 'goodbye'
print(list)  # [4, 5, [1, 4, 'goodbye']]

###############################
########## Problem 3 ##########
###############################
# using keys and indexing, grab the 'hello' from the following dictionaries
d1 = {'simple_key': 'hello'}
d2 = {'k1': {'k2': 'hello'}}
d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}  # grab 'hello'
print(d1['simple_key'])  # 'hello'
print(d2['k1']['k2'])  # 'hello'
print(d3['k1'][0]['nest_key'][1][0])  # 'hello'

############################
######## Problem 4 #########

# Use a set to find the unique values of the list below
mylist = [1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3]

print(set(mylist))  # {1, 2, 3}

#################################
########### Problem 5 ###########
#################################

# You are given two variables
age = 4
name = "Ford-ds"
# use print formatting to print the following string:
"hello my dog's name is Ford-ds and he is 4 years old"

print("hello my dog's name is {} and he is {} years old".format(name, age))  #OR
print(f"hello my dog's name is {name} and he is {age} years old")
