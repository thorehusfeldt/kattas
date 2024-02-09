#include <stdio.h>
#include <string.h>

int main() {
    char s[500001];
    fgets(s, sizeof(s), stdin);
    char bit = '0';
    int l = strlen(s);
    for (int i = 0; i < l; i++) {
        if (s[i] == 'b') {
            s[i] = bit;
            bit = (bit == '0') ? '1' : '0';
        }
    }
    printf("%s\n", s);
    return 0;
}
