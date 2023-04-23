if __name__ == '__main__':
    name = ["introduction", "installingpythonandpycharm", "drawingashape", "variablesanddatatypes", "workingwithstrings", "workingwithnumbers", "gettinginputfromusers", "buildingabasiccalculator", "madlibsgame", "lists", "listfunctions", "tuples", "functions", "returnstatement", "ifstatements", "ifstatementsandcomparisons", "buildingabettercalculator", "dictionaries", "whileloop", "buildingaguessinggame", "forloops", "exponentfunction", "2dlistsandnestedloops", "buildingatranslator", "comments", "tryexcept", "readingfiles", "writingtofiles", "modulesandpip", "classesandobjects", "buildingamultiplechoicequiz", "objectfunctions", "inheritance", "pythoninterpreter"]
    print('****************************')
    i = 0
    with open('/home/lucky/Dropbox/pythonMultipleChoiceQuestion2', 'r') as f:
        print('****************************')
        x = f.readline()
        print(x)
        with open('/home/lucky/' + name[i] + '.xml', 'w') as nf:
            nf.write(x)
            nf.close()
        f.close()



        print('****************************')


