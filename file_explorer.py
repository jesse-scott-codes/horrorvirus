import os
import sys
import time
import random

global running
running = True

#global a
#a = 0

def main():
    try:
        while running:
            #global a
            #a = 0

            #a += 1
            b = random.randint(0,31)
            f = open("mr_skin_ripper_" + str(b) + ".txt", 'a')
            f.write("mr. skin-ripper is watching...\n")
            f.close()

            #if a == 5:
                #sys.exit()
            #elif a == 7:
                #file = open("your_skin_is_mine.txt", 'a')
                #file.write("skin skin skin skin skin skin")
                #file.close()
    except KeyboardInterrupt:
        main()

main()