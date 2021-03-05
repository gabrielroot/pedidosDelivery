from datetime import datetime

from src import db


class BaseModel(db.Model):
    __abstract__ = True

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=True, index=True)

    def save(self, flush=False):
        db.session.add(self)
        db.session.commit()
        if flush:
            db.session.refresh(self)
            db.session.flush()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()


flavorItems = db.Table(
    'flavorItems',
    db.Column('flavor_id', db.Integer, db.ForeignKey('flavor.id'), primary_key=True),
    db.Column('item_id', db.Integer, db.ForeignKey('item.id'), primary_key=True),
    db.Column('created_at', db.DateTime, default=datetime.utcnow, nullable=False),
    db.Column('updated_at', db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False),
    db.Column('deleted_at', db.DateTime, nullable=True, index=True)
)


class Item(BaseModel):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)
    flavors = db.relationship(
        'Flavor',
        secondary=flavorItems,
        lazy='subquery',
        backref=db.backref('Item', lazy=True)
    )


class Flavor(BaseModel):
    __tablename__ = 'flavor'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))
    available = db.Column(db.Boolean, nullable=False, default=True)


class Client(BaseModel):
    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)


class Order(BaseModel):
    __tablename__ = 'order'

    quantity = db.Column(db.Integer)

    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), primary_key=True)
    flavor_id = db.Column(db.Integer, db.ForeignKey('flavor.id'), primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), primary_key=True)
