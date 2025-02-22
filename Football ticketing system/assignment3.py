import sys
r_file = sys.argv[1]
w_file = "output.txt"
with open(r_file) as f:
    feature= f.readlines()

with open("output.txt", "w") as f:

    s = []
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    book = {}       #create an empty dictionary for following category's


    def create_category():
        stairs = []
        x = []
        category_tag = lines.split()[1]             #category name
        row = lines.split()[2][:2]
        column = lines.split()[2][3:]
        for i in range(int(row)):
            stairs.append(alphabet[i] + " X" * int(column))                 #writing "X"es to the empty table
        stairs.reverse()                                                    #to order exact rows
        x.append("  ")
        for b in range(int(column)):
            if len(str(b)) == 1:
                x.append(str(b) + " ")
            else:
                x.append(str(b) + "")
        order = ""
        for j in x:                          # j is for elements 
            if "X" not in j:
                order += str(j)                     
        stairs.append(order)
        if category_tag not in book.keys():
            book[category_tag] = stairs     
            f.write("The category " +category_tag+ " having " +str(int(row)*int(column)) + " seats has been created\n")
            print("The category " +category_tag+ " having " +str(int(row)*int(column)) + " seats has been created\n" , end="") 
        else:
            f.write("Error: Cannot create the category for the second time. The stadium has already " + category_tag+ "\n")
            print("Error: Cannot create the category for the second time. The stadium has already " + category_tag+ "\n", end="")
    

    def show_category():
        category_tag = lines.split()[1]
        f.write("Printing category layout of " + category_tag+ "\n")
        f.write("\n")
        print("Printing category layout of " + category_tag+ "\n")
        for i in book[category_tag]:                                            #i is for lines
            f.write(i + "\n")
            print(i + "\n", end="")

    def sell_ticket():
        seats = lines.split()[4:]
        kind = lines.split()[2]
        name = lines.split()[1]
        t = []
        category_tag = lines.split()[3]
        for i in book[category_tag]:                            # i is for lines
            i = list(i)                             #make lines list
            for k in seats:
                if "-" not in k:                                #to seperate intervals
                    if k[0] == i[0]:
                        if i[int(k[1])*2 +2] == "X":
                            if kind == "student":
                                i[int(k[1])*2 +2] = "S"
                            elif kind == "full":
                                i[int(k[1])*2 +2 ] = "F"
                            elif kind == "season":
                                i[int(k[1])*2 +2 ] = "T"
                            f.write("Success: " + name + " has bought " + k + " at " + category_tag + "\n")
                            print("Success: " + name + " has bought " + k + " at " + category_tag + "\n", end="")
                        else:
                             f.write("Warning: The seat "+ k +" cannot be sold to " + name + " since it was already sold!\n")
                             print("Warning: The seat "+ k +" cannot be sold to " + name + " since it was already sold!\n", end="")
                             break
                else:                                       #for the interval 
                    x = k.index("-")
                    y = k[1:x]
                    z = k[x+1:]

                    if k[0] == i[0]:
                        for m in i[int(y)*2 +2:(int(z)+1)*2+2:2]:
                            if m != "X":
                                f.write("Warning: The seats " + k + " cannot be sold to " + name + " due some of them have already been sold!\n")
                                print("Warning: The seats " + k + " cannot be sold to " + name + " due some of them have already been sold!\n", end="")
                                break
                            else:
                                f.write("Success: " +name+ " has bought " + k + " at " + category_tag + "\n")
                                print("Success: " +name+ " has bought " + k + " at " + category_tag + "\n", end="")
                                if kind == "student":
                                    u = "S"
                                elif kind == "full":
                                    u = "F"
                                elif kind == "season":
                                    u = "T"
                                i[int(y)*2 +2:(int(z)+1)*2+2:2]=[ u for j in i[int(y)*2 +2:(int(z)+1)*2+2:2]]
                                break


            i = "".join(i)
            t.append(i)
        book[category_tag] = t
                            
    def cancel_ticket():
        category_tag = lines.split()[1] 
        seats = lines.split()[2:]   
        t = []
        for i in book[category_tag]:
            i = list(i)  
            for k in seats: 
                if k[0]== i[0]:
                    if i[int(k[1])*2+ 2] == "X":
                        f.write("Error: The seat " + k + " at " + category_tag + " has already been free! Nothing to cancel\n")  
                        print("Error: The seat " + k + " at " + category_tag + " has already been free! Nothing to cancel\n", end="")
                    elif  i[int(k[1])*2+ 2] == "S" and "T" and "F":
                        f.write("Success: The seat " + k + " at " + category_tag + " have been canceled and now ready to sell again\n")   
                        print("Success: The seat " + k + " at " + category_tag + " have been canceled and now ready to sell again\n", end="")         
                        i[int(k[1])*2 + 2] = "X"
                    else:
                        f.write("Error: The category " + category_tag + " has less column than the specified index " + k + "\n")
                        print("Error: The category " + category_tag + " has less column than the specified index " + k + "\n", end="")

            i="".join(i)
            t.append(i)
        book[category_tag] = t

    
    def balance():
        category_tag = lines.split()[1]
        sum_s = 0
        sum_t = 0
        sum_f = 0
        
        for i in book[category_tag]:                            
            i = list(i)[1:]
            for j in i:
                if "S" == j:
                    sum_s += 1
                elif "T" == j:
                    sum_t += 1
                elif "F" == j:
                    sum_f += 1
        revenue = int(sum_f)*20 + int(sum_s)*10 + int(sum_t)*250

        f.write("Category report of "+ category_tag +"\n")
        f.write("-" *30 + "\n")
        f.write("Sum of students = "+ str(sum_s) +", Sum of full pay = " + str(sum_f) + ", Sum of season ticket= " + str(sum_t) +", and Revenues = "+ str(revenue) + " Dollars\n")
        print("Category report of "+ category_tag +"\n", end="")
        print("-" *30 + "\n", end="")
        print("Sum of students = "+ str(sum_s) +", Sum of full pay = " + str(sum_f) + ", Sum of season ticket= " + str(sum_t) +", and Revenues = "+ str(revenue) + " Dollars\n", end="")



    for lines in feature:                               #detecting functions from lines
        if "CREATECATEGORY" in lines:
            create_category()     
            
        elif "SHOWCATEGORY" in lines:
            show_category()
        
        elif "SELLTICKET" in lines:
            sell_ticket()
        elif "CANCELTICKET" in lines:
            cancel_ticket()
        elif "BALANCE" in lines:
            balance()