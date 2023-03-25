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
        self.active_tickets = [] # list of tickets
        self.cost_of_ticket = 10

    def take_ticket(self):
        if self.available_spaces > 0:
            self.available_tickets -= 1
            self.available_spaces -= 1
            print(f'there are {self.available_spaces} left. ')
            current_ticket = Ticket(len(self.active_tickets)+ 1, self.available_spaces, self.cost_of_ticket)
            # if bad driver 
            # current_ticket = Ticket(len(self.active_tickets)+ 1, self.available_spaces, self.cost_of_ticket * 2)
            self.active_tickets.append(current_ticket)
            print(current_ticket.get_ticket_num())
            return input("You have taken a ticket what would you like to do now? ")
        else:
            return input('this is full, go home ')



# name = input(please say name)
# people = [].append(name)
# people = [].pop(name)


# pay for parking method

# if price < 10:
#   print "you still owe money"

# ticket_cost = 10

    def pay_for_parking(self):
        # can also have price attached to timer
        ticket_num = int(input("What number ticket did you have? "))
        for ticket in self.active_tickets:
            if ticket_num == ticket.get_ticket_num(): # the ticket they are trying to pay
                # ticket : the ticket they want to pay for
                payment = int(input(f'The current price for your ticket is ${ticket.get_price()}.\nwhat amount would you like to pay now? '))
                while ticket.get_paid() == False:
                    if payment < ticket.get_price(): # if they have NOT paid full price
                        # print
                        print(f"You still owe {ticket.get_price() - payment}")
                        # get more input
                        payment += int(input("How much do you want to pay?"))
                    # if payment does not = the cost of the ticket, then the ticket.setpaid() would be false
                        #ticket.set_paid()
                    elif payment == ticket.get_price(): # if they have paid full price
                        ticket.set_paid(True)
                    else: # if they paid MORE than they should've
                        print("you idiot, you paid too much, we are keeping your money lol")
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
    def __init__(self, ticket_num, parking_space, price):
        self.ticket_num = ticket_num
        self.parking_space = parking_space
        self.paid = False
        self.price = price # this is default 10 but can be modified if a bad driver

    def get_ticket_num(self):
        return self.ticket_num
    
    def get_parking_space(self):
        return self.parking_space
    
    def get_paid(self):
        return self.paid
    
    def get_price(self):
        return self.price
    
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
