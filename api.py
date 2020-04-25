import requests
import json

SUBSCRIPTION_KEY = "b66c2ed9f72a4e33b33b9d1425975cd3"

vision_service_address = "https://pythonimageanalzer.cognitiveservices.azure.com/"
address = vision_service_address + "vision/v2.0/analyze"

parameters = {"visualFeatures": "Description,Color",
              "language": "en"}
image_path = "/Users/yueyin/PycharmProjects/Microsofe Developer/PolarBear.jpg"
image_data = open(image_path, "rb").read()

headers = {"Content-Type": "application/octet-stream",
           "Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY}

response = requests.post(address, headers=headers, params=parameters, data=image_data)
result = response.json()
print(json.dumps(result))
print()


print(result["requestId"])
print()

print(result["color"]["dominantColorBackground"])
print()

print(result["description"]["tags"][0:3])
print()


for i in result["description"]["tags"]:
    print(i)
print()

person_dict = {"first": "Christopher", "last": "Harrison", "City": "Seattle"}

person_json = json.dumps(person_dict)
print(person_json)
print()