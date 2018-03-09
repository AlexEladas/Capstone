import csv
import math
import sys
#import pyttsx3
import os
import subprocess

def main(arg):
    pri = 1.0/7.0
    test = arg
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
    letters = ['ay','b','c','d','e','water','help','f','g','h','i','j','bathroom','hungry','thank you']
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
    if finald[max(final)] == 'c' or finald[max(final)] == 'thank you':
        if (max(final) * 10 ** 17) < (-10 ** -(3)):
            return 0

    if (max(final) * 10**17) < (-10**-(20)):
        return 0
    else:
        cmd = """pico2wave -w output.wav "<volume level = '100'> {a}" && aplay output.wav""".format( a= finald[max(final)])
        subprocess.call(cmd, shell=True)
        os.system("rm lookdave.wav")
        return 0

if __name__ == "__main__":
    main(sys.argv[1:])
