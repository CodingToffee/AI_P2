import random


class EightQueensProblem:
    def __init__(self, transition_model, initial_state: [int] = None):
        self.initial_state: [int] = initial_state or [random.randint(0, 7) for i in range(8)]
        self.state: [int] = self.initial_state.copy()
        self.transition_model = transition_model

    def heuristic(self, state):
        h = 0
        for index, queen in enumerate(state):
            h += state.count(queen) - 1
            for other_index, other_queen in enumerate(state):
                difference = abs(index - other_index)
                if difference != 0:
                    if queen - difference == other_queen or queen + difference == other_queen:
                        h += 1

        return h

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

    def heuristics_all_actions(self):
        actions = []
        for i in range(8):
            column = []
            for j in range(8):
                new_state = self.state.copy()
                new_state[i] = j
                column.append((new_state, self.heuristic(new_state)))

            actions.append(column)
        return actions

    def print_heuristics_all_actions(self):
        line = ""
        for index, column in enumerate(self.heuristics_all_actions()):
            for state, heuristic in column:
                if state[index] == self.state[index]:
                    line += "|QQ"
                else:
                    if heuristic % 10 == 0:
                        heuristic = str(0) + str(heuristic)
                    else:
                        heuristic = str(heuristic)
                    line += "|" + heuristic
            line += "|\n"

        print(line)
