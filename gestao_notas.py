import os
import pygsheets
from flask import Flask, render_template, request, redirect
from datetime import datetime, timedelta

app = Flask(__name__)

gc = pygsheets.authorize(service_file='/etc/secrets/credenciais.json')
sh = gc.open("Gestão de lançamento de notas")

@app.route('/')
def index():
    turmas_sheet = sh.worksheet_by_title("Turmas")
    turmas = turmas_sheet.get_all_records()
    data_hora = (datetime.utcnow() + timedelta(hours=1)).strftime("%d/%m/%Y %H:%M")
    return render_template("index.html", turmas=turmas, data_hora=data_hora)

@app.route('/acesso', methods=['POST'])
def acesso():
    codigo = request.form.get('codigo', '').strip().lower()
    if codigo == "alunos":
        return redirect('/alunos')
    elif codigo == "notas":
        return redirect('/classificacoes')
    elif codigo == "estatisticas":
        return redirect('/estatisticas')
    elif codigo == "disciplinas":
        return redirect('/disciplinas')
    elif codigo == "media":
        return redirect('/media')
    else:
        turmas_sheet = sh.worksheet_by_title("Turmas")
        turmas = turmas_sheet.get_all_records()
        data_hora = (datetime.utcnow() + timedelta(hours=1)).strftime("%d/%m/%Y %H:%M")
        erro = "⚠️ Código inválido. Tente novamente."
        return render_template("index.html", turmas=turmas, data_hora=data_hora, erro=erro)

@app.route('/alunos')
def alunos():
    alunos_sheet = sh.worksheet_by_title("Alunos")
    alunos = alunos_sheet.get_all_records()
    data_hora = (datetime.utcnow() + timedelta(hours=1)).strftime("%d/%m/%Y %H:%M")
    return render_template("alunos.html", alunos=alunos, data_hora=data_hora)


@app.route('/classificacoes')
def classificacoes():
    classificacoes_sheet = sh.worksheet_by_title("Classificações")
    classificacoes = classificacoes_sheet.get_all_records()
    data_hora = (datetime.utcnow() + timedelta(hours=1)).strftime("%d/%m/%Y %H:%M")
    return render_template("classificacoes.html", classificacoes=classificacoes, data_hora=data_hora)

@app.route('/estatisticas')
def estatisticas():
    estatisticas_sheet = sh.worksheet_by_title("Estatísticas")
    estatisticas = estatisticas_sheet.get_values(start='A2', end='G100', include_tailing_empty=False)
    resumo = estatisticas_sheet.get_values(start='J2', end='N100', include_tailing_empty=False)

    # cabeçalhos
    estatisticas_header = ['ID Turma', 'Turma', 'Número do Aluno', 'Nome do Aluno', 'Disciplina', 'Nota', 'Aprovado']
    resumo_header = ['ID Turma', 'Turma', 'Disciplina', 'Aprovados', 'Reprovados']

    # transformar para lista de dicionários
    estatisticas_data = [dict(zip(estatisticas_header, row)) for row in estatisticas if any(row)]
    resumo_data = [dict(zip(resumo_header, row)) for row in resumo if any(row)]

    data_hora = (datetime.utcnow() + timedelta(hours=1)).strftime("%d/%m/%Y %H:%M")
    return render_template("estatisticas.html", estatisticas=estatisticas_data, resumo=resumo_data, data_hora=data_hora)



@app.route('/disciplinas')
def disciplinas():
    disciplinas_sheet = sh.worksheet_by_title("Disciplina")
    disciplinas = disciplinas_sheet.get_all_records()
    data_hora = (datetime.utcnow() + timedelta(hours=1)).strftime("%d/%m/%Y %H:%M")
    return render_template("disciplinas.html", disciplinas=disciplinas, data_hora=data_hora)


@app.route('/media')
def media():
    media_sheet = sh.worksheet_by_title("Média por turma")
    medias = media_sheet.get_all_records()
    data_hora = (datetime.utcnow() + timedelta(hours=1)).strftime("%d/%m/%Y %H:%M")
    return render_template("media.html", medias=medias, data_hora=data_hora)



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)






