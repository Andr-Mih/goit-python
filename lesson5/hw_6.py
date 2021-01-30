
import re

def normalize(user_string):
    symbol_map = {ord('a'): 'а', ord('b'): 'б', ord('c'): 'ц', ord('d'): 'д', ord('e'): 'е', ord('f'): 'ф',
    ord('g'): 'г', ord('h'): 'х', ord('i'): 'и', ord('j'): 'й', ord('k'): 'к' , ord('l'): 'л', ord('m'): 'м', ord('n'): 'н',
    ord('o'): 'о', ord('p'): 'п', ord('q'): 'кю', ord('r'): 'р', ord('s'): 'с', ord('t'): 'т', 
    ord('u'): 'ю', ord('v'): 'в', ord('w'): 'в', ord('x'): 'икс', ord('y'): 'ы', ord('z'): 'з'}

    translate_string = ''
    for char in user_string:
        if char == char.lower():
            translate_string += char.translate(symbol_map)
        else:
            char = char.lower().translate(symbol_map)
            translate_string += char.upper()

    result_string = re.sub(r'\W', '_', translate_string)
    

    return result_string

u_string = 'How are You?'
print(normalize(u_string))