data=["vishnu","blue","python","positivity"]

with open("dta.txt","r") as file:
    content=file.read()

for word in data:
    content=content.replace("[]",word,1)

with open("dta.txt","w") as file:
    file.write(content)