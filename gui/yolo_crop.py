import os
import cv2
from PIL import Image
import numpy as np

class YoloCrop:
    def __init__(self, input_path=None, output_path=None):
        self.input_path = input_path
        self.output_path = output_path

    def setpath(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        # Ensure the output path exists
        if not os.path.exists(output_path):
            os.makedirs(output_path)

    def get_img_shape(self, path):
        img = cv2.imread(path)
        try:
            return img.shape
        except AttributeError:
            print('error! ', path)
            return (None, None, None)

    def findlinenum(self, line):  # find class id
        if line == '':
            return ' '
        return line[0]

    def openfile(self, tag_name, img_name):  # file load and processing
        openpath_tag = os.path.join(self.input_path, tag_name)
        openpath_img = os.path.join(self.input_path, img_name)

        pure_image_name = os.path.splitext(img_name)[0]
        pure_txt_name = os.path.splitext(tag_name)[0]
        img_extension = os.path.splitext(img_name)[1]  # Get the file extension

        with open(openpath_tag, 'r') as f:
            i = 0
            while True:
                line = f.readline()
                if not line:
                    break
                classnum = self.findlinenum(line)
                print('input image : ' + openpath_img)

                if classnum == '1':  # classnum이 1일 때만 작업 수행
                    # load original coordinates
                    try:
                        ox = float(line[2:10])  # yolov3 transformed point of middle of x
                        oy = float(line[11:19])  # yolov3 transformed point of middle of y
                        ow = float(line[20:28])  # yolov3 transformed point of width
                        oh = float(line[29:38])  # yolov3 transformed point of height
                    except ValueError:
                        print(f'Error parsing line: {line}')
                        continue

                    # load original image information
                    img = Image.open(openpath_img)
                    w_tot, h_tot = img.size

                    # inverse transform
                    x = ox * w_tot
                    y = oy * h_tot
                    w = ow * w_tot
                    h = oh * h_tot

                    # calculate inverse roi coordinates
                    x_max = int(((2 * x) + w) / 2.0)
                    x_min = int(x_max - w)
                    y_max = int(((2 * y) + h) / 2.0)
                    y_min = int(y_max - h)

                    # Cropping
                    crop_img = img.crop((x_min, y_min, x_max, y_max))

                    # convert PIL format to OpenCV format
                    opencv_crop = np.array(crop_img)
                    opencv_crop = opencv_crop[:, :, ::-1].copy()

                    # save images
                    savepath = os.path.join(self.output_path, f'{pure_image_name}{img_extension}')
                    i += 1
                    print('saved : ' + savepath + '\n')
                    cv2.imwrite(savepath, opencv_crop)

    def sorting(self, l1, l2):
        if l1 > l2:
            lmax, lmin = l1, l2
            return lmax, lmin
        else:
            lmax, lmin = l2, l1
            return lmax, lmin


if __name__ == '__main__':
    yolo_crop = YoloCrop()
    yolo_crop.setpath('data/eraser', 'data/good_crop')

    listofall = os.listdir(yolo_crop.input_path)
    listofjpg = [file for file in listofall if file.lower().endswith((".jpg", ".png"))]
    listoftag = [file for file in listofall if file.lower().endswith(".txt")]

    for img_file in listofjpg:
        corresponding_txt_file = os.path.splitext(img_file)[0] + '.txt'
        if corresponding_txt_file in listoftag:
            yolo_crop.openfile(corresponding_txt_file, img_file)
