import folium

# Daten für den Stadt-/Straßenplan und die Punktzahlen der Gebiete
# Beispiel-Daten (kann entsprechend Ihren Daten angepasst werden)
stadtplan_daten = "./landkreise_simplify0.geojson"
punktzahlen_daten = {
    "Gebiet1": 10
}

zentrum = [53.5801094, 9.960519932829179]

# Erstellen der Grundkarte
karte = folium.Map(location=zentrum, zoom_start=13)

# Overlay erstellen und hinzufügen
for gebiet, punktzahl in punktzahlen_daten.items():
    farbe = None
    if punktzahl > 7:
        farbe = 'red'
    elif punktzahl > 3:
        farbe = 'yellow'
    else:
        farbe = 'green'
    
    # Beispiel-Koordinaten für das Overlay (kann entsprechend Ihren Daten angepasst werden)
    overlay_coords = [
        [53.5791094, 9.959519932829179],
        [53.5791094, 9.961519932829179],
        [53.5811094, 9.961519932829179],
        [53.5811094, 9.959519932829179]
    ]
    
    folium.Polygon(
        locations=overlay_coords,
        color=farbe,
        fill=True,
        fill_color=farbe,
        fill_opacity=0.4
    ).add_to(karte)

# Aktuellen Standort hinzufügen
folium.Marker(
    location=zentrum,
    icon=folium.Icon(color='blue', icon='info-sign')
).add_to(karte)

# Karte anzeigen oder speichern
karte.save("karte.html")