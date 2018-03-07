#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 19:56:58 2018

@author: mirandayuan
"""

import numpy as np 
#Transmission Probabilities (order:Verb, Noun, Adv.) e1
#TProb = [[0.3,0.2,0],[0.1,0.4,0.4],[0.3,0.1,0.1],[0,0,0.1]]
TProb = [[3,2,0],[1,4,4],[3,1,1],[0,0,0.1]]
#Emission Probabilities e3
#EProb = [[0.003,0.001,0],[0.004,0.003,0],[0,0,0.002]]
EProb = [[3,1,0],[4,3,0],[0,0,2]]
sentence = ["learning","changes","throughly"]
size = len(sentence)

#initially
Viterbi = [[0 for i in range(size)] for i in range(size + 1)]
Viterbi[0] = [1,0,0]
result = [0 for i in range(size+1)]

#Start
Viterbi[1] = np.multiply(np.multiply(Viterbi[0][0], TProb[0]), EProb[0])
e = 4

#Viterbi Algorithm
for i in range (2,size+1):
    e += 4
    for j in range(0,size):
        temp = np.multiply(np.multiply(Viterbi[i-1][j], TProb[j+1]), EProb[i-1])
        #print(temp)
        if (temp >= Viterbi[i]).all():
            Viterbi[i] = temp
            result[i-1] = j
        #print(Viterbi[i])
        #print(result[i-1])
        #print(e)
#End
End = Viterbi[size] * TProb[size]
result[size] = End[0]
for k in range(0,size):
    if End[k] > result[size]:
        result[size] = k

print("POS of the sentence tokens:")
for v in range(1,size+1):
    print(sentence[v-1])
    if(result[v] == 0):
        print("verb")
    elif(result[v]==1):
        print("noun")
    else:
        print("adv")

print("the probability is: ")
prob = End[size-1] / pow(10,e)
print(prob)

        
    

