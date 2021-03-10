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


class FlavorItems(BaseModel):
    __tablename__ = 'flavorItems'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True,  unique=True)
    flavor_id = db.Column(db.Integer, db.ForeignKey('flavor.id', ondelete="CASCADE"), primary_key=True, nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id', ondelete="CASCADE"), primary_key=True, nullable=False)


class Item(BaseModel):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)
    flavors = db.relationship(
        'Flavor',
        secondary=FlavorItems.__table__,
        lazy='subquery',
        backref=db.backref('Item', lazy=True),
        cascade='all, delete'
    )


class Flavor(BaseModel):
    __tablename__ = 'flavor'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))
    available = db.Column(db.Boolean, nullable=False, default=True)


class Orders(BaseModel):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavorItems_id = db.Column(db.Integer, db.ForeignKey('flavorItems.id', ondelete="CASCADE"), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id', ondelete="CASCADE"), nullable=False)
    
    quantity = db.Column(db.Integer)
    observation = db.Column(db.String(200), nullable=True)
    delivered = db.Column(db.Boolean, nullable=False, default=False)


class Client(BaseModel):
    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    street = db.Column(db.String(200), nullable=False)
    district = db.Column(db.String(200), nullable=False)
    number = db.Column(db.Integer)
    orders = db.relationship(
        FlavorItems,
        secondary=Orders.__table__,
        lazy='subquery',
        backref=db.backref('Client', lazy=True),
        cascade='all, delete'
    )