# --------------
# Code starts here

# Create the lists 
class1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class2=['Hilary Mason','Carla Gentry','Corinna Cortes']
# Concatenate both the strings

new_class=class1+class2
# Append the list
new_class.append('Peter Warden')
# Print updated list

print(new_class)
# Remove the element from the list
new_class.remove('Carla Gentry')
# Print the list
print(new_class)


# Create the Dictionary
courses={'Math':65,'English':70,'History':80,'French':70,'Science':60}



# Slice the dict and stores  the all subjects marks in variable
y=[]
for x in courses:
    y.append(courses[x])

# Store the all the subject in one variable `Total`
Total=sum(y)
# Print the total
print(Total)

# Insert percentage formula
percentage=float((Total/500)*100)
# Print the percentage
print(percentage)



# Create the Dictionary
 
mathematics={'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Bengio':50,'Hilary Mason':70,'Carla Gentry':66,'Corinna Cortes':75}


# Given string
topper=max(mathematics,key=mathematics.get)

# Create variable first_name 
first_name,last_name=topper.split()

# Create variable Last_name and store last two element in the list

# Concatenate the string
full_name=last_name+" "+first_name
# print the full_name

#print(full_name)

# print the name in upper case
certificate_name=full_name.upper()
print(certificate_name)
# Code ends here


