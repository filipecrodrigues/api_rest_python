from .models import Equipamento
from . import db
from datetime import datetime

def criar_equipamento(data):
    equipamento = Equipamento(
        numero_serie=data['numero_serie'],
        modelo=data['modelo'],
        data_entrega=datetime.strptime(data['data_entrega'], '%Y-%m-%d')
    )
    db.session.add(equipamento)
    db.session.commit()
    return equipamento

def listar_equipamentos():
    return Equipamento.query.all()

def atualizar_equipamento(id, data):
    equipamento = Equipamento.query.get(id)
    if equipamento:
        equipamento.numero_serie = data['numero_serie']
        equipamento.modelo = data['modelo']
        equipamento.data_entrega = datetime.strptime(data['data_entrega'], '%Y-%m-%d')
        db.session.commit()
    return equipamento

def deletar_equipamento(id):
    equipamento = Equipamento.query.get(id)
    if equipamento:
        db.session.delete(equipamento)
        db.session.commit()
