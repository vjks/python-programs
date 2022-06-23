def computepay(score):
    if (score > 1):
        return "Bad score" 
    elif(score >= 0.9):
        grade = 'A'
    elif(score >= 0.8):
        grade = 'B'
    elif(score >= 0.7):
        grade = 'C'
    elif(score >= 0.6):
        grade = 'D'
    else:
        grade = 'F'
    return grade

try:
    score = float(input("Enter score:"))
    print(computepay(score))
except:
    print("Bad score")
    