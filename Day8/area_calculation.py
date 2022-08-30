test_h = int(input("Height of The wall: "))
test_w = int(input("Width of the wall: "))
coverage = 5

def paint_calc(test_h, test_w, coverage):
    return (test_h*test_w)/coverage

area_calculator = paint_calc(test_h = test_h, test_w = test_w, coverage = coverage)
print(area_calculator)