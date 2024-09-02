/*#include <stdio.h>

int main(void)
{
    printf("My first C program\n");
    return 0;
}
*/
/*
//sizeof
#include <stdio.h>

int main(void)
{
    printf("%zu\n", sizeof(int));
    return 0;
}
*/
/*
//FloatError
#include <stdio.h>

int main(void)
{
    float f= 0.01f * 0.01f;
    printf("f= %f\n", f);
    printf("f= %.20f\n", f);
    return 0;
}
*/
/*
//Double
#include <stdio.h>

int main(void)
{
    double f= 0.01 * 0.01;
    printf("f= %f\n", f);
    printf("f= %.20f\n", f);
    return 0;
}
*/
/*
//Address
#include <stdio.h>

int main(void)
{
    char ch= 'a';
    int n= 1;
    double d= 1.0;

    printf("address of ch = %p\n", &ch);
    printf("address of n = %p\n", &n);
    printf("address of d = %p\n", &d);
    return 0;
}
*/
/*
//문제 14

#include <stdio.h>

int main(void)
{
    printf("Kim-somyeong\n");
    printf("Gyeonggi-do ansan-si\n");

    return 0;
}

//문제17

#include <stdio.h>

int main(void)
{
    printf("hello\tworld\n");
    
    return 0;
}

#include <stdio.h>

int main(void)
{
    printf("\\");
    return 0;
}

//문제 25
#include <stdio.h>

int main(void)
{
    char charVal = 'A';
    int intVal = 120;
    int largeIntVal = 2011351000;
    unsigned int uintVal = 3011351000u;
    long long llVal = 3011351000LL;
    unsigned long long ullVal = 232322011351000ULL;

    // printf와 sizeof를 사용하여 값과 크기 출력
    printf("'A': value = %c, size = %zu bytes\n", charVal, sizeof(charVal));
    printf("120: value = %d, size = %zu bytes\n", intVal, sizeof(intVal));
    printf("2011351000: value = %d, size = %zu bytes\n", largeIntVal, sizeof(largeIntVal));
    printf("3011351000u: value = %u, size = %zu bytes\n", uintVal, sizeof(uintVal));
    printf("3011351000LL: value = %lld, size = %zu bytes\n", llVal, sizeof(llVal));
    printf("232322011351000ULL: value = %llu, size = %zu bytes\n", ullVal, sizeof(ullVal));

    return 0;
}


//문제26

#include <stdio.h>

int main(void) {
    // 변수 선언
    double doubleVal;
    long double longDoubleVal;

    // 크기 출력
    printf("Size of double: %zu bytes\n", sizeof(doubleVal));
    printf("Size of long double: %zu bytes\n", sizeof(longDoubleVal));

    return 0;
}

*/

//문제27
#include <stdio.h>

int main(void) {
    // 변수 선언
    int intVal;
    long longVal;

    // 크기 출력
    printf("Size of int: %zu bytes\n", sizeof(intVal));
    printf("Size of long: %zu bytes\n", sizeof(longVal));

    return 0;
}