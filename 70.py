while True:
    lua_chon = input("Nhập 'e' để mã hóa hoặc 'd' để giải mã, hoặc nhấn Enter để thoát: ")

    if lua_chon == "":
        break

    if lua_chon == 'e':
        tin_nhan = input("Nhập thông điệp cần mã hóa: ")
        dich = int(input("Nhập độ dịch: "))
        ket_qua = ""
        for kitu in tin_nhan:
            if kitu.isalpha(): #kiem tra co phai chu cai khong
                is_upper = kitu.isupper()
                kitu = kitu.lower()
                ki_tu_dadich = chr(ord(kitu)+dich)
                if is_upper:
                    ki_tu_dadich = ki_tu_dadich.upper()
                ket_qua += ki_tu_dadich
            else:
                ket_qua += kitu
        print("Tin nhắn đã mã hóa:",ket_qua)
    elif lua_chon == 'd':
        tin_nhan = input("Nhập thông điệp cần giải mã: ")
        dich = int(input("Nhập độ dịch: "))
        ket_qua = ""
        for kitu in tin_nhan:
            if kitu.isalpha():
                is_upper = kitu.isupper()
                kitu = kitu.lower()
                ki_tu_dadich = chr(ord(kitu)+dich)
                if is_upper:
                    ki_tu_dadich = ki_tu_dadich.upper()
                ket_qua += ki_tu_dadich
            else:
                ket_qua += kitu
        print("Tin nhắn đã giải mã:",ket_qua)
    else:
        print("Lựa chọn không hợp lệ. Vui lòng nhập 'e' để mã hóa hoặc 'd' để giải mã.")

print("Kết thúc chương trình.")
