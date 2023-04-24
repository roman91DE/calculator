#ifndef CALC_C
#define CALC_C

#include "calc.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

enum OperatorLevel getOperatorLevel(char c)
{
    if (c == '(' || c == ')')
    {
        return PARENTHESIS;
    }
    else if (c == '^')
    {
        return EXPONENT;
    }
    else if (c == '*' || c == '/')
    {
        return MULTIPLICATION_DIVISION;
    }
    else if (c == '+' || c == '-')
    {
        return ADDITION_SUBTRACTION;
    }
    else
    {
        return NO_OPERATOR;
    }
}

float calculateExpressionString(const char *s)
{
    // TODO: Implement this function
    return 0.0;
}

char **tokenizeExpressionString(const char *s)
{
    char **tokens = (char **)malloc(MAX_TOKENS * sizeof(char *));
    for (int i = 0; i < MAX_TOKENS; i++)
    {
        tokens[i] = (char *)malloc(MAX_TOKEN_LENGTH * sizeof(char));
    }
    char currentToken[MAX_TOKEN_LENGTH] = "";

    int tokens_idx = 0;
    int currentToken_idx = 0;

    for (int idx = 0; s[idx] != '\0'; idx++)
    {

        if (s[idx] == ' ')
        {
            if (strcmp(currentToken, "") != 0)
            {
                tokens[tokens_idx] = currentToken;
                tokens_idx++;
                strcpy(currentToken, "");
                currentToken_idx = 0;
            }
            continue;
        }
        enum OperatorLevel opLevel = getOperatorLevel(s[idx]);

        if (opLevel == PARENTHESIS || opLevel == ADDITION_SUBTRACTION || opLevel == MULTIPLICATION_DIVISION || opLevel == EXPONENT)
        {
            if (strcmp(currentToken, "") != 0)
            {
                tokens[tokens_idx] = currentToken;
                tokens_idx++;
                strcpy(currentToken, "");
                currentToken_idx = 0;
            }
            *(tokens[tokens_idx]) = s[idx];
            tokens_idx++;
            continue;
        }
        else if (opLevel == NO_OPERATOR)
        {
            currentToken[currentToken_idx] = s[idx];
            currentToken_idx++;
        }
        else
        {
            printf("Error: Unknown operator %c", s[idx]);
            break;
        }
    }
    tokens[tokens_idx] = "_xxx_";
    return tokens;
}

int freeTokens(char **tokens)
{
    for (int i = 0; i < MAX_TOKENS; i++)
    {
        free(tokens[i]);
    }
    free(tokens);
    return EXIT_SUCCESS;
}

#endif // CALC_C