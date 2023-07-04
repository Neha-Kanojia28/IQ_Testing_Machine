# IQ Testing System application in python
import sys

# Variable Declaration
total_score = bonus = 0
attempt = choice = answer = None

# Empty list in python
attempted_sub_list = []

# Function represents : menu function displays menu for choice
def displayMenu():
    global choice 
    print("Welcome to IQ Testing System..")
    print("\t1. Aptitude")
    print("\t2. Maths")
    print("\t3. English")
    print("\t4. Gk")
    print("\t5. Exit")
    choice = int(input("Enter your choice between 1 to 5 : "))
    operation(choice)
    
# Function used to accept number of attempts 
def attemptNumber():
    attempt = int(input("Enter the number of attempts : "))
    if attempt > 1:
        print("You have already attempted the test..")
        sys.exit
    else :
        displayMenu()
        
def operation(choice):
    global total_score
    if choice in attempted_sub_list :
        print("You have already attempted the subject try another...")
        displayMenu()
    else :
        if choice == 1:
            attempted_sub_list.append(choice)
            answer = float(input("Find the speed, given distance = 5 and time = 2 : "))
            if answer == 2.5 : 
                total_score = total_score + 10
            displayMenu()
        
        elif choice == 2:
            attempted_sub_list.append(choice)
            answer = float(input("Square root of 64 ? : "))
            if answer == 8 : 
                total_score = total_score + 10
            displayMenu()
        
        elif choice == 3:
            attempted_sub_list.append(choice)
            answer = int(input("How many vowels are there? : "))
            if answer == 5 : 
                total_score = total_score + 10
            displayMenu()
            
        elif choice == 4:
            attempted_sub_list.append(choice)
            answer = input("What is capital of Bihar? : ")
            if answer.lower() == "patna" : 
                total_score = total_score + 10
            displayMenu()
            
        elif choice == 5:
            # Calculating Bonus
            if total_score == 10:
                bonus = 0
            elif total_score == 20:
                bonus = 2
            elif total_score == 30 :
                bonus = 5
            elif total_score == 40 :
                bonus= 10
        total_score += bonus
        print("================================")
        print("Bonus : ",bonus)
        print("Total Score : ",total_score)
        if total_score >= 40:
            print("You are genius..")
        elif total_score >= 30 :
            print(" You are intelligent..")
        elif total_score >= 20 :
            print(" Your IQ Level is average..")
        elif total_score >= 10 :
            print(" Your IQ Level is below average..")
        else :
            print(" You need to re appear the test")
        print("================================")
        sys.exit()
        
# Main code starting ....
attemptNumber()
print("Program ends here ... Thank You...")