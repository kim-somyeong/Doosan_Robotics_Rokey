/*
//arithOp
#include <stdio.h>

int main(void)
{
    printf("%d + %d = %d\n", 3, 2, 3+2);
    printf("%d - %d = %d\n", 3, 2, 3-2);
    printf("%d * %d = %d\n", 3, 2, 3*2);
    printf("%d / %d = %d\n", 3, 2, 3/2);
}
*/
/*
//BitShiftOp
#include <stdio.h>

int main(void)
{
    unsigned n1= 0x9FFFFFFF;
    int n2= 0x9FFFFFFF;

    printf("n1 = %x, n2 = %u\n", n1, n2);
    printf("n2 = %X, n2 = %d\n", n2, n2);

    n1= n1<<1; //각각 1비트씩 왼쪽으로 이동
    n2=n2<<1;

    printf("n1= %X\tn1=%u\n", n1, n1);
    printf("n2= %X\tn2=%u\n", n2, n2);

    return 0;
}
*/
/*
//BinaryOp
#include <stdio.h>

int main(void)
{
    int x = 0xF00AB0A0;
    int y = 0x0FA00B0A;

    int xAndY = x&y;
    int xOry = x|y;
    int xXorY = x^y;
    int notX= ~x;

    printf("xAndY = %03X\n", xAndY);
    printf("xOrY = %0X\n", xOry);
    printf("xXorY= %0X\n", xXorY);
    printf("notX = %0X\n", notX);

    return 0;
}
*/
/*
//IncDecOp
#include <stdio.h>

int main(void)
{
    int n = 3;
    int result = n++ + 4;
    int result2 = ++n + 4;
    
    printf("n = %d, result = %d, result2 = %d\n", n, result, result2);
    printf("n = %d\n", n--);
    printf("n = %d\n", --n);
}
*/

//ReadInts
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    int n1;
    int n2;
    printf("정수 한 개를 입력하세요. : ");
    scanf("%d", &n1);
    printf("정수 한 개를 입력하세요. : ");
    scanf("%d", &n2);
    printf("n1 = %d, n2 = %d\n", n1, n2);

    return 0;
}