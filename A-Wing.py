#-------------------------------------------------------------------------------
# Name:        A-Wing
# Purpose:     Fly through the meteor shower
# Version:     1.0
#
# Author:      Bulut Ozturk < firstname dot lastname at gmail dot com >
#
# Created:     03/12/2014
#-------------------------------------------------------------------------------
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or distribute
# this software, either in source code form or as a compiled binary, for any
# purpose, commercial or non-commercial, and by any means.
#
# In jurisdictions that recognize copyright laws, the author or authors of
# this software dedicate any and all copyright interest in the software to the
# public domain. We make this dedication for the benefit of the public at large
# and to the detriment of our heirs and successors. We intend this dedication
# to be an overt act of relinquishment in perpetuity of all present and future
# rights to this software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
# 
# For more information, please refer to <http://unlicense.org>
#-------------------------------------------------------------------------------

import os,sys,time,random,msvcrt

def main():

    global screen
    screen = [space] * 225 # 15 heigh * 15 width

    print('A-Wing\n')
    dummy = input('Press <enter> to start.')

    for t in range(1,1000): # Run for 1000 frames
        if msvcrt.kbhit() == True:
            key = msvcrt.getch()
            if   key == b'a':
                ship.left()
            elif key == b'd':
                ship.right()
            elif key == b'q':
                print('\nYou quit A-Wing.')
                sys.exit(0)
        scroll(t)
        time.sleep(0.05) # Reiterate every 0.1 seconds
    print('\nCongratulations! You have finished A-Wing.')
    sys.exit(0)

def scroll(t):

    meteor = '@'
    shield = '+'
    explsn = '*'

    methit = False

    newmet = random.randint(1,2)
    newshd = random.randint(1,20)

    if newshd == 1:
        shdpos = random.randint(0,15)
    else:
        shdpos = None

    if newmet == 1:
        metpos = random.randint(0,15)
    else:
        metpos = None

    # Pick up shield powerup
    if   screen[180 + ship.posX] == shield:
        ship.shieldup()
    # Hit meteor
    elif screen[180 + ship.posX] == meteor:
        methit = True
        ship.shielddn()

    for i in reversed(range(0,225)):
        # Scroll down
        #  Place ship (hit)
        if   i == 195 + ship.posX and methit == True:
            screen[i] = explsn
        #  Place ship (unhit)
        elif i == 195 + ship.posX and methit == False:
            screen[i] = ship.icon
        #  Copy from line above
        elif i > 14 and screen[i-15] != ship.icon:
            screen[i] = screen[i-15]

        # New line
        #  Place meteor
        elif i == metpos:
            screen[i] = meteor
        #  Place shield
        elif i == shdpos:
            screen[i] = shield
        #  Clear meteor and shield trail
        elif screen[i] == meteor or screen[i] == shield:
            screen[i] = space
        #  Remaining coordinates
        else:
            screen[i] = space

    os.system('cls' if os.name == 'nt' else 'clear')

    border = '_' * 15

    print('Shield:',ship.slevel,'Points:',t)
    print(border)

    for y in range(0,15):
        line = empty
        for x in range(0,15):
            line+=screen[y*15+x]
        print(line)

    print(border)

    if ship.slevel < 1:
        print('\nGame over! You died.')
        sys.exit(0)

class Ship():

    def __init__(self):
        self.posX =5
        self.icon = 'A'
        self.slevel = 1

    def left(self):
        if self.posX > 0:
            self.posX-= 1
        else:
            self.posX = 0

    def right(self):
        if self.posX < 14:
            self.posX+= 1
        else:
            self.posX = 14

    def shieldup(self):
        self.slevel+= 1

    def shielddn(self):
        self.slevel-= 1

if __name__ == '__main__':

    global empty,space
    empty = ''
    space = ' '

    ship = Ship()

    main()
