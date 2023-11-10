chuoi = input("Nhập một chuỗi để kiểm tra palindrome: ")

chuoi_lien = "".join(chuoi.split()).lower()

xuoi_nguoc = True
dodai = len(chuoi_lien)

i = 0
j = dodai - 1

while i < j:
    if chuoi_lien[i] != chuoi_lien[j]:
        xuoi_nguoc = False
        break
    i += 1
    j -= 1

if xuoi_nguoc:
    print(chuoi,'là một chuỗi có tính xuôi ngược')
else:
    print(chuoi,'không phải là chuỗi có tính xuôi ngược')
