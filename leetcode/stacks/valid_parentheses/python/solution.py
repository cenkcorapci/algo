def solve(s: str) -> bool:
    open_brackets: list[str] = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for c in s:
        if c in "([{":
            open_brackets.append(c)
            continue
        if not open_brackets or open_brackets[-1] != pairs.get(c):
            return False
        open_brackets.pop()
    return not open_brackets


def main() -> None:
    print(solve("()[]{}"))


if __name__ == "__main__":
    main()
