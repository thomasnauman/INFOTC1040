import math

def surface_area_finder(radius, height):
    side = 2 * math.pi * float(radius) * float(height)
    face = math.pi * float(radius)**2
    return (face * 2) + side

def pints_needed(surfacearea):
    return int((8/400) * surfacearea)

def main():
    input_file = open("cylinder_dimension_pint_cost_info", "r+")
    output_file = open("cylinder_coatings_estimate_result.txt", "w")
    output_file.close()
    output_file = open("cylinder_coatings_estimate_result.txt", "r+")
    for cylinder in input_file:
        cyl = cylinder.split()
        try:
            if float(cyl[0]) > 0:
                if float(cyl[1]) > 0:
                    if float(cyl[2]) > 0:
                        surface = surface_area_finder(cyl[0], cyl[1])
                        output_file.write(str(pints_needed(surface)) + " pints are required costing " + "$" + str(float(cyl[2])) + "\n")
                    else:
                        output_file.write("Paint cost cannot be calculated. Invalid input.\n")
                else:
                    output_file.write("Paint cost cannot be calculated. Invalid input.\n")
            else:
               output_file.write("Paint cost cannot be calculated. Invalid input.\n")
        except ValueError:
            output_file.write("Paint cost cannot be calculated. Invalid input.\n")
    output_file.close
    input_file.close

main()
