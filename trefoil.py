import sympy as sp
import itertools

class Shadow:
    def __init__(self):
        """
        Initialize as trefoil knot shadow
        """
        self.num_crossings = 3
        self.num_edges = 6
        
        # Each dictionary represents a crossing, and the elements of the value tuples represent the strands.
        self.crossings = [
            {'in': (5, 2), 'out': (0, 3)},
            {'in': (0, 3), 'out': (1, 4)},
            {'in': (1, 4), 'out': (2, 5)}
        ]

    def num_loops(self, state):
        """
        Use the Union-Find data structure to calculate the number of loops for a given state
        `state` is a tuple of 0s and 1s representing the shadow smoothing choice (s_1 or s_2) at each crossing in the order of `crossings`.
        """
        # Initialize the Union-Find structure
        parent = list(range(self.num_edges))
        
        def find(i):
            """Path compression"""
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
            
        def union(i, j):
            """Union"""
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_j] = root_i

        # Smooth each crossing according to the current state
        for i, s in enumerate(state):
            c = self.crossings[i]
            if s == 0: 
                # s_1 connects in[0] to out[1] and in[1] to out[0].
                union(c['in'][0], c['out'][1])
                union(c['in'][1], c['out'][0])
            else:      
                # s_2 connects in[0] to in[1] and out[0] to out[1].
                union(c['in'][0], c['in'][1])
                union(c['out'][0], c['out'][1])

        # Count the number of loops
        loops = len(set(find(i) for i in range(self.num_edges)))
        return loops

def ajp(shadow):
    """
    Compute the AJP
    """
    A = sp.Symbol('A')
    n = shadow.num_crossings
    V_avg = 0
    E_1 = 0.5 * (-A**(-2) - A**2)
    E_2 = 0.5 * (-A**(-4) - A**4)
    
    # Iterate over all possible 2^n states
    for state in itertools.product([0, 1], repeat=n):
        loops = shadow.num_loops(state) 
        
        # Calculate the Kauffman loop value
        P_s = (-A**2 - A**(-2))**(loops - 1)
        
        # Calculate the weight contribution
        weight = 1
        for i in range(n):
            weight *= E_1 if state[i] == 0 else E_2
                
        # Accumulate the weighted polynomial sum
        V_avg += P_s * weight
        
    # Return the expanded algebraic expression
    return sp.expand(V_avg)

trefoil = Shadow()
print(ajp(trefoil))