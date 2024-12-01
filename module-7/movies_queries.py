import mysql.connector

# Database configuration
db_config = {
    'user': 'root',  # Replace with your MySQL username
    'password': 'Tarik38!',  # Replace with your MySQL password
    'host': '127.0.0.1',
    'database': 'movies'  
}

# Connect to the database
try:
    connection = mysql.connector.connect(**db_config)
    if connection.is_connected():
        cursor = connection.cursor()

        # Query 1: Select all fields from the studio table
        print("Studio Table:")
        cursor.execute("SELECT * FROM studio;")
        for row in cursor.fetchall():
            print(row)

        print("\nGenre Table:")
        # Query 2: Select all fields from the genre table
        cursor.execute("SELECT * FROM genre;")
        for row in cursor.fetchall():
            print(row)

        print("\nMovies with Runtime Less Than 2 Hours:")
        # Query 3: Select movie names with runtime < 2 hours
        cursor.execute("SELECT film_name FROM film WHERE film_runtime < 120;")
        for row in cursor.fetchall():
            print(row)

        print("\nFilms Grouped by Director:")
        # Query 4: Get a list of film names and directors grouped by director
        cursor.execute("SELECT film_director, GROUP_CONCAT(film_name) FROM film GROUP BY film_director;")
        for row in cursor.fetchall():
            print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
