class BMI:
    def __init__(self,height, weight):
        self.height = height
        self.weight = weight
    def caluculate_bmi(self):
        return self.weight/(self.height ** 2)


tanaka_bmi = BMI(height=1.80, weight=67.0)
sasami_bmi = BMI(height=1.58, weight=80.0)

#print(tanaka_bmi.height, sasami_bmi.height)
print(tanaka_bmi.caluculate_bmi())
print(sasami_bmi.caluculate_bmi())
