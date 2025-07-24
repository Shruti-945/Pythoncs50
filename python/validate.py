import re
email = input("What is your email?: ").strip() # Eliminates white (blank) space created by the user
#if re.search(".*@.*",email):           # * can also take 0 repitions so wrong


#if re.search(r".+@.+\.edu",email):      # r asks python not to interpret backslash as sth like \n
#\ (escape character)tells python that . means dot only and not some other characters
#But it will also take sentence

#   OR
#if re.search("..*@..*",email):
              #OR

#if re.search(r"^.+@.+\.edu$",email): 
         #OR


#if re.search(r"^[^@]+@[^@]+\.edu$",email:
#if re.search(r"[a-zA-Z0-9_]+@[a-zA-Z0-9_ ]+\.edu$",email):           #space after underscore in[] or use(\w|\s) to accept space

#if re.search(r"^\w+@\w+\.(com|edu|gov|net)$",email,re.IGNORECASE):

#if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(com|edu|gov|net)$",email,re.IGNORECASE) 

              #OR



if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|gov|net)$",email,re.IGNORECASE) :                       # ()? used so that it can have more than 1 domains(subdomain),everything in()is optional,if we remove() only. is optional
               
  print("Valid")
else:
  print("Invalid")

#           OR
# username,domain=email.split("@")

# if username and domain.endswith(".edu"): 
#   print("Valid")
# else:
#   print("Invalid")


          #OR

# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")
