# Parking Garage Project

Your assignment for today is to create a parking garage class to get more familiar with Object Oriented Programming(OOP). This project would usually be a pair programming project. However, for the size our class we will have groups of 3. This means, that one person(The driver) will code the project while the other people(The navigators)will brainstorm and guide to a working solution.
Each of you should share/switch these roles every 30mins-1hr -- Or you may elect to switch "drivers" after creating specific methods of the class.

The Initial Driver needs to Make sure to:
download the files below, create a local folder for the project,  create a github repository, commit the inital files,  share the link

Both navigators should then:
fork the code, clone it.

The current driver MUST share their screen so the navigators can help brainstorm to a working solution.

When code has been updated, you will need to pull down the changes.

Here's an article on doing so -- https://stackoverflow.com/questions/3903817/pull-new-updates-from-original-github-repository-into-forked-github-repository

Your parking gargage class should have the following methods:
- take_ticket
   - This should decrease the amount of tickets available by 1
   - This should decrease the amount of parkingSpaces available by 1
- pay_for_parking
   - Display an input that waits for an amount from the user and store it in a variable
   - If the payment variable is not empty then (meaning the ticket has been paid) ->  display a message to the user that their ticket has been paid and they have 15mins to leave
   - This should update the "currentTicket" dictionary key "paid" to True
-leave_garage
   - If the ticket has been paid, display a message of "Thank You, have a nice day"
   - If the ticket has not been paid, display an input prompt for payment
      - Once paid, display message "Thank you, have a nice day!"
   - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
   - Update tickets list to increase by 1 (meaning add to the tickets list)

You will need a few attributes as well:
- tickets -> list
- parkingSpaces -> list
- currentTicket -> dictionary

NOTE: Use VSCode for this project starting with the following files below. Also, each person in the group should list the portion of the project they were responsible for inside of the python file and inside the README file.

When the project is completed, commit the final changes, sync all pull requests, and each member should submit their respective GitHub links(though the code in each should be the same)


###### List group responsiblities below:
###### Provide name and approximate line numbers where each person wrote their code

NOTE: When one person "wrote" the code, this is the person who 
physically typed out the code. The other person was the 
"driver" at this point and dictated what the other person should type. We tried to do an even split of driving/typing.

Who typed the code:
Lines 1-25: Simon
Lines 26-32: Daniel
Lines 33-54: Simon
Lines 55-62: Daniel
Lines 63-64: Simon
Lines 65-71: Daniel
Lines 72-84: Simon
Lines 85-112: Daniel (Simon added 'break's)
Lines 113-115: Simon
Lines 116-120: Daniel
Lines 121-136: Simon
Lines 137-144: Daniel
Lines 145-149: Simon
Lines 150-152: Daniel
Lines 153-166: Simon
Lines 167-170: Daniel
Lines 171-177: Simon
Lines 178-179: Daniel
Lines 180-184: Simon
Lines 185-210: Daniel
Lines 211-239: Simon
Lines 240-245: Daniel
Lines 246-248: Simon
Lines 249-278: Daniel wrote initial user input code, Simon added statements for handicap