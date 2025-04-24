#game logic

import random


def guess(guess_num: int)-> bool:

    num = random.randint(1,10) #generate a random number
    
    return {"correct": num,"status": guess_num == num}  #return a bool value and correct value whether the number exists or not 