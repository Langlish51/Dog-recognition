#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Franck Tujek
# DATE CREATED: 28/12/2023
# REVISED DATE: 22/02/2024
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# DONE 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
def print_results(results_dic, results_stats_dic, model, print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Function to print the results of the classification.
    """
    # Calculates % correct not-a-dog images
    # Uses conditional statement for when no 'not a dog' images were submitted 
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] /
                                                results_stats_dic['n_notdogs_img']) * 100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0

    # TODO: Calculate percentage of correctly matched images
    results_stats_dic['pct_match'] = (results_stats_dic['n_match'] / results_stats_dic['n_images']) * 100

    print("\n\n*** Results Summary for CNN Model Architecture", model.upper(), "***")
    print("{:20}: {:3d}".format('N Images', results_stats_dic['n_images']))
    print("{:20}: {:3d}".format('N Dog Images', results_stats_dic['n_dogs_img']))
    print("{:20}: {:3d}".format('N Not-Dog Images', results_stats_dic['n_notdogs_img']))

    # Prints summary percentages based on the user's input
    for key in ["pct_match", "pct_correct_dogs", "pct_correct_notdogs", "pct_correct_breed"]:
        if key in results_stats_dic:
            print("{:20}: {:.2f}%".format(key, results_stats_dic[key]))

    # If user set print_incorrect_dogs to True and there were incorrect dog matches
    if print_incorrect_dogs and (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'] != results_stats_dic['n_images']):
        print("\nIncorrect Dog/Not Dog Classifications:")
        
        for key in results_dic:
            # Incorrectly classified as dog/not-a-dog
            if sum(results_dic[key][3:]) == 1:
                print("Image: {:>20}  True: {:>20}  Classifier: {:>20}".format(key, results_dic[key][0], results_dic[key][1]))

    # If user set print_incorrect_breed to True and there were incorrect breed matches
    if print_incorrect_breed and (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']):
        print("\nIncorrect Breed Classifications:")
        
        for key in results_dic:
            # Correctly identified as dogs, but incorrectly classified breeds
            if results_dic[key][3] == 1 and results_dic[key][4] == 1 and results_dic[key][2] == 0:
                print("Image: {:>20}  True: {:>20}  Classifier: {:>20}".format(key, results_dic[key][0], results_dic[key][1]))
