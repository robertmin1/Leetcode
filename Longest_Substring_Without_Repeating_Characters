int lengthOfLongestSubstring(char * s){
    int record[128] = {0};
    int ans = 0;
    int tmp = 0;
    char *l = s;
    char *r = s;

    while (*r) {
        if (record[*r] == 0) {
            record[*r] = 1;
            tmp += 1;
            ans = (tmp > ans) ? tmp : ans;
        } else {
            while (*l != *r) {
                record[*l] = 0;
                tmp -= 1;
                l++;
            }
            l++;
        }
        r++;
    }
    return ans;
}
