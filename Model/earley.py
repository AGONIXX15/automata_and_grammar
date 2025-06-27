"""implementacion de el algoritmo de Earley"""


class State:
    def __init__(self, prod: str, before_dot: list[str], after_dot: list[str], origin: int):
        self.prod: str = prod
        self.before_dot: list[str] = before_dot
        self.after_dot: list[str] = after_dot
        self.origin: int = origin

    def advance(self):
        return State(self.prod, self.before_dot + [self.after_dot[0]], self.after_dot[1:], self.origin)

    def next_symbol(self) -> str | None:
        return self.after_dot[0] if self.after_dot else None

    def is_complete(self) -> bool:
        """mirar si ya termino de procesar la produccion"""
        return len(self.after_dot) == 0

    def __eq__(self, other) -> bool:
        return (self.prod == other.prod and
                self.before_dot == other.before_dot and
                self.after_dot == other.after_dot and
                self.origin == other.origin)

    def __hash__(self) -> int:
        return hash((self.prod, tuple(self.before_dot), tuple(self.after_dot), self.origin))

    def __str__(self) -> str:
        return f"State(prod={self.prod}, before_dot={self.before_dot}, after_dot={self.after_dot}, origin={self.origin})"


def completer(state: State, charts: list[set[State]], index: int):
    for prev_state in list(charts[state.origin]):
        if prev_state.next_symbol() == state.prod:
            new_state = prev_state.advance()
            if new_state not in charts[index]:
                charts[index].add(new_state)


def predictor(state: State, charts: list[set[State]], index: int, productions: dict[str, set[str]]):
    symbol = state.next_symbol()
    if symbol is None:
        return

    for production in productions.get(symbol, []):
        new_state: State = State(symbol, [], list(production), index)
        if new_state not in charts[index]:
            charts[index].add(new_state)


def scanner(state: State, charts: list[set[State]], index: int, input_string: str):
    symbol = state.next_symbol()
    if symbol is not None and index < len(input_string) and input_string[index] == symbol:
        new_state = state.advance()
        if new_state not in charts[index + 1]:
            charts[index + 1].add(new_state)


def earley_parser(input_string: str, production: dict[str, set[str]], s: str, t: set[str],) -> bool:
    """Implementacion del algoritmo de Earley para el analisis sintactico"""
    n = len(input_string)
    charts: list[set[State]] = [set() for _ in range(n + 1)]
    charts[0].add(State("S'", [], list(s), 0))
    for i in range(n + 1):
        changed: bool = True
        while changed:
            changed = False
            current_states = list(charts[i])
            for state in current_states:
                if state.is_complete():
                    # guardamos tamaño anterior y vamos a verificar
                    # si cambio algo en el chart
                    size_before: int = len(charts[i])
                    completer(state, charts, i)
                    if len(charts[i]) > size_before:
                        changed = True
                else:
                    next_symbol = state.next_symbol()
                    if next_symbol in production:
                        size_before: int = len(charts[i])
                        predictor(state, charts, i, production)
                        # verificamos si cambio algo en el chart
                        if len(charts[i]) > size_before:
                            changed = True
                    elif next_symbol in t:
                        size_before: int = len(charts[i])
                        scanner(state, charts, i, input_string)
                        # verificamos si cambio algo en el chart
                        if len(charts[i]) > size_before:
                            changed = True
    final_state = State("S'", list(s), [], 0)
    return final_state in charts[n]


s = "S"
productions = {
    "S": {"A"},
    "A": {"aA", "b"},
}
t = {"a", "b"}
# a*b
<<<<<<< HEAD:Model/earley.py
=======

print(earley_parser("aaab", productions, s, t))  # True
>>>>>>> bf17088 (rebase with the main branch):earley.py
