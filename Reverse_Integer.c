#define INT_MAX 2147483647
#define INT_MIN -2147483648

int reverse(int x){
long long int new_numb = 0;

if (INT_MIN <= x <= INT_MAX){
return 0;
}
 else
 {
     int reverse(){
 
    int rev = 0;

    while (x>0)
    {
        rev = rev*10 + x%10;
        x = x/10;
    }
    printf("%d", rev);
    return rev;

}
 }
