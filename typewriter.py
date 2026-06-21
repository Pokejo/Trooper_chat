import time

def typewriter(text, delay=0.05):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(delay)

    #print()
    time.sleep(1)