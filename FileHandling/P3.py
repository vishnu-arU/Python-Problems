replacements = [
    "Evermore", "Liora", "Liora", "Whispering Pines",
    "ancient kings and forgotten battles", "lost love and brave hearts",
    "Liora", "enchanted crystals and golden feathers",
    "self-belief and kindness", "walk the path of truth", "Liora"
]


with open("sentence.txt","r") as file:
    content=file.read()

for words in replacements:
    content=content.replace("[]",words,1)

with open("sentence.txt","w") as file:
    file.write(content)
          