import re
name=input("What's your name?").strip()
# := walrus operator
if matches :=re.search(r"^(.+), *(.+)$",name):           #re.search captures using parenthesis,* used for multiple spaces
  name=matches.group(2) + " " +matches.group(1)          #notice here 1 is used as start and not 0 in re
  # last,first=matches.groups()
  # name=f"{first} {last}"


# if "," in name:
#   last,first=name.split(", ")   
#   name=f"{first} {last}"
print(f"hello, {name}")