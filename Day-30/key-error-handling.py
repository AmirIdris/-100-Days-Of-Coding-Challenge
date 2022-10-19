facebook_list = [
    {'likes':21, 'comments':2},
    {'likes': 13, 'comments':3, 'share':1},
    {'likes':33, 'comments':8, 'share':2},
    {'comments':4, 'share': 3},
    {'comments':5, 'share': 4}
]

total_likes = 0
for post in facebook_list:
    try:
        total_likes = total_likes + post['likes']
    except KeyError:
        pass
        # total_likes = total_likes + 0

print(total_likes)