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
        self.active_tickets = []

    def take_ticket(self):
        if self.available_spaces > 0:
            self.available_tickets -= 1
            self.available_spaces -= 1
            print(f'there are {self.available_spaces} left. ')
            current_ticket = Ticket(len(self.active_tickets)+ 1, self.available_spaces)
            self.active_tickets.append(current_ticket)
            print(current_ticket.get_ticket_num())
            return input("You have taken a ticket what would you like to do now? ")
        else:
            return input('this is full, go home ')



# name = input(please say name)
# people = [].append(name)
# people = [].pop(name)


#pay for parking method

    def pay_for_parking(self):
        #payment = int(input('what amount would you like to pay now? '))
        ticket_num = int(input("What number ticket did you have? "))
        for ticket in self.active_tickets:
            if ticket_num == ticket.get_ticket_num():
                ticket.set_paid(True) 
            print(ticket.get_paid())
        return input("You have paid for your ticket, please leave. ")
    

    def leave_garage(self):
        self.available_tickets += 1
        self.available_spaces += 1
        ticket_num = int(input("What number ticket did you have? "))
        for ticket in self.active_tickets:
            if ticket_num == ticket.get_ticket_num():
                self.active_tickets.remove(ticket)
        print(len(self.active_tickets))
        return input("Is there anything else you would like to do? ")

    def incorrect_input(self):
        return input("Incorrect input, please try again ")

#if payment isnt empty, display to user you have 15 minutes to leave.


#update currentTicket dict key to true, if it has been paid.





#leave garage method



#if ticket has been paid display thank you message

#if someone takes ticket:
#   garage -= 1
#print('number of spaces left')

class Ticket():
    def __init__(self, ticket_num, parking_space):
        self.ticket_num = ticket_num
        self.parking_space = parking_space
        self.paid = False

    def get_ticket_num(self):
        return self.ticket_num
    
    def get_parking_space(self):
        return self.parking_space
    
    def get_paid(self):
        return self.paid
    
    def set_paid(self, paid):
        self.paid = paid
###################################


spaces = 5
garage = ParkingGarage(5)

answer = input('Welcome to the parking garage, what would you like to do? ')
while True:
    if answer.lower() == "enter":
        answer = garage.take_ticket()

    elif answer.lower() == "pay":
        answer = garage.pay_for_parking()

    elif answer.lower() == "leave":
        answer = garage.leave_garage()
    elif answer.lower() == 'quit':
        break


    else:
        answer = garage.incorrect_input()

print("Have a nice day!")
