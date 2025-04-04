def triangle(side1, side2, side3):
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return "invalid"
    
    if side1 == side2 == side3:
        return "equilateral"
    
    sides = [side1, side2, side3]
    sides.sort()

    if sides[0] + sides[1] < sides[2]:
        return 'invalid'
    elif sides[0] == sides[1] or sides[1] == sides[2]:
        return 'isosceles'
    else:
        return 'scalene'

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True