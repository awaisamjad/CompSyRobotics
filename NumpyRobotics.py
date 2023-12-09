from numpy import *

class NumpyRobotics:
    
    def __init__(self) -> None:
        pass
    
    #~ Transformation Matrix
    def transformation_matrix(self, rotation_matrix, translation_vector):
        rotation_matrix = vstack((rotation_matrix, [0,0,0]))
        translation_vector = vstack((translation_vector, [1]))
        return concatenate((rotation_matrix, translation_vector), axis=1)
    
    #~ Inverse Transformation Matrix
    def inverse_transformation_matrix(self, transformation_matrix):
        rotation_matrix = transformation_matrix[0:3, 0:3]
        translation_vector = transformation_matrix[0:3, 3]
        inverted_translation = -dot(rotation_matrix.T, translation_vector)
        bottom_row = array([0, 0, 0, 1])
        return vstack((hstack((rotation_matrix.T, inverted_translation[:, newaxis])),bottom_row))
    
r =  NumpyRobotics()
transformation_matrix = r.transformation_matrix([[1,2,3],[4,5,6],[7,8,9]], [[1],[2],[3]])

print(r.inverse_transformation_matrix(transformation_matrix))
