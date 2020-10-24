

'''
This class contains basic proparties of the electromagnet.
This class is made for more simple swappings of electromagents models via
database in the future.
'''
class Electromagnet:
    def __init__(self, n=180, R=0.04, relative_permeability_max=10**5):
        # Coil parmeters :
        self.n = n # number of windings
        self.R = R # radius in meter
        # https://en.wikipedia.org/wiki/Permeability_(electromagnetism)
        self.relative_permeability_max = relative_permeability_max
    
    '''
    This function copys the data/parmeters of the electromagenet that is given
    to this elctromagnets. 
    '''
    def copy_electromagnet(self, electromagnet):
        self.set_R(electromagnet.get_R())
        self.set_n(electromagnet.get_n())
        self.set_relative_permeability_max(electromagnet.get_relative_permeability_max())
    
    '''
    Getter function, returns the number of round of the coil in the 
    electromagnet.
    '''
    def get_n(self):
        return self.n
    
    '''
    Setter function, sets the number of round of the coil in the electromagnet.
    '''
    def set_n(self, n):
        self.n = n
        
    '''
    Getter function, returns the radius of the coil in the electromagnet.
    '''
    def get_R(self):
        return self.R
    
    '''
    Setter function, sets the radius of the coil in the electromagnet.
    '''
    def set_R(self, R):
        self.R = R
        
    '''
    Getter function, returns the 'elative permeability max' of the magnetic
    core that is in the electromagnet.
    '''
    def get_relative_permeability_max(self):
        return self.relative_permeability_max
    
    '''
    Setter function, sets the 'elative permeability max' of the magnetic
    core that is in the electromagnet.
    '''
    def set_relative_permeability_max(self, relative_permeability_max):
        self.relative_permeability_max = relative_permeability_max


'''
This class represents the data about the system that can be changed by the
user in the settings.
'''
class Data:
    def __init__(self, ratio=-1, electromagnet=None):
        self.ratio = ratio
        self.electromagnet = electromagnet
        
        # defult parameters :
        if ratio == -1:
            self.ratio = 0.5 / 500
            self.electromagnet = Electromagnet(180, 0.04, 10**5)
    
    '''
    Getter function, returns the ration of the image size to real size of 
    objects in the world.
    '''
    def get_ratio(self):
        return self.ratio
    
    '''
    Setter function, sets the the ration of the image size to real size of 
    objects in the world.
    '''
    def set_ratio(self, ratio):
        self.ratio = ratio
        
    '''
    Getter function, returns the electromagnet parameters.
    '''
    def get_electromagnet(self):
        return self.electromagnet
    
    '''
    Setter function, sets the electromagnet parameters.
    This is a deep copy and not shalow copy.
    '''
    def set_electromagnet(self, electromagnet):
        self.electromagnet = Electromagnet()
        self.electromagnet = copy_electromagnet(electromagnet)
    
