
import math
import numpy as np

'''
Here we convert each group of points that represenrs an object\area in the human body and from this
will find the the axis\line that where we will place the electromagnets, that is to fund the minimal path
from the side to the cancer and that is pass close to the center of the cancer.
'''
class draws_to_points:
    def __init__(self, three_point_CT):
        self.side_one = np.array(three_point_CT[2])
        self.cancer = np.array(three_point_CT[0])
        self.side_two = np.array(three_point_CT[1])
        
        # define vectors 
        self.define_vectors()
        # center of mass of cancer = A
        self.center_cancer = self.center_of_mass(self.c_x, self.c_y, self.len_c)
        # minimum distance between A and each side
        min_index_side_one, min_distance_side_one = self.point_to_minimum_distance(self.center_cancer, self.a_x, self.a_y)
        min_index_side_two, min_distance_side_two = self.point_to_minimum_distance(self.center_cancer, self.b_x, self.b_y)
        # chose minimal distance and continue the line to find the point on the other side
        if (min_distance_side_one >= min_distance_side_two):
            self.point_min_line_side1 = np.array([self.a_x.T[min_index_side_one], self.a_y.T[min_index_side_one]])
            second_vecotr_x = self.b_x
            second_vecotr_y = self.b_y
        else:
            self.point_min_line_side1 = np.array([self.b_x.T[min_index_side_two], self.b_y.T[min_index_side_two]])
            second_vecotr_x = self.a_x
            second_vecotr_y = self.a_y
        index_other_side = self.find_point_on_line_and_side(self.point_min_line_side1, self.center_cancer, second_vecotr_x, second_vecotr_y)
        self.point_min_line_side2 = np.array([second_vecotr_x.T[index_other_side], second_vecotr_y.T[index_other_side]])
        
        
        
    '''
    This function initial all variables and turns the data to numpay vector form.
    '''    
    def define_vectors(self):
        X = 0
        Y = 1
        a = self.side_one
        b = self.side_two
        c = self.cancer
        
        self.len_a = len(a)
        self.len_b = len(b)
        self.len_c = len(c)
        
        self.a_x = a.T[X].reshape((1,self.len_a))
        self.a_y = a.T[Y].reshape((1,self.len_a))
        self.b_x = b.T[X].reshape((1,self.len_b))
        self.b_y = b.T[Y].reshape((1,self.len_b))
        self.c_x = c.T[X].reshape((1,self.len_c))
        self.c_y = c.T[Y].reshape((1,self.len_c))

    '''
    This function find the center of mass of a vector.
    vector_x = the x cordinate of the vector.
    vector_y = the y cordinate of the vector.
    vector_len = the length of the vector.
    return = center , it is [[number], [number]] in numpy form.
    '''
    def center_of_mass(self, vector_x, vector_y, vector_len):
        center = np.array([np.sum(vector_x, axis=1), np.sum(vector_y, axis=1)]) / vector_len
        return center
    
    '''
    This function find the minimal distamce between a point (calles here center) and a vector, also finds
    the index in the vector to indecate the other point the make the minimal distance with the given point.
    center = a point.
    vector_x = the x cordinate of the vector.
    vector_y = the y cordinate of the vector.
    vector_len = the length of the vector.
    return = index = the index in the vector to indecate the other point the make the minimal distance with the given point.
             distance = minimal distance
    '''
    def point_to_minimum_distance(self, center, vector_x, vector_y):
        X = 0
        Y = 1
        distance = np.sqrt( (vector_x - center[X])**2 + (vector_y - center[Y])**2 )
        index = np.argmin(distance)
        return index, np.min(distance)
    
    '''
    Find the two variables the make the linear equation.
    point1 = a numpy vector that represent the first point.
    point2 = a numpy vector that represent the second point.
    return = m = slope
             n = constant
    '''
    def find_linear_equation(self, point1, point2):
        X = 0
        Y = 1
        # y = m*x + n
        m = (point1[Y] - point2[Y]) / (point1[X] - point2[X])
        n = point1[Y] - (m * point1[X])
        return m, n
    
    '''
    find the point the is in the linear equation and on the side, that is the point of the cross between the two lines.
    point1 = a numpy vector that represent the first point.
    point2 = a numpy vector that represent the second point.
    second_vecotr_x = a numpy vector of x values, here the vector is the second side.
    second_vecotr_y = a numpy vector of y values, here the vector is the second side.
    return = point_closest_index = the point where the linear equation (a line from side one throgh the center of the cancer)
             cross the other side.
    '''
    def find_point_on_line_and_side(self, point1, point2, second_vecotr_x, second_vecotr_y):
        m, n = self.find_linear_equation(point1, point2)
        on_line_y = m * second_vecotr_x + n
        difference = np.abs(on_line_y - second_vecotr_y)
        point_closest_index = np.argmin(difference)
        return point_closest_index
    
    '''
    getter function.
    return the two points the will form the minimal line that will be the axis of the electromagnets, and the point of the cancer (2 points ?).
    '''
    def get_points_from_image(self):        
        # TODO: find 2 points on the circle cancer and on the linear eqaution,
        # then to give the doctor the option to chose the point from the two
        # points, where he want to inject the material.
        return [self.point_min_line_side1, self.point_min_line_side2, self.center_cancer, self.center_cancer]
