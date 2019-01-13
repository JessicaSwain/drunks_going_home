#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Version 1.0
Created by Jessica Swain at the University of Leeds

@author: jessicaswain
"""

#----------------------------------------------------------------------------#

HouseX = {"10": 25, "20": 25, "30": 25, "40": 25, "50": 25, "60": 25, "70": 25, "80": 75, "90": 110, "100": 140, "110": 180, "120": 260, "130": 260, "140": 260, "150": 260, "160": 260, "170": 260, "180": 260, "190": 180, "200": 120, "210": 75, "220": 80, "230": 70 , "240": 200, "250": 210}
HouseY = {"10": 25, "20": 60, "30": 110, "40": 140, "50": 180, "60": 225, "70": 275, "80": 275, "90": 275, "100": 275, "110": 275, "120": 275, "130": 255, "140": 180, "150": 140, "160": 110, "170": 60, "180": 25, "190": 25, "200": 25, "210": 25, "220": 210, "230": 60, "240": 215, "250": 70}
#here the key is the house number and the value is the coordinate

DrunkNumbering = {"drunk1": 10, "drunk2": 20, "drunk3": 30, "drunk4": 40, "drunk5": 50, "drunk6": 60, "drunk7": 70, "drunk8": 80, "drunk9": 90, "drunk10": 100, "drunk11": 110, "drunk12": 120, "drunk13": 130, "drunk14": 140, "drunk15": 150, "drunk16": 160, "drunk17": 170, "drunk18": 180, "drunk19": 190, "drunk20": 200, "drunk21": 210, "drunk22": 220, "drunk23": 230, "drunk24": 240, "drunk25": 250}

drunknum = str([DrunkNumbering.values()])
#print(drunknum)
housenumY = str([HouseY.keys()])
#print(housenumY)
housenumX = str([HouseX.keys()])
#print(housenumX)
#houseYcoord = HouseY.values()

#below is an attempt to get the dictionary to write to a text file
#with open('drunkresults.txt','w') as results: 
#    print(HouseX, file='drunkresults.txt')
results = open('drunkresults.txt', 'a')
results.write(drunknum + "\n")
results.write(housenumY + "\n")
results.write(housenumX + "\n")  
results.close()

#----------------------------------------------------------------------------#
import random

class Drunk():
    
        def __init__ (self, environment, drunks, position, y, x):
 
############################  Y & X VALUES  ##################################                     
#both of these have been set at 150 so they start at the pub 
            self._y = 150
            self._x = 150
            print("y value", self._y)
            print("x value", self._x)            
############################  ENVIRONMENT  ###################################           
            self.environment = environment
            self.store = 0
            self.drunks = drunks
            self.store = 0
            self.position = 1
            self.store = 500
##############################  MOVEMENT  ####################################

        def move(self):
#                   for values in DrunkNumbering:
#                if DrunkNumbering.values() == HouseY.keys():    
#            for drunk in self.drunks: 
#                if HouseY.keys == DrunkNumbering.values:
#                    if self._y != any(HouseY.values()):

#above is an attempt at getting the for loops to link the drunk number and
#house number's x and y coordinates to work together for the move function            
            
                    while self._y == 150:
                            self._y = (self._y + random.randint(0,2))
                            self.store -= 1
                            print('leaving the pub')
                            print("y value, left the pub", self._y)
                    else:
                            self._y = (self._y - random.randint(0,2)) % 300
                            self.store -= 1
                            print('leaving the pub')
                            print("y value, left the pub", self._y)
#here the loop is saying while the y value equals 150 move randomly and say 
#that the drunk is leaving the pub                            
                    
                    if self._y != any(HouseY.values()):
                            self._y = (self._y + random.randint(0,10)) % 300
                            self.store -= 1
                            print('trying to get home')
                            print("y value", self._y)
                    else: 
                            self._y = (self._y - random.randint(0,10)) % 300
                            self.store -= 1
                            print('trying to get home')
                            print("y value", self._y)                    
#this loop says if the y value does not match any of the home coordinates
#then the drunk needs to continue to move                            
                    
                    if self._y == any(HouseY.values()):
                            print('home')
                            print("y value", self._y)                        
#this loop finally says when the y value matches one of the home values then
#say they are home                            
                        
#part of the trial and error process:
#                if HouseX.keys == DrunkNumbering.values:
                    #if self._x != any(HouseX.values()):   
                         
                    while self._x == 150:
                            self._x = (self._x + random.randint(0,2)) % 300
                            self.store -= 1
                            print('leaving the pub')
                            print("x value, left the pub", self._x)
                    else:
                            self._x = (self._x - random.randint(0,2)) % 300
                            self.store -= 1
                            print('leaving the pub')
                            print("x value, left the pub", self._x)
#here the loop is saying while the x value equals 150 move randomly and say 
#that the drunk is leaving the pub 

                    if self._x != any(HouseX.values()):
                            self._x = (self._x + random.randint(0,10)) % 300
                            self.store -= 1
                            print('trying to get home')
                            print("x value", self._x)
                    else: 
                            self._x = (self._x - random.randint(0,10)) % 300
                            self.store -= 1
                            print('trying to get home')
                            print("x value", self._x)                    
#this loop says if the x value does not match any of the home coordinates
#then the drunk needs to continue to move 
                    
                    if self._x == any(HouseX.values()):
                            print('home')
                            print("x value", self._x)                     
#this loop finally says when the x value matches one of the home values then
#say they are home 


#this is also part of the trial and error process:
#            if self._y != any(HouseY.values()): 
#                    print('trying to get home')
#                    self._y = (self._y + 1) % 300
#                    self.store -= 5
#            else:
#                    self._y = (self._y - 1) % 300
#                    self.store -= 0
#
#            if self._x != any(HouseX.values()):
#                    self._x = (self._x + 1) % 300
#                    self.store -= 5
#            else:
#                    self._x = (self._x - 1) % 300
#                    self.store -= 0
#
#                
#I added this extra loop in to ensure that both the x and y coordinates match
#                    if self._y == (HouseY.values) and self._x == (HouseX.values):
#                        print('arrived home')                            
###########################  EAT ENVIRONMENT  ################################               
#this is so the graph/model shows where the drunks have moved to and from
        def eat(self):
            if  self.environment[self._y][self._x] > 10:
                self.environment[self._y][self._x] -= 10
                self.store += 10                   
#########################  NEIGHBOURHOOD SHARE  ##############################           
        def share_with_neighbours (self, neighbourhood):
            for drunk in self.drunks:
                dist = self.distance_between(drunk)
            if dist <= neighbourhood: 
                    sum = self.store + drunk.store
                    ave = sum/2
                    self.store = ave
                    drunk.store = ave  
