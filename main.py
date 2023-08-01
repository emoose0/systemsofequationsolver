import numpy as np

print("type coefficients and answers [eg: 8x + 2y = 8 --> input 8 2 8] type 00 to stop REMEMBER: TYPE YOUR VARIABLE VALUES IN ALPHABETICAL ORDER WITH ANS ON LAST PLACE")

inp = "1"
coef = np.array([[]])
answers = np.array([])

enterPressed = 0
equationCount = 0

while inp != "00":
    cInput = []
    inp = input("> ")
    if inp == "00":
         break
    cInput = inp.split()

    for i, j in enumerate(cInput):
        if j.isdigit() == False and (cInput[i+1].isdigit() == False):
                print("ERR: INVALID INPUT: " + j)
                exit()
        else:
            cInput[i] = float(j)
    
    cAns = cInput.pop() #get answer
    cAns = np.array(cAns)

    cInput = np.array(cInput)
    cInput = np.expand_dims(cInput, axis=0)

    if coef.size == 0: 
            coef = cInput
            answers = cAns
    else:
         try:
            coef = np.append(coef, cInput, axis = 0)
            answers = np.append(answers, cAns)
         except ValueError:
              print("ERR: MISSING VARIABLE CHECK INPUT [if your equation has a missing variable then substitute it with 0 eg: 3x + 4z = 12 --> input: 3 0 4 12]")
              exit()

x = np.linalg.solve(coef, answers)
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i, j in enumerate(x):
     print(alphabet[i], ": ", j)
