import csv

students=[]

with open("students.csv") as file:
  #reader=csv.reader(file)
  #for name,home in reader:
  reader=csv.DictReader(file)        #dictreader returns dictionary
  for row in reader:
    #students.append({"name":row["name"],"home":row["home"]})
     students.append(row)               
  # for line in file:
  #   name,home=line.rstrip().split(",")
  #   student={"name":name,"home":home}
  #   students.append(student)
    
    
    #students.append(f"{name} is in {home}")
    # student["name"]=name
    # student["home"]=home

# def get_name(student):
#   return student["name"]

# def get_home():
#   return student["home"]
#    lambda=anonymous function              
for student in sorted(students,key=lambda student:student["name"]):
  print(f"{student['name']} is in {student['home']}")
    

    
    #print(f"{name} is in {home}")