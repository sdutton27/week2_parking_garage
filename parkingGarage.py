# Daniel Richmond & Simon Dutton
# Due March 27, 2023
# Parking Garage Program
# parkingGarage.py 
# This file contains the classes and code necessary to run a ParkingGarage program.
# The program creates an instance of the ParkingGarage() class and adds instances
# of the Ticket() class which the user can pay for before leaving the garage.


class ParkingGarage():
    """
        ParkingGarage(spaces:int)
        A ParkingGarage is an object that holds a parking garage, its total/
        available tickets and spaces, a list of active tickets, and the cost 
        of a space in that parking garage. It takes in the number of spaces 
        in the garage, and the cost of a single space in the garage (which is 
        defaulted to 10).
    """
    def __init__(self, spaces, cost_of_space=10):
        """
            __init__(spaces:int, cost_of_space=10:int)
            The __init__ method for a ParkingGarage object. Initializes the total
            and available number of spaces and tickets, the cost of a space in the 
            garage, the list of active tickets, and what the user options are for input.
        """
        self.total_spaces = spaces
        self.total_tickets = spaces
        self.available_spaces = spaces
        self.available_tickets = spaces
        self.active_tickets = [] # list of tickets
        self.cost_of_space = cost_of_space
        self.options = f'You can "enter" the garage, "pay" for your ticket, "leave" the garage, or "quit" the program. '

    # take ticket function
    def take_ticket(self, handicap=False):
        """
            take_ticket(handicap=False:boolean)
            The take_ticket method for a ParkingGarage. Takes in an optional boolean for if a ticket is 
            being taken from the handicap lot (FREE PARKING)
            If there is room in the garage, the user takes a ticket and gets a ticket number.
            The ticket is added to the list of active tickets, and the number of 
            empty spaces decreases.
            If there is not room in the garage, the user is told to go home and the list of options are 
            presented so other tickets may be paid off and cars can leave.
            Returns the user to the main menu.
        """
        # if there is room, take a ticket
        if self.available_spaces > 0:
            # if the user is a bad parker, then they take up two spots
            bad_driver = input("Do you suck at parking? 'yes' or 'no' ").lower()
            if bad_driver != 'no': #if the user says anything other an an explicit 'no'
                print("You are not a self-declared 'good parker,' so you're gonna have to pay for two spots.")
                if self.available_spaces == 1: #if only 1 spot left, a bad parker couldn't park
                    return input(f"ACTUALLY we only had one spot left. Since we can't trust you to park here, you're gonna have to wait or park somewhere else. Maybe go back to driver's ed. \n{self.options} ")
                current_ticket = Ticket(len(self.active_tickets)+ 1, self.total_spaces - self.available_spaces, self.cost_of_space * 2)
                self.available_tickets -= 1
                self.available_spaces -= 2
            else:
                print("We are trusting that you were honest with us so we will only make you pay for one spot.")
                current_ticket = Ticket(len(self.active_tickets)+ 1, self.total_spaces - self.available_spaces, self.cost_of_space)
                self.available_tickets -= 1
                self.available_spaces -= 1
            if handicap:
                current_ticket.set_paid(True)
            self.active_tickets.append(current_ticket)
            print(f"Your ticket number is {current_ticket.get_ticket_num()}. Don't lose it... \n")
            print(f'There are now {self.available_spaces} spaces left in the parking garage. ')
            return input(f"You have taken a ticket. What would you like to do now? \n{self.options}")
        else:
            # if there is not room in the garage, tell them to go home.
            return input(f'This is full, go home. \n{self.options}')


    # pay for parking function
    def pay_for_parking(self):
        """
            pay_for_parking()
            This function allows the customer to pay for their specific ticket by asking
            which ticket they had. It also keeps track of how much they have paid off of the
            ticket, and if they still owe money on it. If they have overpaid, we keep their 
            extra money.     
            If the inputted ticket number is invalid, the user is sent back to the main options menu. 
            Returns the user to the main menu.
        """
        try: # casting input as int doesn't break the program
            ticket_num = int(input("What number ticket did you have? "))
            for ticket in self.active_tickets:
                if ticket_num == ticket.get_ticket_num(): # the ticket they are trying to pay
                    # ticket : the ticket they want to pay for
                    # if the ticket has been paid for already
                    if ticket.get_paid() == True:
                        return input(f"Ticket #{ticket_num} has already been paid for. What would you like to do instead? \n{self.options}")
                    
                    # if the ticket has not yet been paid for
                    payment = int(input(f'The current price for your ticket is ${ticket.get_price()}.\nwhat amount would you like to pay now? '))
                    # the user has to fully pay for the ticket before they are allowed to exit the loop
                    while ticket.get_paid() == False:
                        if payment < ticket.get_price(): # if they have NOT paid full price
                            ticket.set_amount_owed((ticket.get_price() - payment))
                            print(f"You still owe {ticket.get_price() - payment}")
                            payment += int(input("How much do you want to pay?")) # get more input
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
                return input(f"We could not find that ticket as an active ticket. Please try something else. \n{self.options}") # goes back to main menu
            # when the user has fully paid off their ticket, tell them and return to main menu
            return input(f"Thank you for paying for your ticket, please leave. \n{self.options}")
        except:
            # if the user has inputted their ticket number not as a number
            return input(f"Hey, your ticket number should be a number, not a letter. It's called a ticket 'number' for a reason. \n{self.options}")
    
    # leave garage function
    def leave_garage(self):
        """
            leave_garage()
            The customer is asked for their ticket number.
            If the ticket has been paid for, then the customer leaves the lot
            (adding a new space and ticket to the available spaces/tickets and 
            removing their ticket from the active tickets list)
            If the ticket has not been paid for, we bring the user to the 
            pay_for_parking() method.
            If the user has not properly inputted their ticket number, we tell them
            and bring them back to the main options menu.
            Returns the user to the main menu.
        """
        try: # make sure the ticket is a proper integer!
            ticket_num = int(input("What number ticket did you have? "))
            for ticket in self.active_tickets:
                    if ticket_num == ticket.get_ticket_num():
                        # if ticket has been paid for, allow them to leave
                        if ticket.get_paid() == True:
                            self.active_tickets.remove(ticket)
                            self.available_tickets += 1
                            # if bad driver then add 2 spaces
                            if ticket.get_price() == self.cost_of_space * 2: #if the ticketholder was a bad driver
                                self.available_spaces += 2
                            else:
                                self.available_spaces += 1
                            break
                        else: # if ticket has not been paid for, make them pay
                            print(f"You have not paid for your ticket yet! You still owe ${ticket.get_amount_owed()}. Taking you to the payment kiosk...")
                            return self.pay_for_parking()
            else: #if the number isnt active then have them go back to the main menu.
                return input(f"The ticket number you provided isnt in the list of active tickets, please try something else. \n{self.options}")
            return input(f"You have left the garage. Is there anything else you would like to do? \n{self.options}")
        except: # if the user has inputted something that's not an int
            return input(f"Please put a number and not anything else. \n{self.options}")
    
    
    def incorrect_input(self):
        """
        incorrect_input()
        This function simply states if the user inputs anything that is not within 
        the list of options, it tells them the list of options and asks them to 
        try again.
        """
        return input(f"Incorrect input, please try again \n{self.options}")


