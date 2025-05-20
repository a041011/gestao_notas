import os
import json
from flask import Flask, render_template, request
from datetime import datetime
import pygsheets
from datetime import datetime, timedelta

app = Flask(__name__)

# Autenticação com Google Sheets usando variável de ambiente
gc = pygsheets.authorize(service_file='/etc/secrets/credenciais.json')
sh = gc.open("Gestão de lançamento de notas")

@app.route('/')
def index():
    turmas_sheet = sh.worksheet_by_title("Turmas")
    turmas = turmas_sheet.get_all_records()
    data_hora = (datetime.utcnow() + timedelta(hours=1)).strftime("%d/%m/%Y %H:%M")

    return render_template("index.html", turmas=turmas, data_hora=data_hora)

@app.route('/privado', methods=['GET', 'POST'])
def privado():
    turmas_sheet = sh.worksheet_by_title("Turmas")
    turmas = turmas_sheet.get_all_records()
    data_hora = (datetime.utcnow() + timedelta(hours=1)).strftime("%d/%m/%Y %H:%M")

    if request.method == 'POST':
        codigo = request.form.get('codigo', '').strip()
        if codigo == "1234":
            alunos_sheet = sh.worksheet_by_title("Alunos")
            alunos = alunos_sheet.get_all_records()
            return render_template("alunos.html", alunos=alunos)
        else:
            erro = "⚠️ Código incorreto. Tente novamente."
            return render_template("index.html", turmas=turmas, data_hora=data_hora, erro=erro)

    return render_template("index.html", turmas=turmas, data_hora=data_hora)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Necessário para o Render
    app.run(host='0.0.0.0', port=port)




