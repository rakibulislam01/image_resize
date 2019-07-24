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


# if __name__ == '__main__':
def image_location(img_src, height, weight):
    src = cv2.imread(img_src, cv2.IMREAD_UNCHANGED)
    # total_logo = int(input("Input total logo number: "))

    # for _ in range(total_logo):
    #     height, weight = input().split(" ")
    #     image_resize(src, int(height), int(weight))
    image_resize(src, int(height), int(weight))