class Ticket():
    """
        Ticket(ticket_num:int, parking_space:int, price:int)
        A Ticket object holds the information for a ticket taken for the ParkingGarage.
        It takes in the ticket number (int), the parking space (int), and the price
        of the ticket (int). It also holds values for if the ticket has been paid (boolean)
        and what the amount owed for the ticket is (int).
    """
    def __init__(self, ticket_num, parking_space, price):
        """
        __init__(ticket_num:int, parking_space:int, price:int)
        It takes in the ticket number (int), the parking space (int), and the price
        of the ticket (int). It also holds values for if the ticket has been paid (boolean)
        and what the amount owed for the ticket is (int).
        """
        self.ticket_num = ticket_num
        self.parking_space = parking_space
        self.paid = False
        self.price = price # this is default 10 but can be modified if a bad driver
        self.amount_owed = price # keeps track of money owed

    def get_ticket_num(self):
        """
            get_ticket_num()
            Returns the ticket number.
        """
        return self.ticket_num
    
    def get_parking_space(self):
        """
            get_parking_space()
            Returns the parking space #.
        """
        return self.parking_space
    
    def get_paid(self):
        """
            get_paid()
            Returns if the ticket has been paid for.
        """
        return self.paid
    
    def get_price(self):
        """
            get_price()
            Returns the price of the ticket.
        """
        return self.price
    
    def set_paid(self, paid):
        """
            set_paid(paid:boolean)
            Sets the "paid" variable associated with the ticket to the inputted boolean.
        """
        self.paid = paid

    def get_amount_owed(self):
        """
            get_amount_owed()
            Returns the amount still owed for the ticket.
        """
        return self.amount_owed
    
    def set_amount_owed(self, amount_left_to_pay):
        """
            set_amount_owed(amount_left_to_pay:int)
            Takes in the amount the user still has left to pay and sets to the 
            "amount_owed" variable
        """
        self.amount_owed = amount_left_to_pay

###################################

# creates an instance of a ParkingGarage with 5 spaces
spaces = 5
garage = ParkingGarage(spaces)
handicapped_garage = ParkingGarage(4, 0) # handicapped lot is FREE

# user-input part of program
answer = input(f'Welcome to the parking garage, what would you like to do? \nYou can "enter" the garage, "pay" for your ticket, "leave" the garage, or "quit" the program. ')
while True:
    if answer.lower() == "enter":
        # ask if the user is handicapped/pregnant
        hc_preg = input("Do you have any disabilities/are you pregnant? 'yes' or 'no' ").lower()
        if hc_preg == 'yes':
            print("You can park in our second garage for free. ")
            answer = handicapped_garage.take_ticket(True) # set handicap to True so ticket is already paid for
        else: #if not an explicit yes
            print("Taking you to our regular garage. ")
            answer = garage.take_ticket()
    elif answer.lower() == "pay":
        hc_preg = input("Do you have any disabilities/are you pregnant? 'yes' or 'no' ").lower()
        if hc_preg == 'yes':
            answer = handicapped_garage.pay_for_parking()
        else: #if not an explicit yes
            answer = garage.pay_for_parking()
    elif answer.lower() == "leave":
        hc_preg = input("Do you have any disabilities/are you pregnant? 'yes' or 'no' ").lower()
        if hc_preg == 'yes':
            answer = handicapped_garage.leave_garage()
        else: #if not an explicit yes
            answer = garage.leave_garage()
    elif answer.lower() == 'quit':
        break
    else:
        answer = garage.incorrect_input() #this input can be printed on either garage

#once the user has quit the program
print("Thank you for coming to our parking garage. Have a nice day!")