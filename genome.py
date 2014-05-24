import random
import numpy as np
import matplotlib.pyplot as plt
class genome:
        def __init__(self, length = 0):
                 self.fitness = 0
                 self.bits = []
                 for i in range(length):
                    self.bits.append(random.randint(0, 1))
class ga:
        """
         simple Genetic Algorithms by bluebanboom
         reference:
         AI Techniques for Game Programming
        """
        def __init__(self,
                         pop_size,
                         genome_len,
                         expr = 'y = 0 - 2 * x * x + 8 * x + 4',
                         crossover_rate = 0.7,
                         mutation_rate = 0.01,
                         max_generation = 1000
                         ):

                 self.crossover_rate = crossover_rate
                 self.mutation_rate = mutation_rate
                 self.pop_size = pop_size
                 self.genome_len = genome_len
                 self.generation = 0
                 self.genomes = []
                 self.busy = False
                 self.fittest_genome = genome()
                 self.best_fitness_score = 0
                 self.total_fitness_score = 0
                 self.expr = expr
                 self.max_generation = max_generation

        def create_start_populations(self):
                del self.genomes[0:]
                for i in range(self.pop_size):
                         self.genomes.append(genome(self.genome_len))
                self.generation = 0
                self.best_fitness_score = 0
                self.total_fitness_score = 0

        def selection(self):
                 f_slice = random.uniform(0, 1) * self.total_fitness_score
                 c_f_slice = 0.0
                 selected_genome = 0
                 for i in range(self.pop_size):
                         c_f_slice = c_f_slice + self.genomes[i].fitness
                         if c_f_slice > f_slice:
                                 selected_genome = i
                         break
                 return self.genomes[i]

        def crossover(self, mum, dad):
                 baby1 = []
                 baby2 = []
                 if (random.uniform(0, 1) > self.crossover_rate):
                         baby1 = mum.bits;
                         baby2 = dad.bits;
                         return baby1, baby2
                 cp = random.randint(0, self.genome_len - 1)
                 for i in range(cp):
                         baby1.append(mum.bits[i])
                         baby2.append(dad.bits[i])

                 for i in range(cp, self.genome_len):
                         baby1.append(dad.bits[i])
                         baby2.append(mum.bits[i])
                 return baby1, baby2

        def mutate(self, bits):
                if (random.uniform(0, 1) < self.mutation_rate):
                         mp = random.randint(0, self.genome_len - 1)
                         bits[mp] = int(not bits[mp])

        def decode(self, gen):
                 x = self.bin2int(gen)
                 exec(self.expr)
                 return y

        def bin2int(self, lists):
                 m = 1
                 r = 0
                 lists.reverse()
                 for i in range(len(lists)):
                         r = r + m * lists[i]
                         m = m * 2
                 lists.reverse()
                 return r

        def update_fitness_scores(self):
                 self.total_fitness_score = 0
                 for i in range(self.pop_size):
                         self.genomes[i].fitness = self.decode(self.genomes[i].bits)
                         self.total_fitness_score += self.genomes[i].fitness
                         if self.genomes[i].fitness > self.best_fitness_score:
                                 self.best_fitness_score = self.genomes[i].fitness
                                 self.fittest_genome = self.genomes[i]

        def epoch(self):
                 self.update_fitness_scores()
                 new_babies = 0
                 baby_genomes = []
                 baby1 = genome()
                 baby2 = genome()
                 while (new_babies < self.pop_size):
                         mum = self.selection()
                         dad = self.selection()
                         baby1.bits, baby2.bits = self.crossover(mum, dad)
                         self.mutate(baby1.bits)
                         self.mutate(baby2.bits)
                         baby_genomes.append(baby1)
                         baby_genomes.append(baby2)
                         new_babies = new_babies + 2
                 self.genomes = baby_genomes
                 self.generation += 1
                 if self.generation >= self.max_generation:
                         self.busy = False

        def start(self):
                 self.busy = True
                 self.create_start_populations()

        def get_best_genome(self):
                return self.fittest_genome.bits

        def get_best_variable(self):
                return self.bin2int(self.fittest_genome.bits)

        def get_max_value(self):
                return self.decode(self.fittest_genome.bits)
def main():
        print "-----------------"
        testga = ga(pop_size = 8, genome_len = 4, expr = 'y = 0 - 2 * x * x + 12 * x + 5')
        testga.start()
        while testga.busy:
                 testga.epoch()
        print "Function: %s" % testga.expr
        print "The best genome is: ",
        print testga.get_best_genome()
        print "The variable is: %d" % testga.get_best_variable()
        print "The max value is %d" % testga.get_max_value()
        del testga
        print "-----------------"
        testga = ga(pop_size = 8, genome_len = 4)
        testga.start()
        while testga.busy:
                 testga.epoch()
        print "Function: %s" % testga.expr
        print "The best genome is: ",
        print testga.get_best_genome()
        print "The variable is: %d" % testga.get_best_variable()
        print "The max value is %d" % testga.get_max_value()
        print "-----------------"
        funx=np.arange(-5,5,0.01)
        funy=-funx*funx*2+12*funx+5
        plt.plot(funx,funy)
        plt.grid(True)
        plt.show()

if __name__ == '__main__':
         main()
