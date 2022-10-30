# with open("Lr4.yaml", 'r') as f1:
#     with open("Lr4_1.json", 'w') as f2:
#         sp_list = [0]
#         lines = []
#
#         #TODO make func of checking better, like if "" in the beggining or in the end
#         #TODO check the first part may consist of "two words"
#
#         def write_in(line, f2):
#             if len(line.split()) == 1:
#                 f2.write('"' + check_sym(line.strip()[:-1]) + '":')
#             elif len(line.split()) == 2:
#                 if f_ == 0:
#                     if line.split()[1].isdigit() == False:
#                         if line.split()[1].startswith('"'):
#                             f2.write('"' + check_sym(line.split()[0][:-1]) + '": "' + check_sym(line.split()[1][1:-1]) + '"')
#                         else:
#                             f2.write('"' + check_sym(line.split()[0][:-1]) + '": "' + check_sym(line.split()[1]) + '"')
#                     else:
#                         f2.write('"' + line.split()[0][:-1] + '": ' + line.split()[1])
#                 else:
#                     if line.split()[1].isdigit() == False:
#                         if line.split()[1].startswith('"'):
#                             f2.write('"' + check_sym(line.split()[1][1:-1]) + '"')
#                         else:
#                             f2.write('"' + check_sym(line.split()[1]) + '"')
#                     else:
#                         f2.write(line.split()[1])
#             else:
#                 if f_ == 0:
#                     f2.write('"' + check_sym(line.split()[0][:-1]) + '": "' + check_sym(line.strip()[len(line.split()[0])+2:-1]) + '"')
#                 else:
#                     #ne proveryau vnutry na check_sym
#                     f2.write(line.strip()[len(line.split()[0])+1:])
#
#
#         def check_sym(word):
#             a = ""
#             if word.isdigit():
#                 return word
#             else:
#                 for i in word:
#                     if i == '"':
#                         a += r"\""
#                     else:
#                         a += i
#                 return a
#
#         # def format_lines(line):
#         #     if len(line.split()) == 1:
#         #         return '"'+check_sym(line.strip()[:-1]) + '":'
#         #     elif len(line.split()) == 2:
#         #         pass
#
#
#
#
#         f2.write("{\n")
#         scale = 0
#         f = 0
#         f_ = 0
#         for i in range(119):
#             line = f1.readline()
#             if len(lines) < 2:
#                 lines.append(line)
#             else:
#                 lines.pop(0)
#                 lines.append(line)
#             if line.split()[0] == "-":
#                 f_ = 1
#             spaces = 0
#             for x in range(len(line)):
#                 if line[x] != " ":
#                     spaces = x
#                     break
#             if spaces == scale:
#                 if (len(lines[0].split()) != 1 or len(lines) < 2) and f == 1:
#                     f2.write(',\n')
#                 elif f == 1:
#                     f2.write('null,\n')
#                 write_in(line, f2)
#             else:
#                 if spaces > scale:
#
#                     if spaces not in sp_list:
#                         sp_list.append(spaces)
#                     if f_ == 0:
#                         f2.write(" {\n")
#                     else:
#                         f2.write(" [\n")
#
#                     write_in(line, f2)
#
#                 else:
#                     c = 0
#                     for i in sp_list:
#                         if i > spaces:
#                             c += 1
#                     while sp_list[-1] > spaces:
#                         sp_list.pop(-1)
#                     if f_ == 0:
#                         if spaces in sp_list:
#                             if len(lines[0].split()) != 1 or len(lines) < 2:
#                                 f2.write('}'*c + ',\n')
#                             else:
#                                 f2.write('null' + '}'*c + ',\n')
#                         else:
#                             if len(lines[0].split()) != 1 or len(lines) < 2:
#                                 f2.write('}'*c + '\n')
#                             else:
#                                 f2.write('null' + '}'*c + '\n')
#                     else:
#                         if spaces in sp_list:
#                             if len(lines[0].split()) != 1 or len(lines) < 2:
#                                 f2.write('],\n')
#                             else:
#                                 f2.write('null],\n')
#                         else:
#                             if len(lines[0].split()) != 1 or len(lines) < 2:
#                                 f2.write(']\n')
#                             else:
#                                 f2.write('null]\n')
#                         f_ = 0
#                     write_in(line, f2)
#
#             scale = spaces
#             f = 1
#         f2.write('}'*(len(sp_list)))


