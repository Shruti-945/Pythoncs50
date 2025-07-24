def main():
     prompt=input().split()
     for word in prompt:
          if word==":)" or word==":(" :
               ind=prompt.index(word)
               prompt[ind]=convert(word)
     for word in prompt:
          print(word,end=" ")



def convert(ch):
      if ch==":(" :
          return"🙁"
      else:
           return "🙂"


main()






