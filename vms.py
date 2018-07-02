class Vehicle:

    def __init__(self, name, seats, plate):
        self._name = name
        self._seats = seats
        self._plate = plate
        self._renter = ""
        self._avalible = True
        vehicles.append(self)

    def _display_info(self):
        print("---------------------")
        print(self._name)
        print("Seats : {}".format(self._seats))
        print("Plate : {}".format(self._plate))

    def _display_all(self):
        print("---------------------")
        print(self._name)
        print("Seats : {}".format(self._seats))
        print("Plate : {}".format(self._plate))
        if self._avalible == True:
            print("This vehicle is avalible")
        else:
            print("Sorry, this vehicle is unavalible")

vehicles = []

Vehicle("2005 Volkswagen Golf", 5, "I 747 I")

def _seats_search(self):
    while True:
        try:
            seats = int(input("Enter the number of seats you would like : "))
            break
        except:
            print("Enter a number between 2-8")
    search_count=0
    for v in vehicles:
        if v._seats == seats:
            search_count += 1
            s._display_info()
    print("{} vehicle(s) found.".format(search_count))

_seats_search()
