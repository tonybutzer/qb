# python 3
import urllib.request
import xml.etree.ElementTree as ET

requestXML = """
<?xml version="1.0"?>
<AddressValidateRequest USERID="7705BOLDCJ729">
	<Revision>1</Revision>
	<Address ID="0">
		<Address1>2335 S State</Address1>
		<Address2>Suite 300</Address2>
		<City>Provo</City>
		<State>UT</State>
		<Zip5>84604</Zip5>
	</Address>
</AddressValidateRequest>
"""

#prepare xml string doc for query string
docString = requestXML
docString = docString.replace('\n','').replace('\t','')
docString = urllib.parse.quote_plus(docString)

url = "http://production.shippingapis.com/ShippingAPI.dll?API=Verify&XML=" + docString
print(url + "\n\n")

response = urllib.request.urlopen(url)
if response.getcode() != 200:
	print("Error making HTTP call:")
	print(response.info())
	exit()

contents = response.read()
print(contents)

root = ET.fromstring(contents)
for address in root.findall('Address'):
	print()
	print("Address1: " + address.find("Address1").text)
	print("Address2: " + address.find("Address2").text)
	print("City:	 " + address.find("City").text)
	print("State:	" + address.find("State").text)
	print("Zip5:	 " + address.find("Zip5").text)

