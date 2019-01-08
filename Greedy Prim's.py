class AdjMatrix:
    def __init__(self, vertices):
        self._matrix = []
        self.vertexMap = dict()

        vertices = self.get_unique_vertices(vertices)
        self.add_vertex_names(vertices)
        self.add_vertices(len(vertices))

    def __str__(self):
        key_list = list(self.get_vertex_names())
        out_string = " ".join(key_list) + "\n\n"
        for row in self._matrix:
            out_string += " ".join(str(char) for char in row) + "\n"
        return out_string

    """
    Goes through a list of strings or list of pairs of names (list)
    and converts into a list of lists for later use. Can also handle
    a mix of list of list and list of string (provided space/comma sep)
    (if given a list of lists, output is unchanged)
    outputs processed version
    """
    @staticmethod
    def process_edge_list(edge_list):
        processed_edge_list = []
        for each in edge_list:
            if isinstance(each, str):
                each = each.strip()
                if 1 <= each.count(" ") <= 2:  # either a vertex pair
                    #  or vertex pair with weight
                    each = each.split(" ")  # for space sep
                elif 1 <= each.count(",") <= 2:
                    each = each.split(",")  # for comma sep
                else:
                    raise ValueError("list of edges (if given as a list of strings) must be two vertex names "
                                     "separated by a space or a comma")
                processed_edge_list.append(each)
            elif isinstance(each, list):
                processed_edge_list.append(each)
            else:
                raise ValueError("edge list must either be a list of lists (or vertex names) or a list of strings")
        return processed_edge_list

    """
    Accepts an edge_list (as a list of pairs of vertices)
    outputs a list of unique vertices
    """
    @staticmethod
    def get_unique_vertices(edge_list):
        vertices = []
        for each in edge_list:
            if each[0] not in vertices:
                vertices.append(each[0])
            try:
                if each[1] not in vertices:
                    vertices.append(each[1])
            except IndexError:
                pass
        return vertices

    """
    Maps vertex names to appropriate indexes in the adjacency matrix representation.
    Returns the number of vertexes added in each call.
    Modifies self.vertexMap
    """
    def add_vertex_names(self, unique_vertices):
        initial_vert_num = len(self.vertexMap)
        vert_num = initial_vert_num
        for vertex in unique_vertices:
            if vertex not in self.vertexMap:
                self.vertexMap[vertex] = vert_num
                vert_num += 1
        return vert_num - initial_vert_num

    """
    Gets the matrix index for the vertex name given.
    """
    def _ID(self, v_name):
        return self.vertexMap[v_name]

    """
    Expands the adjacency matrix self._matrix to accommodate new vertices and possible edges.
    """
    def add_vertices(self, num_added):
        if num_added > 0:
            initial_num_vertices = len(self._matrix)
            final_num_vertices = initial_num_vertices + num_added

            # Add to existing rows
            for row_idx in range(initial_num_vertices):
                self._matrix[row_idx] += [0] * num_added

            # Add new rows
            for _ in range(initial_num_vertices, final_num_vertices):
                self._matrix.append([0] * final_num_vertices)

    """
    Takes a list of edges and adds these edges into the matrix.
    The matrix is undirected, so edges are added in both positions (i,j) and (j,i)
    self._matrix is updated to match

    precond: vertexmapping must be defined already and edge_list must
            be a list of lists (pairs of vertex names) 
            self._matrix must be defaulted to correct size already 
    """
    def add_edges(self, edge_list):
        weight = 1  # default weight
        for edge in edge_list:
            start = self._ID(edge[0])
            end = self._ID(edge[1])
            if len(edge) == 3:
                weight = edge[2]  # for each edge where a weight is given, overwrite with correct weight
            self._matrix[start][end] = weight
            self._matrix[end][start] = weight

    """
    Accepts a raw edge list (either a list of lists of vertex name pairs
    or a list of strings of two vertices seperated by space/comma)
    no outputs, modifies self._matrix
    """
    def add_edge_list(self, raw_edge_list):
        edge_list = self.process_edge_list(raw_edge_list)

        # Add new vertices to adjacency matrix and vertex dictionary
        input_vertices = self.get_unique_vertices(edge_list)
        num_vertices_added = self.add_vertex_names(input_vertices)
        self.add_vertices(num_vertices_added)

        # Add new edges to adjacency matrix
        self.add_edges(edge_list)

    """
    Gives the full list of vertex names in this graph
    """
    def get_vertex_names(self):
        return self.vertexMap.keys()

    """
    Determines whether any two vertices are adjacent
    @:param vertOne: a string holding the name of the first vertex
    @:param vertTwo: a string holding the name of the second vertex
    @:return True/False: if adjacent/not adjacent
    """
    def is_adjacent(self, vertex_one, vertex_two):
        start = self._ID(vertex_one)
        end = self._ID(vertex_two)
        return self._matrix[start][end] != 0

    """
    Gets the name of a vertex at a given index of the adjacency matrix.
    """
    def get_vertex_name(self, vert_num):
        for name in self.get_vertex_names():
            if self.vertexMap[name] == vert_num:
                return name

    """
    Returns all edges ([start, end, weight]) connected to a given vertex.
    """
    def get_vertex_edges(self, vertex):
        edges = []
        vertex_row = self._matrix[self._ID(vertex)]
        for col_idx in range(len(vertex_row)):
            if vertex_row[col_idx] > 0:
                edges.append([vertex, self.get_vertex_name(col_idx), vertex_row[col_idx]])
        return edges


################################################################################################

def find_min_edge(graph, tree):
    tree_vertices = tree.get_vertex_names()

    # Get list of edges that connect a vertex in the tree to a vertex not in the tree
    possible_edges = []
    for vertex in tree_vertices:
        vertex_edges = graph.get_vertex_edges(vertex)
        for edge in vertex_edges:
            if edge[1] not in tree_vertices:
                possible_edges.append(edge)

    # Get the edge with the minimum weight
    min_edge = possible_edges[0]
    for edge in possible_edges:
        if edge[2] < min_edge[2]:
            min_edge = edge

    return min_edge


def minimum_spanning_tree(graph, start=None):
    graph_vertices = list(graph.get_vertex_names())
    if start is None or start not in graph_vertices:
        start = graph_vertices[0]
    tree = AdjMatrix([start])
    while len(graph_vertices) > len(tree.get_vertex_names()):
        edge = find_min_edge(graph, tree)
        tree.add_edge_list([edge])
    return tree


G = AdjMatrix([])
edge_list = [["A", "B", 3],
             ["B", "C", 4],
             ["B", "D", 2],
             ["A", "D", 20],
             ["A", "E", 1],
             ["C", "E", 6],
             ["D", "E", 5]]  # Add edge list here
G.add_edge_list(edge_list)
print(G)

MST = minimum_spanning_tree(G)
print(MST)