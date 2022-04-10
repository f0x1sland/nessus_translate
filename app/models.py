from app import db


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)

class Translate(Base):
    __tablename__ = 'translates'

    plugin_id = db.Column(db.String(7), index=True)
    pluginName = db.Column(db.Text())
    solution = db.Column(db.Text())
    synopsis = db.Column(db.Text())
    description = db.Column(db.Text())
    language = db.Column(db.String(2), index=True, default='ru')
    plugin_modification_date = db.Column(db.String(10))

class Plugin(Base):
    __tablename__ = 'plugins'
