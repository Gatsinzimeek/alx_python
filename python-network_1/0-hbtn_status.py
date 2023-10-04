import requests

resp = requests.get('https://alu-intranet.hbtn.io/status')

print(f'- type: {type(resp.content)}$')
print(f'- content: {resp.text}$')