from sudoku import sudoku

sudoku = sudoku()

sudoku.set_value(1, 1, 1)
sudoku.set_value(1, 4, 4)
sudoku.set_value(1, 5, 8)
sudoku.set_value(1, 6, 9)
sudoku.set_value(1, 9, 6)

sudoku.set_value(2, 1, 7)
sudoku.set_value(2, 2, 3)
sudoku.set_value(2, 8, 4)

sudoku.set_value(3, 6, 1)
sudoku.set_value(3, 7, 2)
sudoku.set_value(3, 8, 9)
sudoku.set_value(3, 9, 5)

sudoku.set_value(4, 3, 7)
sudoku.set_value(4, 4, 1)
sudoku.set_value(4, 5, 2)
sudoku.set_value(4, 7, 6)

sudoku.set_value(5, 1, 5)
sudoku.set_value(5, 4, 7)
sudoku.set_value(5, 6, 3)
sudoku.set_value(5, 9, 8)

sudoku.set_value(6, 3, 6)
sudoku.set_value(6, 5, 9)
sudoku.set_value(6, 6, 5)
sudoku.set_value(6, 7, 7)

sudoku.set_value(7, 1, 9)
sudoku.set_value(7, 2, 1)
sudoku.set_value(7, 3, 4)
sudoku.set_value(7, 4, 6)
sudoku.set_value(8, 2, 2)
sudoku.set_value(8, 8, 3)
sudoku.set_value(8, 9, 7)

sudoku.set_value(9, 1, 8)
sudoku.set_value(9, 4, 5)
sudoku.set_value(9, 5, 1)
sudoku.set_value(9, 6, 2)
sudoku.set_value(9, 9, 4)

sudoku.solve()
