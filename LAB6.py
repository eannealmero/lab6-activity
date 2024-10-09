age = int(input("Enter your age: "))
mem = input("Are you already a member?(yes/no): ")
choice1 = "yes"
choice2 = "no"


if age <18:
    if mem == choice1 :
        print("Thank you for being a member! Your fee is 450.00 pesos.")
    if mem == choice2 :
        print("Your fee is 650.00 pesos. Please consider being a member. Thank you.")

elif age >=18 and age <=65:
    if mem == choice1 :
        print("Thank you for being a member! Your fee is 550.00 pesos.")
    if mem == choice2 :
        print("Your fee is 750.00 pesos. Please consider being a member. Thank you.")
        
elif age >=66 and age <=120:
    if mem == choice1 :
        print("Thank you for being a member! Your fee is 400.00 pesos.")
    if mem == choice2 :
        print("Your fee is 600.00 pesos. Please consider being a member. Thank you.")
        
else:
    print("We are sorry to inform you but your age is not appropriate to join our fitness club.")