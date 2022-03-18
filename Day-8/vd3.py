import json

class Patient:
    def __init__(self, name, mrn, birth_date):
        self.name = name
        self.mrn = mrn
        self.birth_date = birth_date

    def to_json(self):
        return json.dumps({
            'name': ...,
            'mrn': ...,
            'birth_date': ...
        })

    def from_json(text):
        data = json.loads(...)
        return Patient(...)

patient = Patient('Nguyen Van A', 'HN023212', '2000-01-01')
text = patient.to_json()
print(text)

# ---------------------------------------------------------

patient = Patient.from_json(text)