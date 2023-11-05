
def calculate_rectangle_area(length, width):
    return length * width


#changes in feature-y 
#changes in feature - z 
#feature-x modifying line.  with merging feature-z and main in CLI both changes have been accepted 



if __name__ == "__main__":
    try:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Insert the width of the rectangle: "))

        if length <= 0 or width <= 0:
            print("Both length and width must be positive numbers.")
        else:
            area = calculate_rectangle_area(length, width)
            print(f"The area of the rectangle is: {area}")
    except ValueError:
        print("Please enter valid numeric values for length and width.")