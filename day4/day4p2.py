def function2():
    with open('day4/input.txt', 'r') as data_file:
        cpt=0
        cptline=0
        
        for line in data_file:
            cptline+=1
            line = line.strip()
            sline = line.split(",")
            half1 = sline[0]
            half2 = sline[1]

            min1 = int(half1.split("-")[0])
            max1 = int(half1.split("-")[1])
            min2 = int(half2.split("-")[0])
            max2 = int(half2.split("-")[1])

            if((min1 <= min2) & (max1 >= max2)):
                cpt += 1
            elif((min2 <= min1) & (max2 >= max1)):
                cpt += 1
            elif((min1 <= min2 & (max1 >= min2)) | (min2 <= min1 & max2 >= min1)):
                cpt += 1
            print(cpt, cptline)

function2()