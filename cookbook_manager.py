import sqlite3
from sqlite3 import Error

def create_connection():
    """Create a database connection"""
    conn = None
    try:
        conn = sqlite3.connect('hipster_cookbooks.db')
        return conn
    except Error as e: 
            print(f"Error establishing connectioni with the void: {e}")
            return None

def create_table(conn): 
    """Create a table structure"""
    try:
        sql_create_cookbooks_table= """
            CREATE TABLE IF NOT EXISTS cookbooks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year_published INTEGER,
            aesthetic_rating INTEGER,
            instagram_worthy BOOLEAN,
            cover_color TEXT
            );"""
        cursor = conn.cursor()
        cursor.execute(sql_create_cookbooks_table)
        print("Successfully created a database structure")
    except Error as e:
        print(f"Error creating table: {e}")

def insert_cookbook(conn, cookbook):
    """Add a new cookbook to your shelf )"""
    sql = '''INSERT INTO cookbooks(title, author, year_published, aesthetic_rating, instagram_worthy, cover_color)
                 VALUES(?,?,?,?,?,?)'''

    try:
        cursor = conn.cursor()
        cursor.execute(sql, cookbook)
        conn.commit()
        print(f"Successfully curated cookbook with id: {cursor.lastrowid}")
        return cursor.lastrowid
    except Error as e:
        print(f"Error adding to collection: {e}")
        return None

def get_all_cookbooks(conn):
    """Browse your entire collection """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cookbooks")
        books = cursor.fetchall()
        for book in books:
            print(f"ID: {book[0]}")
            print(f"Title: {book[1]}")
            print(f"Author: {book[2]}")
            print(f"Published: {book[3]} (vintage is better)")
            print(f"Aesthetic Rating: {'✨' * book[4]}")
            print(f"Instagram Worthy: {'📸 Yes' if book[5] else 'Not aesthetic enough'}")
            print(f"Cover Color: {book[6]}")
            print("---")
        return books
    except Error as e:
        print(f"Error retrieving collection: {e}")
        return []

def track_borrowed_cookbook(conn, cookbook_id, friend_name, date_borrowed):
    """Track which friend borrowed your cookbook and when"""
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO borrow_history (cookbook_id, friend_name, date_borrowed, date_returned)
            VALUES(?, ?, ?, NULL)
        """, (cookbook_id, friend_name, date_borrowed))
        conn.commit()
        print(f"Cookbook ID {cookbook_id} borrowed by {friend_name} on {date_borrowed}")
    except Error as e:
            print(f"Error tracking borrowed cookbook: {e}")
  
def rotate_seasonal_collection(conn, season):
    """Update display recommendations based on season"""
    # Categorize books by season
    # Suggest seasonal arrangements
    # Update instagram_worthy status based on current season

def main():
    # Establish connection to our artisanal database
    conn = create_connection()

    if conn is not None:
        # Create our free-range table
        create_table(conn)

        #Insert some carefully curated sample cookbooks
        cookbooks = [
            ('Foraged & Found: A Guide to Pretending You Know About Mushrooms', 
             'Oak Wavelength', 2023, 5, True, 'Forest Green'),
            ('Small Batch: 50 Recipes You will Never Actually Make', 
             'Sage Moonbeam', 2022, 4, True, 'Raw Linen'),
            ('The Artistic Toast: Advanced Avocado Techniques', 
             'River Wildflower', 2023, 5, True, 'Recycled Brown'),
            ('Fermented Everything', 
             'Jim Kombucha', 2021, 3, True, 'Denim'),
            ('The Deconstructed Sandwich: Making Simple Things Complicated', 
             'Juniper Vinegar-Smith', 2023, 5, True, 'Beige')
        ]

        print("\nCurating your cookbook collection...")
        for cookbook in cookbooks:
            insert_cookbook(conn, cookbook)

        print("\nYour carefully curated collection:")
        get_all_cookbooks(conn)

        conn.close()
        print("\nDatabase connection closed")
    else:
        print("Error! The universe is not aligned for database connections right now.")

if __name__ == '__main__':
    main()