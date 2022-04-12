# Duplicated lines finder.
# Gerhard Eibl.

file = open("A file somewhere in your disk", 'r')
lines = file.readlines()

tab_pipe_1, tab_pipe_2, tab_pipe_3 = [], [], []
count, count2, count3, count4, count_line, pipe_01, pipe_02, pipe_03 = 0, 0, 0, 0, 0, 0, 0, 0
dico_tab_01, dico_tab_02, dico_tab_03 = {}, {}, {}

for line in lines:
    if len(line) == 167:
        tab_pipe_1.append(line[3:-158])
        tab_pipe_2.append(line[11:-126])
        tab_pipe_3.append(line[83:-70])
    elif len(line) == 168:
        tab_pipe_1.append(line[3:-159])
        tab_pipe_2.append(line[11:-127])
        tab_pipe_3.append(line[83:-71])
    count += 1

for line in lines:
    count_line += 1
    if len(line) == 167:
        pipe_01 = line[3:-158]
        pipe_02 = line[11:-126]
        pipe_03 = line[83:-70]
    elif len(line) == 168:
        pipe_01 = line[3:-159]
        pipe_02 = line[11:-127]
        pipe_03 = line[83:-71]

    if pipe_01 not in dico_tab_01:
        dico_tab_01[pipe_01] = count_line
    elif pipe_01 in dico_tab_01:
        count2 += 1
        print("Le pipe_01 :", pipe_01, "à la ligne :", count_line, ", est un doublon")
        print("Origine ligne :", dico_tab_01[pipe_01], "\n")

    if pipe_02 not in dico_tab_02:
        dico_tab_02[pipe_02] = count_line
    elif pipe_02 in dico_tab_02:
        count3 += 1
        print("Le pipe_02 :", pipe_02, "à la ligne :", count_line, ", est un doublon")
        print("Origine ligne :", dico_tab_02[pipe_02], "\n")

    if pipe_03 not in dico_tab_03:
        dico_tab_03[pipe_03] = count_line
    elif pipe_03 in dico_tab_03:
        count4 += 1
        print("Le pipe_02 :", pipe_03, "à la ligne :", count_line, ", est un doublon")
        print("Origine ligne :", dico_tab_03[pipe_03], "\n")

# print("Pipe type_01: |000001|")
# print("***********************************************|\n")
# print(tab_pipe_1, "\n")
#
# print("Pipe type_02: |%004900086100743103893397250A10^")
# print("***********************************************|\n")
# print(tab_pipe_2, "\n")
#
# print("Pipe type_03: |86100743103893|")
# print("***********************************************|\n")
# print(tab_pipe_3, "\n")

print("number of lines :", count, "\n")

print("Pipe_01")
if len(tab_pipe_1) == len(set(tab_pipe_1)):
    print("*************")
    print("- No doubles")
    print("*************\n")
else:
    print("*******************")
    print("-", count2, "Doubles detected")
    print("*******************\n")

print("Pipe_02")
if len(tab_pipe_2) == len(set(tab_pipe_2)):
    print("*************")
    print("- No doubles")
    print("*************\n")
else:
    print("*******************")
    print("-", count3, "Doubles detected")
    print("*******************\n")

print("Pipe_03")
if len(tab_pipe_3) == len(set(tab_pipe_3)):
    print("*************")
    print("- No doubles")
    print("*************\n")
else:
    print("*******************")
    print("-", count4, "Doubles detected")
    print("*******************\n")
