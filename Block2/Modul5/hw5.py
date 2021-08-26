#numb = int(input("Введите целое число: "))
#print("Результат:", end = " ")
#for i in range(numb - 1, 1, -1):
 #   if (numb % i == 0):
  #      print(i, end = " ")
from threading import Thread
from multiprocessing import Process

def delitel(num):
    result = []
    for i in range(1, num+1, 1):
        if (num % i == 0):
            result.append(i)
    print(result)

def factorize(*number):
    for num in number:
        #delitel(num)
        #thread = Thread(target = delitel, args = (num,))
        #thread.start()
        process = Process(target=delitel, args=(num, ))
        process.start()
        process.join()
 

if __name__ == '__main__':
    
    
    a = factorize(128)
    b = factorize(255) 
    c = factorize(99999)
    d = factorize(10651060)
   
    


    
    


