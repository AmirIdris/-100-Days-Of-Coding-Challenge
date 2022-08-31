import os
name = input("what is Your name?\n").lower()
bidd = input("what is Your bidd? ")

bidder_history = {}
bidder_history[name] = bidd


command = input("Are ther any Other bidders? Type 'yes' or 'no'").lower()
run = 1
while run == 1:
        
    if command == 'yes':
        os.system('clear')
        name = input("what is Your name?\n").lower()
        bidd = input("what is Your bidd? ")
        bidder_history[name] = bidd
        command = input("Are ther any Other bidders? Type 'yes' or 'no'").lower()
    else:
        run = 0
        larger = 0
        for bider in bidder_history:
            if int(bider[name]) > larger:
                larger = int(bider[name])


    





print(bidder_history)  


