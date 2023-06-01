from ga.individual_int_vector import IntVectorIndividual


class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        # TODO
        self.forklifts = []  # Lista para armazenar as posições dos genes que representam as divisões dos genomas


    def compute_fitness(self) -> float:
        # TODO
        # Fitness será calculado baseado na quantidade de produtos que o agente apanhou. Quantos mais, melhor
        # ir ao genoma ver a distancia do forklift ao primeiro produto do genoma self.problem.products[]
        # depois ver p_value de cada par de celula 1 a celula 2 e separar o maior numero com os forklifts
        # percorrer sempre o genoma e acrescentar +1 ao forklift
        # também é importante ver a distancia max entre os produtos, para que não haja forklifts parados
        genoma = self.genome
        forklifts = self.problem.forklifts
        products = self.problem.products
        distance = 0
        num_products_caught = 0  # Contador de produtos apanhados
        max_distance_between_products = 0  # Distância máxima entre produtos para evitar forklifts parados
        posAgente = 0  # Índice do forklift atual
        for i in range(len(genoma)):
            gene = genoma[i]
            if gene < len(products):
                # Atualiza a distância do forklift atual ao primeiro produto do genoma
                distance += self.problem.p_value[forklifts[posAgente]][products[gene]]
                num_products_caught += 1
            else:
                # Atualiza a distância entre dois produtos consecutivos no genoma
                distance += self.problem.p_value[products[genoma[i - 1]]][products[genoma[i]]]
                max_distance_between_products = max(max_distance_between_products,
                                                    self.problem.p_value[products[genoma[i - 1]]][
                                                        products[genoma[i]]])
            posAgente = (posAgente + 1) % len(forklifts)  # Avança para o próximo forklift

        # Penaliza a distância máxima entre produtos para evitar forklifts parados
        distance += max_distance_between_products * (len(forklifts) - num_products_caught)

        self.fitness = distance
        return distance

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