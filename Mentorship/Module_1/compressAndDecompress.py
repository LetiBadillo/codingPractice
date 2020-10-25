def decompress(s):
    numberStack = []
    lettersStack = []
    compressed = ""
    number =""
    #3[2[a]2[b]3[c]]

    for element in s:
        if element.isdigit():
           number+=element
        elif element == "[":
             numberStack.append(int(number))
             number = ""
        else:
            if element == "]":
                if(lettersStack and numberStack):
                    times = numberStack.pop()
                    while(lettersStack):
                        letter = lettersStack.pop()
                        compressed+= times*letter
                elif (not lettersStack and numberStack):
                    compressed = compressed*2
            else:
                lettersStack.append(element)   
    return compressed





cases = ["2[4[a]3[b]]]", "2[80[bb]]", "0[b]"]
# Assumptions:
# only letters between brackets
# characters from a-z A-Z
# integer positive numbers
for case in cases:
    result = decompress(case)
    print("result:", result, "lenght", len(result))