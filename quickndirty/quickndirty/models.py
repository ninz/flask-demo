from sqlalchemy import Column, Integer, String, Text
from quickndirty.database import Base


class Scrapbook(Base):
    __tablename__ = 'scrapbook'
    id = Column(Integer, primary_key=True)
    content_url = Column(String(128), unique=True)
    title = Column(String(50), unique=True)
    resource_type = Column(String(32))
    # photo, video, link, rich
    version = Column(String(4))
    author_name = Column(String(64))
    author_url = Column(String(64))
    provider_name = Column(String(64))
    provider_url = Column(String(64))
    thumbnail_url = Column(String(64))
    thumbnail_width = Column(Integer)
    thumbnail_height = Column(Integer)
    url = Column(String(64))
    html = Column(Text)
    width = Column(Integer)
    height = Column(Integer)

    def __init__(self, content_url, title, resource_type=None, version=None, author_name=None, author_url=None,
                 provider_name=None, provider_url=None, thumbnail_url=None, thumbnail_width=None, thumbnail_height=None,
                 url=None, html=None, width=None, height=None):
        self.content_url = content_url
        self.title = title
        self.resource_type = resource_type
        self.version = version
        self.author_name = author_name
        self.author_url = author_url
        self.provider_name = provider_name
        self.provider_url = provider_url
        self.thumbnail_url = thumbnail_url
        self.thumbnail_height = thumbnail_height
        self.thumbnail_width = thumbnail_width
        self.url = url
        self.html = html
        self.width = width
        self.height = height

    def __repr__(self):
        return '<User %r>' % self.title
