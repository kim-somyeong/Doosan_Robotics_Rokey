/*
//membership
#include <stdio.h>

int main(void)
{
    typedef enum {NONE, FRIENDS, SILVER, GOLD, PLATINUM} Membership;

    Membership membership = GOLD;
    printf("membership == Gold : %d\n", membership == GOLD);
    printf("membership == Silver : %d\n", membership == SILVER);
}
*/
/*
//LogicalOp
#include <stdio.h>

int main(void)
{
    typedef enum {NONE, SILVER, GOLD, PLATINUM } Membership;

    Membership membership = GOLD;
    int parkingTime = 30;
    int freeParking = (membership == GOLD || membership == PLATINUM)&& parkingTime <= 120;
    printf("무료 주차 가능 = %d\n", freeParking);
    return 0; 
}
*/
/*
//if
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    char seat = '0';
    printf("극장 좌석 열을 입력하세요. : ");
    scanf("%c",&seat);

    if(seat == 'L'){
        printf("표를 구매합니다.\n");
    }
    return 0;
}
*/
/*
//Parking1
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    char membership;
    printf("멤버십을 한 글자로 입력하세요. (N:멤버십 없음, F:프렌즈, S:실버, G:골드, P:플래티넘): ");
    scanf("%c",&membership);
    printf("주차 시간을 분 단위로 입력하세요: ");
    int parkingTime;
    scanf("%d", &parkingTime);
    if((membership == 'G' || membership == 'P')&& parkingTime <= 120){
        printf("멤버십 : %c, 주차 시간 : %d 분. 무료 주차 가능\n", membership, parkingTime);
    }
    return 0;
}
*/
/*
//Rain
#include <stdio.h>

int main(void)
{
    int chanceOfRain = 35;
    if(chanceOfRain >= 30){
        printf("Bring the umbrella\n");
    }
    if (chanceOfRain < 30){
        printf("You don't need to bring umbrella\n");
    }
    return 0;
}
*/