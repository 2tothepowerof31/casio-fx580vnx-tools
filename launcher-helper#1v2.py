# Credit by @2tothepowerof31
hex_chars=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"] #define hex characters to validate the input
#FE characters (type with shift 8)
fe={
"FE01": "q 8 1 1",
"FE02": "q 8 1 2",
"FE03": "q 8 1 3",
"FE04": "q 8 1 4",
"FE05": "q 8 1 5",
"FE06": "q 8 1 6",
"FE07": "q 8 1 7",
"FE08": "q 8 1 8",
"FE09": "q 8 1 9",
"FE0A": "q 8 1 z",
"FE0B": "q 8 2 1",
"FE0C": "q 8 2 2",
"FE0D": "q 8 3 1",
"FE0E": "q 8 3 2",
"FE0F": "q 8 3 3",
"FE10": "q 8 3 4",
"FE11": "q 8 1 x",
"FE12": "q 8 1 u",
"FE13": "q 8 R 1 2",
"FE14": "q 8 R 1 1",
"FE15": "q 8 4 1",
"FE16": "q 8 4 2",
"FE17": "q 8 4 3",
"FE1A": "q 8 R 2 2",
"FE1B": "q 8 R 2 3",
"FE1C": "q 8 R 2 4",
"FE1D": "q 8 R 4 1",
"FE1E": "q 8 R 4 2",
"FE1F": "q 8 R 2 5",
"FE20": "q 8 R 2 6",
"FE24": "q 8 R 2 8",
"FE25": "q 8 E 1 2",
"FE26": "q 8 E 1 1",
"FE27": "q 8 R 3 4",
"FE28": "q 8 R 3 3",
}
#FD characters (type with shift 7, FD18 is an exception)
fd={
"FD18": "q .",
"FD3A": "q 7 3 7",
"FD3B": "q 7 3 8",
"FD3C": "q 7 3 9",
"FD3D": "q 7 3 z",
"FD3E": "q 7 3 x",
"FD3F": "q 7 3 u",
"FD4C": "q 7 4 7",
"FD4D": "q 7 4 8",
"FD4E": "q 7 4 9",
"FD4F": "q 7 1 4",
"FD54": "q 7 1 6",
"FD55": "q 7 R 2 1",
"FD56": "q 7 1 7",
"FD57": "q 7 R 1 2",
"FD58": "q 7 1 8",
"FD59": "q 7 1 9",
"FD5A": "q 7 2 6",
"FD5B": "q 7 2 7",
"FD5C": "q 7 3 [",
"FD5D": "q 7 R 1 3",
"FD5E": "q 7 R 1 4",
}
#Normal characters that can be typed normally
ct1={
"21": "Q K",
"22": "q K",
"23": "Q y",
"2C": "q )",
"2D": "K",
"2E": ".",
"30": "0",
"31": "1",
"32": "2",
"33": "3",
"34": "4",
"35": "5",
"36": "6",
"37": "7",
"38": "8",
"39": "9",
"40": "Q m",
"41": "M",
"42": "Q z",
"43": "Q x",
"44": "Q u",
"45": "Q j",
"46": "Q k",
"47": "Q l",
"48": "[",
"49": "Q )",
"4A": "q M",
"4B": "Q n",
"50": "q [",
"51": "y",
"52": "q y",
"53": "Q [",
"60": "(",
"68": "q (",
"69": "q 0",
"6C": "T 1 1",
"6D": "T 1 2",
"6E": "T 1 3",
"6F": "T 1 4",
"70": "T 1 5",
"71": "T 1 6",
"72": "q h",
"73": "q i",
"74": "s",
"75": "h",
"76": "q s",
"77": "j",
"78": "k",
"79": "l",
"7A": "q j",
"7B": "q k",
"7C": "q l",
"7D": "i",
"7E": "q +",
"7F": "q p",
"83": "Q +",
"84": "Q p",
"87": "Q .",
"88": "Q O",
"89": "Q P",
"A5": "Q r",
"A6": "+",
"A7": "p",
"A8": "O",
"A9": "P",
"AA": "Q a",
"AD": "q O",
"AE": "q P",
"C0": "z",
"C8": "a",
"C9": "^",
"CA": "q ^",
"D0": ")",
"D4": "u",
"D5": "d",
"D6": "q d",
"D7": "q M",
"D8": "q u",
"D9": "T 2 1",
"DA": "T 2 2",
"DB": "T 2 3",
"DC": "x",
"DD": "T 3 x",
"DE": "T 3 z",
"DF": "T 3 9",
"E0": "T 3 8",
"E1": "T 3 7",
"E2": "T 3 6",
"E3": "T 3 1",
"E4": "T 3 2",
"E5": "T 3 3",
"E6": "T 3 4",
"E7": "T 3 5",
}
s=list(input().upper())
#remove spaces
while s.count(" ")!=0:
    s.remove(" ")
#check valid input 
run=1
if len(s)%2!=0:
    print("Invalid Hex String: invalid hex length(odd)")
    run=0
for item in s:
    if item not in hex_chars:
        run=0
        print("Invalid Hex String: invalid hex character")
        print(item)
        break
#process into key presses
press_inputs=[]
if run==1:
    kthuoc=2
    chia=["".join(s[i : i + kthuoc]) for i in range(0, len(s), kthuoc)]
    i=0
    while i<len(chia):
        if str(chia[i]) not in ct1:
            if chia[i]=="FD":
                temp="".join(chia[i]+chia[i+1])
                if temp in fd:
                    press_inputs.append(fd[temp])
                    i+=1
                else:
                    press_inputs.append("$")
                    i+=1
            elif chia[i]=="FE":
                temp="".join(chia[i]+chia[i+1])
                if temp in fe:
                    press_inputs.append(fe[temp])
                    i+=1
                else:
                    press_inputs.append("$")
                    i+=1
            else:
                press_inputs.append("$")
        else:
            press_inputs.append(ct1[chia[i]])
        i+=1
        print
    print("Output keypress:"," ".join(press_inputs))