import json

f = open('info.json', 'r')
content = f.read()
info = json.loads(content)
f.close()
server = info['server']
domainName = info['domainName']