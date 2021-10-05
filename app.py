from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

nameData = ''
testData = 1

class HelloWorld(Resource):
    def  get(self, name , test):
        return {"Data":"Get Hello World"}
    
    def post(self, name, test):
        nameData=name
        testData=test
        print(nameData+" "+str(testData))
        return {"Data": nameData,"Test":testData}

api.add_resource(HelloWorld,"/helloworld/<string:name>/<int:test>")

if __name__ == "__main__":
    app.run(debug=True)