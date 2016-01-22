#!/usr/bin/python  
# -*- encoding: UTF-8 -*-  

import sys, os, time
import qrcode
from PIL import Image,ImageDraw,ImageFont

#----------------------------------------------------------------------

def gen_logo(version, mypath):
    """
	生成log图
	"""
    img = Image.new('L', (256, 256), 255)
    draw = ImageDraw.Draw(img)
    
    font = ImageFont.truetype(mypath + 'FZY4JW.TTF', 42)
    text = 'HotBlood'
    draw.text((25, 25), text, 100, font=font)
    
    font = ImageFont.truetype(mypath + 'FZY4JW.TTF', 27)
    text = 'Version:' + version
    draw.text((25, 160), text, 100, font=font)
    
    font = ImageFont.truetype(mypath + 'FZY4JW.TTF', 27)
    text = time.strftime("%Y-%m-%d %H:%M", time.localtime())
    draw.text((25, 200), text, 100, font=font)    
    
    img.save(mypath + 'logo.png')
        

def gen_qrcode(string, mypath):  
    """ 
    生成中间带logo的二维码 
    需要安装qrcode, PIL库 
 
    :param string: 二维码字符串 
    :param path: 生成的二维码保存路径
    :param logo: logo文件路径 
    :return: 
    """  
    qr = qrcode.QRCode(  
        version=2,  
        error_correction=qrcode.constants.ERROR_CORRECT_H,  
        box_size=10,  
        border=1  
    )  
    qr.add_data(string)  
    qr.make(fit=True)  
  
    img = qr.make_image()  
    img = img.convert("RGBA")  
  
    if os.path.exists(mypath + 'logo.png'):  
        icon = Image.open(mypath + 'logo.png')  
        img_w, img_h = img.size  
        factor = 4  
        size_w = int(img_w / factor)  
        size_h = int(img_h / factor)  
  
        icon_w, icon_h = icon.size  
        if icon_w > size_w:  
            icon_w = size_w  
        if icon_h > size_h:  
            icon_h = size_h  
        icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)  
  
        w = int((img_w - icon_w) / 2)  
        h = int((img_h - icon_h) / 2)  
        icon = icon.convert("RGBA")  
        img.paste(icon, (w, h), icon)
        
    img.save(mypath + 'qr.png')  
  
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "No channel and version specified."
        sys.exit(-1)
        
    mypath = os.path.split(os.path.realpath(__file__))[0] + '/'
    
    gen_logo(sys.argv[2], mypath)
    gen_qrcode("https://family.123u.com/sites/default/files/gameapk/jieji/index.php?c=" + sys.argv[1] + "&v=" + sys.argv[2], mypath)
    
    print "Check " + mypath + "qr.png"

    