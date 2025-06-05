# printing the pattern 
import sys
num=int(sys.argv[1])
n=1

for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end="")
    print() 
      