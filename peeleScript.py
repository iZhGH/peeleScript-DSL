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
            else:
                print(f"Testing error")
        
interpreter = peeleScript()
interpreter.interpret(peele_model)