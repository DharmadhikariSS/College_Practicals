
#      Satyajeet Dharmadhikari
#      TY CSE R. no 30


def display_numbers():
    for i in range(20, 51):
        print(i)
    action_taker()

def add_num_and_mean():
    print("Addition is: ",sum(range(20,61)))
    print("Mean is: ",sum(range(20,61))/len(range(20,61)))
    action_taker()

def add_20_50():
    add = 0
    for plus in range(51, 101):
        add = add+plus
    print("Addition is: ", add)
    action_taker()

    


def action_taker():
    print('Enter 1 to display numbers from 20 to 50')
    print('Enter 2 to display addition of 20 to 60 and mean')
    print('Enter 3 to display addition of 51 to 100')
    print('Enter 4 to exit')
    action = str(input('Choose your option: '))  

    if action=='1':
        display_numbers()
    elif action=='2':
        add_num_and_mean()
    elif action=='3':
        add_20_50()
    elif action=='4':
        exit()
    else:
        print("You choosed wrong option")
action_taker()
