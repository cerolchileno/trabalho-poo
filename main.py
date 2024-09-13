from Pessoa import Pessoa
from Pessoa import Aluno
from Pessoa import Professor
from Pessoa import Disciplina
from Pessoa import Escola

def main():
    escola = Escola("Escola de Python")

    while True:
        print("\n--- Sistema de Gerenciamento Escolar ---")
        print("1. Adicionar aluno")
        print("2. Adicionar professor")
        print("3. Adicionar disciplina")
        print("4. Exibir alunos")
        print("5. Exibir professores")
        print("6. Exibir disciplinas")
        print("0. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            aluno = criar_aluno()
            escola.adicionar_aluno(aluno)
        elif opcao == 2:
            professor = criar_professor()
            escola.adicionar_professor(professor)
        elif opcao == 3:
            if not escola.professores:
                print("Não há professores cadastrados.")
            else:
                disciplina = criar_disciplina(escola.professores)
                if disciplina:
                    escola.adicionar_disciplina(disciplina)
        elif opcao == 4:
            escola.exibir_alunos()
        elif opcao == 5:
            escola.exibir_professores()
        elif opcao == 6:
            escola.exibir_disciplinas()
        elif opcao == 0:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()