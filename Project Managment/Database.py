# Import SQLite library
import sqlite3 as sq


# Connect to database file
conn = sq.connect("Gaydural.db")


# Create cursor object
cursor = conn.cursor()


# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT,
    Display_Name TEXT,
    Affiliations TEXT,
    Skill_Level TEXT
)
""")

conn.commit()


# ADD RECORD FUNCTION
def add_record(username, display_name, affiliations, skill_level):

    cursor.execute(
        "INSERT INTO records (Username, Display_Name, Affiliations, Skill_Level) VALUES (?, ?, ?, ?)",
        (username, display_name, affiliations, skill_level)
    )

    conn.commit()


# VIEW RECORDS FUNCTION
def view_records():

    cursor.execute("SELECT * FROM records")

    rows = cursor.fetchall()

    return rows


# SEARCH RECORD FUNCTION
def search_record(username):

    cursor.execute(
        "SELECT * FROM records WHERE Username LIKE ?",
        ('%' + username + '%',)
    )

    rows = cursor.fetchall()

    return rows


# DELETE RECORD FUNCTION
def delete_record(record_id):

    cursor.execute(
        "DELETE FROM records WHERE id = ?",
        (record_id,)
    )

    conn.commit()


# UPDATE RECORD FUNCTION
def update_record(record_id, new_skill):

    cursor.execute(
        "UPDATE records SET Skill_Level = ? WHERE id = ?",
        (new_skill, record_id)
    )

    conn.commit()