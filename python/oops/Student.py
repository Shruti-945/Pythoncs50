class Student:
  #__init__= initialization method for objects,self=ref variable i think
  #always take atleast 1 argument self
  def __init__(self,name,house):      #if u don't want house,then house=none
    if not name:
      raise ValueError("Missing name")        #raise for exceptions
    self.name=name
    self.house=house        #we use house,not _house to check with setter
#  ...                #placeholder
  def __str__(self):
    return f"{self.name} from {self.house}"
  
  @property
  def name(self):
    return self._name

  @name.setter
  def name(self,name):
    if not name:
      raise ValueError("Missing name")
    self._name=name  
  #for error correction,use getter and setter
  #Getter
  @property
  def house(self):
    return self._house

  #Setter
  @house.setter
  def house(self,house):
    if house not in ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]:
      raise ValueError("Invalid House")
    self._house=house    #instanc evariable and function cannot be the same name so setter is changed



def main():
  student= get_student()

#setter will raise error if we maliciously change house
  student.house="Number Four,Privet Drive"    #if we use student._house here it will work even with the setter
  print(student)        #__str__ called bcoz ref sent
  #print(f"{student.name} from {student.house}")
    #print(f"{student['name']} from {student['house']}")        #in f string don't use " " both out and in
  
  
  #below for list or tuple
  
  # if student[0]=="Padma":
  #   student[1]="Ravenclaw"
  #print(f"{student[0]} from {student[1]}")
def get_student():
  name=input("Name: ")
  house=input("House: ")
 
#  try:
  return Student(name,house)
  # except ValueError:
  #   ...




    # name=input("Name: ")
    # house=input("House: ")
    # return {"name": name, "house": house}

    
    
    # name=input("Name: ")
    # house=input("House: ")
    # #can return both with dictionary or list or tuple
    #return [name,house]     this is a list         
    #return (name,house)      #this is one value which is a tuple(immutable)

if __name__=="__main__":
  main()