class Car(object):
    name = 'BMW'
    def __init__(self,name):
        self.name = name
    def run(self,speed):
        print('Car-->',self.name,speed,'行驶')
class BMWCar(Car):
    def run(self,speed):
        print('BMWCar-->',self.name,speed,'行驶')
class SVWCar(Car):
    def run(self,speed):
        print('SVWCar-->',self.name,speed,'行驶')

c = Car('Car')
c.run('120迈')

bc = BMWCar('宝马')
bc.run('100迈')

sc = SVWCar('大众')
sc.run('80迈')