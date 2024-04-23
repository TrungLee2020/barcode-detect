from barcode import get_barcode
from model.tiny_yolo import TinyYolo

def main():
    
    image_file = "path/image.img"
    # model = Tinyyolo()
        if image_file is not None:
        # imageText = st.empty()
        # imageLocation = st.empty()
        # imageText.text("Image uploaded")
        # imageLocation.image(image_file)
            image_predicted = model.predict(image_file)
        if image_predicted is not None:
            barcode, info = get_barcode(image_file)
            
            if barcode is not None:
                print(f"Barcode : {barcode}")
            else:
                print(f"Cannot read barcode")
            print("Product info")
            if info and info.get("status"):
                print(info)
            else:
                print("Product not found")
                
if __name__ == '__main__':
    main()