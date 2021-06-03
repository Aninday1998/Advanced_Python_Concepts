# Coroutine

import time


def searcher():

    book = "My name is Ani. I live in Bandel."
    time.sleep(3)
    # Assuming the task is taking 5 seconds to execute

    while True:

        n = yield        # taking one by one
        if n in book:
            print("Text Present")
        else:
            print("Not Present")

sc = searcher()         # creating instances
next(sc)                # next() is used to start the coroutine
sc.send("Ani")          # passing argument
input("Press Any Key:")
sc.send("Bandel")       # passing argument
sc.close()              # closing the coroutine


