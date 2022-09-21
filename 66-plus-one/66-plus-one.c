/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize){

    
    register int last = 0;
    last = digits[digitsSize-1];
    register int size = 0;
    register int carry = 1;
    register int num = 0;
    register int index = 0;
    
    if(last == 9)
    {
        
        for(int i = 0 ; i < digitsSize; i++)
            if(digits[i] != 9) {size = digitsSize; break;}
            else size = digitsSize +1;
        
        int * res = (int*)malloc(sizeof(int)*(size));
        if(size != digitsSize) {index = 1;}
        else {index = 0;}
            
        for(int i = digitsSize-1; i >= 0; i--)
        {
            num = (digits[i] + carry)%10;
            carry = (digits[i] + carry)/10;
            res[i+index] = num;
        }
        
        if (carry){ res[0] = carry;}
        
        *returnSize = size;
        return res;
    }
    else
    {
        digits[digitsSize-1] = last+1;
        *returnSize = digitsSize;
        return digits;   
    }
    

    return NULL;
    
}