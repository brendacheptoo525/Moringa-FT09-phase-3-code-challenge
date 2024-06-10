import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine
from database.setup import create_tables, get_db_connection

# Initial setup and sample data creation
author1 = Author(None, "John Doe")
author2 = Author(None, "Jane Smith")

mag1 = Magazine(None, "Tech Monthly", "Technology")
mag2 = Magazine(None, "Health Weekly", "Health")

article1 = Article(None, "The Rise of AI", "Content about AI", author1.id, mag1.id)
article2 = Article(None, "Healthy Eating Habits", "Content about healthy eating", author1.id, mag2.id)
article3 = Article(None, "Quantum Computing", "Content about quantum computing", author2.id, mag1.id)
article4 = Article(None, "The Future of Tech", "Content about the future of technology", author2.id, mag1.id)

# Print initial data setup
print("Initial Data Setup")
print("Authors:", author1, author2)
print("Magazines:", mag1, mag2)
print("Articles:", article1, article2, article3, article4)
print()

# Define the test cases
class TestModels(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        create_tables()
    
    def setUp(self):
        # Clear the tables before each test
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM articles")
        cursor.execute("DELETE FROM authors")
        cursor.execute("DELETE FROM magazines")
        conn.commit()
        conn.close()

        # Create some sample data for testing
        self.author1 = Author(None, "John Doe")
        self.author2 = Author(None, "Jane Smith")

        self.mag1 = Magazine(None, "Tech Monthly", "Technology")
        self.mag2 = Magazine(None, "Health Weekly", "Health")

        self.article1 = Article(None, "The Rise of AI", "Content about AI", self.author1.id, self.mag1.id)
        self.article2 = Article(None, "Healthy Eating Habits", "Content about healthy eating", self.author1.id, self.mag2.id)
        self.article3 = Article(None, "Quantum Computing", "Content about quantum computing", self.author2.id, self.mag1.id)
        self.article4 = Article(None, "The Future of Tech", "Content about the future of technology", self.author2.id, self.mag1.id)

    def test_author_creation(self):
        self.assertEqual(self.author1.name, "John Doe")
        self.assertEqual(self.author2.name, "Jane Smith")

    def test_article_creation(self):
        self.assertEqual(self.article1.title, "The Rise of AI")
        self.assertEqual(self.article2.title, "Healthy Eating Habits")

    def test_magazine_creation(self):
        self.assertEqual(self.mag1.name, "Tech Monthly")
        self.assertEqual(self.mag2.name, "Health Weekly")
        self.assertEqual(self.mag1.category, "Technology")
        self.assertEqual(self.mag2.category, "Health")

    def test_author_articles(self):
        articles = self.author1.articles()
        self.assertEqual(len(articles), 2)
        self.assertEqual(articles[0].title, "The Rise of AI")
        self.assertEqual(articles[1].title, "Healthy Eating Habits")

    def test_author_magazines(self):
        magazines = self.author1.magazines()
        self.assertEqual(len(magazines), 2)
        self.assertEqual(magazines[0].name, "Tech Monthly")
        self.assertEqual(magazines[1].name, "Health Weekly")

    def test_magazine_articles(self):
        articles = self.mag1.articles()
        self.assertEqual(len(articles), 3)
        self.assertEqual(articles[0].title, "The Rise of AI")
        self.assertEqual(articles[1].title, "Quantum Computing")
        self.assertEqual(articles[2].title, "The Future of Tech")

    def test_magazine_contributors(self):
        contributors = self.mag1.contributors()
        self.assertEqual(len(contributors), 2)
        self.assertEqual(contributors[0].name, "John Doe")
        self.assertEqual(contributors[1].name, "Jane Smith")

    def test_magazine_article_titles(self):
        titles = self.mag1.article_titles()
        self.assertEqual(len(titles), 3)
        self.assertIn("The Rise of AI", titles)
        self.assertIn("Quantum Computing", titles)
        self.assertIn("The Future of Tech", titles)

    def test_article_author(self):
        self.assertEqual(self.article1.author.name, "John Doe")

    def test_article_magazine(self):
        self.assertEqual(self.article1.magazine.name, "Tech Monthly")

if __name__ == "__main__":
    unittest.main()
