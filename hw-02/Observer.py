from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

# Finish the new Observer class!
class Observer():
    '''
    This class creates an artificial night sky observer.
    '''
    
    # This function will get called automatically
    # when a new "observer" is created
    def __init__(self,im1_filename,im2_filename):
        '''
        When initializing the observer, the "red" image should be given
        as the first input argument and the "ir" image should be the second input
        '''
        self.im1_filename = im1_filename
        self.im2_filename = im2_filename
        self.load_images(im1_filename,im2_filename)
        
    def load_images(self,im1_filename,im2_filename):
        '''
        This function is incomplete! It is missing the appropriate input vales
        and the "pass" should be replaced with the appropriate code.
        Update this docstring to explain what the function does (or should do).
        '''
        self.red_data = fits.getdata(im1_filename, ext=0)
        self.ir_data = fits.getdata(im2_filename, ext=0)
    
    def make_composite(self):
        '''
        This function is incomplete! Make sure to finish it and
        then update this docstring to explain what the function does!
        '''
         # Define the array for storing RGB values
        rgb = np.zeros((data[R].shape[0],
                    data[R].shape[1],3))
    
        # Define a normalization factor for our denominator using the R filter image
        norm_factor = data[R].astype("float").max()
    
        # Compute the red channel values and then clip them to ensure nothing is > 1.0
        rgb[:,:,0] = 1.5 * (self.im2_data.astype("float")/norm_factor)
        rgb[:,:,0][rgb[:,:,0] > 1.0] = 1.0
        # Compute the green channel values and then clip them to ensure nothing is > 1.0
        rgb[:,:,1] = ((self.im2_data.astype("float")+self.im1_data.astype("float"))/2)/norm_factor
        rgb[:,:,1][rgb[:,:,1] > 1.0] = 1.0
        # Compute the blue channel values and then clip them to ensure nothing is > 1.0
        rgb[:,:,2] = (self.im1_data.astype("float")/norm_factor)
        rgb[:,:,2][rgb[:,:,2] > 1.0] = 1.0
    
        
    def calc_stats(self):
        '''
        This function gives the mean and standard deviation of the images
        '''
        #Finding the man
        print("The mean of", self.im1_filename , "is " , np.mean(self.red_data))
        print("The mean of", self.im2_filename, "is " , np.mean(self.ir_data))
        print("The standard deviation of", self.im1_filename, "is", np.std(self.red_data))
        print("The standard deviation of", self.im2_filename, "is", np.std(self.ir_data))