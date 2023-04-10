# File Name: main.py
# Student Name and number:
# Date: 10/04/2023
# Program info: This program plots data for the given values as a graph
# References: https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/

import matplotlib.pyplot as plt
  
# this represents how long it took to walk in hours, rounded off for values with decimals, which will be plotted on the x-axis
walk_time_in_hours = [0, 0.1667, 0.25, 0.4167, 0.75, 1, 1.25, 1.4167, 1.5, 1.8333, 2]
# this represents what height was covered in metres, which will be plotted on the y-axis
height_in_metres = [0, 7, 9, 13, 16, 9, 12.5, 18, 19, 27, 30]
  
# this method plots the values above
plt.plot(walk_time_in_hours, height_in_metres, color='blue', linestyle='dashed', linewidth = 2)
  
# sets the axes ranges as per the constraints in the provided diagram
plt.ylim(0, 30)
plt.xlim(0, 2)
  
# names the x-axis according to the passed values (walk_time_in_hours)
plt.xlabel('t (hours)')
# names the y-axis according to the passed values (walk_time_in_hours)
plt.ylabel('h (m)')
  
# gives the plotted graph a descriptive title
plt.title('Path Taken on Adventure')

# this describes what exactly is plotted
plt.legend("Path")

# add grid lines
plt.grid()
  
# render the plot
plt.show()