
############################ Login #########################################
import requests

url = "https://app.autogradr.com/api/login"

payload = "{\"email\":\"abhinav@skillspeed.com\",\"password\":\"coolman123\"}"

s = requests.session() # maintaining session

response = s.post(url, data=payload)

print(response.text)




######################### File upload #############################################

#print("checking for file upload ")




url = "https://app.autogradr.com/api/files/upload"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"files\"; filename=\"solution_fail.zip\"\r\nContent-Type: application/zip\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'origin': "https://app.autogradr.com",
    'x-devtools-emulate-network-conditions-client-id': "C67F89167BF7D55F9EBA8775BF58988",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    'accept': "*/*",
    'referer': "https://app.autogradr.com/assignment/319/project/575",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
    'host': "app.autogradr.com",
    'cache-control': "no-cache",
    
    }

response = s.post(url, data=payload, headers=headers)

#print(response.text)



###########################Checking attempt ##################################

import requests

url = "https://app.autogradr.com/api/attempt"

payload = "{\n  \"assignmentID\": 273,\n  \"questionID\": 515,\n  \"environmentID\": 15,\n   \"files\": [\n        {\n            \"path\": \"solution_fail.zip\",\n            \"checksum\": \"0812ff6e368631047287ea246538b0b3\",\n            \"url\": \"/api/files/0812ff6e368631047287ea246538b0b3\"\n        }\n    ]\n}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    
    }

response = s.post(url, data=payload, headers=headers)

# print(response.text)
# json_response = response.json()

# poll_url = json_response["pollUrl"]


# ###################### Checking poll request #############################

# poll_response = s.get("https://app.autogradr.com"+poll_url)

# print(poll_response.json())



print "Goto https://app.autogradr.com/assignment/273/project/515 to see your result"





