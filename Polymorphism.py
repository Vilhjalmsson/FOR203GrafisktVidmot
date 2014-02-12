#!/usr/bin/env python
#Halldor Jens
#Polymorphism

class Skrar(object):
    fb = 0
    def __init__(self, nafn):
        self.nafn = nafn
    def prenta(self):
        with open(self.nafn, 'r') as myfile:
            print myfile.read()
    def fbfunction(self, text):
        pass

class WriteSkra(Skrar):
    def fbfunction(self, text):
        self.text = text
        with open(self.nafn, "w") as myfile:
            myfile.write(text+'\n')

class AppendSkra(Skrar):
    def fbfunction(self, text):
        self.text = text
        with open(self.nafn, 'a') as myfile:
            myfile.write(text+'\n')

minnfile = Skrar('text')

nr1 = WriteSkra('text')
nr2 = AppendSkra('text')

listi = [nr1, nr2, nr1]

for x in listi:
    x.fbfunction('Hi, my name is Halldor')

minnfile.prenta()
