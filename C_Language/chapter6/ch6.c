/*
//hour, minute
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
//시간을 1분 증가시키는 함수(값변환)
int addOneMinute(int hour, int minute){
    minute++;
    if(minute == 60){
        minute=0;
        hour++;
        if(hour==24){
            hour=0;
        }
    }
    return hour * 100+minute;
    //시간과 분을 하나의 정수로 조합하여 반환
}

int main(){
    int hour, minute, time;

    //사용자로부터 시간 입력 받기
    printf("시간과 분을 입력하세요 (예: 12 30) : ");
    scanf("%d %d", &hour, &minute);

    //1분 증가 함수 호출 및 결과 저장
    time = addOneMinute(hour, minute);

    //결과 출력(시간과 분을 다시 분리)
    printf("변경된 시간은 %02d:%02d 입니다.\n", time/100, time%100);

    return 0;
}
*/
/*
//swap
#include <stdio.h>

void swap(int num1, int num2)
{
    int temp = num1;
    num1 = num2;
    num2 = temp;
}

int main(void)
{
    int x = 5;
    int y = 9;
    swap(x,y);
    printf("x = %d, y = %d\n", x, y);

    return 0;
}
*/
/*
//IsPrimeNumber
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int isPrimeNumber(int m)
{
    if (m<2){return 0; }
    else if(m==2){return 1; }
    for (int i = 3; i<m; i+=2){
        if (m%i == 0){
            return 0;
        }
    }
    return 1;
}

int main(void)
{
    printf("1 is prime number (1 if true 0 otherwise) :%d\n", isPrimeNumber(1));
    printf("2 is prime number (1 if true 0 otherwise) :%d\n", isPrimeNumber(2));
    printf("6 is prime number (1 if true 0 otherwise) :%d\n", isPrimeNumber(6));
    printf("13 is prime number (1 if true 0 otherwise) :%d\n", isPrimeNumber(13));

    return 0;
}
*/
/*
//PrintPrimeNumber
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int isPrimeNumber(int m)
{
    if (m<2){return 0; }
    else if(m==2){return 1; }
    for (int i = 3; i<m; i+=2){
        if (m%i == 0){
            return 0;
        }
    }
    return 1;
}

void printPrimeNumbers(int n1, int n2)
{
    if (n1 >= n2){
        if(n1 == 2 || n2 == 2){printf("소수 : 2\n");}
        if(n1 % 2 == 0){ n1++; } 
        for (int m = n1; m <= n2; m+=2){
            if (isPrimeNumber(m)){printf("소수 : %d\n", m);}
        }
    }
}

int main(void)
{
    int n1;
    int n2;
    printf("두 개 정수 사이의 소수를 출력하기 위해 정수 입력 : ");
    scanf("%d", &n1);
    scanf("%d", &n2);
    printPrimeNumbers(n1, n2);

    return 0;
}
*/
/*
//QuadEqnLocal
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

void printQuadEqnSoln(int a, int b, int c)
{
    double r = sqrt(b*b - 4*a*c);
    double x1 = (-b+r) / (2*a);
    double x2 = (-b-r) / (2*a);
    printf("x1 = %f, x2 = %f\n", x1, x2);
}

int main(void)
{
    printQuadEqnSoln(1, -5, 6);
    printQuadEqnSoln(1, 5, -6);
    return 0;
}
*/
/*
//QuadEqnGlobal
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

double x1;
double x2;

void calcQuadEqn(int a, int b, int c)
{
    double r = sqrt(b*b - 4*a*c);
    x1 = (-b+r) / (2*a);
    x2 = (-b-r) / (2*a);
}

int main(void)
{
    calcQuadEqn(1, -5, 6);
    printf("x1 = %f, x2 = %f\n", x1, x2);
    calcQuadEqn(1, 5, -6);
    printf("x1 = %f, x2 = %f\n", x1, x2);
    return 0;
}
*/
/*
//Random
#include <stdlib.h>
#include <stdio.h>
unsigned seed = 17;

void setSeed(unsigned s)
{
    seed = s;
}

unsigned custom_random()
{
    seed = (seed*seed) + (13*seed) + 19;
    if (seed > RAND_MAX) {seed %= RAND_MAX;}
    return seed;
}

int main(void)
{
    setSeed(50);
    for(int i = 0; i < 10; i++){
        printf("%u ", custom_random());
    }
    return 0;
}
*/
/*
//HiddenScope
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int x=1;

void func1(int x)
{
    printf("func1 : x = %d\n", x);
}

void func2(int n)
{
    x = n;
    printf("func2-1 : x = %d\n", x);
    int x=5;
    printf("func2-2 : x = %d\n",x);
}

int main(void)
{
    printf("main : x = %d\n", x);
    func1(3);
    func2(7);
}
*/
/*
//enum
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

typedef enum {JAN = 1, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC} MONTH;

MONTH getMonth()
{
    int month;
    printf("1~12 사이의 정수를 입력하세요 :");
    scanf("%d", &month);
    return month;
}

int main(void)
{
    MONTH m = getMonth();
    printf("month = %d", m);
    return 0;
}
*/

//sum1toN
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int sum1toN(int n)
{
    if (n==0){return 0;}
    return sum1toN(n-1) + n;
}

int main(void)
{
    int n;
    printf("1 이상의 양의 정수 한 개 입력 : ");
    scanf("%d", &n);
    int sum = sum1toN(n);
    printf("1~%d의 합 sum = %d\n", n, sum);
    return 0;
}