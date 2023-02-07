import random
from collections import defaultdict

PREFIX_LENGTH = 2


def sliding_window(text: str, n: int):
    words = text.split()
    for i in range(len(words) - n + 1):
        yield words[i : i + n]


class MarkovChain:
    def __init__(self):
        self.transitions: defaultdict[tuple[str, ...], defaultdict[str, int]] = defaultdict(lambda: defaultdict(int))

    def add_transition(self, prefix: tuple[str, ...], next_word: str):
        self.transitions[prefix][next_word] += 1

    def parse_text(self, text: str):
        for words in sliding_window(text, PREFIX_LENGTH + 1):
            self.add_transition(tuple(words[:-1]), words[-1])

    def generate_text(self, length=256) -> str:
        result = list(random.choice(list(self.transitions.keys())))
        for _ in range(length):
            prefix = tuple(result[-PREFIX_LENGTH:])
            while len(prefix) < PREFIX_LENGTH:
                prefix = (None,) + prefix
            if prefix not in self.transitions:
                result.append("<end>")
                break
            next_word = random.choices(
                list(self.transitions[prefix].keys()), weights=list(self.transitions[prefix].values())
            )[0]
            result.append(next_word)
        return " ".join(result)


if __name__ == "__main__":
    from pathlib import Path

    chain = MarkovChain()

    for input_path in Path(__file__).parent.glob("texts/*.txt"):
        input_text = input_path.read_text(encoding="utf-8")
        chain.parse_text(input_text)

    print(chain.generate_text())
