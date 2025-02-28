class MapColoringCSP:
    def __init__(self, variables, domains, constraints):
        self.variables, self.domains, self.constraints, self.assignment = variables, domains, constraints, {}
    def is_consistent(self, var, color):
        return all(self.assignment.get(neigh) != color for neigh in self.constraints[var])
    def select_unassigned_variable(self):
        return min([v for v in self.variables if v not in self.assignment], key=lambda v: len(self.domains[v]), default=None)
    def backtrack(self):
        if len(self.assignment) == len(self.variables): return self.assignment
        var = self.select_unassigned_variable()
        for color in self.domains[var]:
            if self.is_consistent(var, color):
                self.assignment[var] = color
                result = self.backtrack()
                if result: return result
                del self.assignment[var]
        return None
regions = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
constraints = {"WA":["NT","SA"], "NT":["WA","SA","Q"], "SA":["WA","NT","Q","NSW","V"], "Q":["NT","SA","NSW"], "NSW":["Q","SA","V"], "V":["SA","NSW"], "T":[]}
domains = {r:["Red","Green","Blue"] for r in regions}
csp = MapColoringCSP(regions, domains, constraints)
print(csp.backtrack())
