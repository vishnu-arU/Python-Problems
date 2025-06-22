import matplotlib.pyplot as plt
import csv 
months=[]
sales=[]



with open("data.csv","r")as file:
    reader=csv.DictReader(file)
    for row in reader:
        months.append(row['month'])
        sales.append(int(row['sales']))

plt.plot(months,sales,marker='s')
plt.title("sales chart")
plt.xlabel("months")
plt.ylabel("no of sales")
plt.show()