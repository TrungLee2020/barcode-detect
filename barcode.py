from zxing import BarCodeReader
import requests, json
import re
from pyzbar.pyzbar import decode
from PIL import Image

def get_barcode(image):
    barcode = info = None
    img_raw = Image.open(image)
    decoded = decode(img_raw)
    
    if decoded:
        try:
            barcode = int(re.findall("[+-]?[0-9][0-9]*|0$",
                                    str(decoded[0].data))[0]) 
            info = _get_product_info(barcode)
        except:
            pass  
    return barcode, info

def _get_product_info(barcode):
    """ Query a product by the barcode number the openFoodFact DB trought API"""
    address = "https://world.openfoodfacts.org/api/v0/product/{}.json".format(barcode)
    r = requests.get(address)
    return json.loads(r.text)

def scan_barcode(image_path):
    # Tạo một đối tượng BarCodeReader
    reader = BarCodeReader()
    # Quét mã vạch từ hình ảnh
    barcode = reader.decode(image_path)
    # Kiểm tra xem mã vạch có được quét thành công không
    if barcode:
        # Trả về thông tin mã vạch
        return barcode.format, barcode.text
    else:
        # Trả về None nếu không tìm thấy mã vạch hoặc không thể giải mã
        return None, None