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
        
