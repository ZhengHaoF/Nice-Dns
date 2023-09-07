import json

f = open('info.json', 'r')
content = f.read()
info = json.loads(content)
f.close()
dnsListRow = info['dns']
domainListRow = info['domain']