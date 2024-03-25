n = int(input("Nhập số nguyên dương n : "))
count = 0

while n:
    count += 1
    n //= 10

print("Số chữ số của n là : ", count)

