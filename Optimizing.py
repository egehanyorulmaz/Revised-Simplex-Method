import json as js
import numpy as np

# text processing (constraint_matrix (number_of_constraint, number_of_variables)
# objective function control ( min -> max ) [1, 2, 3] -> *-1 -> [-1, -2, -3]
# constraint control ( >= -> <=) for all constraints > *-1 > updated_constraint_matrix
# rhs of constraints will be controlled. (must be bi >= 0) -> if violated *-1
# slack variable adding -> constraint matrix, objective_constraint_vector will be updated.
# all_constraint_coef_matrix -> objective coefficient will be included. videonun 10. dakikasındaki olay
# elimizde 3 tane matrix var. coefficient_matrix, variable_vector, objective_coef_vector

def obj_func_control (dict_):

    new_dict = dict_

    if dict_["objective"] == "min":

        new_dict["objective_equation"]["values"] = [-1*a for a in dict_["objective_equation"]["values"]]

        new_dict["objective"] = "max"

    return new_dict

def const_control(dict_):

    newdict = dict_

    for constraint in newdict["constraints"]:

        path = newdict["constraints"][constraint]

        if path["notation"][0].find(">=") != -1:

            path["values"] = [-1*a for a in path["values"]]
            path["notation"] = "<="

    return newdict

def find_variable_num(dict_):

    variable_num = 0
    slack_num = 0

    for element in dict_["variable_list"]:

        if int(element[1:]) > variable_num:

            variable_num = int(element[1:])

    for constraint in dict_["constraints"]:

        path = dict_["constraints"][constraint]["xs"]

        if dict_["constraints"][constraint]["notation"] != "=":

            slack_num += 1

        for element in path:

            if int(element[1:]) > variable_num:

                variable_num = int(element[1:])

    return variable_num, slack_num

def obj_func_treatment(dict_):

    var_num, sl_num = find_variable_num(dict_)

    treated = []
    treated.append(1)


    for i in range(1, var_num+1):

        if "x"+str(i) in dict_["objective_equation"]["xs"]:

            indx = dict_["objective_equation"]["xs"].index("x"+str(i))

            treated.append(dict_["objective_equation"]["values"][indx]*-1)

        else:

            treated.append(0)

    for element in range(sl_num):

        treated.append(0)

    return treated

def matrix_treatment(dict_):

    newdict = dict_

    var_num, sl_num = find_variable_num(dict_)

    matrix_dict = {}

    matrix_dict["Objective_vector"] = obj_func_treatment(newdict)


    for constraint in dict_["constraints"]:
        treated = []
        treated.append(0)

        path = dict_["constraints"][constraint]

        for i in range(1, var_num+1):

            if "x"+str(i) in path["xs"]:

                indx = path["xs"].index("x"+str(i))

                treated.append(path["values"][indx])

            else:

                treated.append(0)

        matrix_dict[constraint] = treated

    for num in dict_["constraints"]:

        counter = 0
        for col in range(sl_num):

            if int(num[len(num)-1:]) == counter:

                matrix_dict["Constraint_{}".format(counter)].append(1)

            else:

                matrix_dict["Constraint_{}".format(counter)].append(0)

            counter += 1

    nplist = [a for a in matrix_dict.values()]

    return np.array(nplist).astype(float)

def var_sl_vec(dict_):

    newdict = dict_

    var_num, sl_num = find_variable_num(newdict)

    var_vec = []
    sl_vec = []

    var_vec.append("z")

    for i in range(1, sl_num+var_num+1):

        var_vec.append("x"+str(i))

    for i in range(var_num+1, var_num+sl_num+1):

        sl_vec.append(i)

    return np.array(var_vec), sl_vec

def rhs_vec (dict_):

    rhs = []
    rhs.append(0)

    for constraint in dict_["constraints"]:

        path = dict_["constraints"][constraint]["rhs"]

        rhs.append(path)

    return np.array(rhs)

def main_func (dict_):

    newdict = dict_

    data1 = obj_func_control (newdict)
    data2 = const_control (data1)

    matrix = matrix_treatment(data2)
    var_vector, slack_vars_positions = var_sl_vec(data2)
    rhs = rhs_vec(data2)

    return matrix, var_vector, rhs, slack_vars_positions

if __name__ == '__main__':

    json = open("Extraction.json")

    data = js.load(json)

    m,v,r,s = main_func(data)
