/*
//5
#include <stdio.h>

int main()
{
    int num1, num2;
    int sum, difference;

    printf("두 정수를 입력하세요 : ");
    scanf("%d %d", &num1, &num2);

    int *ptr1= &num1;
    int *ptr2= &num2;

    sum= *ptr1 + *ptr2;
    difference = *ptr1 - *ptr2;

    printf("합 : %d\n", sum);
    printf("차 : %d\n", difference);

    return 0;
}
*/
/*
//6
#include <stdio.h>

//swap function
void swap(int *a, int *b)
{
    int temp;
    temp= *a;
    *a = *b;
    *b = temp;
}

int main()
{
    int num1, num2;

    printf("두 정수를 입력하세요 :");
    scanf("%d %d", &num1, &num2);

    int *ptr1= &num1;
    int *ptr2= &num2;

    swap(ptr1, ptr2);
    
    printf("첫 번째 수 : %d, 두 번째 수 : %d\n", *ptr1, *ptr2);

    return 0;
}
*/
/*
//7
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num;
    int *ptr = &num;

    printf("정수를 입력하세요 : ");
    scanf("%d", ptr);

    //절댓값
    int new_num = abs(*ptr);

    printf("절댓값 : %d\n", new_num);

    return 0;
}
*/
/*
//8
#include <stdio.h>

int main()
{
    double num1, num2;
    double *ptr1= &num1;
    double *ptr2= &num2;

    printf("두 실수를 입력하세요 : ");
    scanf("%lf %lf", ptr1, ptr2);

    double new_num = (*ptr1) * (*ptr2);

    printf("곱 : %.1f\n", new_num);

    return 0;
}
*/
/*
//9
#include <stdio.h>
#include <string.h>  //strlen() func

int main()
{
    char str[100];
    char *ptr= str;

    printf("문자열을 입력하세요 : ");
    fgets(ptr, sizeof(str), stdin); //포인터를 사용해 문자열 입력

    size_t length= strlen(ptr); //strlen()은 문자열 길이 반환

    //개행문자가 문자열의 끝에 추가되면 제거
    if(ptr[length-1]== '\n'){
        ptr[length-1]=='\0'; //개행 문자 제거
        length--; //길이조정
    }
    printf("문자열의 길이 : %zu\n", length);

    return 0;
}
*/
/*
//A
#include <stdio.h>

int main()
{
    double num1, num2;
    double *ptr1= &num1;
    double *ptr2= &num2;
    double average;

    printf("두 실수를 입력하세요 : ");
    scanf("%lf %lf", ptr1, ptr2);

    average= (*ptr1 + *ptr2) / 2.0;

    printf("평균 : %.1f\n",average);

    return 0;
}
*/
/*
//10
#include <stdio.h>

void print_divisors(int *num)
{
    printf("약수 : ");
    for(int i=1; i<=*num; i++){
        if(*num %i ==0){
            printf("%d ", i);
        }
    }
    printf("\n");
}

int main()
{
    int number;
    int *ptr= &number;

    printf("정수를 입력하세요 : ");
    scanf("%d", ptr);

    print_divisors(ptr);

    return 0;
}
*/
/*
//11
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define MAX_SIZE 10

int main()
{
    int arr[MAX_SIZE];
    int n;

    printf("배열의 길이를 입력하세요 :", MAX_SIZE);
    scanf("%d", &n);

    if(n>MAX_SIZE || n<=0){
        printf("배열 길이가 잘못됨.\n");
        return 1;
    }

    printf("배열 요소를 입력하세요 : ");
    for(int i=0; i<n; i++){
        scanf("%d", &arr[i]);
    }

    //reverse
    printf("역순 베열 : ");
    int *ptr_start= arr;
    int *ptr_end= arr + n - 1;

    while(ptr_end >= ptr_start){
        printf("%d", *ptr_end);
        ptr_end--;
    }

    printf("\n");
    return 0;
}
*/
/*
//12
#include <stdio.h>

int main()
{
    int num1, num2;
    int *ptr1= &num1;
    int *ptr2= &num2;
    int difference;

    printf("두 개의 정수를 입력하세요 : ");
    scanf("%d %d", &num1, &num2);

    difference= *ptr1- *ptr2;

    printf("두 정수 차 : %d\n", difference);

    return 0;
}
*/
/*
//13
#include <stdio.h>
#define N 5

void swapArrays(int *arr1, int*arr2, int size)
{
    for(int i=0; i<size; i++){
        int temp = *(arr1+i);
            *(arr1 + i)= *(arr2 + i);
            *(arr2+i)= temp;
    }
}

void printArray(const int *arr, int size){
    for(int i=0; i<size; i++){
        printf("%d ", *(arr+i));
    }
    printf("\n");
}

int main()
{
    int array1[N];
    int array2[N];

    printf("첫 번째 배열의 %d 개의 요소를 입력 :", N);
    for(int i=0; i<N; i++){
        scanf("%d", &array1[i]);
    }
    printf("두 번째 배열의 %d 개 요소를 입력하세요: ", N);
    for (int i = 0; i < N; i++) {
        scanf("%d", &array2[i]);
    }

    swapArrays(array1, array2, N);

    printf("교환된 첫 번째 배열: ");
    printArray(array1, N);

    printf("교환된 두 번째 배열: ");
    printArray(array2, N);

    return 0;
}
*/
/*
//14
#include <stdio.h>

void square(int *num)
{
    *num= (*num) * (*num); //포인터를 통해 제곱 계산
}

int main()
{
    int number;

    printf("정수를 입력하세요 : ");
    scanf("%d", &number);

    square(&number);
    printf("제곱된 결과 : %d\n", number);

    return 0;
}
*/
/*
//15
#include <stdio.h>

void average(double *num1, double *num2, double *avg)
{
    *avg= (*num1 + *num2)/2.0;
}

int main()
{
    double num1, num2, avg;
    double *ptr1= &num1;
    double *ptr2= &num2;
    double *ptr_avg= &avg;

    printf("write two float : ");
    scanf("%lf %lf", ptr1, ptr2);

    average(ptr1, ptr2, ptr_avg);

    printf("average :%.2f\n", avg);

    return 0;
}
*/
/*
//16
#include <stdio.h>

int main()
{
    char str[100];
    char *ptr = str;
    int length=0;

    printf("문자열을 입력하세요 : ");
    fgets(str, sizeof(str), stdin);

    while(*ptr != '\0'){  //포인터가 문자열 끝에 올때까지 반복
        length++;
        ptr++;
    }

    if(*(ptr - 1)=='\n'){
        length--;
    }
    printf("문자열의 길이 : %d\n", length);

    return 0;
}
*/
/*
//17
#include <stdio.h>

int main()
{
    int n;
    int array[100];
    int *ptr= array;
    int min;

    printf("write the array length :");
    scanf("%d", &n);

    printf("write array[i] : ");
    for(int i=0; i<n; i++){
        scanf("%d", &array[i]);
    }
    min=*ptr;

    for(int i=1; i<n; i++){
        if(*(ptr+i)<min){
            min= *(ptr+i);
        }
    }
    printf("minimum : %d\n", min);
    return 0;
}
*/
/*
//18
#include <stdio.h>

int main()
{
    int num;
    int *ptr= &num;

    printf("write the num : ");
    scanf("%d", ptr);

    printf("약수 : ");
    for(int i=1; i<=*ptr; i++){
        if(*ptr % i ==0){
            printf("%d ", i);
        }
    }
    printf("\n");

    return 0;
}
*/
/*
//19
#include <stdio.h>

#define MAX_SIZE 100

int main()
{
    int n;
    int array[MAX_SIZE];
    int sum = 0;
    int *ptr;

    printf("write the length of array : ");
    scanf("%d", &n);

    printf("write the array[i] : ");
    for(int i=0; i<n; i++){
        scanf("%d", &array[i]);
    }

    ptr= array;

    for(int i=0; i<n; i++){
        sum +=*ptr;
        ptr++;
    }
    printf("total sum : %d\n", sum);

    return 0;
}
*/
/*
//20
#include <stdio.h>

int main()
{
    int num1, num2;
    int *ptr1= &num1;
    int *ptr2= &num2;
    int sum, difference;

    printf("write the two number : ");
    scanf("%d %d", ptr1, ptr2);

    sum = *ptr1;  //sum을 num1로 초기화
    sum += *ptr2; 

    difference = *ptr1; //difference를 num1로 초기화
    difference -= *ptr2;

    printf("sum : %d\n", sum);
    printf("difference : %d\n", difference);

    return 0;
}
*/
/*
//21
#include <stdio.h>

int main()
{
    int num;
    int *ptr = &num;

    printf("write the num :");
    scanf("%d", ptr);

    for(int i=0; i<5; i++){
        (*ptr)++;
        printf("%d ", *ptr);
    }
    return 0;
}
*/
/*
//22
#include <stdio.h>

int main() {
    int length = 5;
    int array[length];
    int *ptr = array;

    printf("배열의 요소를 입력하세요:\n");
    for (int i = 0; i < length; i++) {
        scanf("%d", ptr + i);
    }

    for (int i = 0; i < length; i++) {
        *(ptr + i) *= 2;
    }


    printf("변경된 배열의 요소는:\n");
    for (int i = 0; i < length; i++) {
        printf("%d ", *(ptr + i));
    }
    printf("\n");

    return 0;
}
*/
/*
//23
#include <stdio.h>

int main()
{
    int num1, num2;
    int *ptr1= &num1;
    int *ptr2= &num2;

    printf("write the two num : ");
    scanf("%d %d", ptr1, ptr2);

    if(*ptr1>*ptr2){
        printf("bigger num :%d\n", *ptr1);
    }
    else{
        printf("bigger num : %d\n", *ptr2);
    }
    return 0;
}
*/
/*
//24
#include <stdio.h>

int sum(int *a, int *b){
    return *a+*b;
}

int main()
{
    int num1, num2;
    
    printf("write the two num :");
    scanf("%d %d", &num1, &num2);

    int result= sum(&num1, &num2);

    printf("sum of num : %d\n", result);

    return 0;
}
*/
/*
//25
#include <stdio.h>

void doubleArray(int *arr, int length)
{
    for(int i=0; i<length; i++){
        *(arr+i)*=2; //double array used pointer
    }
}

int main()
{
    int length=5;
    int array[length];

    printf("write the array (total : %d) : ", length);
    for(int i=0; i<length; i++){
        scanf("%d", &array[i]);
    }

    doubleArray(array, length);

    printf("changed array : ");
    for(int i=0; i<length; i++){
        printf("%d ", array[i]);
    }
    printf("\n");
    return 0;
}
*/
/*
//26
#include <stdio.h>

double Average(double *a, double *b)
{
    return (*a + *b)/ 2.0;
}

int main()
{
    double num1, num2;

    printf("write the two float :");
    scanf("%lf %lf", &num1, &num2);

    double average = Average(&num1, &num2);
    printf("two float average : %.2f\n", average);

    return 0;
    
}
*/
/*
//27
#include <stdio.h>
#include <string.h>

int getStringLength(const char *str)
{
    return strlen(str); //str length return
}

int main()
{
    char str[100];

    printf("write the str : ");
    fgets(str, sizeof(str), stdin);

    str[strcspn(str, "\n")]='\0';

    int length= getStringLength(str);

    printf("length : %d\n", length);
    
    return 0;
}
*/
/*
//28
#include <stdio.h>

int findMax(int *arr, int length)
{
    int max= *arr;

    for(int i=0; i<length; i++){
        if(*(arr+i)>max){
            max= *(arr+i);
        }
    }
    return max;
}

int main()
{
    int arr[5];
    int length = 5;
    int max;

    printf("write 5 array :");
    for(int i=0; i<length; i++){
        scanf("%d", &arr[i]);
    }

    max= findMax(arr, length);

    printf("max : %d\n", max);

    return 0;
}
*/

//29
#include <stdio.h>
#include <math.h>

double SquareRoot(int *num)
{
    return sqrt((double)*num);
}

int main()
{
    int number;
    double result;

    printf("write the num : ");
    scanf("%d", &number);

    result= SquareRoot(&number);

    printf("제곱근 : %.2f\n", result);

    return 0;
}