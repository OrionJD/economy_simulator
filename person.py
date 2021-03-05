import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# This is a thing that creates a x-y plot for age-productivity values
x = np.arange(0, 80, 1)

#create range of y-values that correspond to normal pdf with mean=30 and sd=40 
y = norm.pdf(x, 30, 40)

#define plot 
fig, ax = plt.subplots(figsize=(10,10))
ax.plot(x,y)


# This generates random personalities that affect productivity and food consumption of Person objects

class Personality:
    food_modifier = None
    productivity_modifier = None

    def __init__(self):
        self.food_modifier = random.randint(0,2)
        self.productivity_modifier = random.randint(-50, 50) / 100


# This is where you can create a person
class Person:
    name = None
    age = None # between 0 - 80
    productivity = None # between 1 and 2
    personality = None # randomly determined by calling a Personality object
    skill_level = None # randomly determined by probability
    employed = False # a boolean to determinte if they're eligible for employment
    food_consumed = None # between 1 and 3, causes unhappiness if not met
    happiness = None # between -1 and 1. 1 being very happy, and -1 being very angry
    potential = None # this variable determines how much money their skill and productivity will make them on the market


    # Here's the constructor which creates actual person objects

    def __init__(self):

        # this generates the name
        given = random.choice(open('given_names.txt').readlines()).rstrip().capitalize()
        surname = random.choice(open('surnames.txt').readlines()).rstrip().capitalize()
        full = given + " " + surname

        # this creates their personality
        personality = Personality()

        # this initializes all the variables
        self.name = full

        self.age = random.randint(0, 79)

        self.skill_level = random.choice(["low", "medium", "medium", "high"])

        self.food_consumed = 1 + personality.food_modifier # eventually i'm going to make a thing where if they don't have enough food they get unhappy

        self.happiness = 0.25 # i'm placeholding until i can figure out how to make this work

        self.productivity = round(((y[self.age] * 100) + personality.productivity_modifier + self.happiness), 2)

        if self.skill_level == "low":
            self.potential = self.productivity * 20000
        elif self.skill_level == "medium":
            self.potential = self.productivity * 75000
        elif self.skill_level == "high":
            self.potential = self.productivity * 300000
        else:
            print("error")

        self.potential = round(self.potential)









dude = Person()
print()
print(f"name: {dude.name}")
print(f"age: {dude.age}")
print(f"productivity value: {dude.productivity}")
print(f"employed status: {dude.employed}")
print(f"food consumption per cycle: {dude.food_consumed}")
print(f"skill level: {dude.skill_level}")
print(f"income potential: {dude.potential}")
print()