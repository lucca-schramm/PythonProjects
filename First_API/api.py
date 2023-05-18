import pandas as pd
import numpy as np
import flask
from flask import Flask, jsonify, json
app=Flask(__name__)
@app.route('/')
def dados():
    tabela=pd.read_csv('cadastro_funcionarios.csv')
    dados1=tabela['matricula'].to_dict()
    dados2=tabela['nome'].to_dict()
    dados3=tabela['rg'].to_dict()
    dados4=tabela['salario'].to_dict()
    dados5=tabela['estado_civil'].to_dict()
    dados6=tabela['grau_instrucao'].to_dict()
    dados7=tabela['numero_filhos'].to_dict()
    dados8=tabela['idade'].to_dict()
    dados9=tabela['cidade'].to_dict()
    total_salarios=tabela['salario'].sum().astype('float')
    dados_geral1={'total_salarios':total_salarios}
    dados_geral2={
        'matricula':dados1,
        'nome':dados2,
        'rg':dados3,
        'salario':dados4,
        'estado_civil':dados5,
        'grau_instrucao':dados6,
        'numero_filhos':dados7,
        'idade':dados8,
        'cidade':dados9
                    }
    return jsonify(dados_geral2)

app.run(host='0.0.0.0')
    