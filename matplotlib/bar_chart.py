import matplotlib.pyplot as plt

x=["APPLE","ORANGE","GRAPE"]
Y=[25,15,35]

plt.bar(x,Y,color="green")
plt.title("a simple bar chart")
plt.xlabel("Items")
plt.ylabel("count")
plt.show()