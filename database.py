import sqlite3
import bcrypt
import json


DATABASE_NAME = "projectpilot.db"


# ===========================
# Database Connection
# ===========================

def get_connection():
    return sqlite3.connect(DATABASE_NAME)


# ===========================
# Create Users Table
# ===========================

def create_users_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            email TEXT UNIQUE,
            password TEXT
        )
    """)

    conn.commit()
    conn.close()


# ===========================
# Create Project History Table
# ===========================

def create_project_history_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS project_history(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            project_name TEXT,
            messages TEXT,
            project_specification TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(user_id)
                REFERENCES users(id)
        )
    """)

    conn.commit()
    conn.close()


# ===========================
# Register User
# ===========================

def add_user(username, email, password):

    conn = get_connection()
    cursor = conn.cursor()

    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    cursor.execute(
        """
        INSERT INTO users(username, email, password)
        VALUES (?, ?, ?)
        """,
        (
            username,
            email,
            hashed_password.decode("utf-8")
        )
    )

    conn.commit()
    conn.close()


# ===========================
# Login Verification
# ===========================

def check_user(email, password):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM users
        WHERE email = ?
        """,
        (email,)
    )

    user = cursor.fetchone()

    conn.close()

    if user:

        stored_password = user[3]

        if bcrypt.checkpw(
            password.encode("utf-8"),
            stored_password.encode("utf-8")
        ):
            return user

    return None


# ===========================
# Get User ID
# ===========================

def get_user_id(email):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id
        FROM users
        WHERE email = ?
        """,
        (email,)
    )

    user = cursor.fetchone()

    conn.close()

    if user:
        return user[0]

    return None


# ===========================
# Save New Project History
# ===========================

def save_project_history(
    user_id,
    project_name,
    messages,
    project_specification=None
):

    conn = get_connection()
    cursor = conn.cursor()

    messages_json = json.dumps(
        messages,
        ensure_ascii=False
    )

    cursor.execute(
        """
        INSERT INTO project_history(
            user_id,
            project_name,
            messages,
            project_specification
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            user_id,
            project_name,
            messages_json,
            project_specification
        )
    )

    conn.commit()

    history_id = cursor.lastrowid

    conn.close()

    return history_id


# ===========================
# Get User Project History
# ===========================

def get_project_history(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            project_name,
            created_at,
            updated_at
        FROM project_history
        WHERE user_id = ?
        ORDER BY updated_at DESC
        """,
        (user_id,)
    )

    history = cursor.fetchall()

    conn.close()

    return history


# ===========================
# Get One Project
# ===========================

def get_project(history_id, user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            project_name,
            messages,
            project_specification,
            created_at,
            updated_at
        FROM project_history
        WHERE id = ?
        AND user_id = ?
        """,
        (
            history_id,
            user_id
        )
    )

    project = cursor.fetchone()

    conn.close()

    if not project:
        return None

    return {
        "id": project[0],
        "project_name": project[1],
        "messages": json.loads(project[2]),
        "project_specification": project[3],
        "created_at": project[4],
        "updated_at": project[5]
    }


# ===========================
# Update Project History
# ===========================

def update_project_history(
    history_id,
    user_id,
    project_name,
    messages,
    project_specification=None
):

    conn = get_connection()
    cursor = conn.cursor()

    messages_json = json.dumps(
        messages,
        ensure_ascii=False
    )

    cursor.execute(
        """
        UPDATE project_history

        SET
            project_name = ?,
            messages = ?,
            project_specification = ?,
            updated_at = CURRENT_TIMESTAMP

        WHERE id = ?
        AND user_id = ?
        """,
        (
            project_name,
            messages_json,
            project_specification,
            history_id,
            user_id
        )
    )

    conn.commit()

    conn.close()