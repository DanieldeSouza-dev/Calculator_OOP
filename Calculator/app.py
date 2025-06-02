import os
from . import core, interface

class Calculadora:
    def execute(self):
        while True:
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('-=' * 20)
                print('Hello! Welcome to the Calculator OOP 2.0')
                print('-=' * 20)

                interface.menu()
                operator = interface.claim_operator('Choose operator: ')
                dig1 = interface.claim_number('Choose the first number: ')
                dig1 = float(dig1)

                if operator == 'r':
                    result = core.sqrt(dig1)
                    print(f'The result is {result:.2f}')

                    if input('Would you like to proceed? [y/n]').strip().lower() !='y':
                        print('Thank you for testing! See you next time.')
                        break
                    continue

                else:
                    while True:
                        dig2 = interface.claim_number('Choose the second number: ')
                        dig2 = float(dig2)
                        if operator == '/' and dig2 == 0:
                            print('Error: Cannot divide by zero. Please choose another number.')
                            continue
                        break

                result = core.calculate(operator, dig1, dig2)

                print(f'The result is {result}')

                if input('Would you like to proceed? [y/n]').strip().lower() !='y':
                    print('Thank you for testing! See you next time.')
                    break

            except KeyboardInterrupt:
                print('Calculator ended by user. \nSee you next time!')
                break
