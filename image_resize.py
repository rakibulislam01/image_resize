import cv2
from datetime import datetime
import tkinter


def image_resize(src, img_height, img_weight):
    # set a new height in pixels
    d_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    height = img_height
    weight = img_weight

    dsize = (height, weight)

    output = cv2.resize(src, dsize, interpolation=cv2.INTER_AREA)
    nam_loc = 'test/'+d_time+'_'+str(height)+'_'+str(weight)+'.png'
    cv2.imwrite(nam_loc, output)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    src = cv2.imread('python_1.png', cv2.IMREAD_UNCHANGED)
    total_logo = int(input("Input total logo number: "))

    for _ in range(total_logo):
        height, weight = input().split(" ")
        image_resize(src, int(height), int(weight))
