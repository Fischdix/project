name = "name"
gender = ("gender")
age = ("age")
height_in = ("height")
weight_lbs = ("weight")

### AGERANGE() IS IRRELAVANT
agerange1 = (list(range(17, 21)))
agerange2 = (list(range(21, 28)))

bmi = (weight_lbs * 705 / height_in) / height_in
print("BMI:", bmi)
print("Age:", age)
# Gender statement
if gender == ("m"):
    print("Gender: male")
elif gender == ("f"):
    print("Gender: female")
else:
    print("Gender data unavailable")

if age in (range(17,21)):
    if bmi <= (20):
        print(name, "is in the first age bracket")
        print("is not overweight")
    else:
        print(name, "is in the first age bracket")
        print("is overweight")

if age in (range(21, 28)):
    if bmi <= (22):
        print(name, "is in the second age bracket")
        print("is not overweight")
    else:
        print(name, "is in the second age bracket")
        print("is overweight")
