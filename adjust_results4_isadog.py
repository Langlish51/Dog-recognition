#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Franck Tujek
# DATE CREATED: 28/12/2023                             
# REVISED DATE: 22/02/2024
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the 
#          dog name (from dognames.txt) and the 'value' is one. If a label is 
#          found to exist within this dictionary of dog names then the label 
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one 
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog. 
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the 
#           label isn't a dog.
#
##
# DONE 4: Define adjust_results4_isadog function below, specifically replace the None
#       below by the function definition of the adjust_results4_isadog function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    """
    # Initialise a dictionary to hold dog names
    dog_names_dic = {}

    # Read the dog names file and populate the dog_names_dic
    with open(dogfile, 'r') as f:
        for line in f:
            dog_name = line.strip()
            if dog_name not in dog_names_dic:
                dog_names_dic[dog_name] = 1

    # Loop through the results dictionary
    for key in results_dic:
        # Check if pet label is a dog
        if results_dic[key][0] in dog_names_dic:
            pet_label_is_dog = 1
        else:
            pet_label_is_dog = 0

        # Check if classifier label is a dog
        classifier_label_is_dog = 0
        for label in results_dic[key][1].split(","):
            if label.strip() in dog_names_dic:
                classifier_label_is_dog = 1
                break  # Break as soon as we find one matching dog name

        # Update the results dictionary with the new information
        results_dic[key].extend([pet_label_is_dog, classifier_label_is_dog])