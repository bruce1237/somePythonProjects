import copy


class sudoku:
    sudoku_table = []
    possible_values = []
    cell_need_to_solve = 0
    show_log = False

    size = 3
    block_size = 3
    available_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self, show_log=False):
        self.show_log = show_log
        self.generate()

    def generate(self, ):
        col = []
        for b in range(self.size):
            row = []
            for a in range(self.size):
                sudokuBlock = self.generate_block()
                row.insert(a, sudokuBlock)
            col.insert(b, row)
        self.sudoku_table = col

    def generate_block(self):
        block = []
        for x in range(self.block_size):
            row = []
            for y in range(self.block_size):
                row.insert(y, 0)
            block.insert(x, row)
        return block

    def set_value(self, row: int, col: int, value: int):
        a = int((row - 1) / self.block_size)
        b = int((col - 1) / self.block_size)

        d = (col - 1) % self.block_size
        if row > self.block_size:
            c = (row - 1) % self.block_size
        else:
            c = row - 1

        self.sudoku_table[a][b][c][d] = value

    def print(self):
        print("Row -> Block -> row_in_block -> row_in_block_index")
        for row in range(self.size):
            for block in range(self.size):
                for block_row in range(self.block_size):
                    for block_row_index in range(self.block_size):
                        # print(self.sudoku_table[row][block][block_row][block_row_index], end='')
                        print(row, block, block_row, block_row_index, "--",
                              self.sudoku_table[row][block][block_row][block_row_index])
                    print()
                print()
            print()
        print()

    def print_sudoku(self):
        for row in range(self.size):
            for block_row in range(self.block_size):
                for block in range(self.size):
                    print('|  ', end='')
                    for block_row_index in range(self.block_size):
                        pass
                        print(self.sudoku_table[row][block][block_row][block_row_index], end='')
                    print(end='  |  ')
                print('')
                print('--------------------------------')
            print()

    def solve(self):
        self.log("start Solve")
        while True:
            self.cell_need_to_solve = 0
            for row in range(self.size):
                self.log("check row: ", row)
                for block in range(self.size):
                    self.log("check block: ", block)
                    for block_row in range(self.block_size):
                        self.log("check block_row: ", block_row)
                        for block_row_index in range(self.block_size):
                            self.log("check block_row_index: ", block_row_index)
                            if self.sudoku_table[row][block][block_row][block_row_index] == 0:
                                self.log("the cell value is 0")
                                self.cell_need_to_solve += 1
                                self.log("increase the cell_need_to_solve counter by 1 ", self.cell_need_to_solve)
                                self.log("check row")
                                self.check_row(row, block, block_row, block_row_index)
                                self.log("check col")
                                self.check_col(row, block, block_row, block_row_index)
                                self.log("check block")
                                self.check_block(row, block, block_row, block_row_index)
            if self.cell_need_to_solve == 0:
                print("all the cell has been solved!")
                self.print_sudoku()
                exit()

    def check_row(self, row, block, block_row, block_row_index):
        if not self.possible_values:
            self.log("self.possible_values is empty,", self.possible_values)
            self.log("assign available_value into self.possible_values ")
            self.possible_values = copy.copy(self.available_number)

        self.log("possible_values for row:before check ------- ", self.possible_values)

        for each_block in range(self.size):
            for each_block_row_index in range(self.block_size):
                if self.sudoku_table[row][each_block][block_row][each_block_row_index] != 0:
                    if self.sudoku_table[row][each_block][block_row][each_block_row_index] in self.possible_values:
                        self.possible_values.remove(self.sudoku_table[row][each_block][block_row][each_block_row_index])
        self.log("possible_values for row:after check ------- ", self.possible_values)

    def check_col(self, row, block, block_row, block_row_index):
        self.log("possible_values for col:before check ||||||| ", self.possible_values)
        for each_row in range(self.size):
            for each_block_row in range(self.block_size):
                if self.sudoku_table[each_row][block][each_block_row][block_row_index] != 0:
                    if self.sudoku_table[each_row][block][each_block_row][block_row_index] in self.possible_values:
                        self.possible_values.remove(self.sudoku_table[each_row][block][each_block_row][block_row_index])
        self.log("possible_values for col:after check ||||||| ", self.possible_values)

    def check_block(self, row, block, block_row, block_row_index):
        self.log("possible_values for block:before check OOOOO ", self.possible_values)
        for each_block_row in range(self.block_size):
            for each_block_row_index in range(self.block_size):
                if self.sudoku_table[row][block][each_block_row][each_block_row_index] != 0:
                    if self.sudoku_table[row][block][each_block_row][each_block_row_index] in self.possible_values:
                        self.possible_values.remove(self.sudoku_table[row][block][each_block_row][each_block_row_index])
        self.log("possible_values for block:after check OOOOO ", self.possible_values)

        if len(self.possible_values) == 1:
            self.log("there is only 1 value for the cell: ", self.possible_values[0])
            self.cell_need_to_solve -= 1
            self.log("cell_need_to_solve -1: ", self.cell_need_to_solve)
            self.sudoku_table[row][block][block_row][block_row_index] = self.possible_values[0]
        self.log("empty self.possible_values")
        self.possible_values.clear()
        self.log(self.sudoku_table)

    def log(self, *msg):
        if self.show_log:
            print(*msg)
