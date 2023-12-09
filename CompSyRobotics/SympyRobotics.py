from sympy import Matrix, pprint, cos, sin, symbols, pi, simplify

class SympyRobotics:
    def __init__(self):
        pass
    
    def transformation_matrix(self, rotation_matrix, position_vector):
        matrix =  Matrix([
            [rotation_matrix[0], rotation_matrix[1], rotation_matrix[2], position_vector[0]],
            [rotation_matrix[3], rotation_matrix[4], rotation_matrix[5], position_vector[1]],
            [rotation_matrix[6], rotation_matrix[7], rotation_matrix[8], position_vector[2]],
            [0, 0, 0, 1],
        ])

        return matrix
    
    def inverse_transformation_matrix(self, Transformation_Matrix, Steps_to_answer=False):
        self.r11 = Transformation_Matrix[0]
        self.r12 = Transformation_Matrix[1]
        self.r13 = Transformation_Matrix[2]
        self.px =  Transformation_Matrix[3]
        self.r21 = Transformation_Matrix[4]
        self.r22 = Transformation_Matrix[5]
        self.r23 = Transformation_Matrix[6]
        self.py =  Transformation_Matrix[7]
        self.r31 = Transformation_Matrix[8]
        self.r32 = Transformation_Matrix[9]
        self.r33 = Transformation_Matrix[10]
        self.pz =  Transformation_Matrix[11]
        
        self.px_new = -((self.px * self.r11) + (self.py * self.r21) + (self.pz * self.r31))
        self.py_new = -((self.px * self.r12) + (self.py * self.r22) + (self.pz * self.r32))
        self.pz_new = -((self.px * self.r13) + (self.py * self.r23) + (self.pz * self.r33))
        
        inverse_transformation_matrix = Matrix([[self.r11, self.r21, self.r31, self.px_new], 
                                                [self.r12, self.r22, self.r32, self.py_new],
                                                [self.r13, self.r23, self.r33, self.pz_new],
                                                [0, 0, 0, 1]])
        
        if Steps_to_answer:
            print("This is the general transformation matrix \n")
            pprint(Matrix([['r11', 'r12', 'r13', 'px'], 
                          ['r21', 'r22', 'r23', 'py'],
                          ['r31', 'r32', 'r33', 'pz'],
                          ['0', '0', '0', '1']]))
            print("\nIt comprises of the rotation matrix\n")
            pprint(Matrix([['r11', 'r12', 'r13'],
                          ['r21', 'r22', 'r23'],
                          ['r31', 'r32', 'r33']]))
            print("\nThe position vector in column matrix form\n")
            pprint(Matrix([['px'],
                          ['py'],
                          ['py']]))
            print("\nand a bottom row matrix always in the form: \n")
            pprint(Matrix([['0','0','0','1']]))
            print("\nThese are the inputted values\n")
            pprint(Matrix([[self.r11, self.r12, self.r13, self.px], 
                          [self.r21, self.r22, self.r23, self.py],
                          [self.r31, self.r32, self.r33, self.pz],
                          [0,0,0,1]]))
            print("\nThis is the inverse transformation matrix formula. Notice how the rotation matrix is transposed\n")
            pprint((Matrix([["r11", 'r21', 'r31', '-(px*r11)+(py*r21)+(pz*r31)'], 
                           ['r12', 'r22', 'r32', '-(px*r12)+(py*r22)+(pz*r32)'],
                           ['r13', 'r23', 'r33', '-(px*r13)+(py*r23)+(pz*r33)'],
                           ['0', '0', '0', '1']])))
            print("\nTherefore this is the inverse transformation matrix:\n")
            return inverse_transformation_matrix

        else:
            return inverse_transformation_matrix
        
    # Rotation matrix about X
    def rotation_about_X(self, matrix, angle, as_number=False, degrees=True, round_decimal=None, significant_figures=None):
        if degrees:
            angle = angle * pi / 180  # Convert angle to radians if degrees is True

        result = Matrix([[1, 0, 0],
                         [0, cos(angle), -sin(angle)],
                         [0, sin(angle), cos(angle)]]) * matrix

        if as_number:
            result = result.evalf()

            if round_decimal is not None:
                #result = round(result, round_decimal)  # Round to specified decimal places
                result = result.evalf(round_decimal)
            if significant_figures is not None:
                result = round(result, significant_figures - int(result.is_zero))

        return result

    def rotation_about_Y(self, matrix, angle, as_number=False, degrees=True, round_decimal=None, significant_figures=None):
        if degrees:
            angle = angle * pi / 180  # Convert angle to radians if degrees is True

        result = Matrix([[cos(angle), 0, -sin(angle)],
                         [0, 1, 0],
                         [sin(angle), 0 , cos(angle)]]) * matrix

        if as_number:
            result = result.evalf()

            if round_decimal is not None:
                result = round(result, round_decimal)  # Round to specified decimal places

            if significant_figures is not None:
                result = round(result, significant_figures - int(result.is_zero))

        return result

    def rotation_about_Z(self, matrix, angle, as_number=False, degrees=True, round_decimal=None, significant_figures=None):
        if degrees:
            angle = angle * pi / 180  # Convert angle to radians if degrees is True

        result = Matrix([[cos(angle), -sin(angle), 0],
                         [sin(angle), cos(angle), 0],
                         [0, 0, 1]]) * matrix

        if as_number:
            result = result.evalf()

            if round_decimal is not None:
                result = round(result, round_decimal)  # Round to specified decimal places

            if significant_figures is not None:
                result = round(result, significant_figures - int(result.is_zero))

        return result
    
    
    def forward_kinematics(self, degrees=False, DHtable=None) -> Matrix:
        if DHtable is not None:
            number_of_frames = DHtable.rows
        else:
            number_of_frames = int(input("Enter number of frames: "))

        lists = [[] for _ in range(number_of_frames)]
        matrix_variables = {}

        if DHtable:
            for i in range(number_of_frames):
                theta = DHtable[i, 0]
                alpha = DHtable[i, 1]
                a = DHtable[i, 2]
                d = DHtable[i, 3]

                if degrees:
                    theta_val = (float(theta) * pi / 180) if str(theta).replace('.', '', 1).isdigit() else (theta)
                    alpha_val = (float(alpha) * pi / 180) if str(alpha).replace('.', '', 1).isdigit() else (alpha)
                else:
                    theta_val = float(theta) if str(theta).replace('.', '', 1).isdigit() else (theta)
                    alpha_val = float(alpha) if str(alpha).replace('.', '', 1).isdigit() else (alpha)

                a_val = float(a) if str(a).replace('.', '', 1).isdigit() else (a)
                d_val = float(d) if str(d).replace('.', '', 1).isdigit() else (d)

                lists[i].append(theta_val)
                lists[i].append(alpha_val)
                lists[i].append(a_val)
                lists[i].append(d_val)
        else: 
            for i in range(number_of_frames):
                theta = input(f"Enter theta_{i+1}: ")
                alpha = input(f"Enter alpha_{i+1}: ")
                a = input(f"Enter a_{i+1}: ")
                d = input(f"Enter d_{i+1}: ")

                if degrees:
                    theta_val = (float(theta) * pi / 180) if theta.strip().replace('.', '', 1).isdigit() else symbols(theta)
                    alpha_val = (float(alpha) * pi / 180) if alpha.strip().replace('.', '', 1).isdigit() else symbols(alpha)
                else:
                    theta_val = float(theta) if theta.strip().replace('.', '', 1).isdigit() else symbols(theta)
                    alpha_val = float(alpha) if alpha.strip().replace('.', '', 1).isdigit() else symbols(alpha)

                a_val = float(a) if a.strip().replace('.', '', 1).isdigit() else symbols(a)
                d_val = float(d) if d.strip().replace('.', '', 1).isdigit() else symbols(d)

                lists[i].append(theta_val)
                lists[i].append(alpha_val)
                lists[i].append(a_val)
                lists[i].append(d_val)

        # Create transformation matrices
        matrices = []
        for i in lists:
            theta_val = i[0]
            alpha_val = i[1]
            a_val = i[2]
            d_val = i[3]

            # matrix = Matrix([
            #     [cos(theta_val), -sin(theta_val), 0,  a_val],
            #     [(sin(theta_val)*cos(alpha_val)), (cos(theta_val)*cos(alpha_val)), -(sin(alpha_val)), (-(sin(alpha_val)))*d_val],
            #     [(sin(theta_val)*sin(alpha_val)), (cos(theta_val)*sin(alpha_val)), cos(alpha_val), ((cos(alpha_val))*d_val)],
            #     [0,0,0,1],
            # ])
            matrix = Matrix([
                [cos(theta_val), -sin(theta_val)*cos(alpha_val), sin(theta_val)*sin(alpha_val),  a_val*cos(theta_val)],
                [sin(theta_val),  cos(theta_val)*cos(alpha_val), -cos(theta_val)*sin(alpha_val), a_val*sin(theta_val)],
                [0, sin(alpha_val), cos(alpha_val), d_val],
                [0,0,0,1]
            ])
            matrices.append(matrix)

        for i in range(number_of_frames):
            matrix_variables[f"T_{i}_{i+1}"] = matrices[i]

        print("Matrix Variables:")
        for key, matrix in matrix_variables.items():
            print(f"{key}:")
            print(matrix)  
            print() # adds spacing

        # Print the product matrix
        for matrix in matrices[1:]:
            matrices[0] = matrices[0] * matrix
        print("Resulting Product Matrix:")
        return matrices[0]

# Usage
r = SympyRobotics()

theta1, theta2, theta3, theta4, theta5, theta6, a1, a2, a3, a4, a5, a6, d1, d2,  d3, d4, d5, d6, L1, L2, L3, L4, L5, L6 = symbols(
    'theta1, theta2, theta3, theta4, theta5, theta6, a1, a2, a3, a4, a5, a6,d1, d2,  d3, d4, d5, d6, L1, L2, L3, L4, L5, L6', real=True)
dhtable = Matrix([
    [theta1, 0, L1, 0],
    [theta2, 0, L2, 0],
    [theta3, 0, L3, 0],
])
transformation_matrix = r.forward_kinematics(degrees=True, DHtable=dhtable)
transformation_matrix = simplify(transformation_matrix)
pprint(transformation_matrix[3])
