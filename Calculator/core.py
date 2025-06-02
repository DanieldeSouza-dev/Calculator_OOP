from math import sqrt
def calculate(operator, numb1, numb2 = None):
    match operator:
        case '+':
            return numb1 + numb2
        case '-':
            return numb1 - numb2
        case '*':
            return numb1 * numb2
        case '/':
            if numb2 == 0:
                return 'Error, division by 0'
            return numb1 / numb2 
        case '**' :
            return numb1 ** numb2
        case '%':
            return (numb1 * numb2) / 100
        case 'r':
            return sqrt(numb1)
        case _:
            return 'Invalid operation!'
