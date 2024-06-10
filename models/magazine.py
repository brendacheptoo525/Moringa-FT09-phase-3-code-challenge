from database.connection import get_db_connection

class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

        if id is None:  # Create new magazine in the database
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (name, category))
            self.id = cursor.lastrowid
            conn.commit()
            conn.close()

    def __repr__(self):
        return f'<Magazine {self.name}>'

    def articles(self):
        from models.article import Article  # Late import to avoid circular dependency
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return [Article(**article) for article in articles]

    def contributors(self):
        from models.author import Author  # Late import to avoid circular dependency
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT a.*
            FROM authors a
            JOIN articles ar ON a.id = ar.author_id
            WHERE ar.magazine_id = ?
        """, (self.id,))
        contributors = cursor.fetchall()
        conn.close()
        return [Author(**contributor) for contributor in contributors]

    def article_titles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT title FROM articles WHERE magazine_id = ?", (self.id,))
        titles = [row['title'] for row in cursor.fetchall()]
        conn.close()
        return titles or None

    def contributing_authors(self):
        from models.author import Author  # Late import to avoid circular dependency
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT a.*, COUNT(ar.id) as article_count
            FROM authors a
            JOIN articles ar ON a.id = ar.author_id
            WHERE ar.magazine_id = ?
            GROUP BY a.id
            HAVING article_count > 2
        """, (self.id,))
        authors = cursor.fetchall()
        conn.close()
        return [Author(**author) for author in authors] or None
