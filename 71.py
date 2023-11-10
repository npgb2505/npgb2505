x = float(input("Nhập một số để tính căn bậc hai: "))

guess = x / 2.0

while abs(guess * guess - x) > 10**(-12):
    
    guess = (guess + x / guess) / 2

print("Căn bậc hai của",x, "là khoảng ",guess)
