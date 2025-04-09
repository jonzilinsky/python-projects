import random
import time
import os

def get_char():
    llist = ['A', 'B', 'C', 'D', 'E', 'F', 'A', 'B', 'C', 'D', 'E', 'F', 
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', ' ']
    ran_char = random.choice(llist)
    return(ran_char)


def get_row():
    for i in range(random.randint(10,55)):
        print(get_char(),end='', flush=True)
        time.sleep(0.05)
    print('')

def main():
    counter = 0
    try: 
         while True:
            if counter < 100:
                get_row()
                counter += 1
            else:
                if os.name == 'nt':
                    os.system('cls') 
                else:
                    os.system('clear')
                counter = 0
    except KeyboardInterrupt:
        pass 
main()
