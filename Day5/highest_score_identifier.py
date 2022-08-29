scores = input("Please Provide the hole class scores  ").split()
highest_score = 0
for n in range(0,len(scores)):
    
    if int(scores[n]) > int(highest_score):
        highest_score = scores[n]


print(highest_score)
