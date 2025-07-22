from flask import Blueprint, request, jsonify, send_file, current_app
from .controllers import (
    criar_equipamento,
    listar_equipamentos,
    atualizar_equipamento,
    deletar_equipamento
)
from .models import Equipamento
import pandas as pd
import os

bp = Blueprint('main', __name__)

@bp.route('/equipamentos', methods=['POST'])
def criar():
    data = request.json
    equipamento = criar_equipamento(data)
    return jsonify({'id': equipamento.id}), 201

@bp.route('/equipamentos', methods=['GET'])
def listar():
    equipamentos = listar_equipamentos()
    return jsonify([
        {
            'id': e.id,
            'numero_serie': e.numero_serie,
            'modelo': e.modelo,
            'data_entrega': e.data_entrega.strftime('%Y-%m-%d')
        } for e in equipamentos
    ])

@bp.route('/equipamentos/<int:id>', methods=['PUT'])
def atualizar(id):
    data = request.json
    equipamento = atualizar_equipamento(id, data)
    if equipamento:
        return jsonify({'msg': 'Atualizado com sucesso'})
    return jsonify({'msg': 'Equipamento não encontrado'}), 404

@bp.route('/equipamentos/<int:id>', methods=['DELETE'])
def deletar(id):
    deletar_equipamento(id)
    return jsonify({'msg': 'Removido com sucesso'})

@bp.route('/equipamentos/exportar', methods=['GET'])
def exportar_excel():
    equipamentos = listar_equipamentos()

    if not equipamentos:
        return jsonify({"msg": "Nenhum equipamento encontrado para exportar."}), 204

    # Prepara os dados
    dados = [{
        'ID': e.id,
        'Número de Série': e.numero_serie,
        'Modelo': e.modelo,
        'Data de Entrega': e.data_entrega.strftime('%Y-%m-%d')
    } for e in equipamentos]

    # Caminho absoluto
    export_dir = os.path.join(current_app.root_path, 'export')
    os.makedirs(export_dir, exist_ok=True)
    caminho_arquivo = os.path.join(export_dir, 'equipamentos.xlsx')

    df = pd.DataFrame(dados)
    df.to_excel(caminho_arquivo, index=False)

    return send_file(caminho_arquivo, as_attachment=True)

