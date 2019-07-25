from datetime import datetime
import cv2


def image_resize(src, img_height, img_weight):
    # set a new height in pixels
    d_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    height = img_height
    weight = img_weight

    dsize = (height, weight)

    output = cv2.resize(src, dsize, interpolation=cv2.INTER_AREA)
    nam_loc = 'test/' + d_time + '_' + str(height) + '_' + str(weight) + '.png'
    cv2.imwrite(nam_loc, output)
    cv2.destroyAllWindows()


def image_location(img_src, total_h_W):
    src = cv2.imread(img_src, cv2.IMREAD_UNCHANGED)
    i = 0
    j = 1
    for _ in range(5):
        image_resize(src, int(total_h_W[i]), int(total_h_W[j]))
        i = i + 2
        j = j + 2
