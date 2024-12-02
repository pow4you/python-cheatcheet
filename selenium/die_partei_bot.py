from torrequest import TorRequest


tr = TorRequest()

tr.reset_identity() #Reset Tor
response= tr.get('http://ipecho.net/plain')
print ("New Ip Address",response.text)