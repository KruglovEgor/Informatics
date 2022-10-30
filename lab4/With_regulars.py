import re


# function for adding opening/closing {[]} and comas to the previous line
def check(found):
    if len(found[0]) > last_spaces:
        # update our list with spaces
        sp_list.append(len(found[0]))
        # check for list components or normal lines
        if len(found) != 2:
            return "{\n"
        else:
            return "[\n"
    elif len(found[0]) == last_spaces:
        # checking for null situations in normal/list cases
        if last_line != [] and len(last_line) != 2 and last_line[2] == '':
            return "null,\n"
        elif len(last_line) == 2 and last_line[1] == '':
            return "null,\n"
        # for not adding coma to the first line (may be fixed)
        elif last_line != []:
            return ",\n"
        # if the first line
        else:
            return ''
    else:
        # counting how many closing }] we need to put
        c = 0
        for i in sp_list:
            if i > len(found[0]):
                c += 1

        # poping off all extra lvls of spaces we got off
        while sp_list[-1] > len(found[0]):
            sp_list.pop(-1)

        # for usual lines
        if len(last_line) != 2:
            if last_line[2] == '':
                return "null" + "}"*c + ",\n"
            else:
                return "}"*c + ",\n"
        # for list components
        else:
            if last_line[1] == '':
                return "null" + "]" * c + ",\n"
            else:
                return "]" * c + ",\n"


# function for making words look good: str - > "str", "str" -> "str", dig -> dig, "st"r" -> "st\"r"
def check_word(word):
    a = ''
    if word.isdigit():
        return word
    # cause we can't check first 2 and 2 last symbols
    elif len(word) == 1:
        return '"' + word + '"'
    # for not returning none-type
    elif len(word) == 0:
        return ''
    # situations with str, len(str) >= 2
    else:
        # add \ before "
        for i in range(len(word)):
            if word[i] == '"':
                a += r'\"'
            else:
                a += word[i]

        # if it's already had " in the beginning and in the end
        if a[0]+a[1] == r'\"' and a[-2]+a[-1] == r'\"':
            return a[1:-2] + '"'
        else:
            return '"' + a + '"'


# for not list components. Returns 1) spaces, 2) first word, 3) second word (if None -> '')
msq_usual = re.compile(r'( *)"?([\S ]*?)"?: ?("[\S ]*"|[\S ]*)\n?')
# for list components. Returns 1) spaces, 2) word (with no -)
msq_list = re.compile(r'( *)- "?([\S ]*)"?\n?')

# count of spaces in previous line
last_spaces = 0
# list with space-levels we are at
sp_list = [0]
# last line separated with mask
last_line = []


def start(input_file, output_file):
    global last_line, last_spaces
    with open(input_file, 'r') as f1:
        with open(output_file, 'w') as f2:
            f2.write("{\n")
            # checking all our lines
            for i in range(119):
                line = f1.readline()
                # if msq_usual is suitable - choose it, else - msq_list
                s = max(re.findall(msq_usual, line), re.findall(msq_list, line))
                # for list components
                if len(s[0]) == 2:
                    f2.write(check(s[0]) + s[0][0] + check_word(s[0][1]))
                # for usual
                else:
                    f2.write(check(s[0]) + s[0][0] + check_word(s[0][1]) + ": " + check_word(s[0][2]))

                # update last_spaces and last_line
                last_spaces = len(s[0][0])
                last_line = s[0]

            # in the end add all needed closing } (may be fixed)
            f2.write('}' * (len(sp_list)))
    # return our variables to default:
    set_default()


def set_default():
    global last_spaces, sp_list, last_line
    last_spaces, sp_list, last_line = 0, [0], []


start('Lr4.yaml', 'Lr4_2.json')
