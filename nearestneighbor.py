from hashtable import *
from csvreader import *
from truck import *
from packageobject import *
from timekeeping import *

# Loads the 3 trucks with the packages to be delivered
truck1 = manual_load_truck_1()
truck2 = manual_load_truck_2()
truck1_trip2 = manual_load_truck_1_trip2()

# creates an instance of the distance matrix to use for finding the next closest package
distancematrix = populatedistancematrix()
# uses combined distance to find the total distance traveled to ensure it is < 140
combineddistance = 0
# tracks the distance each truck takes
distancefromtruck = 0
# used to calculate how long each delivery takes
timetaken = 0
# creates a time database to store all of my times of delivery
database = timedatabase()


# finds the next package that should be delivered by comparing the current location of the
# truck (last delivery or the hub for starting) to the delivery location of each package to find which is closest
# big O = O(n) but with use of getfloatdistance() which is big o(n^4) gives
# total big O = O(n^5)
def findnextdelivery(currenttruck, startpoint):
    # compare the startpoint with each package using the getfloat distance, and store the losest distance and which package
    # it is
    startaddress = startpoint
    nextaddress = ''
    currclosestdistance = 100
    packagedelivered = None

    for i in currenttruck.packages:
        #fixes package 9 with the correct address and will always happen after 10:20 due to my algo speed
        if i.getid() == '9':
            i.setaddress('410 S State St')
            i.setzip('84111')
        # accounts for the packages that are already delivered
        if 'delivered' in i.getStatus():
            continue
        # compares the distances of the packages delivery locations to the current truck location
        # and if it is a shorter distance, it sets that package to be delivered next
        if getfloatdistance(startaddress, i.getaddress()) < currclosestdistance:
            currclosestdistance = getfloatdistance(startaddress, i.getaddress())
            nextaddress = i.getaddress()
            packagedelivered = i
    return currclosestdistance, nextaddress, packagedelivered


# deliveryfunction first sets all the packages that are on the truck to status: en route
# then stores that initial time as a time stamp into my timestorage database
# then uses findnextdelivery to find the closest package, delivers it, time stamps it, adds the total distance
# then adds the delivery to a queue which keeps track of the packages delivered until they are all delivered
# it uses the mileage to calculate time, and ensures that if other packages go to the same address, that they
# are delivered with the first package to that location
# big O = o(n^3) but with the use of findnextdelivery(O(n^5)) results in
# total big O = O(n^8)
def deliveryfunction(currenttruck, currenttime):
    # uses queue to store delivered packages
    queue = []
    # uses totaldistance to track miles traveled
    totaldistance = 0
    # uses minutestaken to add the time to my total time
    minutestaken = 0

    # set all packages as en route
    for i in currenttruck.packages:
        i.setstatus(f'en route on truck: {truckname(currenttruck)}')

    # stores a snapshot of all packages at the beginning of this delivery route
    timestorage(currenttime)

    # Finds the first delivery and stores its distance, address, and package
    closestdistance, nextaddress, packagedelivered = findnextdelivery(currenttruck, 'Western Governors University\n4001 South 700 East, \nSalt Lake City, UT 84107')
    # sets the package status as delivered
    packagedelivered.setstatus(f'delivered at: {currenttime} by {truckname(currenttruck)}')
    # adds to the total distance traveled
    totaldistance = totaldistance + closestdistance

    # used for all deliveries after the first, does all of the above and checks if other packages should
    # be delivered to that address as well, includes an exit for the loop once deliver is complete
    while len(queue) < len(currenttruck.packages):
        queue.append(packagedelivered)
        # checks if other packages on the truck should be delivered to the same address
        for h in currenttruck.packages:
            if h.getaddress() == nextaddress and 'delivered' not in h.getStatus():
                queue.append(h)
                h.setstatus(f'delivered at: {currenttime} by {truckname(currenttruck)}')

        # time functions here
        # converts the miles taken to minutes
        minutestaken = milestominutes(closestdistance)
        # adds the time taken for delivery to the clock
        currenttime = addminutestodatetime(currenttime, minutestaken)
        # stores a snapshot of deliveries at that time
        timestorage(currenttime)

        # begins the next delivery
        closestdistance, nextaddress, packagedelivered = findnextdelivery(currenttruck, nextaddress)
        # exit condition if all packages are delivered
        if packagedelivered is None:
            break
        packagedelivered.setstatus(f'delivered at: {currenttime} by {truckname(currenttruck)}')
        # adds to the total distance traveled in order to ensure < 140
        totaldistance = totaldistance + closestdistance

    return totaldistance, currenttime