# with open("Lr4.yaml", 'r') as f1:
#     with open("Lr4_1.json", 'w') as f2:
#         # list with spaces steps we made
#         sp_list = [0]
#         # 2 last lines
#         lines = []
#         # start our json file with it
#         f2.write("{\n")
#         # the count of spaces of previous line
#         scale = 0
#         # flag of the first line
#         f = 0
#         # flag of starting with '-' (mean list)
#         f_ = 0
#
#         # function for cheking str and formating it
#         def check_sym(word):
#             if word.startswith('"'):
#                 a = ''
#             else:
#                 a = '"'
#             if word.isdigit():
#                 return word
#             else:
#                 for i in range(len(word)):
#                     if word[i] == '"' and i != 0 and i != len(word)-1:
#                         a += r"\""
#                     elif i == len(word) - 1:
#                         if word[i] == ':':
#                             a += '":'
#                         elif word[i] != '"':
#                             a += word[i] + '"'
#                         else:
#                             a += word[i]
#                     else:
#                         a += word[i]
#                 return a
#
#         # function for formaing lines (it uses check_sym)
#         def format_lines(line):
#             if len(line.split()) == 1:
#                 return check_sym(line.strip())
#             elif len(line.split()) == 2:
#                 if f_ == 0:
#                     return check_sym(line.split()[0]) + check_sym(line.split()[1])
#                 else:
#                     return check_sym(line.split()[1])
#             else:
#                 if f_ == 0:
#                     if line.strip().startswith('"'):
#                         cut = 0
#                         # looking for place where the "key" of dictionary ends
#                         for i in range(len(line.strip())-1):
#                             if line[i] + line[i+1] == '":':
#                                 cut = i+1
#                                 break
#                         # check for null meaning of key
#                         if cut != len(line.strip()-1):
#                             return check_sym(line.strip()[:cut+1]) + " " + check_sym(line.stripe()[cut+2:])
#                         else:
#                             return check_sym(line.strip())
#                     else:
#                         # if the "key" is one word
#                         return check_sym(line.split()[0]) + " " + check_sym(line.strip()[len(line.split()[0]) + 1:])
#                 else:
#                     # if it's the component of list (starts with '-')
#                     return check_sym(line.strip()[2:])
#
#         # running for all our lines
#         for i in range(119):
#             line = f1.readline()
#
#             # making our 2 last lines array
#             if len(lines) < 2:
#                 lines.append(line)
#             else:
#                 lines.pop(0)
#                 lines.append(line)
#
#             # checking for components of list
#             if line.split()[0] == "-":
#                 f_ = 1
#
#             # counting spaces
#             spaces = 0
#             for x in range(len(line)):
#                 if line[x] != " ":
#                     spaces = x
#                     break
#
#             if spaces == scale:
#                 # checking if our previous line was with null meaning
#                 if (len(lines[0].split()) != 1 or len(lines) < 2) and f == 1:
#                     f2.write(',\n')
#                 elif f == 1:
#                     f2.write('null,\n')
#
#             elif spaces > scale:
#                 # adding new levels of spaces we reached
#                 sp_list.append(spaces)
#
#                 if f_ == 0:
#                     f2.write(" {\n")
#                 else:
#                     f2.write(" [\n")
#
#
#             else:
#                 # counting how many closing '}' we must to write
#                 c = 0
#                 for i in sp_list:
#                     if i > spaces:
#                         c += 1
#
#                 # delete all levels we got off
#                 while sp_list[-1] > spaces:
#                     sp_list.pop(-1)
#
#                 if f_ == 0:
#                     # if previous line wasn't with null meaning or if we don't even have 2 lines: do usal thing
#                     if len(lines[0].split()) != 1 or len(lines) < 2:
#                         f2.write('}'*c + ',\n')
#                     # if no - add null part
#                     else:
#                         f2.write('null' + '}'*c + ',\n')
#                 else:
#                     # if previous line wasn't with null meaning or if we don't even have 2 lines: do usal thing
#                     if len(lines[0].split()) != 1 or len(lines) < 2:
#                         f2.write(']'*c + ',\n')
#                     else:
#                         f2.write('null]'*c + ',\n')
#                     # turn off our flag of list components (start with '-') P.s. I couldn't add it at the beggining
#                     # cause we put closing ']' on the next line that can be usual (not component of list)
#                     f_ = 0
#
#             f2.write(" "*spaces + format_lines(line))
#             # make scale be the count of spaces and go for the next line
#             scale = spaces
#             # turn on flag what we passed 1st line
#             f = 1
#
#         # in the end add all necessary closing '}'
#         f2.write('}'*(len(sp_list)))





