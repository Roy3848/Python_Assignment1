# Write a program to sum of the interior angle side in degree. Take side of angle input from console

sides = int(input("Enter the number of sides of the polygon: "))


def angle_total(side_number):
    final_result = (side_number - 2) * 180
    return final_result


print("The total sum of the interior angles of the polygon (in degrees) is:", angle_total(sides))
