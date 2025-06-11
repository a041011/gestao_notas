# Gestão de Lançamento de Notas

📚 **Objetivo**  
Este projeto visa a criação de um sistema simples e eficiente para gerir classificações de alunos, com base em dados armazenados numa folha de cálculo do Google Sheets, e utilizando uma interface web dinâmica desenvolvida com Flask.

---

### ✅ Funcionalidades

- 📄 Visualização pública das turmas disponíveis.
- 🔐 Acesso privado a diferentes secções com palavra-chave.
- 👨‍🎓 Visualização de alunos por turma.
- 📝 Consulta agregada das classificações por módulo.
- 📊 Estatísticas de desempenho com total de aprovados/reprovados.
- 📈 Médias por módulo e turma.
- 🏅 Ranking de alunos com base no desempenho.
- 🔍 Filtro por disciplina.

---

### 🛠️ Tecnologias Utilizadas

- **Flask** – Backend leve para Python.
- **Google Sheets API (pygsheets)** – Fonte de dados.
- **HTML + CSS** – Interface web estilizada.
- **Render** – Plataforma de alojamento da aplicação.

---

### 🧪 Implementação

Os dados são mantidos numa Google Spreadsheet partilhada com folhas para:

- Turmas
- Disciplinas
- Alunos
- Classificações
- Estatísticas
- Médias por turma

A aplicação Flask comunica com esta folha para apresentar dados públicos ou privados, dependendo da chave de acesso introduzida.

---

### 🌐 Acesso

| Página        | Link                     |
|---------------|--------------------------|
| Página pública | [gestao-notas.onrender.com](https://gestao-notas.onrender.com) |
| Repositório GitHub | [Ver no GitHub](https://github.com/a041011/gestao_notas.git) |

---

### 👥 Autores

Projeto desenvolvido por **Raquel, Bruno, Vítor e André**.  
Trabalho académico realizado no âmbito da unidade curricular de **Metodologias Ágeis de Desenvolvimento de Software**.
