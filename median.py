
# MEDIAN COLOR
def MedianColor(colors):
    # Create a dictionary to store counts for each color
    color_counts = {
        'red': 0,
        'green': 0,
        'blue': 0,
        'yellow': 0,
        'brown': 0,
        'pink': 0,
        'orange': 0,
        'cream': 0,
        'white': 0,
        'ash': 0,
        'black': 0,
    }

    # Count occurrences of each color
    for color in colors:
        color_counts[color.lower()] += 1

    # Find the total number of colors
    total_colors = len(colors)

    # Find the median index
    median_index = total_colors // 2

    # Iterate through the color counts to find the color at the median index
    current_index = 0
    for color, count in color_counts.items():
        current_index += count
        if current_index >= median_index:
            median_color = color
            break

    return median_color


# Example usage:
#colors_of_the_week = ['red', 'green', 'blue', 'red', 'yellow', 'blue', 'red']
#result = MedianColor(colors_of_the_week)
#print(f"The median color is: {result}")

