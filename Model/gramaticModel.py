from typing import List, Dict, Set


class Gramatic:
    def __init__(self):
        self.vocabulary = set()
        self.terminals: Set[str] = set()
        self.non_terminals: Set[str] = set()
        self.start_symbol: str = ""
        self.productions: Dict[str, Set[str]] = {}

    def set_non_terminals(self, symbols: List[str]):
        self.non_terminals = set(symbols)

    def set_terminals(self, symbols: List[str]):
        self.terminals = set(symbols)

    def set_start_symbol(self, symbol: str):
        self.start_symbol = symbol
        self.non_terminals.add(symbol)

    def set_vocabulary(self):
        self.vocabulary = self.terminals.union(self.non_terminals)

    def delete_productions(self):
        self.productions = dict()

    def add_production(self, lhs: str, rhs: str):
        if lhs not in self.productions:
            self.productions[lhs] = set()
        self.productions[lhs].add(rhs)

    def __str__(self):
        output = [f"Símbolo inicial: {self.start_symbol}",
                  f"Terminales: {', '.join(sorted(self.terminals))}",
                  f"No terminales: {', '.join(sorted(self.non_terminals))}",
                  "Producciones:"]
        for lhs, rhss in self.productions.items():
            for rhs in rhss:
                output.append(f"  {lhs} -> {rhs}")
        return "\n".join(output)
