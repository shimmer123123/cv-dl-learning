"""
Python 基础语法综合练习
包括变量、数据类型、列表、字典、循环、函数、文件读写、异常处理
"""

import os


#1. 变量与数据类型
name = "CV Learner"
age = 20
gpa = 3.75
is_student = True

print(f"姓名: {name}, 年龄: {age}, GPA: {gpa}, 是否在校生: {is_student}")


#2. 列表操作
scores = [88, 92, 79, 96, 85]
print(f"原始成绩: {scores}")
print(f"最高分: {max(scores)}")
print(f"平均分: {sum(scores) / len(scores):.1f}")

# 列表推导式
passed = [s for s in scores if s >= 60]
print(f"及格成绩: {passed}")


#3. 字典操作
student = {
    "name": "张三",
    "major": "Software Engineering",
    "courses": ["Python", "Data Structures", "OS"],
    "scores": {"Python": 90, "DS": 85, "OS": 88}
}
print(f"\n学生信息: {student['name']}, 专业: {student['major']}")
print(f"已选课程: {student['courses']}")
print(f"Python 成绩: {student['scores']['Python']}")


#4. 函数定义与调用
def calculate_average(score_list):
    """计算平均分"""
    if not score_list:
        return 0
    return sum(score_list) / len(score_list)


def greet(student_name, greeting="你好"):
    """带默认参数的函数"""
    return f"{greeting}, {student_name}!"


avg = calculate_average(scores)
print(f"\n平均分: {avg:.1f}")
print(greet("李四"))
print(greet("王五", "Welcome"))


#5. 字符串操作
text = "  Hello, Computer Vision!  "
print(f"\n原始: '{text}'")
print(f"去空格: '{text.strip()}'")
print(f"小写: '{text.lower().strip()}'")
print(f"替换: '{text.strip().replace('Vision', 'Learning')}'")
print(f"分割: {text.strip().split()}")


#6. 循环
print("\n----- for 循环遍历成绩 -----")
for i, s in enumerate(scores, start=1):
    status = "及格" if s >= 60 else "不及格"
    print(f"第 {i} 门: {s} ({status})")

print("\n----- while 循环累加 -----")
total = 0
count = 0
while count < len(scores):
    total += scores[count]
    count += 1
    if count == 3:
        print("已累加前 3 门，继续...")
print(f"while 循环结果: total={total}")


#7. 文件读写
input_filename = "input.txt"
output_filename = "output.txt"

# 写入测试文件
with open(input_filename, "w", encoding="utf-8") as f:
    f.write("计算机视觉\n")
    f.write("深度学习\n")
    f.write("Python编程\n")
    f.write("OpenCV图像处理\n")

# 读取并处理
try:
    with open(input_filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    processed = []
    for i, line in enumerate(lines):
        line = line.strip()
        processed.append(f"Line {i+1}: '{line}' ({len(line)} chars)\n")

    with open(output_filename, "w", encoding="utf-8") as f:
        f.writelines(processed)

    print(f"\n文件处理完成！共处理 {len(processed)} 行")
    print(f"输入: {input_filename} → 输出: {output_filename}")

except FileNotFoundError:
    print(f"错误: 找不到文件 {input_filename}")
except Exception as e:
    print(f"发生未知错误: {e}")


#8. os 模块简单使用
print(f"\n当前工作目录: {os.getcwd()}")
print(f"目录下的文件: {os.listdir('.')}")

print("\n01_python_basics.py 全部运行完成！")