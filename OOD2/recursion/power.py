def power(a, b):
    """
    หา a^b โดยใช้ recursive
    """
    # Base case คือเมื่อ b เท่ากับ 0 ให้ส่งค่า 1 กลับ
    if b == 0:
        return 1
    # Recursive case คือหา a^(b-1) แล้วคูณด้วย a
    else:
        return a * power(a, b-1)
    
a, b = map(int, input("Enter Input a b : ").split())
print(f"{power(a, b)}")