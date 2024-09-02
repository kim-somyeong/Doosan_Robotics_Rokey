/*
//covert1
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    int n=3;
    int*ptr1=&n;
    unsigned int* ptr2=(unsigned int*) ptr1;

    printf("*ptr2=%u\n", *ptr2);
    return 0;
}
*/
/*
//pointer
#include <stdio.h>

int main(void)
{
    double d= 2.3;
    double* ptrd= &d;

    *ptrd= *ptrd*2;
    printf("d = %f\n", d);

    return 0;
}
*/
/*
//PtrArith
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    int arr[4]= {0, 1, 2, 3};
    int* p1= &arr[2];
    int* p2= p1 + 1;
    int* p0= p1 - 1;
    printf("p1= %p\n", p1);
    printf("p2= p+1 = %p\n", p2);
    printf("p0= p-1 = %p\n", p0);
    printf("p2 - p1 = %td, p2 - p0 = %td\n", p2-p1, p2-p0);

    double darr[4]= {0.0, 1.0, 2.0, 3.0};
    double* dp1= &darr[2];
    double* dp2= dp1 + 1;
    double* dp0= dp1 - 1;
    printf("dp1= %p\n", dp1);
    printf("dp2= dp1 + 1 = %p\n", dp2);
    printf("dp0 = dp - 1 = %p\n", dp0);
    printf("dp2 - dp1 = %td, p2 - dp0 = %td\n", dp2-dp1, dp2-dp0);

    return 0;
}
*/
/*
//ArrPtr4
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    int arr[]= {0, 1, 2, 3};
    int* p= arr;
    for(int i=0; i<4; i++){
        printf("arr[%d]=%d, p[%d]=%d, *(p+%d)= %d\n", i, arr[i], i, p[i], i, *(p+i));
    }
    return 0;
}
*/
/*
//ArrPtr5
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    int arr[]= {0, 1, 2, 3};
    int* p= &arr[1];
    for(int i=0; i<3; i++){
        printf("arr[%d]=%d, p[%d]=%d, *(p+%d)= %d\n", i+1, arr[i+1], i, p[i], i, *(p+i));
    }
    return 0;
}
*/
/*
//ArrPrt6
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    int arr[]= {0, 1, 2, 3};
    int*p= arr;
    printf("포인터 변수 p는 arr[0]의 주소로 저장됨 \n");
    printf("&arr[0]= %p, p= %p, arr[0]= %d, *p= %d\n", &arr[0], p, arr[0], *p);
    p++;
    printf("&arr[1]= %p, p= %p, arr[1]= %d, *p= %d\n", &arr[1], p, arr[1], *p);

    return 0;
}
*/
/*
//ArrPtr7
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    int arr[]= {0, 1, 2, 3};
    int *p= &arr[0];
    for(int i=0; i<4; i++, p++){
        printf("arr[%d]= %d, *p= %d\n", i, arr[i], *p);
    }
    return 0;
}
*/
/*
//func pointer
#include <stdio.h>

void func(int*p)
{
    printf("memory address of p : %p, *p= &d\n", p, *p);
}

int main()
{
    int a= 10;
    int *pa= &a;
    func(pa);
}
*/

//Scanf2
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void readTwoInts(int *px, int *py)
{
    int a;
    int b;
    printf("write the two num : ");
    scanf("%d %d", &a, &b);  //scanf("%d %d", px, py);
    *px= a;
    *py= b;
}

int main()
{
    int x= 0;
    int y= 0;
    readTwoInts(&x, &y);
    printf("x= %d y=%d\n", x, y);
    return 0;
}