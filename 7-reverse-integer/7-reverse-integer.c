#define INT_MAX 2147483647
#define INT_MIN -2147483648

int reverse(int x){
long long int new_numb = 0;

if (INT_MIN <= x <= INT_MAX){
while (x != 0){
new_numb = new_numb*10+ x % 10;
x = x/10;
if ((new_numb >=INT_MAX) || (new_numb <=INT_MIN)){
return 0;
}
}
return new_numb;
}
else{
return 0;
}

}