# Código do dev aqui

from typing import Counter


def corresponding_parenthesis(text):
    open = 0
    close = 0
    result = ''
    for char in text:
        if char == '(':
            open += 1
        elif char == ')':
            close += 1
    
    if open == close:
        result = ''
    elif open > close:
        result = '(' * (open - close)
    elif close > open:
        result = ')' * (close - open)

    return result

corresponding_parenthesis('(())()))((((())')


text = "Ollloco meuuuu, taaa peegaando fogoo biiiiichooo"

def remove_more_than_two_repetitions(text):
    final = ''
    lastchar = ''
    counter = 0
    for char in text:
        if char == lastchar:
            counter += 1
        else:
            counter = 0

        if char != lastchar:
            final += char
        elif char == lastchar and counter < 2:
            final += char

        lastchar = char

    return final

remove_more_than_two_repetitions(text)


