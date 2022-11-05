# !/usr/bin/python3
# -*- coding: utf-8 -*-
import random
import math
from pyfiglet import Figlet
custom_fig = Figlet(font='arrows')
three_fig = Figlet(font='banner3-D')
computer_fig = Figlet(font='larry3d')
test_fig = Figlet(font='banner3-D')

capital = [c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
small = [c for c in "abcdefghijklmnopqrstuvwxyz"]
nums = [c for c in "0123456789"]
special = [c for c in "$&#%?!@€§"]


def chooseNum(content):
    num = random.randint(0, len(content)-1)
    return content[num]


def generateBlock(current, last, separation):
    block = ""

    for i in range(4):
        num = random.randint(0, 3)
        if num == 0:
            block += chooseNum(capital)
        elif num == 1:
            block += chooseNum(small)
        elif num == 2:
            block += chooseNum(nums)
        elif num == 3:
            block += chooseNum(special)

    if current < last:
        block += separation

    return block


def generatePassword(size, sep):
    pw = ""
    parts = int(math.ceil(size / 4.0))
    print("\n[!] The password is constructed out of %i blocks" % parts)
    # print(computer_fig.renderText("\n[!] The password is constructed out of %i blocks" % parts))
    for i in range(parts):
        pw += generateBlock(i, parts-1, sep)

    return pw


def askLength():
    try:
        len = input("[1] Input the length: ")
        # len = input(computer_fig.renderText("[1] Input the length: "))
        if int(len) >= 0:
            return int(len)
        else:
            len = askLength()
    except ValueError:
        len = askLength()

    return int(len)


def askSeparation():
    sep = input("[2] Input the separator (ENTER if none): ")
    # sep = input(computer_fig.renderText("[2] Input the separator (ENTER if none): "))

    return sep


def again(len, sep):
    response = input("[?] Again? (Y|N): ")
    # response = input(computer_fig.renderText("[?] Again? (Y|N): "))

    if response == "Y" or response == "y":
        pw = generatePassword(len, sep)
        print("[+] Your new password could be: " + pw)
        # print(computer_fig.renderText("[+] Your new password could be: " + pw))
        again(len, sep)
    else:
        pass


def start():
    try:
        length = askLength()
        sep = askSeparation()
        pw = generatePassword(length, sep)
        print("[+] Your new password could be: " + pw)
        # print(computer_fig.renderText("[+] Your new password could be: " + pw))
        again(length, sep)
    except KeyboardInterrupt:
        print("\nend.")


for i in range(14):
    print("\n")
print(three_fig.renderText('PassGen'))
print()
start()
