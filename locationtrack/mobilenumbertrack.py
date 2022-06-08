from phonenumbers import geocoder ,carrier
import phonenumbers
from opencage.geocoder import OpenCageGeocode
#country show
numb=phonenumbers.parse("+91") #phone number
yourLocation=geocoder.description_for_number(numb,"en")
print(yourLocation)
#service provider inforamtion
print(carrier.name_for_number(numb,"en"))
key="api key your " # https://opencagedata.com loin past your api key
geocoder=OpenCageGeocode(key)
qurt=str(yourLocation)
res=geocoder.geocode(qurt)
mog=res[0]['geometry']['lat']
mog1=res[0]['geometry']['lng']
print(mog,mog1)
