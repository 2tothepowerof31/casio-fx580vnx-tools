# Credit by @2tothepowerof31
hex_chars=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"] #define hex characters to validate the input
#FE characters (type with shift 8)
fe={
"FE01": "[SHIFT] [8] [1] [1]",
"FE02": "[SHIFT] [8] [1] [2]",
"FE03": "[SHIFT] [8] [1] [3]",
"FE04": "[SHIFT] [8] [1] [4]",
"FE05": "[SHIFT] [8] [1] [5]",
"FE06": "[SHIFT] [8] [1] [6]",
"FE07": "[SHIFT] [8] [1] [7]",
"FE08": "[SHIFT] [8] [1] [8]",
"FE09": "[SHIFT] [8] [1] [9]",
"FE0A": "[SHIFT] [8] [1] [(-)]",
"FE0B": "[SHIFT] [8] [2] [1]",
"FE0C": "[SHIFT] [8] [2] [2]",
"FE0D": "[SHIFT] [8] [3] [1]",
"FE0E": "[SHIFT] [8] [3] [2]",
"FE0F": "[SHIFT] [8] [3] [3]",
"FE10": "[SHIFT] [8] [3] [4]",
"FE11": "[SHIFT] [8] [1] [°' \"]",
"FE12": "[SHIFT] [8] [1] [𝒙⁻¹]",
"FE13": "[SHIFT] [8] [▼] [1] [2]",
"FE14": "[SHIFT] [8] [▼] [1] [1]",
"FE15": "[SHIFT] [8] [4] [1]",
"FE16": "[SHIFT] [8] [4] [2]",
"FE17": "[SHIFT] [8] [4] [3]",
"FE1A": "[SHIFT] [8] [▼] [2] [2]",
"FE1B": "[SHIFT] [8] [▼] [2] [3]",
"FE1C": "[SHIFT] [8] [▼] [2] [4]",
"FE1D": "[SHIFT] [8] [▼] [4] [1]",
"FE1E": "[SHIFT] [8] [▼] [4] [2]",
"FE1F": "[SHIFT] [8] [▼] [2] [5]",
"FE20": "[SHIFT] [8] [▼] [2] [6]",
"FE24": "[SHIFT] [8] [▼] [2] [8]",
"FE25": "[SHIFT] [8] [▲] [1] [2]",
"FE26": "[SHIFT] [8] [▲] [1] [1]",
"FE27": "[SHIFT] [8] [▼] [3] [4]",
"FE28": "[SHIFT] [8] [▼] [3] [3]",
}
#FD characters (type with shift 7, FD18 is an exception)
fd={
"FD18": "[SHIFT] [.]",
"FD3A": "[SHIFT] [7] [3] [7]",
"FD3B": "[SHIFT] [7] [3] [8]",
"FD3C": "[SHIFT] [7] [3] [9]",
"FD3D": "[SHIFT] [7] [3] [(-)]",
"FD3E": "[SHIFT] [7] [3] [°' \"]",
"FD3F": "[SHIFT] [7] [3] [𝒙⁻¹]",
"FD4C": "[SHIFT] [7] [4] [7]",
"FD4D": "[SHIFT] [7] [4] [8]",
"FD4E": "[SHIFT] [7] [4] [9]",
"FD4F": "[SHIFT] [7] [1] [4]",
"FD54": "[SHIFT] [7] [1] [6]",
"FD55": "[SHIFT] [7] [▼] [2] [1]",
"FD56": "[SHIFT] [7] [1] [7]",
"FD57": "[SHIFT] [7] [▼] [1] [2]",
"FD58": "[SHIFT] [7] [1] [8]",
"FD59": "[SHIFT] [7] [1] [9]",
"FD5A": "[SHIFT] [7] [2] [6]",
"FD5B": "[SHIFT] [7] [2] [7]",
"FD5C": "[SHIFT] [7] [3] [𝒙]",
"FD5D": "[SHIFT] [7] [▼] [1] [3]",
"FD5E": "[SHIFT] [7] [▼] [1] [4]",
}
#Normal characters that can be typed normally
ct1={
"21": "[ALPHA] [×10ˣ]",
"22": "[SHIFT] [×10ˣ]",
"23": "[ALPHA] [∫]",
"2C": "[SHIFT] [)]",
"2D": "[×10ˣ]",
"2E": "[.]",
"30": "[0]",
"31": "[1]",
"32": "[2]",
"33": "[3]",
"34": "[4]",
"35": "[5]",
"36": "[6]",
"37": "[7]",
"38": "[8]",
"39": "[9]",
"40": "[ALPHA] [M+]",
"41": "[Ans]",
"42": "[ALPHA] [(-)]",
"43": "[ALPHA] [°' \"]",
"44": "[ALPHA] [𝒙⁻¹]",
"45": "[ALPHA] [sin]",
"46": "[ALPHA] [cos]",
"47": "[ALPHA] [tan]",
"48": "[𝒙]",
"49": "[ALPHA] [)]",
"4A": "[SHIFT] [Ans]",
"4B": "[ALPHA] [S⇔D]",
"50": "[SHIFT] [𝒙]",
"51": "[∫]",
"52": "[SHIFT] [∫]",
"53": "[ALPHA] [𝒙]",
"60": "[(]",
"68": "[SHIFT] [(]",
"69": "[SHIFT] [0]",
"6C": "[OPTN] [1] [1]",
"6D": "[OPTN] [1] [2]",
"6E": "[OPTN] [1] [3]",
"6F": "[OPTN] [1] [4]",
"70": "[OPTN] [1] [5]",
"71": "[OPTN] [1] [6]",
"72": "[SHIFT] [ln]",
"73": "[SHIFT] [log□□]",
"74": "[√□]",
"75": "[ln]",
"76": "[SHIFT] [√□]",
"77": "[sin]",
"78": "[cos]",
"79": "[tan]",
"7A": "[SHIFT] [sin]",
"7B": "[SHIFT] [cos]",
"7C": "[SHIFT] [tan]",
"7D": "[log□□]",
"7E": "[SHIFT] [+]",
"7F": "[SHIFT] [-]",
"83": "[ALPHA] [+]",
"84": "[ALPHA] [-]",
"87": "[ALPHA] [.]",
"88": "[ALPHA] [×]",
"89": "[ALPHA] [÷]",
"A5": "[ALPHA] [CALC]",
"A6": "[+]",
"A7": "[-]",
"A8": "[×]",
"A9": "[÷]",
"AA": "[ALPHA] [phân số]",
"AD": "[SHIFT] [×]",
"AE": "[SHIFT] [÷]",
"C0": "[(-)]",
"C8": "[phân số]",
"C9": "[𝒙□]",
"CA": "[SHIFT] [𝒙□]",
"D0": "[)]",
"D4": "[𝒙⁻¹]",
"D5": "[𝒙²]",
"D6": "[SHIFT] [𝒙²]",
"D7": "[SHIFT] [Ans]",
"D8": "[SHIFT] [𝒙⁻¹]",
"D9": "[OPTN] [2] [1]",
"DA": "[OPTN] [2] [2]",
"DB": "[OPTN] [2] [3]",
"DC": "[°' \"]",
"DD": "[OPTN] [3] [°' \"]",
"DE": "[OPTN] [3] [(-)]",
"DF": "[OPTN] [3] [9]",
"E0": "[OPTN] [3] [8]",
"E1": "[OPTN] [3] [7]",
"E2": "[OPTN] [3] [6]",
"E3": "[OPTN] [3] [1]",
"E4": "[OPTN] [3] [2]",
"E5": "[OPTN] [3] [3]",
"E6": "[OPTN] [3] [4]",
"E7": "[OPTN] [3] [5]",
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
                    press_inputs.append("[▶]")
                    i+=1
            elif chia[i]=="FE":
                temp="".join(chia[i]+chia[i+1])
                if temp in fe:
                    press_inputs.append(fe[temp])
                    i+=1
                else:
                    press_inputs.append("[▶]")
                    i+=1
            else:
                press_inputs.append("[▶]")
        else:
            press_inputs.append(ct1[chia[i]])
        i+=1
    print("Output keypress:",*press_inputs)