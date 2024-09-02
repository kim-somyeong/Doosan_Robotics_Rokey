/*
//문제3
#include <stdio.h>

int divisor=1;

int main(void)
{
    int n= 12;

    for (int divisor = 1; divisor <=n; divisor++){
        if (n%divisor == 0){
            printf("%d ", divisor);
        }
    }
    return 0;
}
*/
/*
//문제4
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

int main(void)
{
    double m, n;
    printf("정수 두 개를 m n 형태로 입력하시오: ");
    scanf("%lf %lf", &m, &n);
    
    double r = pow(m, n);
    printf("m^n = %f\n", r);

    return 0;
}
*/
/*
//문제5
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

int main(void)
{
    float d1, d2, d3, d4, d5;
    printf("다섯 개 실수값을 num1 num2 num3 num4 num5 형태로 입력하세요: ", &d1, &d2, &d3, &d4, &d5);
    scanf("%f %f %f %f %f", &d1, &d2, &d3, &d4, &d5);

    float avg= (d1+d2+d3+d4+d5)/5;

    float avgAvg = (pow(d1-avg,2) + pow(d2-avg,2) + pow(d3-avg,2) + pow(d4-avg,2) + pow(d5-avg,2)) / 5;
    float std= sqrt(avgAvg);
    printf("표준편차 = %f\n",std);
    return 0;
}
*/
/*
//문제6
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    int n=1;
    int n4;

    while(1){
        n4= n*n*n*n;

        if(n4>1000){
            printf("가장 작은 정수 n :%d\n", n);
        }
        n++;
    }
    return 0;
}
*/
/*
//문제7
#include <stdio.h>

int main(void)
{
    int n=1;
    int n4;

    while(1){
        n4= n*n*n*n;

        if(n4>300){
            break;
        }
        printf("n=%d, n4=%d\n", n, n4);
    }
    printf("n=%d, n4=%d\n", n, n4);

    return 0;
}
*/
/*
//문제8
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

int main(void)
{
    int n; //4자리 수
    int n1, n2, n3, n4;

    printf("4자리 수 입력 :");
    scanf("%d", &n);

    if (n < 1000 || n > 9999) {
        printf("4자리 숫자를 입력해야 합니다.\n");
        return 1; // 오류 코드 반환
    }

    // 각 자리수 분리
    n1 = n / 1000;          // 천 단위
    n2 = (n / 100) % 10;    // 백 단위
    n3 = (n / 10) % 10;     // 십 단위
    n4 = n % 10;            // 일 단위
    
    // n과 n1^4 + n2^4 + n3^3 + n4^3 계산
    int sum = pow(n1, 4) + pow(n2, 4) + pow(n3, 3) + pow(n4, 3);
    
    // 결과가 같으면 출력
    if (n == sum) {
        printf("%d = %d^4 + %d^4 + %d^3 + %d^3\n", n, n1, n2, n3, n4);
    } else {
        printf("%d는 조건을 만족하지 않습니다.\n", n);
    }

    return 0;
}
*/
/*
//문제9
#include <stdio.h>

void printClaps(int count){
    for(int i = 0; i < count; i++){
        printf("clap");
    }
}

int main(void)
{
    for(int num = 1; num <= 100; num++){
        int n=num;
        int clapCount=0;

        while (n>0){
            int digit = n%10;
            if(digit==3 || digit==6 || digit==9){
                clapCount++;
            }
            n/=10;
        }

        if (clapCount > 0){
            printf("%d ", num);
            printClaps(clapCount);
            printf("\n");
        }
    }
    return 0;
}
*/
/*
//문제10
#include <stdio.h>
#define TAX_RATE 0.154

//적금 이자와 환급 금액 계싼 함수
void calculate_savings_interest(float annual_interest_rate, int months, float deposit_amount) {
    float total_interest = 0;
    float monthly_interest_rate = (annual_interest_rate / 100) / 12;

    // 총 이자 계산
    for (int month = 1; month <= months; month++) {
        int months_left = months - month + 1;
        float interest = deposit_amount * (monthly_interest_rate * months_left);
        total_interest += interest;
    }

    // 원금 계산
    float principal = deposit_amount * months;
    float total_amount_before_tax = principal + total_interest;

    // 세금 계산
    float tax = total_interest * TAX_RATE;

    // 환급 금액 계산
    float total_amount_after_tax = total_amount_before_tax - tax;

    // 결과 출력
    printf("원금: %.2f 원\n", principal);
    printf("총 이자 금액: %.2f 원\n", total_interest);
    printf("세금: %.2f 원\n", tax);
    printf("환급 금액: %.2f 원\n", total_amount_after_tax);
}

int main() {
    float annual_interest_rate;
    int months;
    float deposit_amount;

    // 사용자 입력
    printf("연 이자율(%%)을 입력하세요: ");
    scanf("%f", &annual_interest_rate);

    printf("기간(월)을 입력하세요: ");
    scanf("%d", &months);

    printf("매월 납입금액을 입력하세요: ");
    scanf("%f", &deposit_amount);

    // 적금 이자 및 환급 금액 계산
    calculate_savings_interest(annual_interest_rate, months, deposit_amount);

    return 0;
}
*/
/*
//문제19
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

//함수 선언
int days_in_month(int month, int year);
int is_leap_year(int year);
int remaining_days(int year, int month, int day);

int main()
{
    int year, month, day;

    printf("write the year: ");
    scanf("%d", &year);
    printf("write the month: ");
    scanf("%d", &month);
    printf("write the day: ");
    scanf("%d",&day);

    int day_left = remaining_days(year, month, day);
    printf("reamin day this year: %d\n", day_left);

    return 0;
}

//윤년 판단
int is_leap_year(int year){
    return(year%4 == 0 &&(year%100 != 0 || year%400 == 0));
}

//월별 일수 반환
int days_in_month(int month, int year){
    switch(month){
        case 1: case 3: case 5: case 7: case 8: case 10: case 12:
            return 31;
        case 4: case 6: case 9: case 11:
            return 30;
        case 2:
            return is_leap_year(year) ? 29 : 28;
        default:
            return 0; // 잘못된 월 입력
    }
}

// 잔여 일수 계산 함수
int remaining_days(int year, int month, int day) {
    int total_days = 0;

    // 현재 월의 남은 일수 계산
    for (int m = month; m <= 12; m++) {
        if (m == month) {
            total_days += days_in_month(m, year) - day;
        } else {
            total_days += days_in_month(m, year);
        }
    }

    // 올해의 모든 월의 일수 계산
    int days_in_year = 0;
    for (int m = 1; m <= 12; m++) {
        days_in_year += days_in_month(m, year);
    }

    // 잔여 일수 계산
    int days_passed = days_in_year - total_days;
    return days_passed;
}
*/
/*
//문제20
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int sum1toN(int n)
{
    if(n==0){return 0;}
    return sum1toN(n-1) + n;   //자기 자신을 return -> 재귀호출
}

int main(void)
{
    int n;
    printf("1 이상의 양의 정수 한 개 입력: ");
    scanf("%d", &n);
    int sum = sum1toN(n);
    printf("1~%d의 합 sum = %d\n", n, sum);

    return 0;
}
*/
/*
//21
#include <stdio.h>
#include <math.h>

double power(double x, double y){
    double result = 1.0;
    for(unsigned i=0; i<y; i++){
        result *= x;
    }
    return result;
}

double power_recursive(double x, double y){
    if(y==0){
        return 1.0;
    }
    return x * power_recursive(x, y-1);
}

int main(void)
{
    double x;
    unsigned y;

    // 사용자로부터 x와 y 입력 받기
    printf("x 값을 입력하세요: ");
    scanf("%lf", &x);
    printf("y 값을 입력하세요: ");
    scanf("%u", &y);

    // pow 함수와 power 함수의 결과 비교
    double pow_result = pow(x, y);
    double power_result = power(x, y);
    double power_recursive_result = power_recursive(x, y);

    printf("pow(x, y) = %lf\n", pow_result);
    printf("power(x, y) (반복문) = %lf\n", power_result);
    printf("power(x, y) (재귀) = %lf\n", power_recursive_result);

    // 비교 결과 출력
    if (fabs(pow_result - power_result) < 1e-6 && fabs(pow_result - power_recursive_result) < 1e-6) {
        printf("결과가 일치합니다.\n");
    } else {
        printf("결과가 일치하지 않습니다.\n");
    }

    return 0;
}
*/
/*
//22
#include <stdio.h>

// 최대 연속 합을 계산하는 함수
int find_max(int *arr, int n) {
    int max_far = arr[0];
    int max_ending = arr[0];

    for (int i = 1; i < n; i++) {
        max_ending = (arr[i] > max_ending + arr[i]) ? arr[i] : max_ending + arr[i];
        max_far = (max_far > max_ending) ? max_far : max_ending;
    }
    return max_far; // 최대 연속 합 반환
}

int main(void) {
    int n;
    printf("숫자 개수 : ");
    scanf("%d", &n);

    if (n <= 0) {
        printf("숫자의 개수는 0보다 커야 합니다.\n");
        return 1;
    }

    int numbers[n];

    // 숫자 입력받기
    for (int i = 0; i < n; i++) {
        printf("숫자 : ");
        scanf("%d", &numbers[i]);
    }

    // 최대 연속 합 계산
    int max_sum = find_max(numbers, n);
    
    // 결과 출력
    printf("최대 부분 숫자 합 : %d\n", max_sum);

    return 0;
}
*/
/*
//23
#include <stdio.h>
#include <stdbool.h>

bool isPrime(int num)
{
    if (num <= 1) {
        return false; // 1과 0은 소수가 아님
    }
    if (num <= 3) {
        return true; // 2와 3은 소수
    }
    if (num % 2 == 0 || num % 3 == 0) {
        return false; // 2와 3의 배수는 소수가 아님
    }
    for (int i = 5; i * i <= num; i += 6) {
        if (num % i == 0 || num % (i + 2) == 0) {
            return false; // i와 i+2로 나누어떨어지면 소수가 아님
        }
    }
    return true; // 나누어떨어지지 않으면 소수
}

int main(void) {
    int n;

    // 사용자로부터 숫자 입력받기
    printf("숫자를 입력하세요: ");
    scanf("%d", &n);

    if (n <= 1) {
        printf("소수가 없습니다.\n");
        return 0;
    }

    // 소수 출력
    printf("소수 :");
    for (int i = 2; i <= n; i++) {
        if (isPrime(i)) {
            printf(" %d", i);
        }
    }
    printf("\n");

    return 0;
}
*/
/*
//24
#include <stdio.h>

int sum_of_digit(int num)
{
    int sum=0;

    num= (num<0)? -num : num; //절대값

    while(num>0){
        sum += num%10;
        num /=10;
    }
    return sum;
}


int main(void) {
    int number;

    // 사용자로부터 숫자 입력받기
    printf("정수를 입력하세요 : ");
    scanf("%d", &number);

    // 자리수 합 계산
    int result = sum_of_digit(number);

    // 결과 출력
    printf("자리수 합: %d\n", result);

    return 0;
}
*/
/*
//25
#include <stdio.h>

// N번째 피보나치 수를 계산하는 함수 (반복문 사용)
int fibonacci(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;

    int a = 0, b = 1, c;

    for (int i = 2; i <= n; i++) {
        c = a + b;  // 현재 피보나치 수 계산
        a = b;      // 이전 두 수 업데이트
        b = c;
    }

    return b; // N번째 피보나치 수 반환
}

int main(void) {
    int N;

    // 사용자로부터 양의 정수 N 입력받기
    printf("양의 정수를 입력하세요: ");
    scanf("%d", &N);

    if (N < 0) {
        printf("양의 정수를 입력해야 합니다.\n");
        return 1;
    }

    // N번째 피보나치 수 계산
    int result = fibonacci(N);

    // 결과 출력
    printf("%d번째 피보나치 수: %d\n", N, result);

    return 0;
}
*/
/*
//26
#include <stdio.h>

// 팩토리얼을 계산하는 함수
unsigned long long factorial(int n) {
    unsigned long long result = 1;

    // 팩토리얼 계산
    for (int i = 1; i <= n; i++) {
        result *= i;
    }

    return result;
}

int main(void) {
    int N;

    // 사용자로부터 양의 정수 N 입력받기
    printf("정수를 입력하세요 : ");
    scanf("%d", &N);

    if (N < 0) {
        printf("양의 정수를 입력해야 합니다.\n");
        return 1;
    }

    // N의 팩토리얼 계산
    unsigned long long fact = factorial(N);

    // 결과 출력
    printf("팩토리얼 : %llu\n", fact);

    return 0;
}
*/
/*
//27
#include <stdio.h>
#include <stdbool.h>

// 홀수 여부를 판별하는 함수
bool is_odd(int num) {
    return (num % 2 != 0); // 숫자가 홀수이면 true, 아니면 false 반환
}

int main(void) {
    int start, end;

    // 사용자로부터 두 정수 입력받기
    printf("두 숫자를 입력하세요 : ");
    scanf("%d %d", &start, &end);

    // 입력 받은 두 숫자 사이의 홀수 출력
    printf("홀수 : ");
    // 두 숫자 사이의 범위를 정렬 (작은 숫자부터 시작)
    if (start > end) {
        int temp = start;
        start = end;
        end = temp;
    }

    // 두 숫자 사이의 모든 홀수를 출력
    bool first = true;
    for (int i = start; i <= end; i++) {
        if (is_odd(i)) {
            if (!first) {
                printf(", ");
            }
            printf("%d", i);
            first = false;
        }
    }
    printf("\n");

    return 0;
}
*/
/*
//28
#include <stdio.h>
#include <math.h>

// 제곱근을 정수로 반환하는 함수
int integer_sqrt(int num) {
    if (num < 0) {
        printf("음수는 제곱근을 계산할 수 없습니다.\n");
        return -1; // 오류 코드
    }
    // sqrt() 함수로 제곱근을 계산하고 정수로 변환
    return (int)sqrt((double)num);
}

int main(void) {
    int number;

    // 사용자로부터 양의 정수 입력받기
    printf("정수를 입력하세요 : ");
    scanf("%d", &number);

    if (number < 0) {
        printf("음수는 제곱근을 계산할 수 없습니다.\n");
        return 1;
    }

    // 제곱근 계산
    int result = integer_sqrt(number);

    // 결과 출력
    printf("제곱근 : %d\n", result);

    return 0;
}
*/
/*
//29
#include <stdio.h>
#include <stdbool.h>

// 소수 여부를 판별하는 함수
bool is_prime(int num) {
    if (num <= 1) {
        return false; // 1 이하의 숫자는 소수가 아님
    }
    if (num == 2) {
        return true;  // 2는 소수
    }
    if (num % 2 == 0) {
        return false; // 짝수는 소수가 아님
    }

    // 3부터 num의 제곱근까지 홀수로 나누어 봅니다
    for (int i = 3; i * i <= num; i += 2) {
        if (num % i == 0) {
            return false; // 나누어 떨어지면 소수가 아님
        }
    }

    return true; // 나누어 떨어지지 않으면 소수
}

int main(void) {
    int number;

    // 사용자로부터 양의 정수 입력받기
    printf("정수를 입력하세요 : ");
    scanf("%d", &number);

    if (number < 0) {
        printf("음수는 소수를 판단할 수 없습니다.\n");
        return 1;
    }

    // 소수 여부 판단
    bool result = is_prime(number);

    // 결과 출력
    if (result) {
        printf("%d는 소수입니다.\n", number);
    } else {
        printf("%d는 소수가 아닙니다.\n", number);
    }

    return 0;
}
*/

//30
#include <stdio.h>
#include <stdbool.h>

// 완전수 여부를 판별하는 함수
bool is_perfect_number(int num) {
    if (num <= 0) {
        return false; // 0 이하의 숫자는 완전수가 아님
    }

    int sum = 0;

    // 1부터 num/2까지의 약수들을 찾아서 합산
    for (int i = 1; i <= num / 2; i++) {
        if (num % i == 0) {
            sum += i;
        }
    }

    // 약수의 합이 num과 같으면 완전수
    return (sum == num);
}

int main(void) {
    int number;

    // 사용자로부터 양의 정수 입력받기
    printf("정수를 입력하세요 : ");
    scanf("%d", &number);

    // 완전수 여부 판단
    bool result = is_perfect_number(number);

    // 결과 출력
    if (result) {
        printf("%d는 완전수입니다.\n", number);
    } else {
        printf("%d는 완전수가 아닙니다.\n", number);
    }

    return 0;
}

