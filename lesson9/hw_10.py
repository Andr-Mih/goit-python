#modul pars

def Error_Input(func):
    def inner(*args):
        x = func(*args)
        if not x in ('add', 'change', 'show', 'phone', 'exit', 'close'):
            print(f'{x} not a command. Please enter again')
        return x
    return inner

def Error_Input1(func):
    def inner(*args):
        x = func(*args)
        try:
            int(x)
            return x
        except:
            print('Phone is not number. Enter again')
           
    return inner

@Error_Input
def pars(line):
    arg1 = line.split(' ')[0]
    return arg1


def pars1(line):
    try:
        arg1 = line.split(' ')[1]
    except:
        arg1 = ""
    return arg1
    

@Error_Input1
def pars2(line):
    try:
        arg1 = line.split(' ')[2]        
    except:        
        arg1 = ""
    return arg1

#modul Handler

def Input_Error(func):
    def inner(*args):
        try:
            x = func(*args)
            return x
        except:
            print(f'ValueError. This name is not exist.')        
    return inner


def add_func(arg1, arg2, data):
    try:
        arg2.isdigit()
        data[arg1] = arg2
        return data
    except:
        return data

def change_func(arg1, arg2, data):
    if arg1 in data.keys():
        if arg2 == None:
            return data
        data[arg1] = arg2
        return data
    else:
        print('Give me a right name')
    

@Input_Error
def phone_func(arg1, data):
    return data[arg1]

def show_func(data):
    return data

def hello_func():
    return 'How can I help you?'

def operate(op, operator):
    return operator[op]

exits = ('exit', 'close', 'goodbye')
operator = {'add': add_func, 'show': show_func, 'change': change_func, 'phone': phone_func}
dat = {'victor': '380502625324'}

def main():
    while True:
        print(hello_func())
        l = input()
        l = l.lower()
        g = pars(l)
        name1 = pars1(l)
        phone1 = pars2(l)
                
        if g in operator:
            n = operate(g, operator)
            if n == show_func:
                print(n(dat))
            elif n == phone_func:
                print(n(name1, dat))                      
            else:
                print(n(name1, phone1, dat))   
           
        if g in exits:
            break




if __name__ == '__main__':
    main()


