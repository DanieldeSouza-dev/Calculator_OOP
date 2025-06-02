def menu():
        print('[+] Adiction')
        print('[-] Subtraction')
        print('[*] Multiplication')
        print('[/] Division')
        print('[**] Exponentiation')
        print('[%] Percentage')
        print('[R] Square Root')
        print('-=' * 20)

def claim_number(msg):
        while True:
            try:
                return float(input(msg))
            except ValueError:
                print('Invalid entry!')
                
def claim_operator(msg):
    valid_operators = ['+', '-', '*', '/', '**', '%', 'r']
    while True:
         op = input(msg).strip().lower()
         if op in valid_operators:
              return op
         print('Invalid operator! Please choose a valid one.')
