class Sms_generico():

    def __init__(self, telefono, mensaje):
        self.telefono = str(telefono)
        self.mensaje = mensaje

    def envio(self):
        import requests
        import json

        telefono = self.telefono[0:11]

        data ={
            "account_id": 3918841,
            "api_key": "b2611cfa-a8b1-4dcc-9f5a-e31899d6a50f",
            'src_number': "13023650926",
            'dst_numbers': telefono,
            'text': self.mensaje
        }
        call = requests.post("https://api.voximplant.com/platform_api/A2PSendSms/", data=data)
        return call.text
