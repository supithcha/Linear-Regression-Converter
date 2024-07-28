import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Data
distances_in_meters = np.array([8.45, 18.44, 13.50, 18.50, 13.49, 8.49, 30.80, 40.81, 40.88, 40.88])
pixel_heights = np.array([97.83, 231.06, 192.36, 240.34, 200.22, 97.57, 290.31, 304.66, 305.31, 306.77])

# Reshape data for sklearn
X = distances_in_meters.reshape(-1, 1)
y = pixel_heights

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Get the slope (conversion factor) and intercept
slope = model.coef_[0]
intercept = model.intercept_

print(f"Slope (conversion factor): {slope}")
print(f"Intercept: {intercept}")

# The formula to convert physical distance to image distance
def physical_to_image_distance(physical_distance):
    return slope * physical_distance + intercept

# Function to convert physical distance to image distance with user input
def get_image_distance_from_user():
    while True:
        user_input = input("Enter the physical distance in meters (or 'q' to quit): ")
        if user_input.lower() == 'q':
            print("Exiting the program.")
            break
        try:
            physical_distance = float(user_input)
            image_distance = physical_to_image_distance(physical_distance)
            print(f"Image Distance: {image_distance:.2f} pixels")
        except ValueError:
            print("Invalid input. Please enter a numerical value or 'q' to quit.")

# Call the function to get input from the user and display the result
get_image_distance_from_user()

# Plot the data and the regression line
plt.scatter(distances_in_meters, pixel_heights, color='blue')
plt.plot(distances_in_meters, model.predict(X), color='red')
plt.xlabel('Distance in meters (Unity)')
plt.ylabel('Pixel height (Camera)')
plt.title('Distance in meters vs Pixel height')

# Save the plot as an image file
plt.savefig('distance_vs_pixel_height.png')

# Display the plot
# plt.show()
