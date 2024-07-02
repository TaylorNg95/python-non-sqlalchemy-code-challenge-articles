class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        """ else:
            raise Exception """

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        """ else:
            raise Exception """

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not hasattr(self, 'title') and isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        """ else:
            raise Exception """
        
class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not hasattr(self, 'name') and isinstance(name, str) and len(name) > 0:
            self._name = name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        st = {}
        for article in Article.all:
            if article.author == self:
                st[article.magazine] = True
        return [key for key, value in st.items()]

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        magazines = self.magazines()
        if magazines:
            st = {}
            for magazine in magazines:
                st[magazine.category] = True
            return [key for key, value in st.items()]
        else:
            return None

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
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        st = {}
        for article in Article.all:
            if article.magazine == self:
                st[article.author] = True
        return [key for key, value in st.items()]

    def article_titles(self):
        articles = self.articles()
        return [article.title for article in articles] if len(articles) > 0 else None

    def contributing_authors(self):
        # returns a list of authors who have written more than 2 articles for the magazine
        articles = self.articles() # these are all the articles that have been written in one magazine
        st = {}
        for article in articles:
            if st.get(article.author):
                st[article.author] += 1
            else:
                st[article.author] = 1
        contr_authors = [key for key, value in st.items() if st[key] > 2]
        return contr_authors if contr_authors else None

    @classmethod
    def top_publisher(cls):
        st = {}
        if Article.all:
            for magazine in cls.all:
                st[magazine] = len(magazine.articles())
            best_publisher = max([value for key, value in st.items()])
            return [key for key, value in st.items() if st[key] == best_publisher][0]
        else:
            return None