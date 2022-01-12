
#I like to steal your cookies then dip them in the soda dispenser
#Imagine being a bunyan plus going to a school with 21 kids plus having no arm nor leg hair and not being in summa
#Imagine not having leg hair and having only indian friends and being hot
#Imagine not being in summa and using discord during school and being a purid bacha

def addition():
    num = int(input("Give me number pls"))
    num2 = int(input("Give me another number bruh bing chilling sussy boy"))
    numans = num + num2
    return numans


print ("ur hot mama cita answer is", addition())





#It will calculate few calculations lol
#Imagine being Aarosh, or Suhrid or Ekush (IAN)))))))))))))))))))))))))))))))))
#Here is the code that I need to put (btw im doing the division part and the while loop)
def division():
    bruh = int(input("INSERT NUMBER HERE FOR THE NUMERO UNO "))
    bruh_2 = int(input("INSERT NUMBER HERE FOR THE NUMERO DOS "))
    if bruh_2 == 0 or bruh_2 < 0:
        bruh_2 = int(input("INSERT NUMBER HERE FOR THE NUMERO DOS AGAIN"))
    bruh_ans = bruh / bruh_2
    print("Your bruh moment be like... ", bruh_ans)

def float_division():
    bruh = float("INSERT NUMBER HERE FOR THE NUMERO UNO ")
    bruh_2 = float("INSERT NUMBER HERE FOR THE NUMERO DOS ")
    if bruh_2 == 0 or bruh_2 < 0:
        bruh_2 = int(input("INSERT NUMBER HERE FOR THE NUMERO DOS AGAIN"))
    bruh_ans = bruh / bruh_2
    print("Your bruh moment be like... ", bruh_ans)

def age_grade():
    age = int(input("Put in a age between 5 to 11"))
    if age < 5 or age > 11:
        age = int(input("Put in a age between 5 to 11"))
    if age == 5:
        print("The grade level is kindergarten.")
    if age == 6:
        print("The grade level is 1st grade.")
    if age == 7:
        print("The grade level is 2nd grade")
    if age == 8:
        print("The grade level is 3rd grade.")
    if age == 9:
        print("The grade level is 4th grade.")
    if age == 10:
        print("The grade level is 5th grade.")
    if age == 11:
        print("The grade level is 6th grade")

while True:
    bruh_cal = input("Bruh u wanna calculate stuff or nah and btw if u need to divide decimals write float_div")
    if bruh_cal == "nah":
        break
    elif bruh_cal == "yes":
        bruh_operator = input("Which bruh moment operator would u like to use")
        if bruh_operator == "div":
            division()
        elif bruh_operator == "float_div":
            float_division()
        else:
            break

