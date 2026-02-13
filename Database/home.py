
#                VEHICLE CLASS

class Vehicle:
    def __init__(self, vehicleId, make, model):
        self._vehicleId = vehicleId
        self._make = make
        self._model = model

    def getVehicleId(self):
        return self._vehicleId

    def getMake(self):
        return self._make

    def getModel(self):
        return self._model


#                DRIVER CLASS

class Driver:
    def __init__(self, driverId, name, contact, licenseNumber):
        self._driverId = driverId
        self._name = name
        self._contact = contact
        self._licenseNumber = licenseNumber
        self._isOnDuty = False
        self._assignedBus = None

    def getName(self):
        return self._name

    def assignBus(self, bus):
        self._assignedBus = bus
        self._isOnDuty = True



#                   BUS CLASS

class Bus(Vehicle):
    def __init__(self, busId, numberPlate, seatingCapacity, vehicleId, make, model):
        super().__init__(vehicleId, make, model)
        self._busId = busId
        self._numberPlate = numberPlate
        self._seatingCapacity = seatingCapacity
        self._driver = None
        self._route = None

    def assignDriver(self, driver):
        self._driver = driver
        driver.assignBus(self)

    def assignRoute(self, route):
        self._route = route

    def getDriver(self):
        return self._driver

    def getRoute(self):
        return self._route

    def getBusId(self):
        return self._busId

    def getNumberPlate(self):
        return self._numberPlate



#                  STOP CLASS
class Stop:
    def __init__(self, stopId, stopName):
        self._stopId = stopId
        self._stopName = stopName

    def getStopName(self):
        return self._stopName



#                ROUTE CLASS

class Route:
    def __init__(self, routeId):
        self._routeId = routeId
        self._stops = []

    def addStop(self, stop):
        self._stops.append(stop)

    def getStops(self):
        return self._stops

    def getRouteId(self):
        return self._routeId



#              SCHEDULE CLASS

class Schedule:
    def __init__(self, scheduleId, route, bus, departure, arrival, status):
        self._scheduleId = scheduleId
        self._route = route
        self._bus = bus
        self._departure = departure
        self._arrival = arrival
        self._status = status

    def getScheduleInfo(self):
        return f"Schedule :{self._scheduleId}:\n {self._departure} to {self._arrival} ({self._status})"



#              PASSENGER CLASS

class Passenger:
    def __init__(self, passengerId, name):
        self._passengerId = passengerId
        self._name = name

    def getName(self):
        return self._name

#      PERSON Class 

class PersonPassssengers:
    
    def __init__(self,PersonPassssengersID,Name,Address):
       self.PersonPassssengersID=PersonPassssengersID
       self.Name=Name
       self.Address=Address
   
    def __str__(self):
        return f"Nmae :{self.Name},\n Address: {self.Address},\n {self.PersonPassssengersID} "
    
#                TICKET CLASS

class Ticket:
    def __init__(self, ticketId, source, destination, fare, time, passenger):
        self._ticketId = ticketId
        self._source = source
        self._destination = destination
        self._fare = fare
        self._time = time
        self._passenger = passenger

    def getTicketInfo(self):
        return f"Ticket {self._ticketId}:\n {self._source} -> {self._destination},\n Fare: {self._fare},\n Passenger: {self._passenger.getName()}"

    
#              TESTING THE SYSTEM



route1 = Route("R1")


route1.addStop(Stop("S1", "Mall Road"))
route1.addStop(Stop("S2", "Kalma Chowk"))


bus1 = Bus("B1", "ABC-123", 40, "V1", "Honda", "HiAce")


driver1 = Driver("D1", "muhammah", "0333-1234567", "L-1234")


bus1.assignDriver(driver1)
bus1.assignRoute(route1)


schedule1 = Schedule("SCH1", route1, bus1, "8:00 AM", "9:00 AM", "On Time")

passenger1 = Passenger("P1", "Murtaza")
ticket1 = Ticket("T1", "Mall Road", "Kalma Chowk", 50, "7:45 AM", passenger1)
personPassssengers1=PersonPassssengers("murtaza","kohat","002")
 
#                PRINT OUTPUT

print(" BUS DETAILS =")
print("Bus ID:", bus1.getBusId())
print("Number Plate:", bus1.getNumberPlate())
print("Driver:", bus1.getDriver().getName())
print("Route:", bus1.getRoute().getRouteId())

print("\n= ROUTE STOPS =")
for stop in route1.getStops():
    print("-", stop.getStopName())

print("\n= SCHEDULE =")
print(schedule1.getScheduleInfo())

print("\n TICKET ")
print(ticket1.getTicketInfo())
print(personPassssengers1)
