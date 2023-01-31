"""
İBRAHİM TUNÇ
30.01.2023
"""

import cv2

location = "qr_codes\\"

def qr_Reader(img):
    
    try:
        reader = cv2.imread(img)
        detector = cv2.QRCodeDetector()
        data,bbox,straight_Code = detector.detectAndDecode(reader)
        print(data)
        return data
    except Exception as E:
        print(E)
        print("QR READER FAILED !")


