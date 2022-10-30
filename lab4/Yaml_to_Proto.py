f_ = 0
count = 0
in_list = 0
last_line = ''
sp_list = [0]


def check_line(line, isNull, ending):
    global count, f_
    if (len(line.split()) == 1 or (len(line.split()) == 2 and line.split()[1] == ':')) and f_ == 0:
        if isNull == 0:
            return 'message ' + line.split()[0][:-1]*(len(line.split()) == 1) + line.split()[0]*(len(line.split()) == 2) + ending
        else:
            count += 1
            return 'string ' + line.split()[0][:-1]*(len(line.split()) == 1) + line.split()[0]*(len(line.split()) == 2) + ' = ' + str(count) + ending
    else:
        if f_ == 0:
            count += 1
            return 'int32 '*(line.split()[1].isdigit()) + 'string '*(not line.split()[1].isdigit()) + line.split()[0][:-1] + ' = ' + str(count) + ending
        else:
            if in_list == 0:
                count += 1
                return 'repeated string ' + last_line.split()[0][:-1]*(len(line.split()) == 1) + line.split()[0]*(len(line.split()) == 2)  + ' = ' + str(count)+ ending
            else:
                return ''


def start(input_file, output_file):
    global f_, count, in_list, sp_list, last_line
    with open(input_file, 'r') as f1:
        with open(output_file, 'w') as f2:
            f2.write("syntax = \"proto3\";\n")
            for i in range(119):
                isNull = 0
                line = f1.readline()

                if f_ == 1:
                    in_list = 1
                else:
                    in_list = 0
                if line.split()[0] == "-":
                    f_ = 1
                else:
                    f_ = 0

                spaces = 0
                for x in range(len(line)):
                    if line[x] != " ":
                        spaces = x
                        break

                if spaces == sp_list[-1]:
                    if last_line != '':
                        ending = ';\n'
                        if (len(last_line.split()) == 1) or (len(line.split()) == 2 and line.split()[1] == ':'):
                            isNull = 1
                            ending = ';\n'
                    else:
                        ending = ''
                # spaces < scale
                elif spaces in sp_list:

                    c = 0
                    for i in sp_list:
                        if i > spaces:
                            c += 1

                    # delete all levels we got off
                    while sp_list[-1] > spaces:
                        sp_list.pop(-1)

                    if f_ == 0:
                        if (len(last_line.split()) == 1) or (len(line.split()) == 2 and line.split()[1] == ':'):
                            isNull = 1
                            ending = ';\n' + spaces*" " + '}'*c + ';\n'
                        else:
                            ending = ';\n' + spaces*" " + '}' * c + ';\n'
                    else:
                        if in_list == 0:
                            ending = ';\n'
                        else:
                            ending = ''

                # spaces > scale
                else:
                    if f_ == 0:
                        sp_list.append(spaces)
                        ending = '{\n'
                    else:
                        if in_list == 0:
                            ending = ';\n'
                        else:
                            ending = ''

                if last_line != '' and in_list == 0:
                    f2.write(sp_list[-1]*" " + check_line(last_line, isNull, ending))

                last_line = line

            isNull, ending = 0, ';' + '}'*(len(sp_list)-1)
            f2.write(sp_list[-1]*" " + check_line(last_line, isNull, ending))


start('Lr4.yaml', 'Lr4_4.proto')