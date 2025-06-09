# print the squares of the first five numbers

num=int(input("enter the number to fill sqares of : "))

for i in range(1,num+1):
    i=i**2
    print(i, end =" ")

    # simplyfy the steps by
    # print(i**2,end=" ")