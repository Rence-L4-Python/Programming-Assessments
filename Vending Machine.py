#The Vending Machine must have the following features as a minimum requirement:
 
    #●	A menu of drinks and snacks presented via the console. The number and range of items is up to you.
    #●	A set of codes that the user can input to select a particular drink or snack.
    #●	 A way of capturing the user’s inputted code.
    #●	A way of managing money. The user should be able to input any amount of money and have the correct change returned.
    #●	A message that tells the user that a particular drink or snack has been dispensed.
    #●	 A message that tells the user how much change they have received.
    #●	 Comments in the code to explain key operations.

#You may wish to add additional features to your Vending Machine to achieve higher marks. Below is an indication of some of these features, however you may also wish to come up with your own:
 
#●	A method of categorising items in the vending machine to improve the user experience (e.g. ‘Chocolate’ or ‘Hot Drinks’).
    #●	A way of allowing users to buy additional items.
#●	An intelligence system for suggesting purchases. For example, if you buy a coffee, the vending machine may suggest that you buy biscuits.
#●	The use of functions to improve the structure of your program.
    #●	A stock system meaning the machine may run out of products

#########################

## dictionary to pull values and display available items
vm={
11: ['Mountain Dew 330mL', 3, 2],
12: ['Pepsi 330mL', 2.50, 4],
13: ['Sprite 330mL', 2.50, 3],
14: ['Fanta Orange 500mL', 3.50, 1],
21: ['Snickers Chocolate Bar', 4, 5],
22: ['Lays Potato Chips', 5, 3],
23: ['Digestives Biscuits', 7.50, 2]
}

## situation
print('You find a vending machine obstructing the middle of the freeway. You exit your car and decide to buy something from it.')
print('You have 25 AED in your wallet.\n')

## using lists since they are mutable and the program requires the budget to decrement with every loop
budget = [25]

## using loop to continually display table and use the program until funds are insufficient 
while True:
    print('\n{:<10} | {:<25} | {:<15} | {:<10}'.format('CODE','REFRESHMENTS','PRICE (AED)','# IN STOCK'))
    for k,v in vm.items():
        refreshments, price, stock = v
        print('{:<10} | {:<25} | {:<15} | {:<10}'.format(k, refreshments, price, stock))

## code
    ask = "\nEnter code: "
    inputcode = int(input(ask))
    try: ## not using "try" results in a KeyError because of the following code
        codename = vm[inputcode][0]
        codeprice = vm[inputcode][1]
        codestock = vm[inputcode][2]
## checks if user input is valid
        if inputcode in vm:
            budget[0] -= codeprice
            vm[inputcode][2] -= 1 ## updating the stock
    except KeyError:
        print("INVALID CODE! Please enter one of the displayed codes.")
        continue
## checks if current budget is enough to buy more items; placement ensures that if budget goes under 0, the program breaks and wont execute the next statement
    if budget[0] >= 0:
        print(f"You order a {codename}, which costs {codeprice} AED.")
        print(f"\nYou currently have {budget} AED in your wallet.")
    else:
        print("\nINSUFFICIENT FUNDS!")
        break
## code for removing an item from the vending machine when it runs out of stock
    if vm[inputcode][2] == 0:
        print(f"{codename} has run out of stock. Removing option from vending machine.")
        del vm[inputcode]
    











