import math

# Nhập tọa độ điểm A
x1 = float(input("Nhập tọa độ x của điểm A: "))
y1 = float(input("Nhập tọa độ y của điểm A: "))

# Nhập tọa độ điểm B
x2 = float(input("Nhập tọa độ x của điểm B: "))
y2 = float(input("Nhập tọa độ y của điểm B: "))

# Tính giá trị của m
m = (x2 - x1) / (y1 - y2)

# Tính giá trị của alpha
alpha = math.degrees(math.atan(m))

# Xuất kết quả
print("Giá trị alpha: ", alpha)
