#!/usr/bin/env python3

from operator import add, sub, mul, truediv, pow
from argparse import ArgumentParser

operatorMapping = {
    "lvl0": {
        "(",
        ")"
    },
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
        if ch in {"(", ")"}:
            if len(cur_token) > 0:
                tokens.append(cur_token)
            tokens.append(ch)
            cur_token = ""
            continue
        if ch in {"+", "-", "*", "/", "^"}:
            if len(cur_token) > 0:
                tokens.append(cur_token)
            tokens.append(ch)
            cur_token = ""
            continue
        cur_token += ch
    else:
        if len(cur_token) > 0:
            tokens.append(cur_token)
    return tokens


def calculateTokenizedExpression(tokens: list[str]) -> float:
    if len(tokens) == 1:
        return float(tokens[0])
    for operator_kind in operatorMapping.keys():
        if operator_kind == "lvl0":
            for token1 in reversed(tokens):
                if token1 == "(":
                    open_index = (len(tokens)-1) - list(reversed(tokens)).index(token1)
                    for token2 in tokens:
                        if token2 == ")":
                            close_index = tokens.index(token2)
                            innerExpressionTokens = tokens[open_index + 1 : close_index]
                            innerExpressionEvaluation = calculateTokenizedExpression(innerExpressionTokens)
                            new_tokens = tokens[: open_index] + [innerExpressionEvaluation] + tokens[close_index + 1 :]
                            return calculateTokenizedExpression(new_tokens)
        else:
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
    parser = ArgumentParser()
    parser.add_argument("expression", type=str, help="The expression to evaluate", required=True)
    args = parser.parse_args()
    print(f"{args.expression} = {calculateExpressionString(args.expression)}")


if __name__ == "__main__":
    main()
