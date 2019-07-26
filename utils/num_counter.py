# _*_ coding: utf-8 _*_
import os

# 新建文本文件
py_num, css_num, html_num, js_num = 0, 0, 0, 0

# root代表根目录下所有子文件夹路径；dir代表所有子文件夹名称；files代表根目录下所有文件名称（包括子文件夹里面的文件名称）
for root, dirs, files in os.walk('../'):
    for file in files:
        if file.endswith('.py'):
            # 根据文件编码加以申明，不然统计的行数会不准确，我要打开的文本文件时encoding = "utf-16-le"格式的
            for count, line in enumerate(open(os.path.join(root, file), "r", encoding="utf-8")):
                py_num += 1
        elif file.endswith('.css'):
            for count, line in enumerate(open(os.path.join(root, file), "r", encoding="utf-8")):
                css_num += 1
        elif file.endswith('.html'):
            for count, line in enumerate(open(os.path.join(root, file), "r", encoding="utf-8")):
                css_num += 1
        elif file.endswith('.js'):
            for count, line in enumerate(open(os.path.join(root, file), "r", encoding="utf-8")):
                css_num += 1
        else:
            pass
print(py_num, css_num, html_num, js_num)
