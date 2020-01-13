def bmiAnswer(wieght,height):
    if wieght<0 or height<0: #Checks if the variables are negative
        return False
    return int(wieght/height**2*10000) #Formula for finding BMI
def  BMI(wieght,height): #Returns the weight level
    bmi=bmiAnswer(wieght,height)
    if bmi is False:
        return 'You are having trouble entering again'
    dictBmi={10:'Underweight',16:'Healthy weight',26:'over-weight',31:'obesity',36:'Severe fat',41:'Severe obesity',50:'Severe obesity'}
    return dictBmi[list(filter(lambda x:x<=bmi,dictBmi))[-1]]




