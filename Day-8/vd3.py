import json

class Patient:
    def __init__(self, name, mrn, birth_date):
        self.name = name
        self.mrn = mrn
        self.birth_date = birth_date

    def to_json(self):
        data = {
            'name': self.name,
            'mrn': self.mrn,
            'birth_date': self.birth_date
        }
        return json.dumps(data)
    # -------------------------------------------------------
    def from_json(text):
        data = json.loads(text)
        name = data['name']
        mrn = data['mrn']
        birth_date = data['birth_date']
        return Patient(name, mrn, birth_date)

patient = Patient('Nguyen Van A', 'HN023212', '2000-01-01')
text = patient.to_json()
print(text)

print('---------------------------------------------------------')

patient = Patient.from_json(text)
print(patient.name, patient.mrn, patient.birth_date)