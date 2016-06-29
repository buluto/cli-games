#-------------------------------------------------------------------------------
# Name:        TicTacToe
# Purpose:     A game of TicTacToe
# Version:     1.0
#
# Author:      Bulut Ozturk < firstname dot lastname at gmail dot com >
#
# Created:     02/10/2014
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

import os,sys,random

def main():

    l = [space] * 10

    oppo = empty

    while oppo == empty:
        oppo = input('Number of players (1 or 2): ')
        if oppo != '1' and oppo != '2':
            print('Invalid value!')
            oppo = empty

    draw(l)
    move(l,oppo)

def draw(l):

    os.system('cls' if os.name == 'nt' else 'clear')

    print('    1   2   3  ')
    print('  -------------')
    print('A | '+l[1]+' | '+l[2]+' | '+l[3]+' |')
    print('  -------------')
    print('B | '+l[4]+' | '+l[5]+' | '+l[6]+' |')
    print('  -------------')
    print('C | '+l[7]+' | '+l[8]+' | '+l[9]+' |')
    print('  -------------\n')

def move(l,oppo):

    etxt = empty
    x = 0

    while x < 9:

        print(etxt)

        if x % 2 == 0:
            pnam = 'Player 1'
            pval = 'X'
            move = input('Your move, '+pnam+': ')
        else:
            pnam = 'Player 2'
            pval = 'O'
            if oppo == '2':
                move = input('Your move, '+pnam+': ')
            else:
                move = aimv(l,x)

        i = mvcv(move)

        etxt = empty
        etxt = mvck(l,i)

        if etxt == empty:
            l[i] = pval
            x+=1

        draw(l)

        if l[1] == l[5] == l[9] != space or \
           l[7] == l[5] == l[3] != space or \
           l[1] == l[2] == l[3] != space or \
           l[4] == l[5] == l[6] != space or \
           l[7] == l[8] == l[9] != space or \
           l[1] == l[4] == l[7] != space or \
           l[2] == l[5] == l[8] != space or \
           l[3] == l[6] == l[9] != space:

            print(pnam+' wins!')
            sys.exit(0)

    print('Stalemate!')
    sys.exit(0)

def mvcv(move):

    cmap = str.maketrans('abcABC','012012')
    i = int(move[0:1].translate(cmap)) * 3 + int(move[1:2])

    return i

def mvck(l,i):

    etxt = empty

    if l[i] != space:
        etxt = 'Invalid move!\n'

    return etxt

def aimv(l,x):

    move = empty
    seedo = random.choice([1,3,7,9])
    seede = random.choice([2,4,6,8])

    if l[1] == space and (
       l[2] == l[3] != space or \
       l[4] == l[7] != space or \
       l[5] == l[9] != space or (
       l[5] == 'X' and x == 1 and seedo == 1 ) ):
        move ='a1'
    if l[2] == space and (
       l[5] == l[8] != space or \
       l[1] == l[3] != space or ( (
       l[4] == 'X' or l[6] == 'X' ) and x == 1 and seede == 2 ) ):
        move = 'a2'
    if l[3] == space and (
       l[1] == l[2] != space or \
       l[7] == l[5] != space or \
       l[9] == l[6] != space or (
       l[5] == 'X' and x == 1 and seedo == 3 ) ):
        move = 'a3'
    if l[4] == space and (
       l[5] == l[6] != space or \
       l[1] == l[7] != space or ( (
       l[2] == 'X' or l[8] == 'X' ) and x == 1 and seede == 4 ) ):
        move = 'b1'
    if l[5] == space and (
       l[2] == l[8] != space or \
       l[4] == l[6] != space or \
       l[1] == l[9] != space or \
       l[3] == l[7] != space or ( (
       l[1] == 'X' or l[3] == 'X' or
       l[7] == 'X' or l[9] == 'X' )
       and x == 1 ) ):
        move = 'b2'
    if l[6] == space and (
       l[4] == l[5] != space or \
       l[3] == l[9] != space or ( (
       l[2] == 'X' or l[8] == 'X' ) and x == 1 and seede == 6 ) ):
        move = 'b3'
    if l[7] == space and (
       l[1] == l[4] != space or \
       l[3] == l[5] != space or \
       l[9] == l[8] != space or (
       l[5] == 'X' and x == 1 and seedo == 7 ) ):
        move = 'c1'
    if l[8] == space and (
       l[2] == l[5] != space or \
       l[7] == l[9] != space or ( (
       l[4] == 'X' or l[6] == 'X' ) and x == 1 and seede == 8 ) ):
        move = 'c2'
    if l[9] == space and (
       l[1] == l[5] != space or \
       l[7] == l[8] != space or \
       l[3] == l[6] != space or (
       l[5] == 'X' and x == 1 and seedo == 9 ) ):
        move = 'c3'

    while move == empty:
        rndm = random.choice(['a','b','c']) + random.choice(['1','2','3'])
        etxt = mvck(l,mvcv(rndm))
        if etxt == empty:
            move = rndm

    return move

if __name__ == '__main__':
    global empty
    empty = ''
    global space
    space = ' '
    main()
