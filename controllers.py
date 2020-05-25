from model import *
from sqlalchemy import or_


def login(email, password):
    try:
        user = User.query.filter(or_(User.email == email, User.username == email)).first()
        if user:
            result = user.verify_password(password, user.password)
            if result:
                return user
    except Exception as e:
        print(e)

    return None


def getUserById(id):
    try:
        return User.query.filter_by(id=id).first()
    except:
        return None


def reportByState(state, disease):
    patients = db.session.query(db.func.count(Patient.estadoSaude), Patient.last_state, Patient.state).group_by(
        Patient.last_state).group_by(Patient.state)

    if state:
        patients = patients.filter(Patient.state == state)
    if disease:
        patients = patients.filter(Patient.diseases.any(Disease.id.in_(disease)))

    patients = patients.all()
    patientList = []
    for patient in patients:
        patientList.append({
            'total': patient[0],
            'data': str(patient[1]),
            'state': State.query.filter_by(id=patient[2]).first().name,
        })
    return patientList
