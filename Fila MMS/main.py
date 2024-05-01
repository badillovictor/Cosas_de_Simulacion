import math
import random

import numpy as np

import Person
import Slot


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
    slots = 1                   # Number of slots people can go in
    slotsList = []              # Slots's list
    queue = []                  # People's list
    poissonAverage = 50         # Average people that will come per hour
    exponencialLambda = 0.25    # Average % of an hour people will stay in a slot
    peoplePerHour = []          # People in the system per hour list
    hoursSimulated = 100        # Hours simulated per N slots
    currentBest = 2147483645    # Control variable to achieve the target 10 average people per hour
    # While we have not reached our target
    while currentBest > 10:
        # Create a N slots list
        for i in range(slots):
            slotsList.append(Slot.Slot())
        # Simulate per minute
        for i in range(hoursSimulated*60):
            # Set new batch of people at the start of each hour
            if timer == 0:
                # Get random number of people to add
                for n in range(poisson(poissonAverage)):
                    # Add them one by one while getting them a random amount of time they'll spend in the queue
                    queue.append(Person.Person(exponencial_distribution(exponencialLambda)))
            # Check each slot to see if it's empty
            for slot in slotsList:
                # If it's empty put the first person in queue in there
                if slot.person is None and len(queue) > 0:
                    slot.person = queue.pop(0)
                # If not then advance the time of the person in there
                elif slot.person is not None:
                    slot.person.advanceTime()
                    # It the person finishes make them go away
                    if slot.person.time <= 0:
                        slot.person = None
                        # If the list has people left put them in the slot
                        if len(queue) > 0:
                            slot.person = queue.pop(0)
            # Before changing hour, count how many people are in the queue
            if timer == 59:
                peopleInQueue = len(queue)
                # And how many people are in a slot
                for slot in slotsList:
                    if slot.person is not None:
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
        # Reset the queue, peoplePerHour and slot lists
        slotsList.clear()
        peoplePerHour.clear()
        queue.clear()
        # Add another slot
        slots += 1
        # Reset the timer and simulate again
        timer = 0

