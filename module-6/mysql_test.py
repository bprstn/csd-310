import mysql.connector

# Database configuration
db_config = {
    'user': 'root',  # Your MySQL username
    'password': 'Tarik38!',  # Your MySQL password
    'host': '127.0.0.1',  # Connecting to local MySQL server
    'database': 'movies'  # Your database name
}

# Test connection
try:
    connection = mysql.connector.connect(**db_config)
    if connection.is_connected():
        print("Connection successful!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()