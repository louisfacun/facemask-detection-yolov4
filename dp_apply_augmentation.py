import albumentations as A
import cv2
import glob
import argparse
import os
from pathlib import Path


def parser():
    parser = argparse.ArgumentParser(description="Apply data augmentation using 'albumentations' library.")
    parser.add_argument("--input", type=str, default="sample_images/train/",
                        help="input folder of images to augment")
    parser.add_argument("--option", type=int, required=True,
                        help="augmentation option")
    return parser.parse_args()


def check_arguments_errors(args):
    """Check if input folder is existing and augmentation option is valid."""
    if not os.path.exists(args.input):
        raise(ValueError("Invalid input folder path {}".format(os.path.abspath(args.input))))
    assert 1 <= args.option <= 3, "Option should be a integer between 1 and 3"


def setup_augmentations(option):
    """
    Create objects of augmentation options using 'albumentations'.
    You can edit this if you want to try other augmentation options and values.
    
    The default values used in the augmentations options are from our research paper.
    
    Args:
        option: An int between 1-3 of augmentation option available.
        
    Returns:
        Albumentation object
    """
    augmentation = None
    if option == 1:
        augmentation = [A.HorizontalFlip(p=1.0)]
    elif option == 2:
        augmentation = [
            A.Rotate(always_apply=False, p=0.5, limit=(-15, 15), interpolation=0, border_mode=0, value=(0, 0, 0)),
            A.Blur(always_apply=False, p=1.0, blur_limit=(5, 7)),
            A.GaussNoise(always_apply=False, p=0.5, var_limit=(10.0, 50.0))
        ]
    elif option == 3:
        augmentation = [
            A.HorizontalFlip(p=1.0),
            A.Rotate(always_apply=False, p=0.5, limit=(-15, 15), interpolation=0, border_mode=0, value=(0, 0, 0)),
            A.Blur(always_apply=False, p=1.0, blur_limit=(5, 7)),
            A.GaussNoise(always_apply=False, p=0.5, var_limit=(10.0, 50.0))
        ]
    transform = A.Compose(augmentation, bbox_params=A.BboxParams(format='yolo'))
    
    return transform


def process_images(files, input_folder, option):
    """Process list of files and start the augmentations.
    
    Args:
        files: A list of file paths of the images.
        input_folder: A string containing the folder location of input images to augment.
        
    """
    number_of_file_processed = 0
    number_of_not_processed = 0
        
    for filepath in files:
        filename_with_ext    = os.path.basename(filepath)
        filename_without_ext = Path(filepath).stem
        
        image = cv2.imread(filepath)
        bboxes = []
        
        try: # Check first if the image has corresponding label file
            with open(input_folder + filename_without_ext + '.txt', 'r') as label_file:
                for line in label_file:
                    label, x, y, w, h = line.split()
                    bboxes.append([float(x), float(y), float(w), float(h), int(label)])
                    
                print("[Processing] " + filename_with_ext)
                transformed = transform(image=image, bboxes=bboxes) # Apply augmentation
                transformed_image = transformed['image']
                transformed_bboxes = transformed['bboxes']
                number_of_file_processed += 1
                
                if not os.path.exists(input_folder + "augmented"):
                    os.makedirs(input_folder + "augmented")
                    
                cv2.imwrite(input_folder + "augmented/aug-" + str(args.option) + "-" + filename_with_ext, transformed_image)
                
                with open(input_folder + "augmented/aug-" + str(args.option) + "-" + filename_without_ext + '.txt', 'a') as f:
                    for line in transformed_bboxes:
                        x = line[0]
                        y = line[1]
                        w = line[2]
                        h = line[3]
                        label = line[4]
                        #f.write("1\n")
                        f.write(str(label) + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h) + "\n")
        except FileNotFoundError:
            print("[Error] Label not found: " + filename_with_ext)   
            number_of_not_processed +=1
            
    output_folder = os.path.abspath(input_folder + "augmented")
    print_result(number_of_file_processed, number_of_not_processed, output_folder, option)
        
        
def print_result(number_of_file_processed, number_of_not_processed, output_folder, option):
    """ Print augmentation result """
    print("----------------------------------")
    print("Number of image processed:" , number_of_file_processed)
    print("Number of image not processed:" , number_of_not_processed)
    print("Output folder: ", output_folder)
    print("Augmentation option used: ", option)
    
    
def list_images(input_folder, ext):
    """TODO: List images based on input folder and file extensions"""
    pass
    
    
if __name__ == '__main__':
    args = parser()
    check_arguments_errors(args)
    transform = setup_augmentations(args.option)
    files = [filepath for filepath in glob.glob(args.input + "/*.jpg")]
    process_images(files, args.input, args.option)
