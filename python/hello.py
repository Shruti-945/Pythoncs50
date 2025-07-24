name=input("What's ur name? ").strip().title()
#we can use these functions with our function also but with strings
print(f"hello,{name}")
#print("hello, " , {name},end="")         #in print func by default end="/n" ,same can be edit as in sep
#print(name)

#print("hello, "friend"")            will give error(for debugging,use '' in start at end)


#z=round(x+y) or round(999+1) will give 1000
#print(f"{z:,}) will give 1,000 thus f strings has more powerful abilities
#z=round(x/y,2) if it is 2/3,it will give 0.67.2 is the upper bound for decimal . rhs digits.
        #or
# print(f"{z:.2f}") will also give 0.67 
# def to create ur own function



#def hello(to="world"):
     #print("hello,",to)

#  hello()
#name=input("What's your name?")
#hello(name)
#we cannot call a topmost function from the bottom so we create a main function at the top and call it at last

#return keyword to return a value 
#n**2 =n^2
#python uses and instead of &&
#bool for boolean True/False

#match number:
#     case 1:
#     print(1)
#     ----
#     case _:
#     print(0)

#match is like switch
# | for or

#no need to initialize a var in python

# try except for exceptions
#NameError is like variable name not defined within the scope
 #or
 # valueerror=value not assigned
