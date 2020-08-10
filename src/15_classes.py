# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
''' 
Parent class 
'''


class LatLon:
    def __init__(self, lat, lon):
        ''' Initialize lat and lon attributes'''
        self.lat = lat
        self.lon = lon


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
''' 
Child class of LatLon 
'''


class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        self.name = name
        super().__init__(lat, lon)
# makes it readable

    def __str__(self):
        return " {}: Lat: {}, Lon: {} ".format(self.name, self.lat, self.lon)


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
''' 
Geocache is the child of Waypoint 
'''
'''
Polymorphism (however you spell it) -  but since we did it inside geocache and as self it overrided (sp?) it and printed it out like we wanted it to for geocache

Basically Polymorphism... is the child overridding the parent method
'''
class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        self.difficulty = difficulty
        self.size = size
        ''' inherit attributes from parent Waypoint '''
        super().__init__(name, lat, lon)
#shorter way to format. 0 = first argument passed to .format. Can access attributes by dot notation
    def __str__(self):
        return " {0.name}: , Diff: {0.difficulty}, Size: {0.size}, Lat: {0.lat}, Lon: {0.lon}".format(self)


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
# YOUR CODE HERE

'''
w1 and geo1 are objects 

'''
w1 = Waypoint('Catacombs', 41.70505, -121.51521)
print('New Waypoint: ', w1)
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method

print('Printed again with ___str___ method: ', w1)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geo1 = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
# Print it--also make this print more nicely
print('Geocache: ', geo1)
