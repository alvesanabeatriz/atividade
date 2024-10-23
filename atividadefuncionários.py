class Funcionario:
    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = salario

    def calcular_bonus(self):
        pass

    def get_nome(self):
        return self._nome

    def get_salario(self):
        return self._salario


class Gerente(Funcionario):
    def calcular_bonus(self):
        return self._salario * 0.2


class Analista(Funcionario):
    def calcular_bonus(self):
        return self._salario * 0.1


class Estagiario(Funcionario):
    def calcular_bonus(self):
        return self._salario * 0.05
    

def menu():
    print("\nMenu:")
    print("1. Cadastrar Funcionário")
    print("2. Consultar Funcionários")
    print("3. Calcular Bônus")
    print("4. Sair")

def main():
    funcionarios = []  # Renomeado para 'funcionarios' para manter a lista de todos os funcionários

    while True:
        menu() 
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Digite seu nome: ")
            salario = float(input("Digite seu salário: "))
            funcao = input("Informe a sua função (gerente, analista, estagiario): ").strip().lower()
            
            if funcao == 'gerente':
                funcionario = Gerente(nome, salario)
            elif funcao == 'analista':
                funcionario = Analista(nome, salario)
            elif funcao == 'estagiario':
                funcionario = Estagiario(nome, salario)
            else:
                print("Cargo inválido!")
                continue
            
            funcionarios.append(funcionario)  # Corrigido para adicionar o funcionário na lista
            print("Cadastrado com sucesso!")

        elif opcao == '2':
            if not funcionarios:
                print("Nenhum funcionário cadastrado.")
            else:
                for f in funcionarios:
                    print(f"Nome: {f.get_nome()}, Salário: R$ {f.get_salario():.2f}")

        elif opcao == '3':
            if not funcionarios:
                print("Nenhum funcionário cadastrado.")
            else:
                for f in funcionarios:
                    bonus = f.calcular_bonus()
                    print(f"Nome: {f.get_nome()}, Bônus: R$ {bonus:.2f}")

        elif opcao == '4':
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
