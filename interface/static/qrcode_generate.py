# -*- coding : utf-8 -*-
# @author : Dell
# @time : 17:04   2019/7/14
# @filename : qrcode_generate.py



import qrcode
qr = qrcode.QRCode(
                    version=10,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                   )#  version是二维码的尺寸，数字大小决定二维码的密度
                    # error_correction：是指误差
                    # box_size:参数用来控制二维码的每个单元(box)格有多少像素点
                    # border: 参数用控制每条边有多少个单元格(默认值是4，这是规格的最小值
qr.add_data('https://github.com')#添加信息， 跳转至二维码页面（未写）
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save('qrcode.png')#保存二维码
