bool isPalindrome(int x)
{
    int remainder, original;
    unsigned int reversed = 0;
    original = x;
   

    while (x!=0)
    {
        remainder = x%10;
        reversed = reversed*10+remainder;
        x/=10;
    }
    if (original<0)
    {
        return false;
    }
    else
    {
        if (original == reversed)
        {
            return true;
        }
        else
        {
            return false;
        }    
    }
}
