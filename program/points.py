
import numpy as np

'''
Here we used the model of two circles : little one for the disease and a bigger one for the body.
We will have 4 points in one line. 2 points on the body and 2 on the disease (2 points on each circle).
This is the model as Rephal said.
'''
class Points:
    def __init__(self, coil1_pair, medicine1_pair, coil2_pair, medicine2_pair, ratio):
        self.coil1_pair = coil1_pair # x,y cordinate of center of coil 1
        self.medicine1_pair = medicine1_pair # x,y cordinate of center of medicine 1 the close to coil 1
        self.coil2_pair = coil2_pair # x,y cordinate of center of coil 2
        self.medicine2_pair = medicine2_pair # x,y cordinate of center of medicine 1 the close to coil 2
        self.ratio = ratio # the ration between a distance in the image to a distance in the real word.
    
    '''
    This function returns the medicine cordinate in a "world" where the coil is in (0,0) that is the center.
    So we need to update the cordinates of the medicine, so we could do the calculations.
    If the cacluculation becomes very complicated then this can make the calculation less havey because we do
    need to add the cordinates of the center of the coil (each time if we are in a loop or integral).
    '''
    def get_medicine_pair_effective(self, coil_number):
        medicine_pair = [0,0]
        coil_pair = [0,0]
        
        if coil_number == 1:
            medicine_pair = self.medicine1_pair
            coil_pair = self.coil1_pair
        elif coil_number == 2:
            medicine_pair = self.medicine2_pair
            coil_pair = self.coil2_pair
        
        return np.array([medicine_pair[0] - coil_pair[0], medicine_pair[1] - coil_pair[1]])
    
    '''
    return the distance between coil and medicine.
    '''
    def get_distance(self, coil_pair, medicine_pair):
        distance_on_map = np.sqrt( (coil_pair[0]-medicine_pair[0])**2 + (coil_pair[1]-medicine_pair[1])**2 )
        print('xas', self.ratio * distance_on_map, 'xas')
        return self.ratio * distance_on_map
    
    '''
    Simple Getter's and Setter's functions :
    '''
    def get_coil1_pair(self):
        return self.coil1_pair
    
    def set_coil1_pair(self, coil1_pair):
        self.coil1_pair = coil1_pair
        
    def get_coil2_pair(self):
        return self.coil2_pair
    
    def set_coil2_pair(self, coil2_pair):
        self.coil2_pair = coil2_pair
        
    def get_medicine1_pair(self):
        return self.medicine1_pair
    
    def set_medicine1_pair(self, medicine1_pair):
        self.medicine1_pair = medicine1_pair
        
    def get_medicine2_pair(self):
        return self.medicine1_pair
    
    def set_medicine2_pair(self, medicine2_pair):
        self.medicine2_pair = medicine2_pair
