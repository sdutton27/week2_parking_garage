# Start Your Code here
#take titcket method
#price = 
#tickets = [{}, {}, {}]
#[{currentTicket = {‘paid’:False}},{}]



class ParkingGarage():
    def __init__(self, spaces):
        self.total_spaces = spaces
        self.total_tickets = spaces
        self.available_spaces = spaces
        self.available_tickets = spaces
    def takeTicket(self):
        self.available_tickets -= 1
        self.available_spaces -= 1




#pay for parking method

def payForPayment():
    payment = int(input('what amount would you like to pay now? '))
#if payment isnt empty, display to user you have 15 minutes to leave.


#update currentTicket dict key to true, if it has been paid.





#leave garage method



#if ticket has been paid display thank you message




spaces = 5
garage = ParkingGarage(5)