import networkx as nx
import dwave_networkx as dnx
from dimod.reference.samplers import ExactSolver

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

# g = nx.star_graph(4)
# g = nx.wheel_graph(5)
g = nx.circular_ladder_graph(12)

# sampler = ExactSolver()
#
# print("classical answer: ", dnx.min_vertex_cover(g, sampler))

d_sampler = EmbeddingComposite(DWaveSampler())

print("D_WAVE answer: ", dnx.min_vertex_cover(g, d_sampler))

# if __name__ == '__main__':
#     # get input from user
#     print("test")
#     P = 2 ** 2000
#     print (P)
