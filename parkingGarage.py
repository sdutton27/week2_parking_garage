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
        self.options = f'You can "enter" the garage, "pay" for your ticket, "leave" the garage, or "quit" the program. '

    def take_ticket(self):
        # if there is room, take a ticket
        if self.available_spaces > 0:
            self.available_tickets -= 1
            self.available_spaces -= 1
            print(f'There are {self.available_spaces} left. ')
            current_ticket = Ticket(len(self.active_tickets)+ 1, self.available_spaces, self.cost_of_ticket)
            # if bad driver 
            # current_ticket = Ticket(len(self.active_tickets)+ 1, self.available_spaces, self.cost_of_ticket * 2)
            self.active_tickets.append(current_ticket)
            print(f"Your ticket number is {current_ticket.get_ticket_num()}. Don't lose it... ")
            return input(f"You have taken a ticket what would you like to do now? {self.options}")
        else:
            # if there is not room in the garage, tell them to go home.
            return input(f'this is full, go home. {self.options}')


# pay for parking method
    def pay_for_parking(self):
        # can also have price attached to timer
        try: # casting input as int doesn't break the program
            ticket_num = int(input("What number ticket did you have? "))
            for ticket in self.active_tickets:
                if ticket_num == ticket.get_ticket_num(): # the ticket they are trying to pay
                    # ticket : the ticket they want to pay for
                    
                    # we need an if-statement to check if the ticket has been paid for already
                    if ticket.get_paid() == True:
                        return input(f"You've already paid for ticket #{ticket_num}. What would you like to do instead? {self.options}")

                    # if the ticket has not yet been paid for
                    payment = int(input(f'The current price for your ticket is ${ticket.get_price()}.\nwhat amount would you like to pay now? '))
                    while ticket.get_paid() == False:
                        if payment < ticket.get_price(): # if they have NOT paid full price
                            # print
                            ticket.set_amount_owed((ticket.get_price() - payment))
                            print(f"You still owe {ticket.get_price() - payment}")
                            # get more input
                            payment += int(input("How much do you want to pay?"))
                        # if payment does not = the cost of the ticket, then the ticket.setpaid() would be false
                            #ticket.set_paid()
                        elif payment == ticket.get_price(): # if they have paid full price
                            ticket.set_amount_owed(0)
                            ticket.set_paid(True)
                            break
                        else: # if they paid MORE than they should've
                            print("you idiot, you paid too much, we are keeping your money lol")
                            ticket.set_amount_owed(0)
                            ticket.set_paid(True)
                            break
                    break
                print(ticket.get_paid())
            else:
                # if the number inputted is not currently an active ticket
                return input(f"We could not find that ticket as an active ticket. Please try something else. {self.options}") # goes back to main menu
            
            return input(f"Thank you for paying for your ticket, you have 15 minutes to leave. {self.options}")
        except:
            # if the user has inputted their ticket number not as a number
            return input(f"Hey, your ticket number should be a number, not a letter. It's called a ticket 'number' for a reason. {self.options}")
    
        # OPTIONS: if the user does not have a proper ticket number (maybe they haven't taken a ticket yet)
                        # for-else statement that says "we couldn't find that ticket"
    

    def leave_garage(self):
        # if ticket has been paid for, allow them to leave
        try:
            ticket_num = int(input("What number ticket did you have? "))
            for ticket in self.active_tickets:
                    if ticket_num == ticket.get_ticket_num():
                        if ticket.get_paid() == True:
                            self.active_tickets.remove(ticket)
                            self.available_tickets += 1
                            self.available_spaces += 1
                            break
                        else: # if ticket has not been paid for, make them pay
                            return input(f"You still owe {ticket.get_amount_owed()}. {self.options}") # gets back to menu
                            break
            #print(len(self.active_tickets))
            else: #if the number isnt active then have them try something else.
                return input(f"The ticket number you provided isnt in the list of active tickets, please try something else. {self.options}")
            return input(f"You have left the garage. Is there anything else you would like to do? {self.options}")
        except:
            return input(f"Please put a number and not anything else. {self.options}")
    def incorrect_input(self):
        return input(f"Incorrect input, please try again {self.options}")


#if someone takes ticket:
#   garage -= 1
#print('number of spaces left')

class Ticket():
    def __init__(self, ticket_num, parking_space, price):
        self.ticket_num = ticket_num
        self.parking_space = parking_space
        self.paid = False
        self.price = price # this is default 10 but can be modified if a bad driver
        self.amount_owed = price # keeps track of money owed

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

    def get_amount_owed(self):
        return self.amount_owed
    
    def set_amount_owed(self, amount_left_to_pay):
        self.amount_owed = amount_left_to_pay

###################################

spaces = 5
garage = ParkingGarage(5)

answer = input(f'Welcome to the parking garage, what would you like to do? {self.options}')
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