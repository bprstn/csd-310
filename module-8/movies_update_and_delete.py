import mysql.connector  # Import MySQL connector to interact with the database

# Step 1: Connect to the database
db_config = {
    'user': 'root',  # Replace with My MySQL username
    'password': 'Tarik38!',  # Replace with my MySQL password
    'host': '127.0.0.1',  # Localhost
    'database': 'movies'  # Database name
}

# Establish connection
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Step 2: Define the show_films function
def show_films(cursor, title):
    # Query to select film details with INNER JOINs
    query = """
        SELECT film_name AS Name, 
               film_director AS Director, 
               genre_name AS Genre, 
               studio_name AS 'Studio Name'
        FROM film
        INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id;
    """
    cursor.execute(query)  
    films = cursor.fetchall()  

    # Print the title and the results are here
    print(f"\n-- {title} --")
    for film in films:
        print(f"Film Name: {film[0]}\nDirector: {film[1]}\nGenre: {film[2]}\nStudio: {film[3]}\n")

# Step 3: Display the initial list of films
show_films(cursor, "DISPLAYING FILMS")

# Step 4: Insert a new film
cursor.execute("""
    INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
    VALUES ('Inception', '2010', 148, 'Christopher Nolan', 
            (SELECT studio_id FROM studio WHERE studio_name = 'Universal Pictures'), 
            (SELECT genre_id FROM genre WHERE genre_name = 'SciFi'));
""")
connection.commit()  # Commit the insert operation
show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

# Step 5: Update the genre of the film Alien to Horror
cursor.execute("""
    UPDATE film
    SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror')
    WHERE film_name = 'Alien';
""")
connection.commit()  # Commit the update operation
show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")

# Step 6: Delete the film Gladiator
cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator';")
connection.commit()  # Commit the delete operation
show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

# Step 7: Close the connection
cursor.close()
connection.close()

