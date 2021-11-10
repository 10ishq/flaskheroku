# import main Flask class and request object
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from waitress import serve

bodyData = {
    "Inputs": {
      "input1": [
        {
          'test_date': "2020-04-30T00:00:00Z",
          'cough': "0",
          'fever': "0",
          'sore_throat': "0",
          'shortness_of_breath': "0",
          'head_ache': "0",
          'corona_result': "negative",
          'age_60_and_above': "None",
          'gender': "female",
          'test_indication': "Other",
        }
      ],
    },
    "GlobalParameters": {}
  }



def postData(jsonData):
    #print(jsonData['Inputs']['input1'][0])
    bodyData['Inputs']['input1'][0] = jsonData

    import urllib.request
    import json
    data = bodyData
    body = str.encode(json.dumps(data))
    url = 'https://ussouthcentral.services.azureml.net/workspaces/fd6af8dd36714712848db07655d91ba2/services/077a9a1ac4c54772bd42fb9a80ef39f9/execute?api-version=2.0&format=swagger'
    api_key = 'abc123' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer v1XxSCYFLyDZN1mmreAClokU2eCFaVAVH03mFitPkcxOnjx6lqoZ0kFBFiSxMMT8wRMjLwkh1KhcjPJDGEHTNA==')}
    req = urllib.request.Request(url, body, headers)
    try:
        response = urllib.request.urlopen(req)

        result = response.read()
        print(json.loads(result))
        return(json.loads(result))
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read().decode("utf8", 'ignore')))
        

# create the Flask app
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def query_example():
    return 'Home Page'

@app.route('/post', methods=['POST'])
def incomingData():
    data= request.get_json()
    #print(data)
    

    mlData = postData(data)
    print(type(mlData))
    

    return mlData



if __name__ == "__main__":
    app.run(debug=True)
