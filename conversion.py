# def makebinnarystr(aStr):
#     binstr = aStr.split('') #101
#     binvallst = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
#     idx = 0
#     declst = []
#
#     for i in range(len(binstr) - 1, -1, -1):
#         declst.append(int(binstr[i]) * binvallst[idx])
#         idx += 1
#
#     return

# binary value represented as a string
# assume 8 bit leangth
def binarytodecimal(aStr = "11111111"):
    # aStr will be 8 characters long
    binarystringarr = aStr.strip().split()

    # holds value of each place of binary
    binaryvaluearr = [128,64,32,16,8,4,2,1]

    idxval = 0

    # create accumulator for decimal value
    decimaltotalvalue = 0

    for binstring in binarystringarr:
        # convert the binary digit to integer value
        convertedbinarydigit = int(binstring)

        # convert binary digit to decimal value
        convertedbinaryvalue = convertedbinarydigit * binaryvaluearr[idxval]

        # acumulate decimal value
        decimaltotalvalue += convertedbinaryvalue

        # increment index value to access next next binary digit value
        idxval += 1
    # return the total decimal value
    return decimaltotalvalue

# Convert all binary inputs
# assume it takes in 8 bits (characters)
# assume either converting to decimal or hexcidecimal only
# def convertbinary(instring = "11111111", convertdecimal = True):
#
#     # hold our result
#     retString = ""
#
#     if convertdecimal == True:
#         retString = binarytodecimal(instring)
#         retString = str(retString)
#
#     else:
#         retString = instring # replace with a conversion for hexidecimal
#
#     return retString


# Convert all binary inputs
# assume it takes in 8 bits (characters)
# assume either converting to both decimal and hexcidecimal
def convertbinary(instring="11111111"):
    # hold our result
    retString = []

    # add the solution to the array
    retString.append(instring)

    # append the decimal value to the array
    retString.append(str(binarytodecimal(instring)))

    #retString.append() instring  # replace with a conversion for hexidecimal




    return retString











#     binstr = aStr.split('') #101
#     binvallst = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
#     idx = 0
#     declst = []