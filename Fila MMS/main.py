import sys

import numpy as np
import random
import math
import Persona, Caja
import matplotlib.pyplot as plt


def exponencial_distribution(lbma):
    div = 1 / (-1 / lbma) * (np.log(random.random()))
    return int(round(60 * div, 0))


def poisson(mi):
    l = math.exp(-mi)
    p = 1
    k = 0
    k += 1
    p *= random.random()
    while p > l:
        k += 1
        p *= random.random()
    return k - 1


if __name__ == '__main__':
    # Declare all control variables
    timer = 0                   # Will control time
    slots = 100                 # Number of slots people can go in
    slotsList = []              # Slots's list
    queue = []                  # People's list
    poissonAverage = 50         # Average people that will come per hout
    exponencialLambda = 0.25    # Average % of an hour people will stay in a slot
    peoplePerHour = []          # People in the system per hour list
    hoursSimulated = 10         # Hours simulated per N slots
    currentBest = 2147483645    # Control variable to achieve the target 10 average people per hour
    # While we have not reached our target
    while currentBest > 10:
        # Create a N slots list
        for i in range(slots):
            slotsList.append(Caja.Caja())
        # Simulate per minute
        for i in range(hoursSimulated*60):
            # Set new batch of people at the start of each hour
            if timer == 0:
                # Get random number of people to add
                for n in range(poisson(poissonAverage)):
                    # Add them one by one while getting them a random amount of time they'll spend in the queue
                    queue.append(Persona.Persona(exponencial_distribution(exponencialLambda)))
            # Check each slot to see if it's empty
            for c in slotsList:
                # If it's empty put the first person in queue in there
                if c.persona is None and len(queue) > 0:
                    c.persona = queue.pop(0)
                # If not then advance the time of the person in there
                elif c.persona is not None:
                    c.persona.advanceTime()
                    # It the person finishes make them go away
                    if c.persona.tiempo <= 0:
                        c.persona = None
                        # If the list has people left put them in the slot
                        if len(queue) > 0:
                            c.persona = queue.pop(0)
            # Before changing hour, count how many people are in the queue
            if timer == 59:
                peopleInQueue = len(queue)
                # And how many people are in a slot
                for c in slotsList:
                    if c.persona is not None:
                        peopleInQueue += 1
                # Add the number of persons in that hour to a list
                peoplePerHour.append(peopleInQueue)
                # Change hour
                timer = 0
            else:
                timer += 1
        # Get the average of people per hour
        roundedAverage = round(np.average(peoplePerHour))
        # Print to visualize data
        print('Con {0} cajas, el promedio de personas en total es de {1}'.format(slots, roundedAverage))
        # See if we have improved towards our target
        currentBest = roundedAverage if roundedAverage < currentBest else currentBest
        # Reset the queue and slot list
        slotsList.clear()
        queue.clear()
        # Add another slot
        slots += 1
        # Reset the timer and simulate again
        timer = 0

