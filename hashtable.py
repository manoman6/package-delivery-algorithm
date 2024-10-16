from packageobject import packageObj


# Creates my hashTable using chaining to prevent collisions
class ChainingHashTable:
    # def _init_ is my constructor
    # self refers to the instance of the class upon calling the method
    # initial capacity will set the size of the array, or to 10 as the default, making it an optional parameter
    # big-O time complexity: 0(n)
    def __init__(self, initial_capactiy=10):
        # initializes the hash table with empty bucket list elements
        self.table = []
        for i in range(initial_capactiy):
            self.table.append([])

    # used to insert a new item into my hash table
    # big-O time complexity: 0(n)
    def insert(self, key, item):
        # this will include my hash function which will determine where my item will go
        # gets the bucket list where the new element will go
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update the key if it already exists in the bucket
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, inserts the items to the end of the buckets list to prevent repeats
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # the search function will look for an item within the hash table with a matching key
    # then it will return the item if found, or "None" if not found
    # big-O time complexity: 0(n)
    def search(self, key):
        # first find the bucket list where the key would be found
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        for key_value in bucket_list:
            # if the key value matches the key of the element
            if key_value[0] == key:
                # returns the info associated with the key
                return key_value[1]
        # if no key is found that matches key value, then nothing is returned
        return None

    # remove function take away an item with matching key from the hash table
    # big-O time complexity: 0(n)
    def remove(self, key):
        # get the bucket list where the item will be removed from
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if the it is found
        for key_value in bucket_list:
            if key_value[0] == key:
                bucket_list.remove(key_value[0],key_value[1])

    # The goal is to get the lookup function to use the ChainingHashTable search function to retrieve the object given
    # the packageID, then retrieve and return its address, city, state, zip, deadline, weight,
    # and status to the user using the packageObj.getInfo function which takes a packageID as the argument
    # big-O time complexity: 0(1)
    def lookup(self, key):
        # first determines if the key(packageID) is found within the hash table
        # if so, then it will assign variable package with the object at the key, and then return its info using getinfo
        if self.search(key) != None:
            package = self.search(key)
            return package.getInfo(key)
        # if the key is not found in the hash table, it will return that the packageID is not found in the system
        else:
            return "Package ID was not found within the system"

    # getstatus function finds the key within the dict and then returns the current status of that
    # package, if not found it returns a not found statement
    # big-O time complexity: 0(1)
    def getStatus(self, key):
        # first determines if the key(packageID) is found within the hash table
        # if so, then it will assign variable package with the object at the key, and then return its info using getinfo
        if self.search(key) != None:
            package = self.search(key)
            return package.getStatus(key)
        # if the key is not found in the hash table, it will return that the packageID is not found in the system
        else:
            return "Package ID was not found within the system"

