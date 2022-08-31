student_scores = {
    "Harry":81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62
}

student_grades = {}

for score in student_scores:
    if student_scores[score] > 90 and student_scores[score] < 100:
        student_grades[score] = "Outstanding"
    elif student_scores[score] > 80 and student_scores[score] < 90:
        student_grades[score] = "Exceed Expectation"
    elif student_scores[score] > 70 and student_scores[score] < 80:
        student_grades[score] = "Acceptable"

    else:
        student_grades[score] = "Fail"

print(student_grades)

# nesting Dictionary and Lists 
travel_log = [
    {
        "country": "france",
        "visits": 12,
        "cities":["parris","Lille", "Dijon"]
    },
    {
        "country":"Germany",
        "visits": 5,
        "cities": ["Berlin", "Humberg", "Stuttgart"]
    }
]

# function that allow us to insert new data in to our travel log ditionary

def add_new_country(country, visits, cities):
    new_dict = {}
    new_dict["country"] = country
    new_dict["visits"] = visits
    new_dict["cities"] = cities

    travel_log.append(new_dict)

    return travel_log

added_new_country = add_new_country("Russi", 2, ["Moscow", "Saint Petersburg"])
print(added_new_country)

