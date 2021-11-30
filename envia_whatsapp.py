import json
import requests

class Envio_whatsapp():

    def __init__(self):
        pass

    def conexion(self):

        data = {
            "username":"itconsultants.testing",
            "password":"itconsultants@123@whatsapp",
        }

        headers = {'Content-type':'application/json', 'Accept':'application/json'}

        url = "https://zyxmedev.com/zyxme/bridge/api/processauthentication/generatebearertoken"

        call = requests.post(url,json=data, headers=headers)       
        respuesta = call.text

        diccionario = {}
        dividido = respuesta.split(",")

        for parte in dividido:
            algo = parte.split(":")
            algo[0]=algo[0].replace("{",'')
            algo[0]=algo[0].replace('"','')
            diccionario[algo[0]]=algo[1]

        diccionario['bearerToken']=diccionario['bearerToken'].replace('"','')

        return diccionario['bearerToken']

    def envio(self,token):

        head = {"Authorization": "Bearer "+token}

        data = {
            "messageContent": "[{\"Type\":\"text\",\"Text\":\"Max Baez\",\"Name\":\"1\"},{\"Type\":\"text\",\"Text\":\"11-06-2021\",\"Name\":\"2\"}]",
            "templateNamespace": "77de18dd_609b_4ece_ba83_314790769b4f",
            "templateName": "dialog_text",
            "appUserId": "56957390481",
            "messageType": "template",
            "appId": "51994204479",
            "sourceType": "WHAD",
            "corpId": 1,
            "orgId": 1
        }

        url = 'https://zyxmedev.com/zyxme/bridge/api/processzyxme/usezyxmemessaging'

        respuesta = requests.post(url, json=data, headers=head)

        print(respuesta.text)