# -*- coding : utf-8 -*-
# @author : Dell
# @time : 17:04   2019/7/14
# @filename : qrcode_generate.py


from MyQR import myqr
import os
import qrcode


def qrcode_genearte(teacher_name,course,classroom):
    qr = qrcode.QRCode(
        version=6,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data('http://127.0.0.1:8000/upload_sign/{}/{}/{}'.format(teacher_name,course,classroom))
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save('./qrcode1/static/img/'+course+'.png')
