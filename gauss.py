import csv
import math
import sys
#import pyttsx3
import os
pri = 1.0/7.0
test = sys.argv[1:]
print (pri)

def gauss(mean, variance, feature):
    p = ((1/math.sqrt(2*math.pi*variance))*math.exp(-((feature - mean)**2)/(2*variance)))
    return p

with open('mean.csv', 'r') as f:
    reader = csv.reader(f)
    m = list(reader)

mean_list = [lst[1:] for lst in m]
print (mean_list)
with open('variance.csv', 'r') as f:
    reader = csv.reader(f)
    v = list(reader)

variance_list = [lst[1:] for lst in v]
print (variance_list)
final = []
finald = {}
letters = ['a','b','c','d','e','water','help']
for i in range(len(mean_list)):
    score = 1.0
    for mean,variance, value in zip(mean_list[i],variance_list[i],test):
        score *= gauss(float(mean),float(variance),float(value))
    score *= pri
    print("Class "+letters[i] +": " + str(score))
    finald[score] = letters[i]
    final.append(score)
#engine = pyttsx3.init()
#engine.say(finald[max(final)])
os.system("pico2wave -w lookdave.wav {b} && aplay lookdave.wav".format(b= finald[max(final)]))
os.system("rm lookdave.wav")
#engine.runAndWait()
