def BMI(wieght,height):
    return int(wieght/height**2*10000)
def  aRuler(bmi):

    dictBmi={10:'Underweight',16:'Healthy weight',26:'over-weight',31:'obesity',36:'Severe fat',41:'Severe obesity',50:'Severe obesity'}
    return dictBmi[list(filter(lambda x:x<=bmi,dictBmi))[-1]]



print(aRuler(BMI(119,173)))
