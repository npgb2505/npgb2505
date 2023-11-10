chuoi = input("Nhập một chuỗi để kiểm tra tính xuôi ngược: ")

xuoi_nguoc = True
dodai= len(chuoi)

i = 0
j = dodai - 1

while i < j:
    if chuoi[i] != chuoi[j]:
        xuoi_nguoc = False
        break
    i += 1
    j -= 1


if xuoi_nguoc:
    print(chuoi,'là một chuỗi có tính xuôi ngược')
else:
    print(chuoi,'không phải là chuỗi có tính xuôi ngược')
