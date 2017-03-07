"""
Recursive Towers of Hanoi

It codes exactly how you think about the problem.
- Move everything above the nth disc to the temporary spot
- Move the nth disc to the desired pole
- Move all those other discs back on top 
"""

def move(n, fromtower, totower, usingtower):
    if (n == 1):
        move.nummoves += 1
        print move.nummoves, ": Move disk from", fromtower, "to", totower
    else:
        move(n-1,fromtower,usingtower,totower)
        move(1,fromtower,totower,usingtower)
        move(n-1,usingtower,totower,fromtower)
    return 0
    
NUM_DISCS = 3
move.nummoves=0
move(NUM_DISCS,"A","C","B")

print "Total moves:",move.nummoves