# getfloat distance is used to locate the distance between to addresses on my distance matrix,
# it uses findrowindex and findcolumnindex which are both O(n) time
# total big O due to function use is
# big O = O(n^4)
def getfloatdistance(node, nextnode):
    # gets the index location for both addresses on the column and row side
    noderow = findrowindex(node)
    nodecolumn = findcolumnindex(node)
    nextnoderow = findrowindex(nextnode)
    nextnodecolumn = findcolumnindex(nextnode)
    distance = 0

    # used to find the distance, since only half the table is filled, I needed two
    # if statements on whether to access from the column or row side
    if distancematrix[noderow][nextnodecolumn] != '':
        distance = float(distancematrix[noderow][nextnodecolumn])
        # print('first if statement')
        return distance
    elif distancematrix[nextnoderow][nodecolumn] != '':
        distance = float(distancematrix[nextnoderow][nodecolumn])
        # print('second if statement')
        return distance
    else:
        return "not working"


# findcolumnindex is used to locate and address on the distance matrix
# big O = O(n)
def findcolumnindex(node):
    # count is used to find the index of the top row of my matrix for what location the package is currently at
    count = 0

    # searches for where the package location is currently on the adjacency matrix
    for index in distancematrix[0]:
        if node in index:
            currcolumnindex = count
            break
        count += 1

    return currcolumnindex


# findrowindex is used to find where an address is located on the distance matrix
# big O = O(n)
def findrowindex(node):
    # count is used to find the index of the top row of my matrix for what location the package is currently at
    count = 0
    for i in range(len(distancematrix)):
        # searches for where the package location is currently on the adjacency matrix
        if str(node) in distancematrix[i][0]:
            currrowindex = count
            break

        count += 1

    return currrowindex

# timestorage is used to store the data of all the packages into a dictionary using addtimetodict
# with the time of the delivery as the key, ensuring there is data for every time a package is delivered
# uses fulldata() with big o of O(n)
# big O = O(n)
def timestorage(currenttime):
    times = []
    times.append(fulldata())
    database.addtimetodict(currenttime, times)

    # print(times)


# fulldata is used to get the information from every package into an array to present to the user when requested
# big O = o(n)
def fulldata():
    array1 = []
    for i in range(41):
        array1.append(str(packageTable.search(str(i))))
    return array1


# runsimulation executes my full delivery service
# first truck begins delivery at 08:00:00 and the other trucks start when the one before finishes
# combined distance is then used to store the total distance traveled by all trucks
# big O = O(n^8)
def runsimulation():
    # used to track total distance
    combineddistance = 0
    # used to begin the clock at 08:00:00
    starttime = minutestodatetime(480)

    # runs the first trucks deliveries
    distancefromtruck, starttime = deliveryfunction(truck1, starttime)
    combineddistance = combineddistance + distancefromtruck
    print('Time that truck 1 finished at: ', starttime)

    # runs the second trip of truck1's deliveries
    distancefromtruck, starttime = deliveryfunction(truck1_trip2, starttime)
    combineddistance = combineddistance + distancefromtruck
    print('Time that truck 1, trip 2 finished at: ', starttime)

    # runs truck 2's deliveries
    distancefromtruck, starttime = deliveryfunction(truck2, starttime)
    combineddistance = combineddistance + distancefromtruck
    print('Time that truck 2 finished at: ', starttime)

    # prints the total distance in miles
    print('Combineddistance: ', combineddistance, " miles")

# used to find get the truck name for printing to the console
def truckname(truck):
    if truck == truck1:
        return "truck 1"
    if truck == truck1_trip2:
        return "truck 1, trip 2"
    if truck == truck2:
        return "truck 2"