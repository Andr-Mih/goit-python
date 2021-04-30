
list_classes = []
class Meta(type):
    
    # тут должно быть ваше решение
    def __new__(cls, name, bases,attr):

        attr['class_number'] = len(list_classes)
        list_classes.append(len(list_classes))
        
        return type.__new__(cls, name, bases,attr)



class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data
        

class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data

assert (Cls1.class_number, Cls2.class_number) == (0, 1)
a, b = Cls1(''), Cls2('')
print(a.class_number, b.class_number)
assert (a.class_number, b.class_number) == (0, 1)