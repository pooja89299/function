# numbers_list = [1, 2, 3, 4, 5, 6, 7, 10, -2]
# print (max(numbers_list))


# a=[1,2,3,4,5,6]
# print(len(a)) 


# def say_hello(name):
#     print ("Hello ", name)
#     print ("Aap kaise ho?")
# say_hello("Aatif")



#Multiple Function Arguments



#Abhi tak humne ek function argument ke saath hi code likha hai. Ab hum thode aur function arguments ke saath code likhte hain.

# def add_numbers(number1, number2):
#     print ("Main do numbers ko add karunga.")
#     print (number1 + number2)
# add_numbers(120, 50)
# num_x = "134"
# name = "Rinki"
# add_numbers(num_x, name)




# def say_hello_people(name_x, name_y, name_z, name_a):
#     print ("Namaste ", name_x) #hindi mein
#     print ("Alah hafiz ", name_y)  #urdu mein
#     print ("Bonjour ", name_z)  #french mein
#     print ("Hello ", name_a) # english mein
# say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya")
# say_hello_people("Steve", "Saswata", "Shakrundin", "Rajeev")



#Python Arbitrary Arguments


# def icecream(*flavours):
#      for flavour in flavours:
#         print("i love"+flavour)

# icecream("chocolate", "butterscotch","vanilla","strawberry")


#Default parameter value


# def attendance(name,status="absent"):
#     print(name,"is",status," today")

# attendance("kartik","present")
# attendance("sonu")
# attendance("vishal","present")
# attendance("umesh")

# Debug Code
#Ab hum function se related code ko debug karenge.

 
# def greet(*names):
#     for name in names:
#         print("Welcome", name)


# greet("Rinki", "Vishal", "Kartik", "Bijender") 



# def info(name, age  ):
#    print(name + " is " + age + " years old")

# info("Sonu","12")
# info("Sana", "17")
# info("Umesh", "18")


# def studentDetails(name,currentMilestone,mentorName):
#     print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)


# studentDetails("Nilam","loop","riya")


#Question 2

#function_print_lines naam ka ek function likho jo 2 strings 
# leta ho, aur unko neeche diye hue dhang se print karta ho. Jaise agar 
# hum usko "Mera naam Rishabh hai." aur "Main NavGurukul ka co-Founder hun."
#  denge toh woh yeh print karega




# def n(naam,pooja):
#     print(naam)
#     print(pooja)
# n("mera naam Rishabh hai. aur main ","navgurukul ka co-founder hun")