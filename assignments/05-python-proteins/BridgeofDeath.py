#!/usr/bin/env python3

import os
import sys

def main():
   answers = {}
   for thing in ['name', 'quest', 'favortite color']:
      answer = input('What is your {}? '.format(thing))
      print(answer)
      answers[thing] = answer

   print(answers)

main()
