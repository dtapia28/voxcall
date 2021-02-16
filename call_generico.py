class Generico():

    def __init__(self, mensaje, telefono):
        self.mensaje = mensaje
        self.telefono = telefono

    def llamada(self):
        import requests
        import json

        data ={
            'domain': 'itcdaniel',
            'access_token': '8e537ea23c79260ee98885cf30031903',
            'scenario_id': 17847,
            'phone': self.telefono,
            'phone_number_id': 1976,
            'variables': json.dumps({"mensaje": self.mensaje})
        }
        call = requests.post("https://kitapi-us.voximplant.com/api/v3/scenario/runScenario", data=data)
        return call.text             