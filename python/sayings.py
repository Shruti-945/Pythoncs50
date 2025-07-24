def main():
  hello("world")
  goodbye("world")

def goodbye(name):
  print(f"goodbye, {name}")

def hello(name):
  print(f"hello, {name}")

#__name__=as given main when the file is run from cmd line
if __name__=="__main__":
  main()