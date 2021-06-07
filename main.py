# 
# main.py
# 
# created at 07/06/2021 14:45:47
# written by llamaking136
# 

# MIT License
#     
# Copyright (c) 2021 llamaking136
#     
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#     
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#     
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


#!/usr/bin/python3

import os, sys, random, time
from enum import Enum as enum

if not os.path.exists("/usr/bin/say"):
    print("Error! Cannot find `say` program in `/usr/bin`!", file = sys.stderr)
    exit(1)

phonetics = {
        "a": "alpha",
        "b": "bravo",
        "c": "charlie",
        "d": "delta",
        "e": "echo",
        "f": "foxtrot",
        "g": "golf",
        "h": "hotel",
        "i": "india",
        "j": "juliett",
        "k": "kilo",
        "l": "lima",
        "m": "mike",
        "n": "november",
        "o": "oscar",
        "p": "papa",
        "q": "quebec",
        "r": "romeo",
        "s": "sierra",
        "t": "tango",
        "u": "uniform",
        "v": "victor",
        "w": "wiskey",
        "x": "x-ray",
        "y": "yankee",
        "z": "zulu",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
        "0": "zero"
}

class Mode(enum):
    easy = 0
    med = 1
    hard = 2

phonetic = True
mode = None

def get_callsign_based_on_mode(mode):
    if mode == Mode.easy:
        return easy_callsigns, easy_length, easy_delay
    elif mode == Mode.med:
        return med_callsigns, med_length, med_delay
    elif mode == Mode.hard:
        return hard_callsigns, hard_length, hard_delay
    else:
        return None, None, None

# TODO: make configurations customizable in a cfg file somewhere
easy_callsigns = "aeiou24680"
easy_length    = (4, 6)
easy_delay     = 1
med_callsigns  = easy_callsigns + "bcdwxyrstpq135"
med_length     = (4, 6)
med_delay      = 0.5
hard_callsigns = "".join(phonetics.keys())#med_callsigns + "fghjklmnpqvz9"
hard_length    = (4, 6)
hard_delay     = 0

def startup():
    print("Welcome to HAM Listen! This game will try to help you advance")
    print("in listening to callsigns on-the-fly.")
    print("The game has three modes: easy, medium, and hard.")
    print("Easy has the highest delay between letters and hard has the lowest")
    print("delay between letters.")
    print("You can press Control-C at any time to stop the program.")

def main():
    global phonetic, mode
    while True:
        print("Saying callsign...")
        callsign_base, length, delay = get_callsign_based_on_mode(mode)
        temp = []
        for _ in range(random.randint(length[0], length[1])):
            temp += random.choice(callsign_base)
        callsign = "".join(temp)
        for i in temp:
            if phonetic:
                os.system("say " + phonetics[i])
            else:
                os.system("say " + i)
            time.sleep(delay)
        print("What was the callsign said?")
        callsign_heard = input("> ")
        if callsign_heard != callsign:
            print("Whoops! Looks like you didn't get this one. The callsign was " + callsign + ".")
        else:
            print("Congrats, you got it right!")
        print("Press return to continue...")
        input()

startup()
print("Now, please input mode (e: easy, m: medium, h: hard).")
while True:
    temp = input("> ").lower()
    if temp not in "emh":
        continue
    else:
        if temp[0] == "e":
            mode = Mode.easy
            break
        elif temp[0] == "m":
            mode = Mode.med
            break
        elif temp[0] == "h":
            mode = Mode.hard
            break
        else:
            continue
print("Please input phonetic letters or not (y: yes, n: no).")
while True:
    temp = input("> ").lower()
    if temp not in "yn":
        continue
    else:
        if temp[0] == "y":
            phonetic = True
            break
        elif temp[0] == "n":
            phonetic = False
            break
        else:
            continue

try:
    main()
except (KeyboardInterrupt, EOFError):
    exit(0)

