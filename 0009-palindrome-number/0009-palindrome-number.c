#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isPalindrome(int x){
    unsigned int reversed = 0;
    int original = x;
    while (x!=0)
    {
        reversed = reversed*10 + x%10;
        x/=10;
    }
    if(original<0){return false;}
    else if (original == reversed){return true;}
    else{return false;}    
}