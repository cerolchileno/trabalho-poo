class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, CPF: {self.cpf}")

class Aluno(Pessoa):
    def __init__(self, nome, idade, cpf, matricula):
        super().__init__(nome, idade, cpf)
        self.matricula = matricula
        self.disciplinas = []

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Matrícula: {self.matricula}")
        print("Disciplinas:")
        for disciplina in self.disciplinas:
            print(f" - {disciplina.nome}")

class Professor(Pessoa):
    def __init__(self, nome, idade, cpf, salario):
        super().__init__(nome, idade, cpf)
        self.salario = salario

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Salário: {self.salario}")

class Disciplina:
    def __init__(self, nome, codigo, professor):
        self.nome = nome
        self.codigo = codigo
        self.professor = professor
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def exibir_informacoes(self):
        print(f"Disciplina: {self.nome}, Código: {self.codigo}")
        print(f"Professor: {self.professor.nome}")
        print("Alunos matriculados:")
        for aluno in self.alunos:
            print(f" - {aluno.nome}")

class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []
        self.professores = []
        self.disciplinas = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def adicionar_professor(self, professor):
        self.professores.append(professor)

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def exibir_alunos(self):
        print("Alunos matriculados:")
        for aluno in self.alunos:
            aluno.exibir_informacoes()

    def exibir_professores(self):
        print("Professores cadastrados:")
        for professor in self.professores:
            professor.exibir_informacoes()

    def exibir_disciplinas(self):
        print("Disciplinas oferecidas:")
        for disciplina in self.disciplinas:
            disciplina.exibir_informacoes()

def criar_aluno():
    nome = input("Nome do aluno: ")
    idade = input("Idade do aluno: ")
    cpf = input("CPF do aluno: ")
    matricula = input("Matrícula do aluno: ")
    return Aluno(nome, idade, cpf, matricula)

def criar_professor():
    nome = input("Nome do professor: ")
    idade = input("Idade do professor: ")
    cpf = input("CPF do professor: ")
    salario = float(input("Salário do professor: "))
    return Professor(nome, idade, cpf, salario)

def criar_disciplina(professores):
    nome = input("Nome da disciplina: ")
    codigo = input("Código da disciplina: ")
    for i, professor in enumerate(professores, start=1):
        print(f"{i}. {professor.nome}")
    opcao = int(input("Escolha o professor pelo índice: ")) - 1
    if 0 <= opcao < len(professores):
        return Disciplina(nome, codigo, professores[opcao])
    else:
        print("Professor inválido!")
        return None