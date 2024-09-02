/*
//ConstArray
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define SIZE 10 // 상수 선언

int main(void)
{
    const int n =15;
    int m = 10;
    int a[m];
    int b[n];
    int c[SIZE];
    int securityNums[30];

    a[0] = 1;
    printf("%d\n", a[0]);
    return 0;
}
*/
/*
//ErrorIndex
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define SIZE 3

int main(void)
{
    int nums[SIZE];
    int n = 4;
    nums[0] = 4;
    nums[1] = 3;
    nums[2] = 9;

    for (int i =0; i < SIZE; i++){
        printf("nums[%d] = %d\n", i, nums[i]);
    }
    return 0;
}
*/
/*
//SizeArr
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define SIZE 5

int main(void)
{
    int nums[SIZE];
    printf("size of nums[0] = %d\n", sizeof(nums[0]));
    printf("size of nums = %d\n", sizeof(nums));

    return 0;
}
*/
/*
//InitArr1
#include <stdio.h>

int globalNums[5];

int main(void)
{
    static int staticNums[5];
    int localNums[5];

    for(int i = 0; i<5; i++){
        printf("globalnums[%d]=%d, staticNums[%d]=%d, localNums[%d]=%d\n", i, globalNums[i], i, staticNums[i], i, localNums[i]);
    }
    return 0;
}
*/
/*
//InitArr2
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define ARRAY_SIZE(arr, element)(sizeof((arr))/sizeof((element)))

int main(void)
{
    int nums[]={1, 2, 3, 4, 5};
    printf("size of nums = %d\n", ARRAY_SIZE(nums, nums[0]));
    for(int i=0; i<ARRAY_SIZE(nums, nums[0]); i++){
        printf("nums[%d]=%d\n", i, nums[i]);
    }
    double nums2[]= {1.1, 2.2, 3.3};
    printf("size of nums2= %d\n", ARRAY_SIZE(nums2, nums2[0]));
    for(int i = 0; i<ARRAY_SIZE(nums2, nums2[0]); i++){
        printf("nums[%d]=%f\n", i, nums2[i]);
    }
    return 0;
}
*/
/*
//InitArr3
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define SIZE 5

int main(void)
{
    int num1[SIZE] = {1, 2, 3, 4, 5};
    int num2[SIZE] = {1, 2, 3};
    int num3[SIZE] = {1, 2, 3, 4, 5, 6};

    for(int i = 0; i<SIZE; i++){
        printf("num1[%d]=%d, num2[%d]=%d, num3[%d]= %d\n", i, num1[i], i, num2[i], i, num3[i]);
    }
    return 0;
}
*/
/*
//array
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define SIZE 5

int main(void)
{
    int arr1[SIZE] = {1, 2, 3, 4, 5};
    int arr2[SIZE];

    for(int i=0; i<SIZE; i++){
        arr2[i]=arr1[i];
        printf("arr2[%d]=%d\n", i, arr2[i]);
    }
    return 0;
}
*/
/*
//printTVSize
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define ARRAY_SIZE(arr, element) (sizeof((arr)) / sizeof((element)))

void printTVSize(double size) {printf("TV Size : %f cm\n", size);}

int main(void)
{
    double tvSizes[]= {32 * 2.54, 42 * 2.54, 55 * 2.54, 65 * 2.54, 75 * 2.54};

    for(int i=0; i<ARRAY_SIZE(tvSizes, tvSizes[0]); i++){
        printTVSize(tvSizes[i]);
    }
    return 0;
}
*/
/*
//print TV Size
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void printTVSizes(double sizes[])
{
    for(int i=0; i<5; i++){
        printf("TV size : %f cm\n", sizes[i]);
    }
}

int main(void)
{
    double tvSizes[]={81.28, 106.68, 139.70, 165.10, 190.50};

    printTVSizes(tvSizes);

    return 0;
}
*/
/*
//printArrSize
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void printArrSize(int arr[])
{
    printf("sizeof(arr) = %zu\n", sizeof(arr));
    printf("sizeof(arr[1]) = %zu\n", sizeof(arr[1]));
}

int main(void)
{
    int nums[] = {1, 2, 3, 4, 5};
    printf("sizeof(nums) = %zu\n", sizeof(nums));
    printArrSize(nums);
    return 0;
}
*/
/*
//array address
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void printArrAddr(int arr[])
{
    printf("address of arr = %p\n", arr);
}

int main(void)
{
    int nums[]= {1, 2, 3, 4, 5};
    printf("address of nums = %p\n", nums);
    printf("address of nums[0] = %p\n", &nums[0]);
    printArrAddr(nums);

    return 0;
}
*/
/*
//printTVSizes2
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define ARRAY_SIZE(arr, element) (sizeof((arr))/ sizeof((element)))

void printTVSizes(double sizes[], int size)
{
    for(int i=0; i<5; i++){
        printf("TV size : %f cm\n", sizes[i]);
    }
}

int main(void)
{
    double tvSizes[]={81.28, 106.68, 139.70, 165.10, 190.50};

    printTVSizes(tvSizes, ARRAY_SIZE(tvSizes, tvSizes[0]));

    return 0;
}
*/
/*
//IncreaseArr
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void increaseArray(int arr[], int size)
{
    for (int i=0; i < size; i++){
        arr[i]++;
    }
}

int main(void)
{
    int nums[5]= {1, 2, 3, 4, 5};
    increaseArray(nums, 5);
    for(int i=0; i<5; i++){
        printf("%d ", nums[i]);
    }
    return 0;
}
*/
/*
//SwapArrayElement
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define SIZE 6

void swapArrayElements(int arr[], int idx1, int idx2)
{
    int temp= arr[idx1];
    arr[idx1]= arr[idx2];
    arr[idx2]=temp;
}

void printArrayElements(int arr[], int size)
{
    for (int i=0; i<size; i++){
        printf("%d", arr[i]);
    }
    printf("\n");
}

int main(void)
{
    int nums[SIZE]= {4, 9, 7, 8, 6, 5};

    printArrayElements(nums, SIZE);
    swapArrayElements(nums, 2, 4);
    printArrayElements(nums, SIZE);

    return 0;
}
*/
/*
//DynamicArray
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int shiftArray(int arr[], int size, int n)
{
    int arr1[size];

    for(int i=0; i<size-n; i++){
        arr1[i+n]=arr[i];
    }
    for(int i=size-n, j=0; i<size; i++, j++){
        arr1[j]=arr[i];
    }
    for(int i=0; i<size; i++){
        arr[i]=arr1[i];
    }
}

void printArray(int arr[], int size)
{
    for(int i=0; i<size; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
}

#define SIZE 5
#define SIZE2 7

int main(void)
{
    int arr[SIZE]={1, 2, 3, 4, 5};
    printArray(arr, SIZE);
    shiftArray(arr, SIZE, 2);
    printArray(arr, SIZE);

    int arr2[SIZE2]={1, 2, 3, 4, 5, 6, 7};
    printArray(arr2,SIZE2);
    shiftArray(arr2, SIZE2, 4);
    printArray(arr2, SIZE2);

    return 0;
}
*/
/*
//Init2DArr
#include <stdio.h>

#define ROWS 3
#define COLUMNS 5

int main(void)
{
    int arr2[ROWS][COLUMNS];

    for(int row=0; row<ROWS; row++){
        for(int column=0; column<COLUMNS; column++){
            arr2[row][column]=(row*COLUMNS +column+1);
        }
    }

    printf("a[0][0]=%d, a[1][3]=%d\n", arr2[0][0], arr2[1][3]);
    return 0;
}
*/
/*
//RowsOf2DArr
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    int arr2[][5]= {{1, 2, 3, 4, 5}, {6, 7, 8}, {11,12}};
    int rows= sizeof(arr2)/ sizeof(arr2[0][0])/5;
    printf("rows=%d\n", rows);
    return 0;
}
*/
/*
//Print2DArrtUsingSubarray
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define ROWS 3
#define COLUMNS 5

void printArrayElements(const int arr[], int size)
{
    for(int i=0; i<size; i++){
        printf("%d ",arr[i]);
    }
    printf("\n");
}

int main(void)
{
    int arr2[ROWS][COLUMNS] = {{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10},{11,12, 13, 14, 15}};
    
    for (int row=0; row<ROWS; row++){
        printArrayElements(arr2[row],COLUMNS);
    }
    return 0;
}
*/

//Init3DArry
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define DEPTH 3
#define ROWS 3
#define COLUMNS 5

int main(void)
{
    int arr3[DEPTH][ROWS][COLUMNS];
    for(int depth=0; depth<DEPTH; depth++){
        for(int row=0; row<ROWS; row++){
            for(int column=0; column<COLUMNS; column++){
                arr3[depth][row][column] = depth*ROWS*COLUMNS + row*COLUMNS + column+1;
            }
        }
    }
    printf("arr3[0][0][1] = %d, arr3[1][0][4]= %d\n", arr3[0][0][1], arr3[1][0][4]);
    return 0;
}