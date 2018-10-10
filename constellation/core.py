import typing

import networkx as nx


class Pattern:
    patterns: typing.Dict[str, 'Pattern'] = {}

    def __init__(self, name: str, validator: typing.Callable[[typing.Any], bool] = lambda _: True,
                 parameter_type: typing.Type = typing.Any):
        self.implementations = []
        self.validator = validator
        self.parameter_type = parameter_type
        self.name = name

        if name in self.patterns:
            raise ValueError(f"Pattern name {name} is already taken.")

        self.patterns[name] = self

    def register_impl(self, implementation: 'Implementation'):
        self.implementations.append(implementation)

    def __str__(self):
        return f"{self.name}<{self.parameter_type}>"


Placeholder = Pattern("Placeholder")

Argument = Pattern("Argument")

Constant = Pattern("Constant")


class Implementation:
    def __init__(self, pattern: Pattern, graph: nx.DiGraph):
        self.pattern = pattern
        self.graph = graph
        self.pattern.register_impl(self)


class Function:
    def __init__(self, graph: nx.MultiDiGraph, inputs: typing.Dict[int, typing.List[int]],
                 outputs: typing.Dict[int, int]):
        """
        :param graph: A MultiDiGraph encoding the sub-computation
        :param inputs: Mapping from each input number to a set of associative inputs. These nodes should all have type
                        Argument.
        :param outputs: Mapping from output number to output node. These nodes should have type Placeholder.
        """
        self.graph = graph
        self.inputs = inputs
        self.outputs = outputs

        for input_id, input_nodes in inputs.items():
            for node_id in input_nodes:
                node_type = graph.nodes[node_id]['type']
                if node_type is not Argument:
                    raise ValueError(f"Expected Argument at input node {node_id}. Instead received {node_type}")

        for node_id in outputs.values():
            node_type = graph.nodes[node_id]['type']
            if node_type is not Placeholder:
                raise ValueError(f"Expected Placeholder at output node {node_id}. Instead received {node_type}")

    @property
    def input_arity(self):
        return sum(map(len, self.inputs.values()))

    @property
    def output_arity(self):
        return len(self.outputs)
