/*
//1
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define MAX_SIZE 10

int find_max(int arr[], int size)
{
    int max=arr[0];

    for(int i=1; i<size; i++){
        if(arr[i]>max){
            max=arr[i]; //new max_size
        }
    }
    return max;
}

int main(void)
{
    int numbers[MAX_SIZE];
    int size= MAX_SIZE;

    printf("배열의 요소를 입력 : ");

    for(int i=0; i<size; i++){
        printf("요소 %d : ", i+1);
        scanf("%d", &numbers[i]);
    }

    int max_value= find_max(numbers, size);

    printf("max : %d\n", max_value);

    return 0;
}
*/
/*
//2
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define SIZE 3

void print_reverse(int arr[], int size)
{
    printf("print array reverse : \n");
    for(int i=size-1; i>=0; i--){
        printf("%d", arr[i]);
    }
    printf("\n");
}

int main(void)
{
    int numbers[SIZE];

    printf("write the array :\n");

    for (int i=0; i<SIZE; i++){
        printf("요소 %d: ", i+1);
        scanf("%d", &numbers[i]);
    }
    print_reverse(numbers, SIZE);

    return 0;
}
*/
/*
//6
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

#define N 10

int main(void)
{
    int coefficients [N+1] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11};
    double x;
    double result = 0.0;

    printf("x 값을 입력하세요 :");
    scanf("%lf", &x);

    for (int i = N; i>=0; i--){
        result += coefficients[i] * pow(x, i);
    }

    printf("다항식의 결과 :%.2f\n", result);

    return 0;
}
*/
/*
//7
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define MAX_SIZE 10

// 배열에서 중복된 값을 제거하고 유니크한 값만 출력하는 함수
void print_unique(int arr[], int size) {
    int unique[MAX_SIZE];
    int unique_size = 0;
    int is_duplicate;

    for (int i = 0; i < size; i++) {
        is_duplicate = 0;
        // 중복 검사
        for (int j = 0; j < unique_size; j++) {
            if (arr[i] == unique[j]) {
                is_duplicate = 1;
                break;
            }
        }
        // 중복이 아닌 경우 unique 배열에 추가
        if (!is_duplicate) {
            unique[unique_size] = arr[i];
            unique_size++;
        }
    }

    // 유니크한 값 출력
    printf("유니크한 값 : ");
    for (int i = 0; i < unique_size; i++) {
        printf("%d ", unique[i]);
    }
    printf("\n");
}

int main() {
    int n;
    printf("배열의 길이를 입력하세요: ");
    scanf("%d", &n);

    if (n > MAX_SIZE) {
        printf("배열의 길이는 최대 %d까지 지원됩니다.\n", MAX_SIZE);
        return 1;
    }

    int array[n];

    printf("배열 요소를 입력하세요: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &array[i]);
    }

    // 중복 제거 및 유니크한 값 출력
    print_unique(array, n);

    return 0;
}
*/
/*
//8
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define MAX_SIZE 5

// 짝수만 출력하는 함수
void print_even_numbers(int arr[], int size) {
    printf("짝수 : ");
    for (int i = 0; i < size; i++) {
        if (arr[i] % 2 == 0) { // 짝수 확인
            printf("%d ", arr[i]);
        }
    }
    printf("\n");
}

int main() {
    int n;

    printf("배열의 길이를 입력하세요: ");
    scanf("%d", &n);

    if (n > MAX_SIZE) {
        printf("배열의 길이는 최대 %d까지 지원됩니다.\n", MAX_SIZE);
        return 1;
    }

    int array[n];

    printf("배열 요소를 입력하세요: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &array[i]);
    }

    // 짝수만 출력
    print_even_numbers(array, n);

    return 0;
}
*/
/*
//9
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define MAX_SIZE 5

// 배열에서 최솟값과 최댓값을 찾는 함수
void find_min_max(int arr[], int size, int *min, int *max) {
    *min = arr[0];
    *max = arr[0];

    for (int i = 1; i < size; i++) {
        if (arr[i] < *min) {
            *min = arr[i];
        }
        if (arr[i] > *max) {
            *max = arr[i];
        }
    }
}

int main() {
    int n;
    int min, max;

    printf("배열의 길이를 입력하세요: ");
    scanf("%d", &n);

    if (n > MAX_SIZE) {
        printf("배열의 길이는 최대 %d까지 지원됩니다.\n", MAX_SIZE);
        return 1;
    }

    int array[n];

    printf("배열 요소를 입력하세요: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &array[i]);
    }

    // 최솟값과 최댓값 계산
    find_min_max(array, n, &min, &max);

    // 결과 출력
    printf("최솟값 : %d, 최댓값 : %d\n", min, max);

    return 0;
}
*/
/*
//10
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define MAX_SIZE 5

// 배열의 요소들의 총합을 계산하는 함수
int calculate_sum(int arr[], int size) {
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
    return sum;
}

int main() {
    int n;
    int sum;

    printf("배열의 길이를 입력하세요: ");
    scanf("%d", &n);

    if (n > MAX_SIZE) {
        printf("배열의 길이는 최대 %d까지 지원됩니다.\n", MAX_SIZE);
        return 1;
    }

    int array[n];

    printf("배열 요소를 입력하세요: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &array[i]);
    }

    // 요소들의 총합 계산
    sum = calculate_sum(array, n);

    // 결과 출력
    printf("총합 : %d\n", sum);

    return 0;
}
*/
/*
//11
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define MAX_SIZE 5

// 배열에서 홀수와 짝수의 개수를 계산하는 함수
void count_odd_even(int arr[], int size, int *odd_count, int *even_count) {
    *odd_count = 0;
    *even_count = 0;

    for (int i = 0; i < size; i++) {
        if (arr[i] % 2 == 0) {
            (*even_count)++;
        } else {
            (*odd_count)++;
        }
    }
}

int main() {
    int n;
    int odd_count, even_count;

    printf("배열의 길이를 입력하세요: ");
    scanf("%d", &n);

    if (n > MAX_SIZE) {
        printf("배열의 길이는 최대 %d까지 지원됩니다.\n", MAX_SIZE);
        return 1;
    }

    int array[n];

    printf("배열 요소를 입력하세요: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &array[i]);
    }

    // 홀수와 짝수 개수 계산
    count_odd_even(array, n, &odd_count, &even_count);

    // 결과 출력
    printf("홀수 개수 : %d, 짝수 개수 : %d\n", odd_count, even_count);

    return 0;
}
*/
/*
//12
#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

#define MAX_SIZE 5

// 배열의 각 요소의 출현 빈도를 계산하는 함수
void count_frequencies(int arr[], int size) {
    int counted[MAX_SIZE] = {0}; // 최대 크기만큼의 배열 초기화
    int freq[MAX_SIZE] = {0};    // 출현 빈도 배열 초기화

    for (int i = 0; i < size; i++) {
        int element = arr[i];
        int found = 0;

        // 이미 빈도를 계산했는지 확인
        for (int j = 0; j < i; j++) {
            if (arr[j] == element) {
                found = 1;
                break;
            }
        }

        if (!found) {
            int count = 0;
            for (int k = 0; k < size; k++) {
                if (arr[k] == element) {
                    count++;
                }
            }
            printf("%d : %d회\n", element, count);
        }
    }
}

int main() {
    int n;

    printf("배열의 길이를 입력하세요: ");
    scanf("%d", &n);

    if (n > MAX_SIZE) {
        printf("배열의 길이는 최대 %d까지 지원됩니다.\n", MAX_SIZE);
        return 1;
    }

    int array[n];

    printf("배열 요소를 입력하세요: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &array[i]);
    }

    // 각 요소의 출현 빈도 계산 및 출력
    printf("각 요소의 출현 빈도 :\n");
    count_frequencies(array, n);

    return 0;
}
*/
/*
//13
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define MAX_SIZE 5

// 두 번째로 큰 수를 찾는 함수
int find_second_largest(int arr[], int size) {
    int first = -2147483648;  // 최소 정수 값으로 초기화
    int second = -2147483648; // 최소 정수 값으로 초기화

    for (int i = 0; i < size; i++) {
        if (arr[i] > first) {
            second = first;
            first = arr[i];
        } else if (arr[i] > second && arr[i] != first) {
            second = arr[i];
        }
    }
    return second;
}

int main() {
    int n;

    printf("배열의 길이를 입력하세요: ");
    scanf("%d", &n);

    if (n > MAX_SIZE) {
        printf("배열의 길이는 최대 %d까지 지원됩니다.\n", MAX_SIZE);
        return 1;
    }

    int array[n];

    printf("배열 요소를 입력하세요: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &array[i]);
    }

    // 두 번째로 큰 수 계산
    int second_largest = find_second_largest(array, n);

    // 결과 출력
    if (second_largest == -2147483648) {
        printf("두 번째로 큰 수를 찾을 수 없습니다.\n");
    } else {
        printf("두 번째로 큰 수 : %d\n", second_largest);
    }

    return 0;
}
*/
/*
//14
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define MAX_SIZE 5

// 배열을 오름차순으로 정렬하는 함수 (버블 정렬)
void bubble_sort(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Swap arr[j] and arr[j + 1]
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main() {
    int n;

    printf("배열의 길이를 입력하세요: ");
    scanf("%d", &n);

    if (n > MAX_SIZE) {
        printf("배열의 길이는 최대 %d까지 지원됩니다.\n", MAX_SIZE);
        return 1;
    }

    int array[n];

    printf("배열 요소를 입력하세요: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &array[i]);
    }

    // 배열 오름차순 정렬
    bubble_sort(array, n);

    // 정렬된 배열 출력
    printf("정렬된 배열 :");
    for (int i = 0; i < n; i++) {
        printf(" %d", array[i]);
    }
    printf("\n");

    return 0;
}
*/
/*
//15
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define MAX_SIZE 5

// 최소값의 위치를 찾는 함수
int find_min_index(int arr[], int size) {
    int min_index = 0;  // 최소값의 인덱스를 초기화합니다.

    for (int i = 1; i < size; i++) {
        if (arr[i] < arr[min_index]) {
            min_index = i;  // 현재 요소가 최소값보다 작으면 인덱스를 업데이트합니다.
        }
    }

    return min_index;
}

int main() {
    int n;

    printf("배열의 길이를 입력하세요: ");
    scanf("%d", &n);

    if (n > MAX_SIZE) {
        printf("배열의 길이는 최대 %d까지 지원됩니다.\n", MAX_SIZE);
        return 1;
    }

    int array[n];

    printf("배열 요소를 입력하세요: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &array[i]);
    }

    // 최소값의 위치 찾기
    int min_index = find_min_index(array, n);

    // 결과 출력
    printf("최소값 위치 : %d\n", min_index);

    return 0;
}
*/
/*
//16
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define MAX_SIZE 4

int main() {
    int n;

    printf("배열의 길이를 입력하세요: ");
    scanf("%d", &n);

    if (n > MAX_SIZE) {
        printf("배열의 길이는 최대 %d까지 지원됩니다.\n", MAX_SIZE);
        return 1;
    }

    int array[n];
    long long product = 1;  // 곱을 저장할 변수 (큰 수를 저장하기 위해 long long 사용)

    printf("배열 요소를 입력하세요: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &array[i]);
        product *= array[i];  // 현재 요소를 곱합니다.
    }

    // 결과 출력
    printf("요소들의 곱: %lld\n", product);

    return 0;
}
*/
/*
//17
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define MAX_SIZE 7

int main() {
    int n;
    int search_num;

    printf("배열의 길이를 입력하세요: ");
    scanf("%d", &n);

    if (n > MAX_SIZE) {
        printf("배열의 길이는 최대 %d까지 지원됩니다.\n", MAX_SIZE);
        return 1;
    }

    int array[n];

    printf("배열 요소를 입력하세요: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &array[i]);
    }

    printf("찾고자 하는 숫자를 입력하세요: ");
    scanf("%d", &search_num);

    printf("숫자 %d 위치: ", search_num);
    int found = 0;  // 숫자가 발견되었는지 여부를 표시하는 플래그

    for (int i = 0; i < n; i++) {
        if (array[i] == search_num) {
            if (found) {
                printf(", ");
            }
            printf("%d", i);
            found = 1;  // 숫자가 발견된 경우 플래그를 설정
        }
    }

    if (!found) {
        printf("해당 숫자는 배열에 없습니다.");
    }

    printf("\n");

    return 0;
}
*/
/*
//18
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define MAX_SIZE 6

int main() {
    int n;

    printf("배열의 길이를 입력하세요: ");
    scanf("%d", &n);

    if (n > MAX_SIZE) {
        printf("배열의 길이는 최대 %d까지 지원됩니다.\n", MAX_SIZE);
        return 1;
    }

    int array[n];

    printf("배열 요소를 입력하세요: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &array[i]);
    }

    printf("그룹 합: ");
    for (int i = 0; i < n; i += 2) {
        int sum = array[i];
        if (i + 1 < n) { // 배열의 범위를 초과하지 않는지 확인
            sum += array[i + 1];
        }
        if (i > 0) {
            printf(" ");
        }
        printf("%d", sum);
    }

    printf("\n");

    return 0;
}
*/

//19
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define MAX_SIZE 5

int main() {
    int n;

    printf("배열의 길이를 입력하세요: ");
    scanf("%d", &n);

    if (n > MAX_SIZE) {
        printf("배열의 길이는 최대 %d까지 지원됩니다.\n", MAX_SIZE);
        return 1;
    }

    int array[n];
    int temp;

    printf("배열 요소를 입력하세요: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &array[i]);
    }

    // 왼쪽으로 한 칸 이동
    temp = array[0];
    for (int i = 0; i < n - 1; i++) {
        array[i] = array[i + 1];
    }
    array[n - 1] = temp;

    // 결과 출력
    printf("이동 후 배열: ");
    for (int i = 0; i < n; i++) {
        if (i > 0) {
            printf(" ");
        }
        printf("%d", array[i]);
    }
    printf("\n");

    return 0;
}