# creates a package object which will hold each package as an object and all the data with it
class packageObj:

    # constructor
    def __init__(self, packageID, address, city, state, zip, deadline, weight, status='hub'):
        self.packageID = packageID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.status = status

    # prints all of the objects data
    def __str__(self):
        return f'ID: {self.packageID}, address: {self.address}, city: {self.city}, state: {self.state}, zip: {self.zip}, Deadline: {self.deadline}, weight: {self.weight}, status: {self.status}'

    # returns the information of the object
    def getInfo(self, packageID):
        return self.address, self.city, self.state, self.zip, self.deadline, self.weight, self.status

    # returns the deadline of the package
    def getDeadline(self, packageID):
        return self.deadline

    # returns the status of the package
    def getStatus(self):
        return self.status

    # sets the status of the package
    def setstatus(self, status):
        self.status = status

    # gets the ID of the package
    def getid(self):
        return self.packageID

    # gets the address of the package
    def getaddress(self):
        return self.address

    # sets the address of the package (used for package 9)
    def setaddress(self, address):
        self.address = address

    # sets the zip of the package (used for package 9)
    def setzip(self, zip):
        self.zip = zip
