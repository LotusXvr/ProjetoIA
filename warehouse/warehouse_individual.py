from ga.individual_int_vector import IntVectorIndividual
from warehouse.cell import Cell


class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        # TODO
        self.forklifts = []  # Lista para armazenar as posições dos genes que representam as divisões dos genomas
        self.fitness = 0

    # Fitness será calculado baseado na quantidade de produtos que o agente apanhou. Quantos mais, melhor
    # ir ao genoma ver a distancia do forklift ao primeiro produto do genoma self.problem.products[]
    # depois ver p_value de cada par de celula 1 a celula 2 e separar o maior numero com os forklifts
    # percorrer sempre o genoma e acrescentar +1 ao forklift
    # também é importante ver a distancia max entre os produtos, para que não haja forklifts parados
    def compute_fitness(self) -> float:
        # TODO
        genoma = self.genome
        forklifts = self.problem.forklifts
        products = self.problem.products
        distance = 0
        num_products_caught = 0  # Contador de produtos apanhados
        pos_agente = 0  # Índice do forklift atual
        # Calcula a distância percorrida por cada forklift
        for i in range(len(genoma)):
            gene = genoma[i]
            if gene < len(products):
                # Atualiza a distância do forklift atual ao primeiro produto do genoma
                distance += self.get_pair_distance(forklifts[pos_agente], products[gene-1])
                num_products_caught += 1
            else:
                # Atualiza a distância entre dois produtos consecutivos no genoma
                prev_gene = genoma[i - 1]
                distance += self.get_pair_distance(products[prev_gene], products[gene-1])

        distance += self.get_pair_distance(forklifts[pos_agente], self.problem.agent_search.exit)
        self.fitness = distance
        return self.fitness

    # obter a distancia entre pares, verifica a ordem a qual o par está guardado no array de pares
    def get_pair_distance(self, cell1: Cell, cell2: Cell) -> int:
        for pair in self.problem.agent_search.pairs:
            if pair.cell1 == cell1 and pair.cell2 == cell2 or pair.cell1 == cell2 and pair.cell2 == cell1:
                return pair.value
        return 0

    # este serve para meter o boneco a funcionar. ultima coisa a ser feita
    def obtain_all_path(self):
        paths = []
        genoma = self.genome
        forklifts = self.problem.forklifts
        posForkAnterior = 0
        for i in range(1, len(forklifts)):
            cut = genoma[posForkAnterior:forklifts[i]]
            posForkAnterior = forklifts[i]
            path = []
            for gene in cut:
                path.append(self.problem.products[gene])  # Append the actual product based on the gene index
            paths.append(path)
        return paths

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
        return new_instance