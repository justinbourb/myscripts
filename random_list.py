'''random_list.py
creates a random list of integers between 25 to 50
prints out the list and it's reverse
written by Justin Bourbonniere 4/22/17
started: 6:44am finished: 6:59am'''

import random

def random_num_list():
    #creates the lists
    random_list=[]
    #I've looked up the correct way to do this
    #reverse_random_list=[None]*10
    reverse_random_list=[0,0,0,0,0,0,0,0,0,0]

    #generates random numbers and prints the lists
    for i in range(0,10):
        random_list.append(random.randint(25,50))
        reverse_random_list[9-i]=random_list[i]
    print("This is the list in order", random_list)
    print("This is the list in reverse",reverse_random_list)


if __name__ == "__main__":
    random_num_list()

