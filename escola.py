import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# Criar tabela Aluno
cursor.execute('''
    CREATE TABLE IF NOT EXISTS aluno (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        idade INTEGER,
        turma TEXT
    )
''')

# Criar tabela Professor
cursor.execute('''
    CREATE TABLE IF NOT EXISTS professor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        disciplina TEXT
    )
''')

# Criar tabela Disciplina
cursor.execute('''
    CREATE TABLE IF NOT EXISTS disciplina (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT
    )
''')

# Criar tabela Nota
cursor.execute('''
    CREATE TABLE IF NOT EXISTS nota (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_aluno INTEGER,
        id_disciplina INTEGER,
        valor REAL,
        FOREIGN KEY (id_aluno) REFERENCES aluno (id),
        FOREIGN KEY (id_disciplina) REFERENCES disciplina (id)
    )
''')

# Criar tabela Frequencia
cursor.execute('''
    CREATE TABLE IF NOT EXISTS frequencia (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_aluno INTEGER,
        id_disciplina INTEGER,
        presente BOOLEAN,
        FOREIGN KEY (id_aluno) REFERENCES aluno (id),
        FOREIGN KEY (id_disciplina) REFERENCES disciplina (id)
    )
''')

# Classe Aluno
class Aluno:
    def __init__(self, nome, idade, turma):
        self.nome = nome
        self.idade = idade
        self.turma = turma

    def salvar(self):
        cursor.execute('INSERT INTO aluno (nome, idade, turma) VALUES (?, ?, ?)',
                       (self.nome, self.idade, self.turma))
        conn.commit()

    def excluir(self):
        cursor.execute('DELETE FROM aluno WHERE id = ?', (self.id,))
        conn.commit()

