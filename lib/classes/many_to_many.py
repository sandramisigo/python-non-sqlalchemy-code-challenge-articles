class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of the Author class")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of the Magazine class")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")

        self._title = title  # Title should not be modified after initialization
        self.author = author
        self.magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        return self._title


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name  # Making it private to prevent modification

    @property
    def name(self):
        return self._name

    def articles(self):
        """ this will returns a list of all articles written by the author."""
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        """this will return  a unique list of magazines the author has contributed to."""
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        """this creates  and returns a new Article  associated with this author."""
        return Article(self, magazine, title)

    def topic_areas(self):
        """this will return a unique list of categories of the magazines the author has contributed to."""
        categories = list(set(magazine.category for magazine in self.magazines()))
        return categories if categories else None


class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("Name")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise ValueError("the category must be a not be an empty string.")

    def articles(self):
        """this function will returns a list of all articles published in a magazine."""
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        """this function will return a unique list of authors who have contributed to the magazine ."""
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        """the function will return titles of articles in the magazine if they are not there returns none ."""
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        """this function will return a list of authors who have written more than two articles in the magazine ."""
        author_counts = {}
        for article in self.articles():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1

        contributing_authors = [author for author, count in author_counts.items() if count > 2]
        return contributing_authors if contributing_authors else None

    @classmethod
    def top_publisher(cls):
        """the function will returns the magazine with the most published articles, or None if no articles exist."""
        if not Article.all:
            return None
        return max(cls.all, key=lambda mag: len(mag.articles()), default=None)
