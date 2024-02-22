#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Franck Tujek
# DATE CREATED: 28/12/2023                                  
# REVISED DATE: 22/02/2024
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0: pet image label (string).
#
##
# Imports python modules
import os

# DONE 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Create an empty dictionary for the results
    results_dic = {}

    # Retrieve the files from the given directory
    file_list = os.listdir(image_dir)

    # Go through the files
    for filename in file_list:
        # Skip files starting with . (hidden files)
        if filename.startswith('.'):
            continue

        # Create a pet label from the filename
        pet_label = os.path.splitext(filename)[0].replace('_', ' ').lower().strip()

        # Add the filename and the pet label to the results dictionary
        # Only add if the filename doesn't already exist in the dictionary
        if filename not in results_dic:
            results_dic[filename] = [pet_label]
        else:
            print(f"Warning: Duplicate file name {filename} found.")

    # Return the results dictionary
    return results_dic
