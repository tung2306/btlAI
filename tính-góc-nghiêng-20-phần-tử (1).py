import math
import pandas as pd
import openpyxl
from collections import deque

toado = pd.read_excel (r'C:\Users\Fstore\Desktop\toado.xlsx')
x1 = list(toado.x1)
y1 = list(toado.y1)
x2 = list(toado.x2)
y2 = list(toado.y2)
def print_queue(queue):
    """In giá trị từ hàng đợi"""
    for i, value in enumerate(queue):
        print(f"Giá trị của alpha[{i}] = {value}")

#def input_coordinates(index):
    """Nhập tọa độ A và B từ người dùng"""
    #x1 = float(input(f"Nhập tọa độ x của điểm A[{index}]: "))
    #y1 = float(input(f"Nhập tọa độ y của điểm A[{index}]: "))
    #x2 = float(input(f"Nhập tọa độ x của điểm B[{index}]: "))
    #y2 = float(input(f"Nhập tọa độ y của điểm B[{index}]: "))
    #return x1, y1, x2, y2 

def calculate_alpha_queue():
    """Tính toán và lưu giá trị alpha vào hàng đợi"""
    alpha_queue = deque()  # Khởi tạo hàng đợi để lưu trữ giá trị alpha

    for i in range(20):
        #x1, y1, x2, y2 = input_coordinates(i)

        # Tính giá trị của m
        m = (x2[i] - x1[i]) / (y1[i] - y2[i])

        # Tính giá trị của alpha
        alpha = math.degrees(math.atan(m))

        # Lưu giá trị alpha vào hàng đợi
        alpha_queue.append(alpha)

    return alpha_queue

def calculate_average(queue):
    """Tính giá trị trung bình của hàng đợi"""
    average = sum(queue) / len(queue)
    return average

def replace_queue_element(queue, i, beta):
    """Thay thế giá trị phần tử thứ [i] trong hàng đợi bằng giá trị beta"""
    queue[i] = beta

# Chạy hàm calculate_alpha_queue() để tính toán và lưu giá trị alpha vào hàng đợi
alpha_queue = calculate_alpha_queue()

# In giá trị từ hàng đợi
print_queue(alpha_queue)

# Tính giá trị trung bình của hàng đợi alpha_queue
average_alpha = calculate_average(alpha_queue)
print("Giá trị trung bình của alpha_queue:", average_alpha)

# Thay thế giá trị phần tử thứ [i] trong alpha_queue bằng giá trị beta
# i = int(input("Nhập vị trí phần tử i: "))
# beta = float(input("Nhập giá trị beta: "))
# replace_queue_element(alpha_queue, i, beta)

# In giá trị từ hàng đợi sau khi thay thế
# print_queue(alpha_queue)
