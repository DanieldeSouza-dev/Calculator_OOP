def menu():
        print('[+] Adiction')
        print('[-] Subtraction')
        print('[*] Multiplication')
        print('[/] Division')
        print('[**] Exponentiation')
        print('[%] Percentage')
        print('[R] Square Root')
        print('\033[0:34m-=\033[0m' * 20)

def claim_number(msg):
        while True:
            try:
                return float(input(msg))
            except ValueError:
                print('\033[0:31mInvalid entry!\033[0m')
                
def claim_operator(msg):
    valid_operators = ['+', '-', '*', '/', '**', '%', 'r']
    while True:
         op = input(msg).strip().lower()
         if op in valid_operators:
              return op
         print('\033[0:31mInvalid operator! Please choose a valid one.\033[0m')
