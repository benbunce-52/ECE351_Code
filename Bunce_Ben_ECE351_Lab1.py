# -*- coding: utf-8 -*-
################################################################
##
# Ben Bunce #
# ECE351 - 52 #
# Lab 1 #
# 9.9.2021 #
##
################################################################

import numpy as np
import scipy . signal as sig
import time
import matplotlib . pyplot as plt

###############################
        ##  Part 2  ##
###############################

t = 1
print ( t )
print ("t =",t )
print ("t =",t ," seconds ")
print ("t is now =",t /3 , "\n... and can be rounded using ‘round () ‘",round ( t /3 ,4) )

print ("\n",3**2,"\n")

###### Matrix and Lists ######

list1 = [0 ,1 ,2 ,3]
print ("list1 :", list1 )
list2 = [[0] ,[1] ,[2] ,[3]]
print ("list2 :", list2 )
list3 = [[0 ,1] ,[2 ,3]]
print ("list3 :", list3 )
array1 = np . array ([0 ,1 ,2 ,3])
print ("array1 :", array1 )
array2 = np . array ([[0] ,[1] ,[2] ,[3]])
print ("array2 :", array2 )
array3 = np . array ([[0 ,1] ,[2 ,3]])
print ("array3 :", array3 )

print("\n")

print ( np . pi )

print("\n")

print ( np . arange (4) ,"\n",
np . arange (0 ,2 ,0.5) ,"\n",
np . linspace (0 ,1.5 ,4),"\n")

list1 = [1 ,2 ,3 ,4 ,5]
array1 = np . array ( list1 )
print ("list1 :", list1 [0] , list1 [4])
print ("array1 :", array1 [0] , array1 [4])
array2 = np . array ([[1 ,2 ,3 ,4 ,5] , [6 ,7 ,8 ,9 ,10]])
list2 = list ( array2 )
print ("array2 :", array2 [0 ,2] , array2 [1 ,4])
print ("list2 :", list2 [0] , list2 [1], "\n")

print ( array2 [: ,2] , array2 [0 ,:], "\n")

print ("1x3:", np . zeros (3) )
print ("2x2:", np . zeros ((2 ,2) ) )
print ("2x3:", np . ones ((2 ,3) ) )

print("\n")

###### Plotting ######

steps = 0.1 # step size
x = np . arange ( -2 ,2+ steps , steps )
y1 = x + 2
y2 = x **2

plt . figure ( figsize =(12 ,8) ) 
plt . subplot (3 ,1 ,1) # subplot 1: subplot format (row , column , number )
plt . plot (x , y1 ) # choosing plot variables for x and y axes
plt . title ("Lab 1 Sample Plots") # title for entire figure

plt . ylabel ("Subplot 1") # label for subplot 1
plt . grid ( True ) # show grid on plot

plt . subplot (3 ,1 ,2) # subplot 2
plt . plot (x , y2 )

plt . ylabel ("Subplot 2") # label for subplot 2
plt . grid ( which ='both') # use major and minor grids

plt . subplot (3 ,1 ,3) # subplot 3
plt . plot (x , y1 ,"--r", label ="y1 ")
plt . plot (x , y2 ,"o", label ="y2 ") # plotting both functions on one plot
plt . axis ([ -2.5 , 2.5 , -0.5 , 4.5]) # define axis
plt . grid ( True )
plt . legend ( loc ="lower right") # prints legend on the plot
plt . xlabel ("x") # x- axis label for all three subplots ( entire figure )
plt . ylabel ("Subplot 3") # label for subplot 3
plt . show ()

###### Complex Numbers ######

cRect = 2 + 3j
print ( cRect )

cPol = abs( cRect ) * np . exp (1j * np . angle ( cRect ) )
print ( cPol ) # stores in rectangular form

cRect2 = np . real ( cPol ) + 1j * np . imag ( cPol )
print ( cRect2 ) # converting from polar to rectangular

#print ("\n", np . sqrt (3*5 - 5*5) )

print ("\n", np . sqrt (3*5 - 5*5 + 0j ) )




