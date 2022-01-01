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