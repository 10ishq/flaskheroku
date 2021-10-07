from flask import Flask
import requests

from flask_restful import Api, Resource

URL = "https://g6s8n9qe4g.execute-api.us-east-2.amazonaws.com/default/LambdaTest"

app = Flask(__name__)
api = Api(app)

nameData = ''
testData = 1

class HelloWorld(Resource):
    def  get(self, name , test):
        payload = {"first_parameter":name,"second_parameter":test}
        
        r = requests.post(URL,json=payload)
        data=r.json()
        print(r.text)
        return data
    
    

api.add_resource(HelloWorld,"/helloworld/<int:name>/<int:test>")

if __name__ == "__main__":
    app.run(debug=True)
