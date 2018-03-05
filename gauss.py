import csv
import math
import sys
#import pyttsx3

pri = 0.2
test = sys.argv[1:]


def gauss(mean, variance, feature):
    p = (1/math.sqrt(2*math.pi*variance))*math.exp((-(feature - mean)**2)/2*variance)
    return p

with open('mean.csv', 'r') as f:
    reader = csv.reader(f)
    m = list(reader)

mean_list = [lst[1:] for lst in m]

with open('variance.csv', 'r') as f:
    reader = csv.reader(f)
    v = list(reader)

variance_list = [lst[1:] for lst in v]
final = []
finald = {}
letters = ['a','b','c','d','e']
for i in range(len(mean_list)):
    score = 1
    for mean,variance, value in zip(mean_list[i],variance_list[i],test):
        score *= gauss(float(mean),float(variance),float(value))
    score *= pri
    print("Class "+letters[i] +": " + str(score))
    finald[score] = letters[i]
    final.append(score)
#engine = pyttsx3.init()
#engine.say(finald[max(final)])
#engine.say("Hungry")
#engine.say("Water")
#engine.runAndWait()
