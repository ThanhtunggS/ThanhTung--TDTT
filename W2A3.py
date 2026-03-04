def tinh_toan_ab (a,b):
    tong = a + b
    hieu = a -b
    tich = a*b
    phan_nguyen = a//b
    phan_du = a%b
    phep_chia = round(a/b,2)
    return (tong, hieu, tich, phan_nguyen, phan_du, phep_chia)
a, b = map(int, input("Nhập 2 số: ").split())
tong, hieu, tich, phan_nguyen, phan_du, phep_chia = tinh_toan_ab(a,b)
print("Answer:", tong, hieu, tich, phan_nguyen, phan_du, phep_chia, sep="|")

