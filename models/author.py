from database.connection import get_db_connection

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

        if id is None:  # Create new author in the database
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
            self.id = cursor.lastrowid
            conn.commit()
            conn.close()

    def __repr__(self):
        return f'<Author {self.name}>'

    def articles(self):
        from models.article import Article  # Late import to avoid circular dependency
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return [Article(**article) for article in articles]

    def magazines(self):
        from models.magazine import Magazine  # Late import to avoid circular dependency
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.*
            FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self.id,))
        magazines = cursor.fetchall()
        conn.close()
        return [Magazine(**magazine) for magazine in magazines]