# Classe Professor
class Professor:
    def __init__(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina

    def salvar(self):
        cursor.execute('INSERT INTO professor (nome, disciplina) VALUES (?, ?)',
                       (self.nome, self.disciplina))
        conn.commit()

    def excluir(self):
        cursor.execute('DELETE FROM professor WHERE id = ?', (self.id,))
        conn.commit()

# Classe Disciplina
class Disciplina:
    def __init__(self, nome):
        self.nome = nome

    def salvar(self):
        cursor.execute('INSERT INTO disciplina (nome) VALUES (?)', (self.nome,))
        conn.commit()

    def excluir(self):
        cursor.execute('DELETE FROM disciplina WHERE id = ?', (self.id,))
        conn.commit()

# Classe Nota
class Nota:
    def __init__(self, id_aluno, id_disciplina, valor):
        self.id_aluno = id_aluno
        self.id_disciplina = id_disciplina
        self.valor = valor

    def salvar(self):
        cursor.execute('INSERT INTO nota (id_aluno, id_disciplina, valor) VALUES (?, ?, ?)',
                       (self.id_aluno, self.id_disciplina, self.valor))
        conn.commit()

    def excluir(self):
        cursor.execute('DELETE FROM nota WHERE id = ?', (self.id,))
        conn.commit()

# Classe Frequencia
class Frequencia:
    def __init__(self, id_aluno, id_disciplina, presente):
        self.id_aluno = id_aluno
        self.id_disciplina = id_disciplina
        self.presente = presente

    def salvar(self):
        cursor.execute('INSERT INTO frequencia (id_aluno, id_disciplina, presente) VALUES (?, ?, ?)',
                       (self.id_aluno, self.id_disciplina, self.presente))
        conn.commit()

    def excluir(self):
        cursor.execute('DELETE FROM frequencia WHERE id = ?', (self.id,))
        conn.commit()

escolha_tipo = int(input("Você quer apagar ou excluir um dado?\n(digite 0 para adicionar ou 1 para apagar)\n"))

if(escolha_tipo==0):
    # Solicitar dados do aluno pelo prompt de comando
    nome_aluno = input("Digite o nome do aluno:\n")
    idade_aluno = int(input("Digite a idade do aluno:\n"))
    turma_aluno = input("Digite a turma do aluno:\n")

    # Criar instância do aluno e salvar no banco de dados
    aluno1 = Aluno(nome=nome_aluno, idade=idade_aluno, turma=turma_aluno)
    aluno1.salvar()

    # Solicitar dados do professor pelo prompt de comando
    nome_professor = input("Digite o nome do professor:\n")
    disciplina_professor = input("Digite a disciplina do professor:\n")

    # Criar instância do professor e salvar no banco de dados
    professor1 = Professor(nome=nome_professor, disciplina=disciplina_professor)
    professor1.salvar()

    # Solicitar dados da disciplina pelo prompt de comando
    nome_disciplina = input("Digite o nome da disciplina:\n")

    # Criar instância da disciplina e salvar no banco de dados
    disciplina1 = Disciplina(nome=nome_disciplina)
    disciplina1.salvar()

    # Solicitar dados da nota pelo prompt de comando
    id_aluno_nota = int(input("Digite o ID do aluno para a nota:\n"))
    id_disciplina_nota = int(input("Digite o ID da disciplina para a nota:\n"))
    valor_nota = float(input("Digite o valor da nota:\n"))

    # Criar instância da nota e salvar no banco de dados
    nota1 = Nota(id_aluno=id_aluno_nota, id_disciplina=id_disciplina_nota, valor=valor_nota)
    nota1.salvar()

    # Solicitar dados da frequência pelo prompt de comando
    id_aluno_freq = int(input("Digite o ID do aluno para a frequência:\n"))
    id_disciplina_freq = int(input("Digite o ID da disciplina para a frequência:\n"))
    presente_freq = input("O aluno está presente? (Digite 'True' ou 'False'):\n").lower() == 'true'

    # Criar instância da frequência e salvar no banco de dados
    frequencia1 = Frequencia(id_aluno=id_aluno_freq, id_disciplina=id_disciplina_freq, presente=presente_freq)
    frequencia1.salvar()
elif escolha_tipo==1:
    # Solicitar dados para exclusão
    tipo_dado_excluir = input("Digite o tipo de dado a ser excluído (aluno/professor/disciplina/nota/frequencia):\n").lower()
    id_dado_excluir = int(input(f"Digite o ID do {tipo_dado_excluir} a ser excluído:\n"))

    # Realizar a exclusão
    if tipo_dado_excluir == 'aluno':
        aluno_a_excluir = Aluno(nome='', idade=0, turma='')
        aluno_a_excluir.id = id_dado_excluir
        aluno_a_excluir.excluir()
        nota_a_excluir = Nota(id_aluno=0, id_disciplina=0, valor=0.0)
        nota_a_excluir.id = id_dado_excluir
        nota_a_excluir.excluir()
        frequencia_a_excluir = Frequencia(id_aluno=0, id_disciplina=0, presente=False)
        frequencia_a_excluir.id = id_dado_excluir
        frequencia_a_excluir.excluir()
    elif tipo_dado_excluir == 'professor':
        professor_a_excluir = Professor(nome='', disciplina='')
        professor_a_excluir.id = id_dado_excluir
        professor_a_excluir.excluir()
    elif tipo_dado_excluir == 'disciplina':
        disciplina_a_excluir = Disciplina(nome='')
        disciplina_a_excluir.id = id_dado_excluir
        disciplina_a_excluir.excluir()
    elif tipo_dado_excluir == 'nota':
        nota_a_excluir = Nota(id_aluno=0, id_disciplina=0, valor=0.0)
        nota_a_excluir.id = id_dado_excluir
        nota_a_excluir.excluir()
    elif tipo_dado_excluir == 'frequencia':
        frequencia_a_excluir = Frequencia(id_aluno=0, id_disciplina=0, presente=False)
        frequencia_a_excluir.id = id_dado_excluir
        frequencia_a_excluir.excluir()
    else:
        print("Tipo de dado não reconhecido. Operação de exclusão cancelada.")
# Fechar a conexão com o banco de dados ao final do programa
conn.close()