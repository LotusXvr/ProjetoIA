import constants
from agentsearch.heuristic import Heuristic
from warehouse.warehouse_problemforSearch import WarehouseProblemSearch
from warehouse.warehouse_state import WarehouseState


class HeuristicWarehouse(Heuristic[WarehouseProblemSearch, WarehouseState]):

    def __init__(self):
        super().__init__()
        self._lines_goal_matrix = None
        self._cols_goal_matrix = None

    def compute(self, state: WarehouseState) -> float:
        # TODO
        h = 0
        for i in range(state.rows):
            for j in range(state.columns):
                if state.matrix[i][j] == constants.PRODUCT:
                    # calculate distance from the product to the forklift
                    h += abs(i - state.line_forklift) + abs(j - state.column_forklift)
        return h

    def __str__(self):
        return "# TODO"

