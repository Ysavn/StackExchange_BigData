import os
import numpy as np
from ValidateAndClean import validateAndCleanBadges as VAC_Badges, validateAndCleanComments as VAC_Comments, \
    validateAndCleanUsers as VAC_Users

def validateAndClean(outputPath, inputPath):
    '''

    Validate necessary fields and clean duplicate rows for every required XML file,
    saving the result as numpy array

    :param outputPath:
    :param inputPath:
    :return:
    '''

    if not os.path.isdir(outputPath):
        os.makedirs(outputPath)

    validatedbadges = np.array(VAC_Badges.validate_badge(inputPath))
    np.save(outputPath + 'badges.npy', validatedbadges)
    
    validatedComments = np.array(VAC_Comments.validate_comment(inputPath))
    np.save(outputPath + 'Comments.npy', validatedComments)
    
    validated_user_with_Loc = np.array(VAC_Users.validate_user_loc(inputPath))
    np.save(outputPath + 'Users.npy', validated_user_with_Loc)

