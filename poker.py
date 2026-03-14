#!/usr/bin/env python3
"""
Poker Cash Game Quick Logger
Just press ENTER repeatedly - that's it.

Enter once   → log a win
Then:
  ENTER ×1   → very small win
  ENTER ×2   → small win
  ENTER ×3   → medium win
  ENTER ×4   → large win

Then:
  ENTER ×1   → blind steal
  ENTER ×2   → bluff
  ENTER ×3   → quality of hand

Any other number of presses or Ctrl+C → quit
"""

import sys
import time
from datetime import datetime


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


def main():
    print("Poker Cash Win Logger  –  just press ENTER")
    print("───────────────────────────────────────────")
    print("  (press Ctrl+C or type anything to quit)\n")
    
    log_file = "poker-wins.log"
    
    while True:
        try:
            # First: wait for any enter to start logging a win
            sys.stdin.readline()   # just waits for enter
            
            count_size = count_enters("How big was it?  →  ")
            
            if count_size < 1:
                continue
                
            if count_size == 1:
                size = "very small"
            elif count_size == 2:
                size = "small"
            elif count_size == 3:
                size = "medium"
            elif count_size == 4:
                size = "large"
            else:
                print(f"   → {count_size}× ENTER = I don't know that size, skipping…")
                continue
                
            count_source = count_enters("How did you win it?  →  ", max_count=3)
            
            if count_source < 1:
                continue
                
            if count_source == 1:
                source = "blind steal"
            elif count_source == 2:
                source = "bluff"
            elif count_source == 3:
                source = "quality of hand"
            else:
                print(f"   → {count_source}× ENTER = unknown source, skipping…")
                continue
            
            now = datetime.now().strftime("%Y-%m-%d  %H:%M")
            line = f"{now}  {size:9}   {source}\n"
            
            print(f"  LOGGED → {line.strip()}")
            print("-"*40)
            
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(line)
                
        except KeyboardInterrupt:
            print("\nBye!")
            break
        except Exception as e:
            print(f"\nError: {e}")
            time.sleep(1.5)


if __name__ == "__main__":
    try:
        import select   # only needed for nicer timeout
    except ImportError:
        pass
    
    main()
