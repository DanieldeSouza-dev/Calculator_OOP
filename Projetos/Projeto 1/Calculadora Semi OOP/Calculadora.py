import os
from math import sqrt

class Calculadora: #cria calsse para ser usada como orientação a objeto

    def __init__(self): #define o valor inicial para 0 (evitar calculos enviesados)
        self.num1 = 0
        self.num2 = 0
    def limpar_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def criar_barra(self): #barrinha bonita (inicio de interface)
        print('=' * 40)
    
    def obter_numero(self, mensagem): #valida o numero
        while True:
            try:
                return float(input(mensagem))
            except ValueError:
                print('Entrada invalida!')
    
    def escolher_operador(self): #menu binito
        self.criar_barra()
        print('[+] Soma')
        print('[-] Subtração')
        print('[*] Multiplicação')
        print('[/] Divisão')
        print('[**] Potência')
        print('[%] Porcentagem')
        print('[R] Raiz Quadrada')
        self.criar_barra()
        return input('Escolha um operador: ').strip().lower()
    
    def calcular(self):
        operador = self.escolher_operador() #altera o nome para facilitar digitação
        
        self.num1 = self.obter_numero('Digite um número: ')
        self.num1 = float(self.num1)
        
        if operador == 'r': #condição caso o operador seja Raiz quadrada (não precisa de segundo digito e pergunta se quer finalizar aqui mesmo)
            print(f'A raiz quadrada de {self.num1} é {sqrt(self.num1):.2f}')
            return
        
        self.num2 = self.obter_numero('Escolha outro número: ')
        self.num2 = float(self.num2)
        
        match operador: #math e case de operadores
            case '+':
                resultado = self.num1 + self.num2
            case '-':
                resultado = self.num1 - self.num2
            case '*':
                resultado = self.num1 * self.num2
            case '/':
                resultado = self.num1 / self.num2 if self.num2 !=0 else print('Erro! Divisão por 0.')
            case '**':
                resultado = self.num1 ** self.num2
            case '%':
                resultado = (self.num1 * self.num2) / 100
            case _:
                print('Operação inválida!')
                return
        print(f'O resultado é {resultado}')
    
    def executar(self): #estrutura principal de execução em ordem e com loop
        while True:
            
            self.limpar_console()
            self.criar_barra()
            print('Olá, seja bem vindo a Calculadora POO 1.0!')
            self.criar_barra()
            self.calcular()
            
            continuar = input('Deseja continuar? [s/n]').strip().lower()
            if continuar != 's':
                print('Encerrando calculadora, volte sempre!')
                break

if __name__ == '__main__':
    app = Calculadora()
    app.executar() #chama calculadora para funcionar (não sei o pq de ter o if name == main e nem o pq de ser app)
                    #agora sei o pq: basicamente o python não consegue chamar a calculadora de fato, por ela ser uma classe e ser dinamica. 
                    # Porém quando eu transformo em "app" ele consegue chamar