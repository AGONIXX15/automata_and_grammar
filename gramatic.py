import re
from collections import deque


# diccionario guarda lista string
def language(v: set[str], t: set[str], s: str, p: dict[str, list[str]], max_iterations: int) -> set[str]:
    n: set[str] = v - t

    ans: set[str] = set()

    def helper(string: str, can_save: bool, iterations: int) -> None:
        if iterations >= max_iterations:
            return

        if can_save:
            ans.add(string)
            return

        for key, values in p.items():
            for match in re.finditer(key, string):
                for val in values:
                    new_str: str = "".join(
                        string[:match.start()]+val+string[match.end():])
                    save: bool = all(x in t for x in new_str)
                    helper(new_str, save, iterations + 1)

    for inicial_string in p[s]:
        can_save: bool = all(x in t for x in inicial_string)
        helper(inicial_string, can_save, 0)
    return ans


def language1(v: set[str], t: set[str], s: str, p: dict[str, list[str]], max_iterations: int) -> set[str]:
    queue = deque([(s, 0)])
    ans: set[str] = set()
    visited: set[str] = set()
    while queue:
        initial, iterations = queue.popleft()
        if initial in visited:
            continue
        visited.add(initial)
        if iterations >= max_iterations:
            continue

        if all(x in t for x in initial):
            ans.add(initial)

        for key, values in p.items():
            for match in re.finditer(key, initial):
                for val in values:
                    new_str: str = "".join(
                        initial[:match.start()] + val + initial[match.end():])
                    queue.append((new_str, iterations+1))
    return ans


def check(v: set[str], t: set[str], s: str, p: dict[str, list[str]], word: str, max_iterations: int) -> bool:
    if any(ch not in t for ch in word):
        return False
    queue = deque([(s, 0)])
    while queue:
        current_str, level = queue.popleft()
        if level >= max_iterations:
            return False

        if current_str == word:
            return True

        for key, values in p.items():
            for match in re.finditer(key, current_str):
                for val in values:
                    new_str: str = "".join(
                        current_str[:match.start()] + val + current_str[match.end():])
                    if len(new_str) <= len(word):
                        queue.append((new_str, level+1))


v = {'a', 'b', 'A', 'B', 'S'}
t = {'a', 'b'}
s = 'S'
p = {'S': ['A'], 'A': ['aA', 'bS', 'B', ''], 'B': ['bB', 'aA', 'bS']}

# v = {'0', '1'}
# t = {'0', '1'}
# s = 'S'
# p = {'S': ['0', '11S']}

print(language1(v, t, s, p, 25))
