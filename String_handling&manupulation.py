# title function for string
name = "vishnulal"
formatted_name =name.title()
print(formatted_name)


#replace in string
location="tvm"
new_location=location.replace("tvm","kollam")
print(new_location)

# split used in strings
message="your booking id is : USR123.keep it safe"
booking_id=message.split(":")[1].split(".")[0].strip()
print(booking_id)
# here i have used strip also

# using if in strings
promo_msg="use zomato100 to get the discound"
if "zomato100" in promo_msg:
    print("offer applied")

# findfunction in String (the position)
feedback="the driver was polite and the trip was smooth"
print(f"the position is {feedback.find("smooth")}")


# important in string 
name="vishnu lal"
intial= "".join([word[0].upper() for word in name.split()])
print(intial)

# for the above we have used forloop in a line so writr for loop first the write the balance before it 


# cleaning the string 
# strip function is used

dirty_string ="       hello      "
print(f"the cleaned string is {dirty_string.strip()}")


# counting the length 

words="the trip was amazing and the car was amazing"
word=len(words.split())
print(word)