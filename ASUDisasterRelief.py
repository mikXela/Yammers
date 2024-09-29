import folium
import pandas as pd



# Define the coordinates of ASU Tempe Campus
asu_tempe_coords = [33.4219999, -111.9400044]

# Create a Folium map centered on ASU Tempe Campus
map_asu = folium.Map(location=asu_tempe_coords, zoom_start=15)

#turn csv into PANDAS table and read markers
table = pd.read_csv("ASU Disaster Relief - Sheet1.csv")

print(table.head())
#print(table.size)
for i in range (2,len(table)):
    x = table.loc[i, 'X']
    y = table.loc[i,'Y']
    name = table.loc[i,'Location']

    if table.loc[i, 'Overall'] >= 8:
        icon_image = "easy.png"
    elif table.loc[i, 'Overall'] >= 6:
        icon_image = "hard.png"
    elif table.loc[i, 'Overall'] >= 4:
        icon_image = "insane.png"
    else:
        icon_image = "extreme.png"

    icon = folium.CustomIcon(
    icon_image,
    icon_size=(30, 30),
    )

    folium.Marker(
        location = [x,y],
        icon=icon,
        popup=name
    ).add_to(map_asu)

# Add a marker to the map for ASU Tempe Campus

"""folium.Marker(
    location=asu_tempe_coords,
    popup="ASU Tempe Campus",
    tooltip="ASU Tempe Campus"
).add_to(map_asu)"""

#bathroom search
#
# Display the map
map_asu.save("disaster_relief.html")
