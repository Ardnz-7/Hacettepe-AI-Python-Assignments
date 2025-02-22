readFile = "doctors_aid_inputs.txt"
patientList = []
writeFile= "doctors_aid_outputs.txt"
with open(readFile) as f:
    x = f.readlines()
with open(writeFile, "w") as f:


    def create():
        global patientList
        y = []
        y = line.split(", ")
        y[0] = y[0].replace("create ","")
        y[-1] = y[-1].replace("\n","")
        a = -1
        for i in range(len(patientList)):
            if patientList[i][0] == y[0]:
                a=i
        if a == -1:
            patientList.append(y)
            f.write("Patient " + y[0]+ " is recorded.\n")
        else:
            f.write("Patient " + y[0]+ " cannot recorded due to duplication\n")
        return patientList

    def remove():
        y = []
        y = line.split()
        a = y.pop()
        for i in patientList:
            if a != i[0]:
                pass
            elif a == i[0]:
                f.write("Patient " + a + " is removed\n")
                patientList.remove(i)
            else:
                f.write("Patient " + a + " cannot be removed due to absence\n")



    def list():
        f.write("Patient\t Diagnosis\t Disease\t\t Disease\tTreatment\tTreatment\nName\t Accuracy\t Name\t\t\t  Incidence\t Name\t\t Risk\n")
        for i in patientList:
            f.write(i[0]+"\t"+str(float(i[1])*100)+"%"+"\t\t"+i[2]+"\t"+ str(i[3]) +"\t" + i[4]+"\t"+str(int(float(i[5])*100))+ "%\n")


    def probability():
        b = line.split()[1]
        for i in patientList:
            if i[0] == b:
                p = float(int(i[3][0:2]) / 10**5) / (float(int(i[3][0:2]) / 10**5)+1- float(i[1]))
                p = p*100
                a = round(p,2)
                f.write("Patient "+b+ " has a probability of "+ str(a) + "%" + " of having "+i[2]+".\n")

    def recommendation():
        b = line.split()[1]
        for i in patientList:
            if i[0] == b:
                p = float(int(i[3][0:2]) / 10**5) / (float(int(i[3][0:2]) / 10**5)+1- float(i[1]))
                p = p*100
                a = round(p,2)
                if a < float(i[5])*100 :
                    f.write("System suggests "+ b+" NOT to have the treatment.\n")
                else:
                    f.write("System suggests "+b+" to have the treatment.\n")







    for line in x:
        if "create" in line:
            create()
        elif "remove" in line:
            remove()
        elif "list" in line:
            list()
        elif "probability" in line:
            probability()
        elif "recommendation" in line:
            recommendation()

