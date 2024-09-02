print("="*50, end="\n")
print("="," "*46, "=")
print("=", " "*8, "Welcome to Hello World Cafe!!", " "*7, "=")
print("="," "*46, "=")
print("=", " "*8, "We deliver Happiness!!!", " "*13, "=")
print("="," "*46, "=")
print("="*50, end="\n")

#메뉴 설정
Menu ={
    "Americano" : 2500,
    "Cafe Latte" : 3500,
    "Espresso" : 3000,
    "Green Tea" : 3300
}
for item, price in Menu.items():
    print(f'{item}:{price}')

print("="*50, end="\n")

#사용자 입력
americano_count= int(input("Americano : "))
latte_count= int(input("Cafe Latte :"))
espresso_count=int(input("Espresso :"))
green_count=int(input("Green Tea :"))

#총 가격 계산
total_price=americano_count*Menu['Americano'] + latte_count*Menu['Cafe Latte'] + espresso_count*Menu['Espresso'] + green_count*Menu['Green Tea']

#총 가격 출력
print("="*50, end="\n")
print(f'total :{total_price}')

#메뉴 추가
new_item_name= input('include name: ')
new_item_price= int(input('write the price: '))
Menu[new_item_name]=new_item_price

print("\nUpgrade Menu :")
for item, price in Menu.items():
    print(f'{item} : {price}')

print("="*50, end="\n")

#사용자 입력
americano_count= int(input("Americano : "))
latte_count= int(input("Cafe Latte :"))
espresso_count=int(input("Espresso :"))
green_count=int(input("Green Tea :"))
new_item_count=int(input(f'{new_item_name} :'))

total_price=americano_count*Menu['Americano'] + latte_count*Menu['Cafe Latte'] + espresso_count*Menu['Espresso'] + green_count*Menu['Green Tea'] + new_item_count*Menu[new_item_name]

#수정 주문 요약 출력
print("\n주문 요약:")
print(f"Americano: {americano_count}개")
print(f"Cafe Latte: {latte_count}개")
print(f"Espresso: {espresso_count}개")
print(f"Green Tea: {green_count}개")
print(f"{new_item_name}: {new_item_count}개")

#수정 총 가격 출력
print("="*50, end="\n")
print(f"총 가격: {total_price}원")
print("="*50, end="\n")