class Bnc_Credito():

    def __init__(self, nombre, banco, monto, fecha, telefono):
        self.nombre = nombre
        self.banco = banco
        self.monto = monto
        self.fecha = fecha
        self.telefono = telefono

    def llamada(self):
        import requests
        import json
        data ={
            'domain': 'itcdaniel',
            'access_token': '8e537ea23c79260ee98885cf30031903',
            'scenario_id': 17797,
            'phone': self.telefono,
            'phone_number_id': 1976,
            'variables': json.dumps({"nombre": self.nombre,
                        "banco": self.banco,
                        "monto": self.monto,
                        "fecha":self.fecha})
        }
        call = requests.post("https://kitapi-us.voximplant.com/api/v3/scenario/runScenario", data=data)
        return call.text

class Bnc_Prdcto():

    def __init__(self, nombre, banco, opcion, fecha, telefono):
        self.nombre = nombre
        self.banco = banco
        self.opcion = opcion
        self.fecha = fecha
        self.telefono = telefono

    def llamada(self):
        import requests
        import json
        data ={
            'domain': 'itcdaniel',
            'access_token': '8e537ea23c79260ee98885cf30031903',
            'scenario_id': 17798,
            'phone': self.telefono,
            'phone_number_id': 1976,
            'variables': json.dumps({"nombre": self.nombre,
                        "banco": self.banco,
                        "opcion": self.opcion,
                        "fecha":self.fecha})
        }
        call = requests.post("https://kitapi-us.voximplant.com/api/v3/scenario/runScenario", data=data)
        return call.text

class Bnc_Cuota():

    def __init__(self, nombre, banco, monto, telefono):
        self.nombre = nombre
        self.banco = banco
        self.monto = monto
        self.telefono = telefono

    def llamada(self):
        import requests
        import json
        data ={
            'domain': 'itcdaniel',
            'access_token': '8e537ea23c79260ee98885cf30031903',
            'scenario_id': 17799,
            'phone': self.telefono,
            'phone_number_id': 1976,
            'variables': json.dumps({"nombre": self.nombre,
                        "banco": self.banco,
                        "monto":self.monto})
        }
        call = requests.post("https://kitapi-us.voximplant.com/api/v3/scenario/runScenario", data=data)
        return call.text

class Bnc_cambio():

    def __init__(self, nombre, banco, telefono):
        self.nombre = nombre
        self.banco = banco
        self.telefono = telefono

    def llamada(self):
        import requests
        import json
        
        data ={
            'domain': 'itcdaniel',
            'access_token': '8e537ea23c79260ee98885cf30031903',
            'scenario_id': 17803,
            'phone': self.telefono,
            'phone_number_id': 1976,
            'variables': json.dumps({"nombre": self.nombre,
                        "banco": self.banco})
        }
        call = requests.post("https://kitapi-us.voximplant.com/api/v3/scenario/runScenario", data=data)
        return call.text