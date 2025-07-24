#sys is a cmd line module in python,there is a variable called sys.argv which represents argument vector which is the list of things typed by the human before they hit enter
import sys
if len(sys.argv)<2:
  sys.exit("Too few arguments")
elif len(sys.argv)>2:
  sys.exit("Too many arguments")
for arg in sys.argv[1:-1]:                   #splicing of list from 1 to end if [1:] but from end to start by [1:-1]-it will exclude last item so nothing will be printed,to print ur name use[1:]
  print("hello,my name is",arg)
  
  #if the name is input in double quotes,the whole thing will be passed as one argument

#   try:
#     print("hello,my name is",sys.argv[1])
#   except IndexError:
#     print(
#       "Too few arguments")

# #sys.argv[0] is the name of program
# print("hello,my name is", sys.argv[0])
# print("hello,my name is", sys.argv[1])



# or better yet,just add this
# name = " ".join(sys.argv[1:])
# print("hello, my name is", name)





