def word_count(s):
          l=s.split()
          print("The number of words in the sentence :",len(l))
          return
def  longest_word(s):
          l=s.split()
          length=0
          temp=""
          for k in l:
                    if len(k) >= length:
                              length = len(k)
                              temp = k
          print("The longest word in the sentence is",temp,"with",length,"letters.")
          return
def reverse(s):
          new_string=""
          for k in range(len(s)-1,-1,-1):
                    new_string+=s[k]
          print("Reversed Sentence : ",new_string)
          return
def prime_check(n):
          if n<0:
                    print(n,"is not a positive integer!")
                    return
          if n==1 or n==0:
                    print(n, "is neither prime nor composite.")
                    return
          for k in range(2,n):
                    if n%k == 0:
                              print(n, "is a composite number.")
                              return
          else:
                    print(n, "is a prime number.")

s=input("Enter a sentence : ")
word_count(s)
longest_word(s)
reverse(s)
n= int(input("Enter an integer: "))
prime_check(n)

