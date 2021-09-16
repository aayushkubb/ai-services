Template to create simple request of your AI models.

# How to use

Install required packages

## Run Service
python 

## Run using
!curl --request POST \
--url http://localhost:5000/post \
--header "Content-Type:application/json" \
--data '{"data":"Any data can be shared here"}'


import requests
files ='{"data":"Any data can be shared here"}'
response = requests.post('http://localhost:5000/post', data=files)
response.json()
