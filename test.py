import curses
from curses import wrapper
import time 
import random

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the typing test bruh!\n")
    stdscr.addstr("you can do it, lets go,press any key to continue")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr,target,crt_text,wpm=0):
    stdscr.addstr(target)                                       
    stdscr.addstr(1,0,f"WPM: {wpm}")
    for i,char in enumerate(crt_text):
        correct_txt = target[i]
        color = curses.color_pair(1)
        if char != correct_txt:
         
            color= curses.color_pair(2)                       
        stdscr.addstr(0,i,char,color)  
def load_text():
    with open("hi.txt","r") as f:
        lines=f.readlines()
        return random.choice(lines).strip()


def wpm_test(stdscr):
    target = load_text()
    crt_text=[]
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time,1)
        wpm = round((len(crt_text)/(time_elapsed/60))/5)

        stdscr.clear()
        display_text(stdscr,target,crt_text,wpm)
        stdscr.refresh()

        if "".join(crt_text) == target:
            stdscr.nodelay(False)
            break
 
        try:
            key = stdscr.getkey() #blocking func it makes the code wait 
        except:
            continue         #if no input cntnu

        if ord(key) == 27:                                          #4th
            break
        if key in ("KEY_BACKSPACE","\b","\x7f"):
            if len(crt_text)>0:
                crt_text.pop()
        elif len(crt_text) < len(target):
            crt_text.append(key)
def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLACK)
    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2,0,"You have completed the text! , Press any key to continue..")
        key = stdscr.getkey()

        if ord(key) == 27:
            break
wrapper(main)
        