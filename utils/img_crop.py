from PIL import Image
import os
import scipy.io as scio
import numpy as np

file_url = './data_orig/crop.txt'
file_save_dir = '../dataset/imgs'
file_mat_dir = './data_orig/images_tracker'

def crop():
    img_box_dict = dict()
    with open(file_url, 'r') as f:
        lines = f.readlines()
        for line in lines:
            name, y_start, y_end, x_start, x_end = map(lambda x: x.strip(), line.split())
            # the left, upper, right, and lower pixel coordinate
            img_box_dict[name.split('.')[0]] = map(lambda x:int(x), (x_start, y_start, x_end, y_end))
    for filename in os.listdir(file_save_dir):
        if "_raw" in filename:
            name =  filename.split('.')[0].split('_')[0]
            if not img_box_dict.has_key(name):
                continue
            file_save_name = os.path.join(file_save_dir, name + '_crop.jpg')
            if os.path.isfile(file_save_name):
                continue
            try:
                img = Image.open(os.path.join(file_save_dir, filename))
                img.crop(img_box_dict[name]).save(file_save_name)
            except:
                print "error:", filename

    print "all done"



if __name__ == '__main__':
    # crop()
    data = scio.loadmat(os.path.join(file_mat_dir, "00001.mat"))
    print len(data['tracker'][0])


# w, h = 512, 512
# data = np.zeros((h, w, 3), dtype=np.uint8)
# data[256, 256] = [255, 0, 0]
# img = Image.fromarray(data, 'RGB')
# img.save('my.png')
# img.show()