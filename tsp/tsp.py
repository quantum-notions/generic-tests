import dwave_networkx as dnx
import networkx as nx

from dimod.reference.samplers import ExactSolver

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

G = nx.complete_graph(4)
G.add_weighted_edges_from({(0, 1, 1), (0, 2, 2), (0, 3, 3), (1, 2, 3), (1, 3, 4), (2, 3, 5)})

sampler = ExactSolver()
d_sampler = EmbeddingComposite(DWaveSampler())

answer = dnx.traveling_salesman(G, sampler)
d_answer = dnx.traveling_salesman(G, d_sampler, 1)

print(answer)
print(d_answer)
