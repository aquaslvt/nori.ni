import sys
import os
import time
import random
import math
import cups
# import toml

stack = []
char = ''
code = []

# Search for file arguments

if len(sys.argv) == 1:
  file_argument = 'main.nii'
else:
  file_argument = sys.argv[1]

# Open the file

with open(file_argument, 'r') as file:
    for line in file:
        row = [char if char != ' ' else ' ' for char in line.rstrip('\n')]
        code.append(row)

# Adjust the length of each row by padding with empty strings
code = [row + [''] * (max(len(row) for row in code) - len(row)) for row in code]

x = 0
y = 0
direction = ''

directions = ['left', 'right', 'up', 'down']
numbers = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

def run():
  global stack, char, code, x, y, direction, numbers

  # Update direction & current command

  while y < len(code) and x < len(code[y]):

    if direction == 'left':
      x -= 1
    
    elif direction == 'right':
      x += 1
    
    elif direction == 'up':
      y -= 1
    
    elif direction == 'down':
      y += 1

    char = code[y][x] if y < len(code) and x < len(code[y]) else ''

    # Direction commands

    if char == '<':
      direction = 'left'
    
    elif char == '>':
      direction = 'right'
    
    elif char == '^':
      direction = 'up'
    
    elif char == 'v':
      direction = 'down'

    elif char == 'Q':
      direction = directions[random.randint(0,3)]

    elif char == ';':
      sys.exit()

    # Input/output commands

    elif char == 'N':
        stack.append(int(input()))

    elif char == 'I':
      stack.append(input())
    
    elif char == 'o':
      print(stack.pop())

    elif char == 'O':
      print(stack.pop(), end='')

    elif char == 'X':
      os.system('clear')

    elif char == ',':
     a = input()
     for character in a:
       stack.append(ord(character))

    elif char == '.':
     print(chr(stack.pop()))

    # Stack manipulation commands

    elif char == '!':
      stack.pop()
    
    elif char in numbers:
      stack.append(int(char, 16))

    elif char == '\'':
      x += 1
      string_temp = []

      while code[y][x] != '\'':
        character = code[y][x]
        string_temp.append(character)
        x += 1

      stack.append(''.join(string_temp))

    # Math commands

    elif char == '+':
        stack.append(stack.pop() + stack.pop())

    elif char == '-':
      a = stack.pop()
      b = stack.pop()
      stack.append(b - a)

    elif char == '*':
      stack.append(stack.pop() * stack.pop())

    elif char == '/':
      a = stack.pop()
      b = stack.pop()
      stack.append(b / a)

    elif char == '%':
      a = stack.pop()
      b = stack.pop()
      stack.append(a % b)

    elif char == '°':
      a = stack.pop()
      b = stack.pop()
      stack.append(b ** a)

    elif char == 'z':
      stack.append(math.sqrt(stack.pop()))

    elif char == 'c':

      stack.append(math.ceil(stack.pop()))

    elif char == 'f':
      stack.append(math.floor(stack.pop()))

    elif char == 'r':
      stack.append(random.random())

    elif char == ':':
      stack.append(stack[-1])

    elif char == '@':
      stack[-1], stack[-2] = stack[-2], stack[-1]

    elif char == '$':
      stack.reverse()

    elif char == 'V':
      a = stack.pop()
      stack.insert(0, a)

    elif char == 'W':
      a = stack.pop(0)
      stack.insert(-1, a)

    elif char == 'b':
      stack.append(random.randint(0, 1))

    elif char == '?':
      if stack.pop() == 0:
        x += 1

    elif char == '#':
      time.sleep(0.1)
      sys.stdout.flush()

    elif char == '_':
      conn = cups.Connection()
      default_printer = conn.getDefault()

      if default_printer:
        printer = conn.getPrinters()
        print_job_id = conn.printFile(default_printer, '.meow/spoing.pdf', 'Print Job', {})

        if print_job_id:
          print('Ayo, look at your printer >:3')
        else:
          print('SPOING DIDN\'T PRINT!?!?!?')
      else:
        print('no printer TwT')
try:
  run()
except KeyboardInterrupt:
  print('\n\nExited with ^C')