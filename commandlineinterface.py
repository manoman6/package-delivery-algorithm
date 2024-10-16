from nearestneighbor import *
from timekeeping import *


# find_nearest_time is used to take the users input time and find the (floor) closest time to that
# which was saved to the time dictionary Sources: (W3schools.com), (Christopher MarkietaChristopher Markieta & PaulGPaulG, 2012)
# big O = O(n)
def find_nearest_time(user_input):
    # sorts the keys of the timedit which are all the times that a package was delivered to list sortedtimes
    sorted_times = sorted(database.timedict.keys(), key=lambda x: datetime.strptime(x, '%H:%M:%S').time())

    # Convert user input to a datetime.time object
    # takes the user's input and converts it to a datetime to be used for comparison
    user_time = datetime.strptime(user_input, '%H:%M:%S').time()

    # lasttime will hold the last matching time
    last_time = None

    # Iterates over sorted time keys
    for timekey in sorted_times:
        # changes the currenttime to a datetime format for evaluation to the usertime
        current_time = datetime.strptime(timekey, '%H:%M:%S').time()

        # checks if the user's time is before the current time
        if user_time < current_time:
            break
        # if the user time is greater than the time, then I know the lasttime noted was the floor of the time asked
        last_time = timekey

    return database.timedict[last_time] if last_time else None


# used to print all of the packages at the time closest to when the user requested
# uses findnearest time which is O(n)
# big O = O(n^2)
def printformattedresponse(time):
    targetarray = find_nearest_time(time)
    # used to remove None from the dictionary entry
    del targetarray[0][0]
    # prints the results in a row for each package
    for index in targetarray[0]:
        print(index)

# userinteractive is used as my commandline interface with the user
# big O = O(n) but uses printformattedrespone which is o(n^2)
# big O = O(n^3)
def userinteractive():
    responsetime = ''
    # ensures an exit from the loop if the user is done with the program
    while responsetime != 'q':
        print('Delivery service begins at 08:00:00.\nTo quit the evaluation service enter \'q\'\nPlease enter a time to check the status of delivery in format HH:MM:SS: ')
        responsetime = input()
        if responsetime == 'q':
            continue
        # ensures that the user does not ask for a time prior to deliver service beginning
        if responsetime < '08:00:00':
            print('That is before delivery service has begun.')
            continue
        printformattedresponse(responsetime)