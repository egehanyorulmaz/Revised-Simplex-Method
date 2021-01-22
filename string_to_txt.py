def objective_to_txt(string):

    myTxt = open("objective.txt", "w+")

    for i in range(1):

        myTxt.write(string)


    myTxt.close()

def constraints_to_txt(string):

    valTxt = open("values.txt", "w+")
    resultTxt = open("result.txt", "w+")
    variableTxt = open("constraint_variables.txt", "w+")

    equations = string.split("_")

    idenList = ["<=", ">=", "<", ">"]

    identifierList = []

    for equ in equations:

        identifier = ""

        for i in idenList:

            found = equ.find(i)

            if found != -1:

                identifierList.append(i)

                break

    idencounter=0

    for equation in equations:

        counter = 0

        sides = equation.split(identifierList[idencounter])

        for side in sides:

            if counter == 0:

                element = side.split("*")

                valstr = ""
                variablestr =""

                for val in element:

                    if val.find("x") !=-1 and element.index(val) != len(element)-1:

                        num = int(val[2:])

                        valstr = valstr + " " + str(num)

                        variablestr = variablestr + " " + val[:2]

                    elif element.index(val) != len(element)-1:
                        num = int(val)

                        valstr = valstr + " " + str(num)

                    else:
                        variablestr = variablestr + " " + val

                valTxt.write(valstr)
                valTxt.write("\n")

                variableTxt.write(variablestr)
                variableTxt.write("\n")

            else:

                resultTxt.write(side + " " + identifierList[idencounter])
                resultTxt.write("\n")

            counter += 1

        idencounter += 1

    valTxt.close()

    resultTxt.close()


def variablestr_to_txt(string):

    myTxt = open("variables.txt", "w+")

    myTxt.write(string)

    myTxt.close()

def objectivestr_to_txt(string):

    myTxt = open("objectivestr.txt", "w+")

    myTxt.write(string)

    myTxt.close()


#string = "1*x1+3*x2<=10_-1*x2+2*x3<=5"

#constraints_to_txt(string)
