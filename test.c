#include <stdio.h>

int main()
{
    short x[5] = {0x4e65, 0x7477, 0x6f72, 0x6b69, 0x6e67};
    char ch[10] = {'N', 'e', 't', 'w', 'o', 'r', 'k', 'i', 'n', 'g'};
    short ret = 0xf3df;
    short show = ret;
    for (int i = 0; i < 5; i++)
    {
        show += x[i];
        printf("%c:%#x\n", ch[i * 2], ch[i * 2]);
        printf("%c:%#x\n", ch[i * 2 + 1], ch[i * 2 + 1]);
    }

    printf("answer:%#x\n", show);
    printf("ans:%#x\n", 62431);
}