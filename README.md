# Physical to Image Distance Converter

This project converts physical distances (in meters) to image distances (in pixels) using linear regression. It also allows continuous user input for converting physical distances to image distances until the user decides to exit.

## Requirements

- Python 3.x
- NumPy
- scikit-learn
- Matplotlib

## Installation

1. Clone the repository or download the script.
2. Install the required Python packages using pip:

```bash
pip install numpy scikit-learn matplotlib
```
## Usage
1. Run the script using Python:
```bash
python distance_to_pixel_converter.py
```
2. The script will prompt you to enter physical distances in meters. Type the distance and press Enter to get the corresponding image distance in pixels. To exit the program, type q and press Enter.

## Example
After running the script, you will see output like this:
```bash
Slope (conversion factor): 5.794554853894569
Intercept: 75.05712826961945
Enter the physical distance in meters (or 'q' to quit): 10
Image Distance: 132.00 pixels
Enter the physical distance in meters (or 'q' to quit): 15
Image Distance: 160.97 pixels
Enter the physical distance in meters (or 'q' to quit): q
Exiting the program.
```
## Plot
The script also generates a plot showing the data points and the regression line. The plot is saved as distance_vs_pixel_height.png in the same directory as the script.
