from geopy.geocoders import Nominatim

# Initialisierung des Geokodierungsobjekts
geolocator = Nominatim(user_agent="my_geocoder")

# Adresse für die Geokodierung
adresse = "quickbornstraße 24 hamburg"

# Geokodierung der Adresse
location = geolocator.geocode(adresse)

# Überprüfung der Geokodierungsergebnisse
if location:
    latitude = location.latitude
    longitude = location.longitude
    print(f"Koordinaten von '{adresse}': ({latitude}, {longitude})")
else:
    print("Die Adresse konnte nicht geokodiert werden.")
