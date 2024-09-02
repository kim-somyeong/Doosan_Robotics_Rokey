/*
//divisorwhile.c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    int n;
    printf("약수를 출력할 1 이상의 정수 한 개를 입력하세요 : ");
    scanf("%d", &n);
    if (n>=1){
        int divisor = 1;
        while(divisor <= n){
            if (n%divisor==0){
                printf("%d", divisor);
            }
            divisor++;
        }
    }
    else{
        printf("1 미만의 정수가 입력되었습니다. 프로그램을 종료합니다\n");
    }
    return 0;
}
*/
/*
//InputAlpha.c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    char ch;
    char newlinechar;
    printf("영문 알파벳 문자 한 개를 입력하세요. : ");
    scanf("%c",&ch);
    scanf("%d", &newlinechar);

    while((ch < 'A' || ch > 'Z') && (ch >= 'a' && ch <= 'z')){
        printf("알파벳이 아닌 문자가 입력되었습니다. 다시 입력하세요.");
        scanf("%c", &ch);
        scanf("%c", &newlinechar);
    }
    printf("ch = %c\n", ch);
    return 0;
}
*/
/*
//divisor DoWhile
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    int n;
    printf("약수를 출력할 1 이상의 정수 한 개를 입력하세요.");
    scanf("%d", &n);
    if(n>= 1){
        int divisor = 1;
        do{
            if(n%divisor == 0){
                printf("%d", divisor);
            }
            divisor++;
        }while (divisor <= n);
    }
    else{
        printf("1 미만의 정수가 입력되었습니다. 프로그램을 종료합니다 \n");
    }
    return 0;
}
*/
/*
//Input Alpha3
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    char ch;
    char newlinechar;

    int first = 1;
    do{
        if (first){
            printf("영문 알파벳 문자 한 개를 입력하세요.");
            first=0;
        }
        else{
            printf("알파벳 아닌 문자가 입력되었습니다. 다시 입력하세요.");
        }
        scanf("%c", &ch);
        scanf("%c", &newlinechar);
    }while ((ch<'A'||ch>'Z')&&(ch<'a' || ch>'z'));

    printf("ch= %c\n", ch);
    return 0;
}
*/
/*
//TwoDigitsSumTo10
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    for(int first=1, second=9; first<10; first++, second--){  //변수 2개를 for문 안에서 같이 초기화
        printf("%d%d\t", first, second);
    }
    return 0;
}
*/
/*
//divisorFor
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    int n;
    printf("약수를 출력할 1 이상의 정수 한 개를 입력하세요. : ");
    scanf("%d", &n);

    if(n>=1){
        for(int divisor = 1; divisor<= n; divisor++){
            if(n%divisor == 0){
                printf("%d ",divisor);
            }
        }
    }
    else{
        printf("1 미만의 정수가 입력되었습니다. 프로그램을 종료합니다\n");
    }
    return 0;
}
*/
/*
//InputAlphaFor
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    char ch;
    char newlinechar;
    printf("영문 알파벳 문자 한 개를 입력하세요 : ");
    scanf("%c", &ch);
    scanf("%c", &newlinechar);

    for( ; (ch < 'A' || ch> 'Z') && (ch < 'a' || ch > 'z'); ){
        printf("알파벳 아닌 문자가 입력되었습니다. 다시 입력하세요: ");
        scanf("%c", &ch);
        scanf("%c", &newlinechar);
    }

    printf("ch= %c\n", ch);
    return 0;
}
*/
/*
//Max4Divisors
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    int n;
    printf("약수를 출력할 1 이상의 정수 한 개를 입력하세요. : ");
    scanf("%d", &n);

    int num0Divisors = 0;
    if(n>=1){
        for(int divisor = 1; divisor <= n; divisor++){
            if (n%divisor == 0){
                printf("%d ", divisor);
                num0Divisors++;
                if(num0Divisors == 4){break;}
            }
        }
    }else{
            printf("1 미만의 정수가 입력되었습니다. 프로그램을 종료합니다\n");
    }
            return 0;
}
*/
//oddDivisor
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    int n;
    printf("약수를 출력할 1 이상의 정수 한 개를 입력하세요. : ");
    scanf("%d", &n);

    if (n>=1){
        for(int divisor = 1; divisor <= n; divisor++){
            if(n%divisor == 0){
                if(divisor % 2 == 0){continue;}
                printf("%d ", divisor);
            }
        }
    }else{
        printf("1 미만의 정수가 입력되었습니다. 프로그램을 종료합니다\n");
    }
    return 0;
}