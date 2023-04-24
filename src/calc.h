#ifndef CALC_H
#define CALC_H

#define MAX_TOKENS 64
#define MAX_TOKEN_LENGTH 32

enum OperatorLevel {
    NO_OPERATOR = 0,
    PARENTHESIS = 1,
    EXPONENT = 2,
    MULTIPLICATION_DIVISION = 3,
    ADDITION_SUBTRACTION = 4,

};

enum OperatorLevel getOperatorLevel(char c);
float calculateExpressionString(const char *s);
char** tokenizeExpressionString(const char *s);


#endif // CALC_H