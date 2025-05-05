from textx import metamodel_from_file


def move_command_processor(move_cmd):
    if move_cmd.steps == 0:
        move_cmd.steps = 1


class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0


    def __str__(self):
        return f"Robot position is {self.x}, {self.y}."


    def interpret(self, model):
        for c in model.commands:
            if model.commands[0].__class__.__name__ != "InitialCommand":
                raise Exception("You must initialize a position first!")
           
            if c.__class__.__name__ == "InitialCommand":
                print(f"Setting position to: {c.x}, {c.y}")
                self.x = c.x
                self.y = c.y
            elif c.__class__.__name__ == "MoveCommand":
                print(f"Going {c.direction} for {c.steps} step(s).")
                move = {
                    "up": (0, 1),
                    "down": (0, -1),
                    "left": (-1, 0),
                    "right": (1, 0),
                    "upleft": (-1, 1),
                    "upright": (1, 1),
                    "downleft": (-1, -1),
                    "downright": (1, -1)
                }[c.direction]
                self.x += c.steps * move[0]
                self.y += c.steps * move[1]
            elif c.__class__.__name__ == "SpinCommand":
                print("Performing a 360-degree spin!")
            print(self)


robot_mm = metamodel_from_file('robot.tx')
robot_mm.register_obj_processors({'MoveCommand': move_command_processor})
robot_model = robot_mm.model_from_file('program.rbt')
robot = Robot()
robot.interpret(robot_model)