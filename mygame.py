from colorama import Fore, Back, Style
import sys
import time


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)


print(Fore.WHITE + "▓█████   ██████  ▄████▄   ▄▄▄       ██▓███  ▓█████  ▐██▌  ▐██▌ ")
print(Fore.WHITE + "▓█   ▀ ▒██    ▒ ▒██▀ ▀█  ▒████▄    ▓██░  ██▒▓█   ▀  ▐██▌  ▐██▌ ")
print(Fore.WHITE + "▒███   ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██░ ██▓▒▒███    ▐██▌  ▐██▌ ")
print(Fore.WHITE + "▒▓█  ▄   ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██▄█▓▒ ▒▒▓█  ▄  ▓██▒  ▓██▒ ")
print(Fore.WHITE + "░▒████▒▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██▒ ░  ░░▒████▒ ▒▄▄   ▒▄▄  ")
print(Fore.RED + "░░ ▒░ ░▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░▒▓▒░ ░  ░░░ ▒░ ░ ░▀▀▒  ░▀▀▒ ")
print(Fore.RED + " ░ ░  ░░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░▒ ░      ░ ░  ░ ░  ░  ░  ░ ")
print(Fore.RED + "   ░   ░  ░  ░  ░          ░   ▒   ░░          ░       ░     ░ ")
print(Fore.RED + "   ░  ░      ░  ░ ░            ░  ░            ░  ░ ░     ░    ")
print(Fore.RED + "                ░                                              ")

slowprint(Fore.YELLOW + "Welcome to Escape!!")
time.sleep(1.25)
name = input(Fore.RED + "Please enter your name: ")
time.sleep(1.25)
slowprint(Fore.YELLOW + f"Hello {name}.... \n ...the time has come for you to be put to the test...")

def the_game():
    slowprint(Fore.RED + "You wake up...chained by your feet to a pole in a basement...with no recollection of how you got there..")
    time.sleep(1.25)
    slowprint(Fore.RED + "...the chains around your feet are secured by a padlock which can be unlocked by a code...")
    time.sleep(1.25)
    slowprint(Fore.RED + "...the code for the padlock has been implanted into the palm of your hand, a scalpel has been provided for some 'assistance'..")



def lets_begin():
    slowprint(Fore.YELLOW + "Great...let us begin...")
    the_game()


def no_choice():
    slowprint(Fore.YELLOW + "You have no choice in the matter...Let's begin!!")
    the_game()


def ready():
    decision = input(Fore.RED + "Are you ready?\n   ►   [Y/N]: ")
    if decision == "Y" or decision == "y":
        lets_begin()
    elif decision == "N" or decision == "n":
        no_choice()
    else:
        slowprint(Fore.YELLOW + "A simple yes or no will do...")
        ready()


ready()

def the_game2():
    slowprint(Fore.RED + "Having sliced into the palm of your hand....you carefully remove the code and unlock the padlock from the chains to free your feet...")
    time.sleep(1.25)
    slowprint(Fore.RED + "You make your way to the only door which appears to be activated by some sort of voice control...or sound..")
    time.sleep(1.25)
    slowprint(Fore.RED + "...a voice from a speaker echoes throughout the basement.")
    time.sleep(1.25)
    slowprint(Fore.WHITE + " '\x1B[3mHow much noise can you make to open the door....\n oh I forgot to mention only screams of pain can unlock it..\x1B[0m' ")
    time.sleep(1.25)
    slowprint(Fore.RED + "On a table, next to the door, are a hammer and a nail gun...it would appear that these will be needed...")
    time.sleep(2)
    evil()

def the_game3():
    decision = input(Fore.YELLOW + "Are you ready to choose?\nHammer or nail gun  ►   [H/N]:  ")
    if decision == "H" or decision == "h":
        hammer()
    elif decision == "N" or decision == "n":
        nail_gun()
    else:
        slowprint("I will ask again!!")
    the_game3()

def the_game4():
    slowprint(Fore.RED + "You stagger through the recently unlocked door...it seems your screams of pain, were sufficient....")
    time.sleep(1.25)
    slowprint(Fore.RED + "...in front of you is a set of stairs...\n ...you put one foot on them and it burns through the sole of your shoe...")
    time.sleep(1.25)
    slowprint(Fore.WHITE + " '\x1B[3mIt appears that the stairs are coated in some sort of acid glue...\x1B[0m' ")
    slowprint(Fore.RED + "...Looks like this could be your way out...." )
    stairs()

def end_game():
    slowprint(Fore.RED + "....to be continued\nthanks for playing")
    time.sleep (1.00)
    exit()

def the_game5():
    slowprint(Fore.YELLOW + "..In agony you reach the top of the stairs....you breathe a huge sigh of relief")
    time.sleep(1.25)
    slowprint(Fore.WHITE + " '\x1B[3mThis nightmare could finally be over.....\x1B[0m' ")
    slowprint(Fore.YELLOW + "...the front door is wide open....")
    slowprint(Fore.YELLOW + "... you decide to run to the door...")
    slowprint(Fore.YELLOW + "...you take a deep breath before you exit this nightmare...")
    time.sleep(2)
    slowprint(Fore.RED + "...a funny smelling cloth covers your mouth and nose.....as you slowly fall to the floor you think to yourself")
    slowprint(Fore.WHITE + " '\x1B[3m...chloroform...\x1B[0m' ")
    time.sleep(3)
    slowprint(Fore.RED + "..As your head hits the laminate flooring you blink and see a familiar face hovering over you....")
    time.sleep(1.25)
    slowprint(Fore.WHITE + " '\x1B[3mHi sis did you really think I would forget what you did.....\x1B[0m' ")
    end_game()

