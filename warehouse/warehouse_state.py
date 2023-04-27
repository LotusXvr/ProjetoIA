import numpy as np
from PIL.ImageEnhance import Color
from numpy import ndarray

import constants
from agentsearch.state import State
from agentsearch.action import Action
from warehouse.actions import *

class WarehouseState(State[Action]):

    def __init__(self, matrix: ndarray, rows, columns):
        super().__init__()
        # TODO

        self.rows = rows
        self.columns = columns
        self.matrix = np.full([self.rows, self.columns], fill_value=0, dtype=int)

        for i in range(self.rows):
            for j in range(self.columns):
                self.matrix[i][j] = matrix[i][j]
                if self.matrix[i][j] == constants.FORKLIFT:
                    self.line_forklift = i
                    self.column_forklift = j
                if self.matrix[i][j] == constants.EXIT:
                    self.line_exit = i
                    self.column_exit = j

    '''
    nos can_moves horizontais o agente apenas pode andar para o lado se não estiver numa das bordas
    horizontais e quiser-se mover para OutOfBounds e se não for um prateleira. Pode mover se ao lado for uma
    célula vazia ou um produto
    
    nos can_moves verticais o agente apenas pode andar para cima ou baixo se não estiver numa das bordas
    verticais e quiser-se mover para OutOfBounds e se não for um prateleira ou um produto. Pode mover se ao 
    lado for uma célula vazia
    
    em nenhum dos casos se pode mover para cima de um agente
    '''

    def can_move_up(self) -> bool:
        forklift_up = self.matrix[self.line_forklift - 1][self.column_forklift]
        if self.line_forklift > 0:
            if forklift_up != constants.SHELF and forklift_up != constants.PRODUCT:
                return True
        return False

    def can_move_right(self) -> bool:
        forklift_right = self.matrix[self.line_forklift][self.column_forklift + 1]
        if self.column_forklift < self.columns - 1:
            if forklift_right != constants.SHELF:
                return True
        return False

    def can_move_down(self) -> bool:
        forklift_down = self.matrix[self.line_forklift + 1][self.column_forklift]
        if self.line_forklift < self.rows - 1:
            if forklift_down != constants.SHELF and forklift_down != constants.PRODUCT:
                return True
        return False

    def can_move_left(self) -> bool:
        forklift_left = self.matrix[self.line_forklift][self.column_forklift - 1]
        if self.column_forklift > 0:
            if forklift_left != constants.SHELF:
                return True
        return False

    def move_up(self) -> None:
        self.matrix[self.line_forklift][self.column_forklift] = constants.EMPTY
        self.matrix[self.line_forklift - 1][self.column_forklift] = constants.FORKLIFT
        self.line_forklift -= 1
        pass

    def move_right(self) -> None:
        self.matrix[self.line_forklift][self.column_forklift] = constants.EMPTY
        self.matrix[self.line_forklift][self.column_forklift + 1] = constants.FORKLIFT
        self.column_forklift += 1
        pass

    def move_down(self) -> None:
        self.matrix[self.line_forklift][self.column_forklift] = constants.EMPTY
        self.matrix[self.line_forklift + 1][self.column_forklift] = constants.FORKLIFT
        self.line_forklift += 1
        pass

    def move_left(self) -> None:
        self.matrix[self.line_forklift][self.column_forklift] = constants.EMPTY
        self.matrix[self.line_forklift][self.column_forklift - 1] = constants.FORKLIFT
        self.column_forklift -= 1
        pass

    def get_cell_color(self, row: int, column: int) -> Color:
        if row == self.line_exit and column == self.column_exit and (
                row != self.line_forklift or column != self.column_forklift):
            return constants.COLOREXIT

        if self.matrix[row][column] == constants.PRODUCT_CATCH:
            return constants.COLORSHELFPRODUCTCATCH

        if self.matrix[row][column] == constants.PRODUCT:
            return constants.COLORSHELFPRODUCT

        switcher = {
            constants.FORKLIFT: constants.COLORFORKLIFT,
            constants.SHELF: constants.COLORSHELF,
            constants.EMPTY: constants.COLOREMPTY
        }
        return switcher.get(self.matrix[row][column], constants.COLOREMPTY)

    def __str__(self):
        matrix_string = str(self.rows) + " " + str(self.columns) + "\n"
        for row in self.matrix:
            for column in row:
                matrix_string += str(column) + " "
            matrix_string += "\n"
        return matrix_string

    def __eq__(self, other):
        if isinstance(other, WarehouseState):
            return np.array_equal(self.matrix, other.matrix)
        return NotImplemented

    def __hash__(self):
        return hash(self.matrix.tostring())
