#include "calc.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    for (int i = 1; i < argc; i++)
    {
        printf("CalculateExpressionString:\n%s == %f\n", argv[i], calculateExpressionString(argv[i]));

        char **tokens = tokenizeExpressionString(argv[i]);
        for (int j = 0; strcmp(tokens[j], "_xxx_") != 0; j++)
        {
            printf("Token %d: %s;", j, tokens[j]);
        }
        printf("\n");
    }

    return 0;
}
