def sum_of_number(n):
    tong = 0
    for i in range (1, n+1):
        tong += i
    return tong
while (True):
    try:
        n = int(input("Nhập số nguyên n: "))
        if n <= 1000:
            tong = sum_of_number(n)
            print (tong)
            break
        else:
            print ("n lớn hơn 1000")
            continue
    except ValueError:
        print ("Vui lòng nhập một số nguyên hợp lệ!")   
        continue     