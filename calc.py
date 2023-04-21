from operator import add, sub, mul, truediv, pow
from sys import argv

operatorMapping = {
    "lvl1": {
        "^": pow,
    },
    "lvl2": {
        "*": mul,
        "/": truediv,
    },
    "lvl3": {
        "+": add,
        "-": sub,
    },
}


def tokenizeExpressionString(s: str) -> list[str]:
    tokens = []
    cur_token = ""
    for ch in s:
        if ch == " ":
            continue
        if ch in {"+", "-", "*", "/", "^"}:
            tokens.append(cur_token)
            tokens.append(ch)
            cur_token = ""
            continue
        cur_token += ch
    else:
        tokens.append(cur_token)
    return tokens


def calculateTokenizedExpression(tokens: list[str]) -> float:
    if len(tokens) == 1:
        return float(tokens[0])
    for operator_kind in operatorMapping.keys():
        for token in tokens:
            if token in operatorMapping[operator_kind].keys():
                index = tokens.index(token)
                operator = operatorMapping[operator_kind][token]
                left = tokens[index - 1]
                right = tokens[index + 1]
                evaluation = operator(float(left), float(right))
                new_tokens = tokens[: index - 1] + [evaluation] + tokens[index + 2 :]
                return calculateTokenizedExpression(new_tokens)

    else:
        raise ValueError("Invalid expression")
    
def calculateExpressionString(s: str) -> float:
    tokens = tokenizeExpressionString(s)
    return calculateTokenizedExpression(tokens)


def main():
    if len(argv) == 1:
        print("Please provide an expression to evaluate")
        return 1

    for expression in argv[1:]:
        print(f"{expression} = {calculateExpressionString(expression)}")
    return 0


if __name__ == "__main__":
    main()
