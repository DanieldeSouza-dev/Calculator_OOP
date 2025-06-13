import os
from . import core, interface

class Calculadora:
    def execute(self):
        while True:
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('\033[0:34m-=\033[0m' * 20)
                print('\033[0:36mHello! Welcome to the Calculator OOP 2.0\033[0m')
                print('\033[0:34m-=\033[0m' * 20)

                interface.menu()
                operator = interface.claim_operator('\033[0:36mChoose operator: \033[0m')
                dig1 = interface.claim_number('\033[0:36mChoose the first number: \033[0m')
                dig1 = float(dig1)

                if operator == 'r':
                    result = core.sqrt(dig1)
                    print(f'\033[0:32mThe result is {result:.2f}\033[0m')

                    if input('\033[0:34mWould you like to proceed? [y/n]\033[0m').strip().lower() !='y':
                        print('Thank you for testing! See you next time.')
                        break
                    continue

                else:
                    while True:
                        dig2 = interface.claim_number('\033[0:36mChoose the second number: \033[0m')
                        dig2 = float(dig2)
                        if operator == '/' and dig2 == 0:
                            print('\033[0:31mError: Cannot divide by zero. Please choose another number.\033[0m')
                            continue
                        break

                result = core.calculate(operator, dig1, dig2)

                print(f'\033[0:32mThe result is {result}\033[0m')

                if input('Would you like to proceed? [y/n]').strip().lower() !='y':
                    print('Thank you for testing! See you next time.')
                    break

            except KeyboardInterrupt:
                print('Calculator ended by user. \nSee you next time!')
                break