# function for cheking str and formating it
def check_sym(word):
    if word.startswith('"'):
        a = ''
    else:
        a = '"'
    if word.isdigit():
        return word
    else:
        for i in range(len(word)):
            if word[i] == '"' and i != 0 and i != len(word)-1:
                a += r"\""
            elif i == len(word) - 1:
                if word[i] == ':':
                    a += '":'
                elif word[i] != '"':
                    a += word[i] + '"'
                else:
                    a += word[i]
            else:
                a += word[i]
        return a


# function for formaing lines (it uses check_sym)
def format_lines(line):
    if len(line.split()) == 1:
        return check_sym(line.strip())
    elif len(line.split()) == 2:
        if f_ == 0:
            return check_sym(line.split()[0]) + check_sym(line.split()[1])
        else:
            return check_sym(line.split()[1])
    else:
        if f_ == 0:
            if line.strip().startswith('"'):
                cut = 0
                # looking for place where the "key" of dictionary ends
                for i in range(len(line.strip())-1):
                    if line[i] + line[i+1] == '":':
                        cut = i+1
                        break
                # check for null meaning of key
                if cut != len(line.strip()-1):
                    return check_sym(line.strip()[:cut+1]) + " " + check_sym(line.stripe()[cut+2:])
                else:
                    return check_sym(line.strip())
            else:
                # if the "key" is one word
                return check_sym(line.split()[0]) + " " + check_sym(line.strip()[len(line.split()[0]) + 1:])
        else:
            # if it's the component of list (starts with '-')
            return check_sym(line.strip()[2:])


# list with spaces steps we made
sp_list = [0]
# 2 last lines
lines = []
# the count of spaces of previous line
scale = 0
# flag of the first line
f = 0
# flag of starting with '-' (mean list)
f_ = 0


def start(input_file, output_file):
    global scale, f, f_
    with open(input_file, 'r') as f1:
        with open(output_file, 'w') as f2:
            # start our json file with it
            f2.write("{\n")
            # running for all our lines
            for i in range(119):
                line = f1.readline()

                # making our 2 last lines array
                if len(lines) < 2:
                    lines.append(line)
                else:
                    lines.pop(0)
                    lines.append(line)

                # checking for components of list
                if line.split()[0] == "-":
                    f_ = 1

                # counting spaces
                spaces = 0
                for x in range(len(line)):
                    if line[x] != " ":
                        spaces = x
                        break

                if spaces == scale:
                    # checking if our previous line was with null meaning
                    if (len(lines[0].split()) != 1 or len(lines) < 2) and f == 1:
                        f2.write(',\n')
                    elif f == 1:
                        f2.write('null,\n')

                elif spaces > scale:
                    # adding new levels of spaces we reached
                    sp_list.append(spaces)

                    if f_ == 0:
                        f2.write(" {\n")
                    else:
                        f2.write(" [\n")

                else:
                    # counting how many closing '}' we must write
                    c = 0
                    for i in sp_list:
                        if i > spaces:
                            c += 1

                    # delete all levels we got off
                    while sp_list[-1] > spaces:
                        sp_list.pop(-1)

                    if f_ == 0:
                        # if previous line wasn't with null meaning or if we don't even have 2 lines: do usual thing
                        if len(lines[0].split()) != 1 or len(lines) < 2:
                            f2.write('}'*c + ',\n')
                        # if no - add null part
                        else:
                            f2.write('null' + '}'*c + ',\n')
                    else:
                        # if previous line wasn't with null meaning or if we don't even have 2 lines: do usual thing
                        if len(lines[0].split()) != 1 or len(lines) < 2:
                            f2.write(']'*c + ',\n')
                        else:
                            f2.write('null]'*c + ',\n')
                        # turn off our flag of list components (start with '-') P.s. I couldn't add it at the beggining
                        # cause we put closing ']' on the next line that can be usual (not component of list)
                        f_ = 0

                f2.write(" "*spaces + format_lines(line))
                # make scale be the count of spaces and go for the next line
                scale = spaces
                # turn on flag what we passed 1st line
                f = 1

            # in the end add all necessary closing '}'
            f2.write('}'*(len(sp_list)))
    # return our variables to default:
    set_default()


def set_default():
    global sp_list, lines, scale, f, f_
    sp_list, lines, scale, f, f_ = [0], [], 0, 0, 0


start('Lr4.yaml', 'Lr4_1.json')