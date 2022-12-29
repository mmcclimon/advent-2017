from collections import defaultdict


class TuringMachine:
    def __init__(self):
        self.tape = defaultdict(int)
        self.cursor: int = 0
        self.state: str = 'A'

        # Sure, I could parse the input, or I could just write this nonsense
        self.instructions = {
            'A': ((1, 1, 'B'), (0, -1, 'B')),
            'B': ((1, -1, 'C'), (0, 1, 'E')),
            'C': ((1, 1, 'E'), (0, -1, 'D')),
            'D': ((1, -1, 'A'), (1, -1, 'A')),
            'E': ((0, 1, 'A'), (0, 1, 'F')),
            'F': ((1, 1, 'E'), (1, 1, 'A')),
        }

    def step(self):
        instr = self.instructions[self.state][self.tape[self.cursor]]
        self.tape[self.cursor] = instr[0]
        self.cursor += instr[1]
        self.state = instr[2]

    def checksum(self):
        return len(list(filter(lambda v: v == 1, self.tape.values())))


m = TuringMachine()
for _ in range(12683008):
    m.step()

print(m.checksum())
