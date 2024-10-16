import csv
from packageobject import packageObj
from hashtable import ChainingHashTable

# initialize the lists that I will be using to store the data
# and later access it
packageList = []
distanceTable = []
distancematrix = []


# uses the distance table to first place into an array, and then divide that array into a matrix
def populatedistancematrix():
    # use count to skip the first lines of csv file that dont have data
    count = 0

    # Open the CSV file in read mode
    #big O = O(n^3)
    with open('WGUPSDistanceTable2.csv', 'r') as csvfile:
        # Create a reader object
        csv_reader = csv.reader(csvfile)

        # Iterate through the rows in the CSV file skipping the first 7 rows
        for row in csv_reader:
            if count < 7:
                count += 1
                continue

            # append the rows to distance table
            distanceTable.append(row)

    # This is used to append the data from distance table into a matrix distanceMatrix to look up the distances between
    # points
    for j in range(len(distanceTable)):
        r = []
        for i in distanceTable[j][:]:
            r.append(i)
        distancematrix.append(r)

    # return the distance matrix for the algorithm (nearest neighbor)
    return distancematrix


# reads the package table and puts each row into a list, then each index in the list is made into
# a package object with the next data as its traits
# big o = O(n^3)
def populatePackageTable():
    # Open the CSV file in read mode
    with open('WGUPS Package File.csv', 'r') as csvfile:
        # Create a reader object
        csv_reader = csv.reader(csvfile)

        # Iterate through the rows in the CSV file
        for row in csv_reader:
            # Access each element in the row
            packageList.append(row)

    # create objects array to hold the packageObj's
    objects = []

    # remove the first index which held bad data
    packageList.pop(0)

    # instantiate a list of objects from the packageList data into objects list to load into hash table
    for item in packageList:
        package = packageObj(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
        objects.append(package)

    # make packageTable variable a hashTable type
    packageTable = ChainingHashTable()

    # populate the packageTable (hashTable) with the packages
    for obj in objects:
        packageTable.insert(key=obj.packageID, item=obj)

    return packageTable
