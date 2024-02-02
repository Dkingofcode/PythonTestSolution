import psycopg2
from collections import Counter



# MEAN COLOR
colors = []


def FindMeanColor(colors):
 for color in colors:
    redColors = 0
    greenColors = 0
    blueColors = 0
     
    def RGBFinder(color):
     if(color == 'red'):
        return 255 #redSum = 255
     elif(color == 'green'):
        return 255
   # greenSum = 255
     elif(color == 'blue'):
        return 255
   # blueSum = 255
     elif(color == 'yellow'):
        return 510
   # yellowSum = 510
     elif(color == 'white'):
        return 765 
   # whiteSum = 765
     elif(color == 'black'):
        return 0
   # blackSum = 0
     elif(color == 'pink'):
        return 650
   # pinkSum = 650
     elif(color == 'orange'):
        return 420
   # orangeSum = 420
     elif(color == 'cream'):
        return 716
   # creamSum = 716
     elif(color == 'ash'):
        return 507
   # ashSum = 507
     else:
         return 0
    totalNumber = len(colors)
    redColors += RGBFinder(color)
    greenColors += RGBFinder(color)
    blueColors += RGBFinder(color)

    Mean = (redColors/totalNumber, greenColors/totalNumber, blueColors/totalNumber)    
    return Mean

FindMeanColor()

# MOST WORN COLOR IN THE WEEK
def MostWornColor(colors):
     # Initialize counts for each color
    redCount = 0
    greenCount = 0
    blueCount = 0
    yellowCount = 0
    brownCount = 0
    pinkCount = 0
    orangeCount = 0
    creamCount = 0
    whiteCount = 0
    ashCount = 0
    blackCount = 0
    for color in colors:
         count = 0
         if(color == 'red'):
             redCount += 1
         elif(color == 'green'):
             greenCount += 1
         elif(color == 'blue'):      
             blueCount += 1
         elif(color == 'yellow'):
             yellowCount += 1
         elif(color == 'brown'):
             brownCount += 1
         elif(color == 'pink'):
             pinkCount += 1
         elif(color == 'orange'):
             orangeCount += 1
         elif(color == 'cream'):
             creamCount += 1                
         elif(color == 'white'):
             whiteCount += 1
         elif(color == 'ash'):
              ashCount += 1
         elif(color == 'black'):
             blackCount += 1         
         else:
             return 0
         
    # Create a dictionary for easy comparison
    color_counts = {
        'red': redCount,
        'green': greenCount,
        'blue': blueCount,
        'yellow': yellowCount,
        'brown': brownCount,
        'pink': pinkCount,
        'orange': orangeCount,
        'cream': creamCount,
        'white': whiteCount,
        'ash': ashCount,
        'black': blackCount,
    }

    # Find the color with the maximum count
    most_worn_color = max(color_counts, key=color_counts.get)

    return most_worn_color

         


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




# If a color is chosen at random what is the probability that the color is red?
def probability_of_red(colors):
    # Count the occurrences of red
    red_count = colors.count('red')

    # Calculate the total number of colors
    total_colors = len(colors)

    # Calculate the probability
    probability_red = red_count / total_colors

    return probability_red
    
    
    
    
    
    
    
# Save the colors and their frquencies in a postresql database
def save_colors_to_database(colors):
    # Count the frequencies of each color
    color_frequencies = Counter(colors)

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        dbname='your_database_name',
        user='your_username',
        password='your_password',
        host='your_host',
        port='your_port'
    )

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    try:
        # Create a table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS color_frequencies (
                color VARCHAR(255) PRIMARY KEY,
                frequency INTEGER
            )
        ''')

        # Insert or update color frequencies in the table
        for color, frequency in color_frequencies.items():
            cursor.execute('''
                INSERT INTO color_frequencies (color, frequency)
                VALUES (%s, %s)
                ON CONFLICT (color) DO UPDATE SET frequency = EXCLUDED.frequency
            ''', (color, frequency))

        # Commit the changes
        conn.commit()

    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()



#  Write a recursive searching algorithm to search for a number in a list of numbers
def RecursiveSearch(target, numbers, i=0):
    # Base case: If the index is equal to the length of the list, the element is not found.
    if i == len(numbers):
        return False

    # Check if the current element is equal to the target.
    if numbers[i] == target:
        return True
    else:
        # Recursive case: Increment the index and call the function again.
        return RecursiveSearch(target, numbers, i + 1)

# Example usage:
numbers_list = [1, 2, 3, 4, 5]
target_number = 3
result = RecursiveSearch(target_number, numbers_list)

if result:
    print(f"{target_number} is in the list.")
else:
    print(f"{target_number} is not in the list.")


# Write a program that generates random 4 digit numbers of 0s and 1s and converts the generated number to base 10.
import random

def BinaryConverter():
    # Generate a random 4-digit binary number
    binary_number = ''.join(random.choice('01') for _ in range(4))
    
    # Convert the binary number to base 10
    decimal_number = int(binary_number, 2)
    
    return binary_number, decimal_number

# Write a program to sum the first 50 fibonacci numbers

def FirstFib(n):
    if(n <= 2):
      return 1
    else:
      return FirstFib(n - 1) + FirstFib(n - 2) 
    
    
    
    
    
    