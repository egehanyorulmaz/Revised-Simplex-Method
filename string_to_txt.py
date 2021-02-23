import json as js

def save_as_JSON(obj, var_list, obj_equ, const):

    dict = {}

    dict["objective"] = obj
    dict["variable_list"] = var_extractor(var_list)
    dict["objective_equation"] = extractor(obj_equ, False)
    dict["constraints"] = extractor(const)

    with open('Extraction.json', 'w') as fp:
        js.dump(dict, fp, indent=4)

def var_extractor(text):

    var_vector = []

    elements = text.split(" ")

    for element in elements:

        var_vector.append(element)

    return var_vector

def extractor(text, flag = True):

    equdict = {}

    if "_" in text:

        equations = text.split("_")

        for counter, equation in enumerate(equations):

            nodedict = {}

            vals, xs, signs, rhs = string_manupulator(equation)

            nodedict["values"] = vals
            nodedict["xs"] = xs
            nodedict["notation"] = signs
            nodedict["rhs"] = rhs

            equdict["Constraint_{}".format(counter)] = nodedict

    elif flag == False:

        vals, xs, signs, rhs= string_manupulator(text + "<0")

        equdict["values"] = vals
        equdict["xs"] = xs

    else:

        vals, xs, signs, rhs= string_manupulator(text)

        equdict["values"] = vals
        equdict["xs"] = xs
        equdict["notation"] = signs
        equdict["rhs"] = rhs

    return equdict

def string_manupulator(equation):

    comparisons = ["<", ">"]

    signs = []

    if " " in equation:

        equation = equation.replace(" ", "")

    symbol = ""

    for symbols in comparisons:

        if symbols in equation:

            indx = equation.index(symbols)

            symbol = equation[indx]

            if equation[indx+1] == "=":

                symbol = symbol + "="

    signs.append(symbol)

    equation = equation.replace(symbol, "!")

    sides = equation.split("!")

    countedx = sides[0].count("x")

    for times in range(countedx-1):

        if "+" in sides[0][1:]:

            indx = sides[0].index("+", sides[0].index("x"))

            sides[0] = sides[0][:indx] + "!" + sides[0][indx+1:]

        elif "-" in sides[0][1:]:

            indx = sides[0].index("-", sides[0].index("x"))

            sides[0] = sides[0][:indx] + "!-" + sides[0][indx+1:]

    elements = sides[0].split("!")

    values = []

    xs = []

    for element in elements:

        if "*" in element:

            indx = element.index("*")

            values.append(int(element[:indx]))

            xs.append(element[indx+1:])

        elif element.index("x") != 0:

            indx = element.index("x")

            values.append(int(element[:indx]))

            xs.append(element[indx:])

        else:

            values.append(1)

            xs.append(element[:])

    return values, xs, signs, int(sides[1])

if __name__ == "__main__":

    val = "x1+x2-4*x3<=10_-1*x2+2*x3>5"

    save_as_JSON("max", "x1 x2 x3 x4", "2*x1-3*x2+5*x3", val)
