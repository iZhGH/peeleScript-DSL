import pygame
import time 
pygame.init()
slapazzAudio = 'slapazz.wav'
slapazzClip = pygame.mixer.Sound(slapazzAudio)

from textx import metamodel_from_file
peele_mm = metamodel_from_file('peeleScript.tx')
peele_model = peele_mm.model_from_file('program.ps')

class peeleScript:

    def __init__(self): 
        self.variables = {}
        studentNames = ['A-Aron', 'Jayquelin', 'Ba-la-kay', 'Dee-Nice', 'Tim-o-thy']
        for student in studentNames:
            self.variables[student] = None

    def interpret(self, model):
        for c in model.statements:
            if c.__class__.__name__ == "Attendance":
                if self.variables[c.name] is not None:
                    print(f"{c.name} is present!")
                else:
                    print(f"{c.name} is absent!") 



            elif c.__class__.__name__ == "Assignment":
                if c.name not in self.variables:
                    raise NameError(f"Invalid student name: {c.name}")
                self.variables[c.name] = c.value

            elif c.__class__.__name__ == "Fronthand":
                if self.variables[c.name] is None:
                    self.variables[c.name] = 0  
                self.variables[c.name] += 1
                
            elif c.__class__.__name__ == "Backhand":
                if self.variables[c.name] is None:
                    self.variables[c.name] = 0  
                self.variables[c.name] -= 1
            
            elif c.__class__.__name__ == "McCringleberry":
                if self.variables[c.name] is None:
                    self.variables[c.name] = 0  
                self.variables[c.name] += 3

            elif c.__class__.__name__ == "output":
                print(f"{c.text}")
                

            elif c.__class__.__name__ == "slapAzz":
                if c.fizz == 0 or c.buzz == 0:
                    raise ValueError("slap/Azz cannot be 0!")
                
                for i in range(1, c.length + 1):
                    if i % c.fizz == 0 and i % c.buzz == 0:
                        print("slapAzz!")
                        slapazzClip.play()
                        time.sleep(2)
                    elif i % c.fizz == 0:
                        print("slap!")
                    elif i % c.buzz == 0:
                        print("azz!")
                    else:
                        print(i) 
                


                
interpreter = peeleScript()
interpreter.interpret(peele_model)