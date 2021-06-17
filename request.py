import requests

url ="http://localhost:5000/predict_api"
r= requests.post(url,json={"Day":13,"month":3,"year":1986,"open":3600})

print(r.json())