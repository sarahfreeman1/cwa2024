#import statements here
import pandas as pd
from statistics import mean
import csv
import serial
from time import sleep
#function to give a remark on my mood based on avg_mood value
def interpret_mood(avg_mood):
    if avg_mood >= 9:
        return "Excellent mood today, thank god"
    elif avg_mood <  5:
        return "Middlin today, thanks for asking"
    elif 5 <= avg_mood < 9:
        return "Improving thanks."
    else:
        return "Not really sure, not enough info \n"
#Take them in as integers, as all inputs default to strings
spiritual_wellbeing = int(input("On a scale of 1-10 from bad to good, how spiritual are you feeling?"))
physical_wellbeing = int(input("On a scale of 1-10 from lazy to energetic, how much energy do you have?"))
mental_wellbeing = int(input("On a scale of 1-10 from depressed to very happy, how are you feeling mentally ?"))
avg_mood = round(mean([spiritual_wellbeing,physical_wellbeing,mental_wellbeing]),2)
mood_remark = interpret_mood(avg_mood)
print("My Average mood today is ",mood_remark, " ", avg_mood)
df = pd.read_csv('Microbitdata.csv')
print(df)
# Convert 'Timestamp' column to datetime, is it necessary
#df['time (seconds)'] = pd.to_datetime(df['time (seconds)'], errors='coerce')
app_use = df['use'].min()
app_donotuse = df['do not use'].max()
app_sometimes = df['sometimes'].mean()
print (app_use,app_donotuse,app_sometimes, avg_mood)
f = open("BR1-3_105688-2.csv", "a", newline='')
csver = csv.writer(f)

csver.writerow([app_use, app_donotuse, app_sometimes, avg_mood])
f.close()