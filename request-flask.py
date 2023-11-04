import requests

end_point = "http://127.0.0.1:9696/predict"

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

result = requests.post(end_point, json=data).json()
print(result)
