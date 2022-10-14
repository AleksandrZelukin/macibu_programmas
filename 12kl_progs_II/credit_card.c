#include <stdio.h>
#include <cs50.h>
#include <math.h>
 
//Function declaration
int cardLuhn(long num);
void cardClassify(int ret, long num);
 
int main(void)
{
    //Prompts the user for the card number
    long num;
    num = get_long("Number: ");
 
    if (num > pow(10, 16) || num < pow(10, 12))
    {
        printf("INVALID\n");
    }
    else
    {
        int ret = cardLuhn(num);
        cardClassify(ret, num);
    }
    return 0;
}
 
//Function for Luhn's Algorithm
int cardLuhn(long num)
{
    long tempNum = num;
 
    //Algorithm for digits multiplied by 2
    long dig, digSum = 0, loopSum = 0;
    for (int i = 1; i < 9; i++)
    {
        dig = 2 * (tempNum % (long) pow(10, 2 * i) / (long) pow(10, 2 * i - 1));
        int m, n = dig;
        while (n > 0)
        {
            m = n % 10;
            loopSum += m;
            n = n / 10;
        }
        digSum = loopSum;
    }
 
    //Algorithm for digits not multiplied by 2
    for (int i = 1; i < 9; i++)
    {
        dig = tempNum % (long) pow(10, 2 * i - 1) / (long) pow(10, 2 * i - 2);
        digSum += dig;
    }
 
    if (digSum % 10 == 0)
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
 
//Function for classifying the card
void cardClassify(int ret, long num)
{
    if (ret != 0)
    {
        printf("INVALID\n");
    }
    //AMEX condition
    else if (num % (long) pow(10, 15) / (long) pow(10, 13) == 37 || num % (long) pow(10, 15) / (long) pow(10, 13) == 34)
    {
        printf("AMEX\n");
    }
    //VISA or MASTERCARD condition
    else if (num / (long) pow(10, 15) > 1)
    {
        if (num % (long) pow(10, 16) / (long) pow(10, 15) == 4)
        {
            printf("VISA\n");
        }
        else if (num % (long) pow(10, 16) / (long) pow(10, 14) > 50 && num % (long) pow(10, 16) / (long) pow(10, 14) < 56)
        {
            printf("MASTERCARD\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else if (num % (long) pow(10, 13) / (long) pow(10, 12) == 4)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}