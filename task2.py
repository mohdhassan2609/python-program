#given an integer ,perform the following conditional actions:if N is odd, print Weird  if N is even and in inclusive range of 2 to 5,print Not Weird  if N is even  and in the inclusive range 6 to 20,print Weird    if N is even and greater than 20,print Not Weird  input format:a single line containing a positive integer,contraints:1<=N<=100 output format:print Weird if the number is Weird;otherwisw print Not Weird


import math
import os
import random 
import re
import sys
N=int(input())
if(1<=N<=100)
  if(N%2==0)
     if(2<=N<=5)
         print("Not Weird")
         
     if(6<=N<=20)
         print("Weird")
     if(N>20)
         print("Not Weird")  
  else:
      print("Weird")
