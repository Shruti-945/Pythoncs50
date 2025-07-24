# names=[]
# for _ in range(3):
#   names.append(input("What's ur name?"))

# for name in sorted(names):
#   print(f"hello, {name}")
  
name=input("What's ur name?")
#w will open and rewrite the file while a will append but without gaps
with open("names.txt", "a") as file:
  file.write(f"{name}\n")
#file.close()