from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

# def main():
#     # Initialize the database and create tables
#     create_tables()

#     # Collect user input
#     author_name = input("Enter author's name: ")
#     magazine_name = input("Enter magazine name: ")
#     magazine_category = input("Enter magazine category: ")
#     article_title = input("Enter article title: ")
#     article_content = input("Enter article content: ")

#     # Connect to the database
#     conn = get_db_connection()
#     cursor = conn.cursor()


#     '''
#         The following is just for testing purposes, 
#         you can modify it to meet the requirements of your implmentation.
#     '''

#     # Create an author
#     cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
#     author_id = cursor.lastrowid # Use this to fetch the id of the newly created author

#     # Create a magazine
#     cursor.execute('INSERT INTO magazines (name, category) VALUES (?,?)', (magazine_name, magazine_category))
#     magazine_id = cursor.lastrowid # Use this to fetch the id of the newly created magazine

#     # Create an article
#     cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
#                    (article_title, article_content, author_id, magazine_id))

#     conn.commit()

#     # Query the database for inserted records. 
#     # The following fetch functionality should probably be in their respective models

#     cursor.execute('SELECT * FROM magazines')
#     magazines = cursor.fetchall()

#     cursor.execute('SELECT * FROM authors')
#     authors = cursor.fetchall()

#     cursor.execute('SELECT * FROM articles')
#     articles = cursor.fetchall()

#     conn.close()

#     # Display results
#     print("\nMagazines:")
#     for magazine in magazines:
#         print(Magazine(magazine["id"], magazine["name"], magazine["category"]))

#     print("\nAuthors:")
#     for author in authors:
#         print(Author(author["id"], author["name"]))

#     print("\nArticles:")
#     for article in articles:
#         print(Article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]))

# if __name__ == "__main__":
#     main()

create_tables()
# Create some authors
author1 = Author(None, "John Doe")
author2 = Author(None, "Jane Smith")

# Create some magazines
mag1 = Magazine(None, "Tech Monthly", "Technology")
mag2 = Magazine(None, "Health Weekly", "Health")

# Create some articles
article1 = Article(None, "The Rise of AI", "Content about AI", author1.id, mag1.id)
article2 = Article(None, "Healthy Eating Habits", "Content about healthy eating", author1.id, mag2.id)
article3 = Article(None, "Quantum Computing", "Content about quantum computing", author2.id, mag1.id)
article4 = Article(None, "The Future of Tech", "Content about the future of technology", author2.id, mag1.id)

# Test Author methods
print(author1.articles())
print(author1.magazines())
# Test Magazine methods
print(mag1.articles())
print(mag1.contributors())
print(mag1.article_titles())
print(mag1.contributing_authors())

# Test Article methods
print(article1.author)
print(article1.magazine)