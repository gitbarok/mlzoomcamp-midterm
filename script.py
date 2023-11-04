import pickle

THRESHOLD = 0.01


def load(filename: str):
    with open(filename, "rb") as f_in:
        return pickle.load(f_in)


data = {
    "gender": "M",
    "car_owner": "N",
    "propert_owner": "Y",
    "children": 1,
    "annual_income": 198000.0,
    "type_income": "Working",
    "education": "Secondary / secondary special",
    "marital_status": "Widow",
    "housing_type": "House / apartment",
    "mobile_phone": 1,
    "work_phone": 0,
    "phone": 1,
    "email_id": 1,
    "type_occupation": "Laborers",
    "family_members": 3,
    "age": 37.0,
    "employee_status": 1,
}

data_2 = {
    "gender": "F",
    "car_owner": "N",
    "propert_owner": "N",
    "children": 0,
    "annual_income": 180000.0,
    "type_income": "Pensioner",
    "education": "Secondary / secondary special",
    "marital_status": "Married",
    "housing_type": "House / apartment",
    "mobile_phone": 1,
    "work_phone": 0,
    "phone": 0,
    "email_id": 0,
    "type_occupation": "unidentified",
    "family_members": 2,
    "age": 60.0,
    "employee_status": 1,
}

data_false = {
    "gender": "F",
    "car_owner": "Y",
    "propert_owner": "N",
    "children": 0,
    "annual_income": 315000.0,
    "type_income": "Commercial associate",
    "education": "Higher education",
    "marital_status": "Married",
    "housing_type": "House / apartment",
    "mobile_phone": 1,
    "work_phone": 1,
    "phone": 1,
    "email_id": 0,
    "type_occupation": "unidentified",
    "family_members": 2,
    "age": 60.0,
    "employee_status": 0,
}

# F,Y,N,0,315000.0,Commercial associate,Higher education,Married,House / apartment,1,1,1,0,unidentified,2,1,37.0,0
# F,Y,N,0,315000.0,Commercial associate,Higher education,Married,House / apartment,1,1,1,0,unidentified,2,1,37.0,0
# F,Y,N,0,315000.0,Commercial associate,Higher education,Married,House / apartment,1,1,1,0,unidentified,2,1,37.0,0
# F,N,N,0,180000.0,Pensioner,Secondary / secondary special,Married,House / apartment,1,0,0,0,unidentified,2,1,60.0,1

model, dv = load("model/randomforest.bin")

X_test = dv.transform([data_false])

y_pred = model.predict_proba(X_test)[0, 1]

print(y_pred)
