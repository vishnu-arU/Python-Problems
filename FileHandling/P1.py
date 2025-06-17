# finding and replacing Words in a file

with open("file.txt","r")as file:
    content = file.read()

    if "[]"in content:
        content=content.replace("[]","vishnu") 
  
with open("file.txt", "w") as file:
    file.write(content)
