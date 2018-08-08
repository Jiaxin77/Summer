
#定义计算的流程结构
class Graph:

    def __init__(self):
        self.operations = []
        self.placeholders = []
        self.variables = []

    def as_default(self):
        global _default_graph
        _default_graph = self


class placeholder:

    def __init__(self):
        self.output = None
        self.go = []

        _default_graph.placeholders.append(self)


class Variable:

    def __init__(self, initial_value=None):
        self.output = initial_value
        self.go = []

        _default_graph.variables.append(self)


class Operation:

    def __init__(self, come=[]):
        self.come = come
        self.go = []
        self.output = None

        for i in come:
            i.go.append(self)

        _default_graph.operations.append(self)


class matmul(Operation):

    def __init__(self, n, m):
        super().__init__([n, m])

    def compute(self,a,b):
        return a.dot(b)


class add(Operation):

    def __init__(self, n, m):
        super().__init__([n, m])

    def compute(self, a, b):
        return a + b