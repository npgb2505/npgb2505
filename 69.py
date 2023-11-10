so_pi = 0
for so_hang in range(15):
    if so_hang == 0:
        so_pi += 3
    else:
        dau = (-1)**(so_hang+1)
        d = 2*so_hang
        mau_so = (d)*(d+1)*(d+2)
        so_pi += (dau)*(4/mau_so)
    print(so_pi)