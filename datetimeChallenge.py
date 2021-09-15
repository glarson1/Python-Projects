#The challenge was this
"""The Portland-based company you work for just opened two new branches.
One is in New York City, the other in London.
They need a very simple program to find out if the branches are open or closed. The hours of both branches are 9:00 a.m.-5:00 p.m. in their own time zone.

Import the datetime module and any others to aid in time zone calculations.

Create a script that will find out the current times in the Portland HQ and NYC and London branches. Then, compare that time with each branch's hours to see if they are open or closed.

Print out to the screen the three branches and whether they are open or closed. """



import datetime
import pytz #this is an api with all timezones and what not 



EST = pytz.timezone('America/New_York') #formatted in the syntax that pytz is happy with

york = datetime.datetime.now(EST) #datetime.datetime.now() gets the datetime for right now. pass in EST for the time in America/New York or var EST

BST = pytz.timezone('Europe/London')

london = datetime.datetime.now(BST)

PST = pytz.timezone('America/Los_Angeles')

portland = datetime.datetime.now(PST)

print("The time in New York is currently " +york.strftime("%I:%M %p"))

print("The time in London is currently " +london.strftime("%I:%M %p"))

print("The time in Portland is currently " + portland.strftime("%I:%M %p"))

def todayAtLondon (hr, min=0, sec=0, micros=0):
   now = datetime.datetime.now(BST)
   return now.replace(hour=hr, minute=min, second=sec, microsecond=micros)


if london < todayAtLondon (9) or london > todayAtLondon (17):
   print("The London branch is not open")
else:
    print("The London branch is open")


def todayAtNewYork (hr, min=0, sec=0, micros=0):
   now = datetime.datetime.now(EST)
   return now.replace(hour=hr, minute=min, second=sec, microsecond=micros)


if york < todayAtNewYork (9) or york > todayAtNewYork (17):
   print("The New York branch is not open")
else:
    print("The New York branch is open")

def todayAtPortland (hr, min=0, sec=0, micros=0):
   now = datetime.datetime.now(PST)
   return now.replace(hour=hr, minute=min, second=sec, microsecond=micros)


if york < todayAtPortland (9) or york > todayAtPortland (17):
   print("The Portland branch is not open")
else:
    print("The Portland branch is open")    
