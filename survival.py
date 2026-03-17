#!/usr/bin/env python3

import sys
import time
from datetime import datetime


def calc(m1, m2, h, s, d, win):
    x1 = (float(h) / float(s)) * (1 - float(d)) * ((float(m2) / float(m1)) + float(d))
    x2 = (float(h) / float(s)) * (1 + float(d)) * ((float(m2) / float(m1)) + float(d))
    if win:
        return x2
    else:
        return x1

def count_enters(prompt: str, max_count: int = 4) -> int:
    """Count how many times user presses Enter in a row"""
    print(prompt, end="", flush=True)
    count = 0
    
    while True:
        # Set raw mode so we can read single keystrokes without enter
        # But for simplicity we just read line by line here
        line = sys.stdin.readline().rstrip("\r\n")
        
        if line == "":          # just pressed Enter
            count += 1
            print("." * count, end="", flush=True)
            time.sleep(0.15)
        else:
            # User typed something → probably wants to quit
            print("\n   → aborted")
            return -1
            
        # Timeout after ~1.5 seconds of no more enters
        # We give the user a bit of time between presses
        start = time.time()
        while time.time() - start < 1.4:
            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                break
            time.sleep(0.08)
        else:
            # timeout → user stopped pressing
            break
    
    print()  # new line after dots
    return count

if __name__ == "__main__":
    try:
        import select   # only needed for nicer timeout
    except ImportError:
        pass
while True:
	x = count_enters("Loss or Gain? ")
	delta = 0.01
	survival_metric = 200 # hands you can survive
	hands_played = 0
	money0 = 0
	money1 = 0
	money0 = float(input("Money started: "))
	money1 = float(input("Money ended: "))
	hands_played = float(input("Hands played: "))
	print(str(calc(money0, money1, hands_played, survival_metric, delta, x==1)))
