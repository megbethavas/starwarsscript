#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 21:24:22 2020

@author: meaganbethavas
"""

import os
this_file = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(this_file, 'SW_EpisodeIV.txt')
file = open('/Users/meaganbethavas/Documents/SW_EpisodeIV.txt', 'r')
def main(): 

    
    line_list = []
    with open('/Users/meaganbethavas/Documents/SW_EpisodeIV.txt', 'r') as my_file:
        for line in my_file:
              line_list.append(line) #make a list from file
        line_list = [each_string.lower() for each_string in line_list] #lowercase all words in script
        
        def removing(line_list): #strip list of punctuation
            for i in line_list:
                if i == '?':
                    line_list.remove('?')
                if i == '!':
                    line_list.remove('!')
                if i == '.':
                    line_list.remove('.')
                if i == ',':
                    line_list.remove(',')
                if i == '...':
                    line_list.remove('...')
                    return line_list 
                
        removing(line_list)
        
    
                    
        character_list = [
    'threepio', 'luke', 'imperial officer', 'vader', 'rebel officer',
    'trooper', 'chief pilot', 'captain', 'woman', 'fixer', 'camie',
    'biggs', 'deak', 'leia', 'commander', 'second officer', 'owen',
    'aunt beru', 'ben', 'tagge', 'motti', 'tarkin', 'bartender',
    'creature', 'human', 'han', 'greedo', 'jabba', 'officer cas',
    'voice over deathstar intercom', 'gantry officer', 'intercom voice',
    'trooper voice', 'first trooper', 'first officer', 'second trooper',
    'officer', 'willard', 'dodonna', 'wedge', 'man', 'red leader',
    'chief', 'massassi intercom voice', 'red ten', 'red seven', 'porkins',
    'red nine', 'red eleven', 'gold leader', 'astro-officer',
    'control officer', 'gold two', 'gold five', 'wingman', 'voice',
    'technician'
    ]
        
        character = input("Enter character name:")
        count = 0 #count characters occurences in script
        for word in line_list:
                found = word.find(character)
                if found != -1 and found != 0:
                    count += 1
                    continue #continue to have for loop count each character in list

                    
        my_dict = {} #create empty dictionary
        for i in character_list: #dictionary will read character as key and count as value
            my_dict.setdefault(character, count)
        
                
        print("Character speech count:", my_dict)

main()