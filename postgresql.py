import psycopg2
from collections import Counter

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

# Example usage:
colors_of_the_week = ['red', 'green', 'blue', 'red', 'yellow', 'blue', 'red']
save_colors_to_database(colors_of_the_week)
