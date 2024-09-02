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