from app import db


class Equipamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero_serie = db.Column(db.String(50), nullable=False)
    modelo = db.Column(db.String(100), nullable=False)
    data_entrega = db.Column(db.Date, nullable=False)
