

def q1(): 
   x = input("In: ")
if x[-1] == "y" :
    print("-ies")
elif x[-2] == "ey" :
    print("-eys")
elif x[-3:] == "ife":
    print("-ives")
else: 
    print("-s")


def q2(): 
  num = int(input("In: "))
  if num > 0:
    print(f"{num} is positive")
  elif num == 0:
    print("(no output for zero)")
  else :
    print(f"{num} is negative")
def q3(): 
 



#Do not alter the following code
#Comment out the following code when running your tests

q1()
q2()
