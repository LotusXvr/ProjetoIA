from ga.individual_int_vector import IntVectorIndividual
from warehouse.cell import Cell


class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        # TODO
        self.path = []  # Lista para armazenar as posições dos genes que representam as divisões dos genomas
        self.fitness = 0
        self.forklifts = problem.forklifts
        self.products = problem.products
        self.max_steps = 0
        self.cell_path = []

    # Fitness será calculado baseado na quantidade de produtos que o agente apanhou. Quantos mais, melhor
    # ir ao genoma ver a distancia do forklift ao primeiro produto do genoma self.problem.products[]
    # depois ver p_value de cada par de celula 1 a celula 2 e separar o maior numero com os forklifts
    # percorrer sempre o genoma e acrescentar +1 ao forklift
    # também é importante ver a distancia max entre os produtos, para que não haja forklifts parados
    def compute_fitness(self) -> float:
        # TODO
        k = 0
        path = []

        # Calcula a distância percorrida por cada forklift
        for i in range(len(self.forklifts)):
            path.append([self.forklifts[i]]) # adicionar o forklift ao path

            while k < len(self.genome):
                gene = self.genome[k]

                if gene <= len(self.products): # se o gene for menor ou igual ao numero de produtos
                    prev_gene = gene - 1 # gene anterior
                    path[i].append(self.products[prev_gene]) # adicionar o produto ao path
                    k += 1
                else:
                    k += 1 # se o gene for maior que o numero de produtos, passa para o proximo gene
                    break

            path[i].append(self.problem.agent_search.exit) # adicionar a saida ao path

        # CALCULAR A FITNESS
        fitness = 0
        for i in range(len(path)): # percorre os forklifts
            for j in range(len(path[i]) - 1): # percorre as celulas
                fitness += self.get_pair_distance(path[i][j], path[i][j + 1]) # soma a distancia entre as celulas

        self.path = path
        self.fitness = fitness
        return self.fitness

    # obter a distancia entre pares, verifica a ordem a qual o par está guardado no array de pares
    def get_pair_distance(self, cell1: Cell, cell2: Cell) -> int:
        for pair in self.problem.agent_search.pairs:
            if pair.cell1 == cell1 and pair.cell2 == cell2 or pair.cell1 == cell2 and pair.cell2 == cell1:
                return pair.value
        return 0

    # este serve para meter o boneco a funcionar. ultima coisa a ser feita
    def obtain_all_path(self):
        cell_path = []
        max_steps = 0
        # percorrer o path e ir buscar os forklifts
        for i in range(len(self.forklifts)):
            cell_path.append([])
            for j in range(len(self.path[i]) - 1): # percorre as celulas
                # descobrir a celula que o forklift vai percorrer
                cell_path[i].extend(self.get_pair_cells(self.path[i][j], self.path[i][j + 1])) # adicionar as celulas ao path
                # impedir que o forklift fique parado no mesmo sitio (na mesma celula),
                # sendo que a celula inicial não pode ser igual à celula final do percurso anterior
                if j < len(self.path[i]) - 2: # se não for a ultima celula
                    cell_path[i].pop(-1) # remover a ultima celula do percurso

            # descobrir o numero de passos que o forklift vai dar
            if len(cell_path[i]) > max_steps:
                max_steps = len(cell_path[i])

        self.max_steps = max_steps
        self.cell_path = cell_path
        return self.cell_path, self.max_steps

    def get_pair_cells(self, cell1: Cell, cell2: Cell) -> list:
        for pair in self.problem.agent_search.pairs:
            if pair.cell1 == cell1 and pair.cell2 == cell2:
                return pair.cells # retorna a ordem das celulas
            elif pair.cell1 == cell2 and pair.cell2 == cell1:
                return pair.cells[::-1] # inverte a ordem das celulas
        return []
    def __str__(self):
        string = 'Fitness: ' + f'{self.fitness}' + '\n'
        string += str(self.genome) + "\n\n"
        # TODO
        return string

    def better_than(self, other: "WarehouseIndividual") -> bool:
        return True if self.fitness < other.fitness else False

    # __deepcopy__ is implemented here so that all individuals share the same problem instance
    def __deepcopy__(self, memo):
        # TODO
        new_instance = self.__class__(self.problem, self.num_genes)
        new_instance.genome = self.genome.copy()
        new_instance.fitness = self.fitness
        new_instance.path = self.path.copy()
        new_instance.max_steps = self.max_steps
        new_instance.cell_path = self.cell_path.copy()
        return new_instance