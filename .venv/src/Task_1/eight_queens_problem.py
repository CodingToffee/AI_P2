
class EightQueensProblem:
    def __init__(self, initial_state = [(int, int)]):
        if not len(initial_state) == 8:
            raise ValueError("queens_positions must have a length of 8!")
        self.initial_state = initial_state

    def vertical_horizontal_hit(self, queen: (int, int)):
        h = 0
        for other_queen in self.initial_state:
            if queen == other_queen:
                continue
            if queen[0] == other_queen[0]:
                h += 1
            if queen[1] == other_queen[1]:
                h += 1

        return h

    def diagonal_hit(self, queen: (int, int)):
        h = 0
        queen_x = queen[0]
        queen_y = queen[1]
        for other_queen in self.initial_state:
            if other_queen == queen:
                continue
            while queen_x > 0 and queen_y > 0:
                queen_x -= 1
                queen_y -= 1
                if queen_x == other_queen[0] and queen_y == other_queen[1]:
                    h += 1
                    print("hit other queen in loop 1at position: ", queen_x, queen_y)
            queen_y = queen[1]
            queen_x = queen[0]

            while queen_x <= 8 and queen_y <= 8:
                queen_x += 1
                queen_y += 1
                if queen_x == other_queen[0] and queen_y == other_queen[1]:
                    h += 1
                    print("hit other queen in loop 2at position: ", queen_x, queen_y)
            queen_y = queen[1]
            queen_x = queen[0]

            while queen_x <= 8 and queen_y > 0:
                queen_x += 1
                queen_y -= 1
                if queen_x == other_queen[0] and queen_y == other_queen[1]:
                    h += 1
                    print("hit other queen in loop 3 at position: ", queen_x, queen_y)
            queen_y = queen[1]
            queen_x = queen[0]

            while queen_x > 0 and queen_y <= 8:
                queen_x -= 1
                queen_y += 1
                if queen_x == other_queen[0] and queen_y == other_queen[1]:
                    h += 1
                    print("hit other queen in loop 4at position: ", queen_x, queen_y)
            queen_y = queen[1]
            queen_x = queen[0]

        return h



    def h(self):
        h = 0
        for queen in self.initial_state:
            h += self.diagonal_hit(queen)
            h += self.vertical_horizontal_hit(queen)
            print(h)

        return h


    def print(self):
        print("________________")
        line = ""
        for i in range(1, 9):
            for j in range(1, 9):
                # print Queens
                if (j, i) in self.initial_state:
                    line += "|Q"
                else:
                    if (i % 2 == 1 and j % 2 == 1) or (i % 2 == 0 and j % 2 == 0):
                        line += "|_"
                    else:
                        line += "|#"

            line += "|\n"
        print(line)
