#-------------------------------------------------------------------------------
# Name:        FlapPy
# Purpose:     Help Flappy the Python fly to freedom
# Version:     1.0
#
# Author:      Bulut Ozturk < firstname dot lastname at gmail dot com >
#
# Created:     01/12/2014
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
    screen = [space] * 180 # 9 heigh * 20 width

    print('FlapPy\n')
    dummy = input('Press <enter> to start.')

    for t in range(1,1000): # Run for 1000 frames
        os.system('cls' if os.name == 'nt' else 'clear')
        if msvcrt.kbhit() == True and msvcrt.getch() != empty:
            flappy.flap()
        scroll(t%8)
        time.sleep(0.1) # Reiterate every 0.1 seconds
    print('\nCongratulations! You have finished FlapPy.')
    sys.exit(0)

def scroll(n):

    block = '#'
    crash = '@'

    buffer = [space] * 9

    nextgate = {'top':0,'gap':0,'btm':0}

    # Next gate
    nextgate['top'] = random.randint(1,5)
    nextgate['gap'] = random.randint(2,3)
    nextgate['btm'] = 9 - nextgate['top'] - nextgate['gap']

    if n == 0: # Every 8th frame
        addcol = [block] * nextgate['top'] + \
                 [space] * nextgate['gap'] + \
                 [block] * nextgate['btm']
    else:
        addcol = buffer

    death = empty

    if n%2 == 0: # Every 2nd frame
        flappy.posY+= 1
        if flappy.posY > 9:
            death = 'drowned'

    for i in range(0,180):
        j = i + 1
        if   j == (flappy.posY - 1) * 20 + 2:
            if screen[i+1] != space:
                screen[i] = crash
                death = 'crashed'
            else:
                screen[i] = flappy.icon
        elif j%20 != 0 or j == 1:
            if screen[i+1] != flappy.icon:
                screen[i] = screen[i+1]
            else:
                screen[i] = space
        else:
            screen[i] = addcol[int(i/20)]

    bordertop = '_' * 20
    borderbtm = '~' * 20

    if screen[0] == block:
        flappy.score+= 1

    print('Score:',flappy.score)
    print(bordertop)

    for y in range(0,9):
        line = empty
        for x in range(0,20):
            line+=screen[y*20+x]
        print(line)

    print(borderbtm)

    if death != empty:
        print('\nGame over! You '+death+'.')
        sys.exit(0)

class Flappy():

    def __init__(self):
        self.posY  = 5
        self.score = 0
        self.icon  = 'S'

    def flap(self):
        if self.posY > 0:
            self.posY-= 1
        else:
            self.posY = 0

if __name__ == '__main__':

    global empty,space
    empty = ''
    space = ' '

    flappy = Flappy()

    main()
