from textx import metamodel_from_file
peele_mm = metamodel_from_file('peeleScript.tx')
peele_model = peele_mm.model_from_file('program.ps')
