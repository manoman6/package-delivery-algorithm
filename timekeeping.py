from datetime import datetime, timedelta


# function to convert float to datetime value
# uses delta time to be able to add to it using another datetime
# takes the minutes taken and converts it into a datetime
# big O = O(1)
def minutestodatetime(minutes):
    # converts minutes to deltatime
    delta_time = timedelta(minutes=minutes)
    # sets the baseline because that is needed for the deltatime to work
    baseline = datetime(2024, 1, 1)
    # adds the minutes taken to the baseline which just results in the minuts converting to the datetime I need
    new_time = baseline + delta_time

    return new_time.strftime('%H:%M:%S')


# addminutestodatetime is used to convert minutes to datetime format and add it to my current time
# essentially acts as my clock
# big O = O(1)
def addminutestodatetime(time_str, minutes):
    # sets time as my current time for deliveries
    time = datetime.strptime(time_str, '%H:%M:%S')

    # sets additional time to the minutes taken in a timedelta form
    additional_time = timedelta(minutes=minutes)

    # sets new time as the addition of the minutes to the current time
    new_time = time + additional_time

    # returns a new time
    return new_time.strftime('%H:%M:%S')


# milestominutes converts the number of miles traveled to minutes using 18mph
# big O = O(1)
def milestominutes(miles):
    minutes = miles / 18 * 60
    return minutes


# timedatabase is a class that keeps a dictionary of all the times that a package is delivered
# used to access the data at user's request
class timedatabase():

    # used as a constructor
    def __init__(self):
        self.temparray = []
        self.timedict = {}

    # used to add an entry into the dictionary
    def addtimetodict(self, time, array1):
        self.timedict[time] = array1

