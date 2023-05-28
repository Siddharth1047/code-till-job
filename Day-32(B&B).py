# N-Queen by Using Back & Bound

class NQueen:
    def __init__(self, size):
        self.size = size
        self.board = [[0] * size for _ in range(size)]
        self.solutions = []

    def solve(self):
        self.place_queen(0)
        self.print_solutions()

    def place_queen(self, col):
        if col == self.size:
            self.add_solution()
            return

        for row in range(self.size):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                self.place_queen(col + 1)
                self.board[row][col] = 0

    def is_safe(self, row, col):
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        for i, j in zip(range(row, self.size), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        return True

    def add_solution(self):
        solution = []
        for row in range(self.size):
            queen_col = self.board[row].index(1)
            solution.append(queen_col)
        self.solutions.append(solution)

    def print_solutions(self):
        for solution in self.solutions:
            print(solution)


# Example usage
n = int(input("Enter the board size (N): "))
n_queen = NQueen(n)
n_queen.solve()