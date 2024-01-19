
from myutils.myutils import*


origin_folder = r'C:\Users\camiq\Documents\project_x\image_pytools\raw_input'
destination_folder = r'C:\Users\camiq\Documents\project_x\image_pytools\output'



#convert_jpg_rgb_to_jpg_gray(origin_folder, destination_folder)
#resize_images(destination_folder, destination_folder, "jpg")

prepare_dataset(origin_folder, destination_folder)

#origin_folder_msk = r'C:\Users\camiq\Documents\project_x\image_pytools\raw_input\aisladores_p1\buen_estado\segmented_buenas'

#convert_labeled_images_to_masks(origin_folder_msk, destination_folder)