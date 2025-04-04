RIGHT_ANGLE = 90

def is_valid(angles):
    if sum(angles) != 180:
        return False
    for angle in angles:
        if angle <= 0:
            return False
    return True

def triangle(ang1, ang2, ang3):
    angles = [ang1, ang2, ang3]

    if not is_valid(angles):
        return 'invalid'
    
    if RIGHT_ANGLE in angles:
        return 'right'
    elif max(angles) > RIGHT_ANGLE:
        return 'obtuse'
    else:
        return 'acute'

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True