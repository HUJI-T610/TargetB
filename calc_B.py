
from points import Points
#from electromagnet import Electromagnet
import math

'''
Here we do our calculations of the necessary current I we need to get to
the wanted magnetic filed B.
'''
class Calc_B:
    def __init__(self, wanted_B, all_points, electromagnet_parameters):
        self.wanted_B = wanted_B # A scalar value in Tesla
        self.all_points = all_points # A Points type class, contains all the 4 points (coiles and medicine)
        self.electromagnet = electromagnet_parameters # A Electromagnet type class, contains all the information about the electromagnet
        self.mu_max = self.electromagnet.get_relative_permeability_max() # the constant that we multuply to uncrease B, because the magnetic core.
        
        
        self.mu_0 = 4 * math.pi * math.pow(10, -7)  # T*m/A
        self.maximum_I = 5 # Ampere, this is a const
        
        # data for coil 1 :
        self.I_needed1 = 1 # Ampere
        self.B_needed1 = 0 # Tesla
        # data for coil 2 :
        self.I_needed2 = 1 # Ampere
        self.B_needed2 = 0 # Tesla
    
    '''
    This function calculates the magnetic field in 1D axis at apoint x with
    a current of I in the loop.
    x = the distance from the center of the coil on the central axis.
    I = the current in the loop/
    '''
    def B_one_coil(self, x, I):
        # return self.mu_max * (self.mu_0*self.electromagnet.n*I*(self.electromagnet.R**2))/(2*(self.electromagnet.R**2 + x**2)**(3/2))
        
        eta = self.electromagnet.n / 4 # density.
        R = self.electromagnet.R
        const = self.mu_0 * eta * I * (R**2) / (2 * (R**2))
        part = lambda pos : (x + pos) / math.sqrt((x+pos)**2 + R**2)
        return const * (part(0.05) - part(0.01))
    
    
    '''
    Calculate the magnetic field and the current from the first coil.
    '''
    def calculate_B_and_I_coil1(self):
        I = 1 # Ampere
        x = self.all_points.get_distance(self.all_points.get_coil1_pair(), self.all_points.get_medicine1_pair())
        di = 0.1
        B = self.B_one_coil(x,I)
        while (B < self.wanted_B and I < self.maximum_I):
            I = I + di
            B = self.B_one_coil(x,I)
        self.I_needed1 = I
        self.B_needed1 = B
    
    '''
    Calculate the magnetic field and the current from the second coil.
    '''
    def calculate_B_and_I_coil2(self):
        I = 1 # Ampere
        x = self.all_points.get_distance(self.all_points.get_coil2_pair(), self.all_points.get_medicine2_pair())
        di = 0.1
        B = self.B_one_coil(x,I)
        while (B < self.wanted_B and I < self.maximum_I):
            I = I + di
            B = self.B_one_coil(x,I)
        self.I_needed2 = I
        self.B_needed2 = B

    '''
    Getter function, that returns the magnetic field from the first coil.
    '''
    def get_B_coil1(self):
        return self.B_needed1
    
    '''
    Getter function, that returns the cuurent field from the first coil.
    '''
    def get_I_coil1(self):
        return self.I_needed1

    '''
    Getter function, that returns the magnetic field from the second coil.
    '''
    def get_B_coil2(self):
        return self.B_needed2
    
    '''
    Getter function, that returns the current field from the second coil.
    '''
    def get_I_coil2(self):
        return self.I_needed2
