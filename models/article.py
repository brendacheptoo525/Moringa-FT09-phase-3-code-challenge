from database.connection import get_db_connection

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

        if id is None:  # Create new article in the database
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)", 
                           (title, content, author_id, magazine_id))
            self.id = cursor.lastrowid
            conn.commit()
            conn.close()

    def __repr__(self):
        return f'<Article {self.title}>'

    @property
    def author(self):
        from models.author import Author  # Late import to avoid circular dependency
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE id = ?", (self.author_id,))
        author = cursor.fetchone()
        conn.close()
        return Author(**author)

    @property
    def magazine(self):
        from models.magazine import Magazine  # Late import to avoid circular dependency
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id = ?", (self.magazine_id,))
        magazine = cursor.fetchone()
        conn.close()
        return Magazine(**magazine)
