# print even numbers from 1 to 10

num = int(input("enter the number : "))
for i in range(0,num+1):
    if i %2==0:
        print(f" {i}:the number is even")
    