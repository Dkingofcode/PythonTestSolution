
# VARIANCE OF THE COLORS

def ColorVariance(colors):
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

    # Calculate the mean count
    mean_count = total_colors / len(color_counts)

    # Calculate the variance
    variance = sum((count - mean_count) ** 2 for count in color_counts.values()) / len(color_counts)

    return variance
