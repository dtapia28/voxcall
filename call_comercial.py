class Comercial_aumento():

    def __init__(self, nombre, casa_comercial, monto, telefono):
        self.nombre = nombre
        self.casa_comercial = casa_comercial
        self.monto = monto
        self.telefono = telefono

    def llamada(self):
        import requests
        import json

        data ={
            'domain': 'itcdaniel',
            'access_token': '8e537ea23c79260ee98885cf30031903',
            'scenario_id': 17805,
            'phone': self.telefono,
            'phone_number_id': 1976,
            'variables': json.dumps({"nombre": self.nombre,
                        "casa_comercial": self.casa_comercial,
                        "monto": self.monto})
        }
        call = requests.post("https://kitapi-us.voximplant.com/api/v3/scenario/runScenario", data=data)
        return call.text

class Comercial_producto():

    def __init__(self, nombre, casa_comercial, producto, fecha, telefono):
        self.nombre = nombre
        self.casa_comercial = casa_comercial
        self.producto = producto
        self.fecha = fecha
        self.telefono = telefono

    def llamada(self):
        import requests
        import json

        data ={
            'domain': 'itcdaniel',
            'access_token': '8e537ea23c79260ee98885cf30031903',
            'scenario_id': 17812,
            'phone': self.telefono,
            'phone_number_id': 1976,
            'variables': json.dumps({"nombre": self.nombre,
                        "casa_comercial": self.casa_comercial,
                        "producto": self.producto,
                        "fecha": self.fecha})
        }
        call = requests.post("https://kitapi-us.voximplant.com/api/v3/scenario/runScenario", data=data)
        return call.text

class Comercial_cuota():

    def __init__(self, nombre, casa_comercial, monto, telefono):
        self.nombre = nombre
        self.casa_comercial = casa_comercial
        self.monto = monto
        self.telefono = telefono

    def llamada(self):
        import requests
        import json

        data ={
            'domain': 'itcdaniel',
            'access_token': '8e537ea23c79260ee98885cf30031903',
            'scenario_id': 17826,
            'phone': self.telefono,
            'phone_number_id': 1976,
            'variables': json.dumps({"nombre": self.nombre,
                        "casa_comercial": self.casa_comercial,
                        "monto": self.monto})
        }
        call = requests.post("https://kitapi-us.voximplant.com/api/v3/scenario/runScenario", data=data)
        return call.text