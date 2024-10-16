from packageobject import *
from csvreader import *
from hashtable import *
from csvreader import *


# creates a truck class that to deliver all the packages, has a constructor and an add function
class truck:
    def __init__(self):
        self.SPEED = 18
        self.id = id
        self.packages = []
        self.packageCount = 0
        self.timeleaving = 0
        self.distancetraveled = 0

    # add_package is used to add a package to the trucks package list
    # big O = O(1)
    def add_package(self, package):
        self.packages.append(package)
        self.packageCount += 1

# construct the package table to load the trucks
packageTable = populatePackageTable()

# the function to populate truck 1
# big O = O(n)
def manual_load_truck_1():
    truck1 = truck()
    truck1.add_package(packageTable.search('1'))
    truck1.add_package(packageTable.search('29'))
    truck1.add_package(packageTable.search('7'))
    truck1.add_package(packageTable.search('30'))
    truck1.add_package(packageTable.search('8'))
    truck1.add_package(packageTable.search('34'))
    truck1.add_package(packageTable.search('40'))
    truck1.add_package(packageTable.search('13'))
    truck1.add_package(packageTable.search('39'))
    truck1.add_package(packageTable.search('14'))
    truck1.add_package(packageTable.search('15'))
    truck1.add_package(packageTable.search('16'))
    truck1.add_package(packageTable.search('19'))
    truck1.add_package(packageTable.search('20'))
    truck1.add_package(packageTable.search('37'))
    #set status of packages as "at hub"
    for package in truck1.packages:
        package.setstatus('at hub')

    return truck1

# the function to populate truck 1 trip 2
# big O = O(n)
def manual_load_truck_1_trip2():
    truck1_trip2 = truck()
    truck1_trip2.add_package(packageTable.search('6'))
    truck1_trip2.add_package(packageTable.search('5'))
    truck1_trip2.add_package(packageTable.search('21'))
    truck1_trip2.add_package(packageTable.search('4'))
    truck1_trip2.add_package(packageTable.search('24'))
    truck1_trip2.add_package(packageTable.search('23'))
    truck1_trip2.add_package(packageTable.search('26'))
    truck1_trip2.add_package(packageTable.search('22'))
    truck1_trip2.add_package(packageTable.search('10'))
    truck1_trip2.add_package(packageTable.search('11'))
    truck1_trip2.add_package(packageTable.search('31'))
    truck1_trip2.add_package(packageTable.search('25'))

    # set status of packages as "at hub"
    for package in truck1_trip2.packages:
        package.setstatus('at hub')

    return truck1_trip2


# the function to populate truck 2
# big O = O(n)
def manual_load_truck_2():
    truck2 = truck()
    truck2.add_package(packageTable.search('17'))
    truck2.add_package(packageTable.search('12'))
    # truck2.add_package(packageTable.search('25'))
    truck2.add_package(packageTable.search('28'))
    truck2.add_package(packageTable.search('32'))
    truck2.add_package(packageTable.search('3'))
    truck2.add_package(packageTable.search('18'))
    truck2.add_package(packageTable.search('36'))
    truck2.add_package(packageTable.search('38'))
    truck2.add_package(packageTable.search('27'))
    truck2.add_package(packageTable.search('35'))
    truck2.add_package(packageTable.search('2'))
    truck2.add_package(packageTable.search('33'))
    truck2.add_package(packageTable.search('9'))

    # set status of packages as "at hub"
    for package in truck2.packages:
        package.setstatus('at hub')

    return truck2


# used to find get the truck name for printing to the console
def truckname(truck):
    if truck == truck1:
        return "truck 1"
    if truck == truck1_trip2:
        return "truck 1, trip 2"
    if truck == truck2:
        return "truck 2"