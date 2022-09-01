import os





is_finished = False

while not is_finished:
    bids = {}

    name = input("what is Your name?\n").lower()
    bidd = int(input("what is Your bidd? $"))
    
    bids[name] = bidd

    command = input("Are ther any Other bidders? Type 'yes' or 'no'").lower()

    if command == 'yes':
        os.system('clear')

    elif command == 'no':
        larger = 0
        winner = ""
        for bid in bids:
            print(bid)
            bid_amount = bids[bid]
            if bid_amount > larger:
                larger = bid_amount
                winner = bid
        is_finished = True
        print(f"Winner is {winner} with ${larger}")




    



 


