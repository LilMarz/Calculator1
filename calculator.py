#It will calculate few calculations lol
#Hello this is Aarosh coming from out of the water
#Imagine not being in Summa
#Imagine not having much leg hair
#Imagine being Ian Bunyan

def division():
    num = int(input("pls give a number lol "))
    num_2 = int(input("another one pls "))
    if num_2 == 0 or num_2 < 0:
        num_2 = int(input("pls give another number cuz that number is dogwater like u"))
    num_answer = num / num_2
    print("ur hot mama cita answer will be... ", num_answer)

def float_division():
    num = float("pls give a number lol ")
    num_2 = float("another one pls ")
    if num_2 == 0 or num_2 < 0:
        num_2 = int(input("pls give another number cuz that number is dogwater like u"))
    num_answer = num / num_2
    print("Your bruh moment be like... ", num_answer)

while True:
    num_calculator = input("hi i am nerdy guy do u wanna give me hot mama cita equation and i will solve like joe he he ha ha?")
    if num_calculator == "no":
        break
    elif num_calculator == "yes":
        num_operator = input("give me a operator wait does this seem familiar??? scratch reference???")
        if num_operator == "div":
            division()
        elif num_operator == "float_div":
            float_division()
        else:
            break