import os
import cv2
from PIL import Image
import numpy

class YoloCrop:
    def __init__(self, input_path=None, output_path=None):
        self.input_path = input_path
        self.output_path = output_path

    def setpath(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def get_img_shape(self, path):
        img = cv2.imread(path)
        try:
            return img.shape
        except AttributeError:
            print('error! ', path)
            return (None, None, None)

    def findlinenum(self, line): #find class id 
        if line == '':
            return ' '
        return line[0]  
    
    def openfile(self, tag_name, jpg_name): #file load and processing
        openpath_tag = os.path.join(self.input_path, tag_name)
        openpath_jpg = os.path.join(self.input_path, jpg_name)

        pure_image_name = os.path.splitext(jpg_name)
        pure_txt_name = os.path.splitext(tag_name)

        f = open(openpath_tag,'r')
        i = 0
        while True:
            if pure_txt_name != pure_txt_name : continue
                
            line = f.readline()
            if not line: break
            classnum = self.findlinenum(line)
            print('input image : ' + openpath_jpg)
        
            if classnum == '1': # classnum이 1일 때만 작업 수행
                #load original coordinates
                ox=float(line[2:10]) #yolov3 transformed point of middle of x
                oy=float(line[11:19]) #ylolv3 transformed point of middle of y
                ow=float(line[20:28]) #yolov3 transformed point of width
                oh=float(line[29:38]) #yolov3transformed point of height

                #load original image imformation
                img = Image.open(openpath_jpg)
                w_tot,h_tot = img.size

                #inverse transform
                x = ox*w_tot
                y = oy*h_tot
                w = ow*w_tot
                h = oh*h_tot

                #calculate inverse roi coordinates
                x_max = int(((2*x)+w)/2.0)
                x_min = int(x_max - w)
                y_max = int(((2*y)+h)/2.0)
                y_min = int(y_max - h)

                #Cropping
                crop_img = img.crop((x_min, y_min, x_max, y_max))
                
                #convert pil format to opencv format
                opencv_crop = numpy.array(crop_img)
                opencv_crop = opencv_crop[:, :, ::-1].copy()
                
                #save images
                new_path = os.path.splitext(jpg_name)
                
                savepath = os.path.join(self.output_path, f'{classnum}_{new_path[0]}_{i}.jpg')
                i = i + 1
                print('saved : ' + savepath + '\n')
                cv2.imwrite(savepath, opencv_crop)

        f.close

    def sorting(self, l1, l2):
        if l1 > l2:
            lmax, lmin = l1, l2
            return lmax, lmin
        else:
            lmax, lmin = l2, l1
            return lmax, lmin

if __name__ == '__main__':
    yolo_crop = YoloCrop()
    yolo_crop.setpath('data\eraser', 'data\good_crop')

    listofall = os.listdir(yolo_crop.input_path)
    listofjpg = [file for file in listofall if file.endswith(".jpg") or file.endswith(".JPG")]
    listoftag = [file for file in listofall if file.endswith(".txt") or file.endswith(".TXT")]

    for i in range(len(listofjpg)):
        yolo_crop.openfile(listoftag[i], listofjpg[i])
