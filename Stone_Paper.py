import random, time
comp_inp = {1:"Stone",2:"Paper", 3:"Scissors"}

user_input_menu = int(input("1. Play the Game \n2. Exit "))
name = input("Enter your name: ")
print("\n")
time.sleep(1)
print("Initiating the Game, Get Ready {}!!".format(name))
time.sleep(1)
print("\n")
if user_input_menu == 1:
    flag = True
    count = 0
    while flag:
        time.sleep(1)
        print("Please Choose Any One By Entering The Number")
        user_input = int(input("1. Stone \n2. Paper \n3. Scissors"))
        computer_input = random.randint(1,3)
        if computer_input == 1 and user_input == 2 or computer_input == 2 and user_input == 3 or computer_input == 3 and user_input == 1:
            time.sleep(1)
            print(name," Wins. As Computer Took Out {}".format(comp_inp[computer_input]))
            count+=1
            print("\n")
            print("\n")
        
        elif computer_input == user_input:
            time.sleep(1)
            print("Round Draw. Computer Took Out {}".format(comp_inp[computer_input]))
            print("\n")
            print("\n")
        

        else:
            time.sleep(1)
            print(name,' Looses, Computer took out {}'.format(comp_inp[computer_input]))
            print("Score of ", name, " is {}".format(count))
            flag = False
            print("\n")
            print("\n")


elif user_input_menu == 2:
    exit
else:
    print("Incorrect Option")

