#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Franck Tujek
# DATE CREATED: 28/12/2023                                 
# REVISED DATE: 22/02/2024
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model within classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 
import os

# DONE 3: Define classify_images function below, specifically replace the None
#       below by the function definition of the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend method. Be sure to
    format the classifier labels so that they will match your pet image labels.
    The format will include putting the classifier labels in all lower case 
    letters and stripping the leading and trailing whitespace characters from them.
    Parameters: 
      images_dir (str): The full path to the folder of images to be classified.
      results_dic (dict): Results Dictionary with keys as image filenames and values
                          as lists. Lists contain pet image label at index 0.
                          New indexes, classifier label (1) and match indicator (2),
                          are added by this function.
      model (str): CNN model architecture to use for classification; 
                   should be one of 'resnet', 'alexnet', or 'vgg'.
    """
    # Loop through each image in the results dictionary
    for key in results_dic:
        # Build path to image
        image_path = os.path.join(images_dir, key)

        # Classify the image using the selected model
        model_label = classifier(image_path, model)

        # Format the classifier label
        model_label = model_label.lower().strip()

        # Check if the labels match
        truth = results_dic[key][0]
        found = False  # Flag to mark if any match is found
        for label in model_label.split(','):
            if truth == label.strip():  # Check if trimmed label matches the truth
                found = True
                break  # Break the loop if a match is found

        # Update the results dictionary with the classifier label and match status
        # Note: index 1 in the list will now be the classifier label, 
        #       index 2 in the list will be 1 if match else 0
        results_dic[key].extend([model_label, int(found)])
