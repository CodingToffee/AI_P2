import random

class EightQueensProblem:
    def __init__(self, transition_model, initial_state: [int] = None):
        self.initial_state: [int] = initial_state or [random.randint(0, 7) for i in range(8)]
        self.state: [int] = self.initial_state.copy()
        self.transition_model = transition_model

    def horizontal_hit(self):
        h = 0
        for queen in self.state:
            # get number of times, another queen is in the same row
            h += self.state.count(queen) - 1

        return h

    def diagonal_hit(self):
        h = 0
        for index, queen in enumerate(self.state):
            for other_index, other_queen in enumerate(self.state):
                difference = abs(index - other_index)
                if difference != 0:
                    if queen - difference == other_queen or queen + difference == other_queen:
                        h += 1

        return h

    def heuristic(self):
        return self.horizontal_hit() + self.diagonal_hit()

    def print_state(self):
        print("________________")
        line = ""
        for i in range(8):
            for index, queen in enumerate(self.state):
                if queen == i:
                    line += "|Q"
                elif (i % 2 == 0 and index % 2 == 0) or (i % 2 == 1 and index % 2 == 1):
                    line += "|_"
                else:
                    line += "|#"

            line += "|\n"
        print(line)



