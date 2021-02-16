class Medico_hora():

    def __init__(self, nombre, fecha, hora, medico, especialidad, centro, direccion, telefono):
        self.nombre = nombre
        self.fecha = fecha
        self.hora = hora
        self.medico = medico
        self.especialidad = especialidad
        self.centro = centro
        self.direccion = direccion
        self.telefono = telefono

    def llamada(self):
        import requests
        import json

        data ={
            'domain': 'itcdaniel',
            'access_token': '8e537ea23c79260ee98885cf30031903',
            'scenario_id': 17828,
            'phone': self.telefono,
            'phone_number_id': 1976,
            'variables': json.dumps({"nombre": self.nombre,
                        "fecha": self.fecha,
                        "hora": self.hora,
                        "medico": self.medico,
                        "especialidad": self.especialidad,
                        "centro": self.centro,
                        "direccion": self.direccion})
        }
        call = requests.post("https://kitapi-us.voximplant.com/api/v3/scenario/runScenario", data=data)
        return call.text

class Medico_entrega():

    def __init__(self, nombre, tipo_2, telefono):
        self.nombre = nombre
        self.tipo_2 = tipo_2
        self.telefono = telefono

    def llamada(self):
        import requests
        import json

        data ={
            'domain': 'itcdaniel',
            'access_token': '8e537ea23c79260ee98885cf30031903',
            'scenario_id': 17829,
            'phone': self.telefono,
            'phone_number_id': 1976,
            'variables': json.dumps({"nombre": self.nombre,
                        "tipo": self.tipo_2})
        }
        call = requests.post("https://kitapi-us.voximplant.com/api/v3/scenario/runScenario", data=data)
        return call.text  