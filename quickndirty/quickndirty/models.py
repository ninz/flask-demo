from sqlalchemy import Column, Integer, String, Text
from quickndirty.database import Base
from quickndirty import app


class Scrapbook(Base):
    __tablename__ = 'scrapbook'
    id = Column(Integer, primary_key=True)
    content_url = Column(String(128), unique=True)
    title = Column(String(50), unique=True)
    # photo, video, link, rich
    resource_type = Column(String(32))
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

    def __init__(self, content_url, **kwargs):
        self.content_url = content_url
        for k, v in kwargs.iteritems():
            # type is a reserved word, can't name a var type
            if k == 'type':
                self.resource_type = v
            if hasattr(self, k):
                setattr(self, k, v)

    def __repr__(self):
        return '<Scrap %r>' % self.title

    def as_dict(self):
        db_dict = self.__dict__
        if '_sa_instance_state' in db_dict:
            del db_dict['_sa_instance_state']
        return db_dict