def climb():
    slowprint(Fore.RED + "You climb the stairs as the acid glue melts through the soles of your shoes and slowly begins to eat away at your feet..")
    the_game5()

def y_or_n():
    slowprint(Fore.YELLOW + "Are you sure....you may end up stuck here forever....")
    stairs()

def stairs():
    decision =  input(Fore.YELLOW + "Do you dare to climb the stairs?  ►   [Y/N]:   ")
    if decision == "Y" or decision == "y":
        climb()
    elif decision == "N" or decision == "n":
        y_or_n()
    else:
        slowprint("YES or NO.....IT'S NOT THAT HARD TO DECIDE!!")
    stairs()


def hammer():
    slowprint(Fore.YELLOW + "..You pick up the hammer and smack it on the tip of your fingers, causing you to let out a gut wrenching scream..")
    time.sleep(1.25)
    use_both()

def nail_gun():
    slowprint(Fore.YELLOW + "...You pick up the nail gun and aim at the middle of your wrist...causing you to let out a blood curdling scream..")
    time.sleep(1.25)
    use_both()

def use_both():
    slowprint(Fore.WHITE + " '\x1B[3mWhat a shame.... it looks like you have to combine them both together!!\x1B[0m")
    slowprint(Fore.YELLOW + "You smack your finger tips with the hammer with all your strength and then impale your wrist with the nail gun....which unlocks the door...")
    the_game4()

def evil():
    print(Fore.WHITE + "_____$___________________________________$")
    print(Fore.WHITE + "_____$$_________________________________$$")
    print(Fore.WHITE + "_____$_$_______________________________$_$")
    print(Fore.WHITE + "____$$_$$__________$$$$$$$$$$$$_______$$_$$")
    print(Fore.WHITE + "____$$__$$______$$$$$$_______$$$$$___$$__$$")
    print(Fore.WHITE + "___$$____$$__$$$$______________$$$$_$$____$$")
    print(Fore.WHITE + "___$$_____$$$$$___________________$$$_____$$")
    print(Fore.WHITE + "___$$_____$$___$$$_________________$$_____$$")
    print(Fore.WHITE + "___$$_____$$__$__$$_____________$$$_$_____$$")
    print(Fore.WHITE + "____$$___$$__$_$__$___________$$__$__$___$$")
    print(Fore.WHITE + "_____$$$$___$__$___$_________$____$___$$$$")
    print(Fore.WHITE + "_____$$_______$$$___$_______$____$$_____$$")
    print(Fore.WHITE + "____$$________$$$$___$_____$____$$$$_____$$")
    print(Fore.WHITE + "___$$________$$$$$$___$___$$___$$$$$_____$$")
    print(Fore.WHITE + "___$$________$$$$$$$___$__$___$$$$$$$____$$$")
    print(Fore.WHITE + "__$$________$$$$$$$$$__$$_$__$$$$$$$$_____$$")
    print(Fore.WHITE + "__$$________$$$$$$$$$___$$$__$$$$$$$$_____$$")
    print(Fore.WHITE + "__$$________$$$$$$$$$$__$$__$$$$$$$$$_____$$")
    print(Fore.WHITE + "__$$________$$$$$$$$$$$____$$$$$$$$$______$$")
    print(Fore.WHITE + "__$$________$$$$$$$$$$$$___$$$$$$$$$______$$")
    print(Fore.WHITE + "__$$_________$$$$_$$$_$$___$__$$$$$$______$$")
    print(Fore.WHITE + "__$$__________$$$$$$$_$$___$_$$$$$$_______$$")
    print(Fore.WHITE + "__$$__________$$$$$$$_$$___$_$$$$$________$$")
    print(Fore.WHITE + "___$$_______$___$$$$$$$____$$$$$_________$$")
    print(Fore.WHITE + "___$$$______$$$$_________________________$$")
    print(Fore.WHITE + "____$$_____$$_$$$________________$$$____$$")
    print(Fore.WHITE + "_____$$_______$_$$________________$$___$$")
    print(Fore.WHITE + "______$$______$_$$$___________$$$$____$$")
    print(Fore.WHITE + "_______$$_____$$__$$$$$$$$$$$$$$_____$$")
    print(Fore.WHITE + "________$$$___$______$$$$$_________$$$")
    print(Fore.WHITE + "__________$$$____________________$$$$")
    print(Fore.WHITE + "____________$$$_________________$$$")
    print(Fore.WHITE + "______________$$$$____________$$$$")
    print(Fore.WHITE + "_________________$$$$$____$$$$$$")
    print(Fore.WHITE + "____________________$$$$$$$$$$")
    the_game3()


def scalpel():
    slowprint(Fore.RED + "A steady hand is key...we don't want you to cut too deep..")
    time.sleep(1.25)
    the_game2()

def me_you():
    slowprint(Fore.RED + "Either you do it or the other option will be much more painful...SO I WILL ASK YOU AGAIN!!")
    ready1()

def ready1():
    decision = input(Fore.YELLOW + "Are you prepared to cut into your hand?\n   ►   [Y/N]:  ")
    if decision == "Y" or decision == "y":
        scalpel()
    elif decision == "N" or decision == "n":
        me_you()
    else:
        slowprint(Fore.YELLOW + "I WILL ASK YOU AGAIN!!")
        ready1()


ready1()


