
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

         

