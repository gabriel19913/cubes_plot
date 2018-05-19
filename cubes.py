from matplotlib import pyplot as plt

# This command creates a list from 1 until 5000 for the x axis.
x_values = range(1, 5001)
y_values = []

# The loop below calculate the cube of each element from the x axis and
# storage at the y_values list that represents the y axis.
for x in x_values:
    y_values.append(x ** 3)

# The scatter funcion plots all the points of x and y axis. 
# The parameter c and cmap creates a colormap that start with a light red
# color and ends with a dark red color. 
# The parameter s indicates the line's thickness 
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=30)

# The function below defines the graph's title and font size 
plt.title('Cubes Numbers', fontsize=24)

# The function below defines the x axis' title and font size
plt.xlabel('Values', fontsize=14)

# The function below defines the y axis' title and font size
plt.ylabel('Cubes', fontsize=14)

# The function below defines the numbers' font size in both axis
plt.tick_params(axis='both', labelsize=14)

# The function shows the graph in another window 
plt.show()
