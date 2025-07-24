names=[]

with open("names.txt") as file:
  for line in file:
    names.append(line.rstrip())

for name in sorted(names,reverse=True):       #z to a sort
  print(f"hello, {name}")


#with open("names.txt","r") as file:
  
  
  # for line in file:
  #   print("hello," ,line.rstrip())


#   lines=file.readlines()
# for line in lines:
#   print("hello",line.rstrip())      #strip off the end of the line