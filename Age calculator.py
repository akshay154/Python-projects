#Take users name as input
name = input("Enter your name :\n")

#take users birth year as input and convert it into an integer
year =int (input("Year of birth:\n"))

#calculate age and convert it into string
age =str(int(2020 - year))

#printing the calculated age of user
print("========================================")
print("Hello "+name+ "!" + " you are now "+ age + " years old ||" )
print("========================================")

#takes input to exit 
input("press enter to quit")

