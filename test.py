from urllib.request import urlopen , Request
import json
import time

req = Request("http://api.open-notify.org/iss-now.json")

# def SendCordination(rel):
# 	response = urlopen(rel)

# 	data = json.loads(response.read())
# 	#print(data)

# 	longitude = data["iss_position"]["longitude"]
# 	latitude = data["iss_position"]["latitude"]

# 	# Convert to float if you need them as numbers ins	tead of strings
# 	longitude_float = float(longitude)
# 	latitude_float = float(latitude)

# 	print(f"Longitude: {longitude}")
# 	print(f"Latitude: {latitude}")
# 	time.sleep(1)


def SendCordination2(ref):	
	while(True):
		response = urlopen(ref)

		data = json.loads(response.read())
		#print(data)

		longitude = data["longitude"]
		latitude = data["latitude"]
		altitude = data["altitude"]
		velocity = data["velocity"]

		# Convert to float if you need them as numbers ins	tead of strings
		longitude_float = float(longitude)
		latitude_float = float(latitude)
		altitude_float = float(altitude)
		velocity_float = float(velocity)

		print(f"Longitude: {longitude}")
		print(f"Latitude: {latitude}")
		print(f"Altitude: {altitude}")
		print(f"Velocity: {velocity}")
		time.sleep(5)
	return longitude_float, latitude_float , altitude_float, velocity_float

#fetch the crew data :
# print("===================first=============================")
# SendCordination(req)
req = Request("https://api.wheretheiss.at/v1/satellites/25544")
print("======================new Ip==========================")
SendCordination2(req)

def sendIssNames(req2):
	req2 = Request("http://api.open-notify.org/astros.json")
	response2 = urlopen(req2)

	data2 = json.loads(response2.read())
	print(data2)

	People_List = data2["people"]

	print(People_List)


#print(obj['timestamp'])
#print(obj['iss_position']['latitude'], obj['data']['iss_position']['latitude'])

# Example prints:
#   1364795862
#   -47.36999493 151.738540034
