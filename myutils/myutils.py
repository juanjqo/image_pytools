from PIL import Image
import glob, os
import re


def convert_rgb_to_gray(input_format, output_format, origin_folder, destination_folder):
    print('Converting' + input_format + 'images to grayscale' + output_format + 'images...')
    print("Origin folder: ", origin_folder)
    print("Destination folder: ", destination_folder)
    i = 0
    os.chdir(origin_folder)
    format = "*."+input_format
    for file in glob.glob(format): #glob.glob("*.png"):
        i = i + 1
        im = Image.open(file)
        rgb_im = im.convert('L')
        rgb_im.save(destination_folder + '/' + file[:-3] + output_format)

def convert_png_rgb_to_jpg_gray(origin_folder, destination_folder):
    convert_rgb_to_gray("png", "jpg", origin_folder, destination_folder)

def convert_jpg_rgb_to_jpg_gray(origin_folder, destination_folder):
    convert_rgb_to_gray("jpg", "jpg", origin_folder, destination_folder)

def convert_labeled_images_to_masks(origin_folder, destination_folder):
    print('Converting labeled images to masks images...')
    print("Origin folder: ", origin_folder)
    print("Destination folder: ", destination_folder)
    print(origin_folder)
    os.chdir(origin_folder)
    # basename(path)
    i = 0

    for file in glob.glob("*.png"):
        i = i + 1

        #os.rename(file, origin_folder + '/rgb_' + str(i) + '_mask.png')
    threshold = 50
    for file in glob.glob("*.png"):
        i = i + 1
        rgb_im = Image.open(file)
        rgb_im = rgb_im.convert('L')  # 'RGBA'  #'L'
        rgb_im = rgb_im.point(lambda p: 255 if p > threshold else 0)
        rgb_im = rgb_im.convert('1')  # 'RGBA'  #'L'


        #m = re.search('semantic_segmentation(.+?).png', file)
        #found = m.group(1)
        #new_file = 'rgb' + found + '_mask.png'
        rgb_im.save(destination_folder + '/' + file)


def resize_images(origin_folder, destination_folder, input_format, w=512, h=512):
    print('Resizing images...')
    print("Origin folder: ", origin_folder)
    print("Destination folder: ", destination_folder)
    i = 0
    os.chdir(origin_folder)
    format = "*."+input_format
    for file in glob.glob(format): #glob.glob("*.png"):
        i = i + 1
        im = Image.open(file)
        im = im.resize((w, h))
        im.save(destination_folder + '/' + file)



def prepare_dataset(origin_folder, destination_folder):
    #destination_folder_rgb = destination_folder + "/data/imgs"
    #destination_folder_msk = destination_folder + "/data/masks"

    destination_folder_rgb = destination_folder + "/data/imgs"
    if not os.path.exists(destination_folder_rgb):
        os.makedirs(destination_folder_rgb)

    destination_folder_msk = destination_folder + "/data/masks"
    if not os.path.exists(destination_folder_msk):
        os.makedirs(destination_folder_msk)

    data_folder = destination_folder + "/data"

    convert_jpg_rgb_to_jpg_gray(origin_folder, data_folder)
    resize_images(data_folder, data_folder, "jpg")

    convert_labeled_images_to_masks(origin_folder,data_folder)
    resize_images(data_folder, data_folder, "png")

    i = 0
    os.chdir(data_folder)
    for file in glob.glob("*.jpg"):
        i = i + 1
        im = Image.open(file)
        m = re.search('(.+?).jpg', file)
        found = m.group(1)
        ch = len(found)-1
        
        im.save(destination_folder_rgb + "/" + "rgb_" + str(i)+".jpg")
        im = Image.open(file[:-3] + "png")
        im.save(destination_folder_msk + "/" + "rgb_" + str(i) + "_mask.png")



        #print(len(found))
    #im.save(destination_folder_rgb + file[:-3] + "jpg")






