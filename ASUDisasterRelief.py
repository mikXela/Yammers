import folium
from folium.plugins import Search
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
    description = (
    "<h1>" + name + "</h1><br>" +
    "Overall: " + str(table.loc[i, "Overall"]) + "<br>" +
    "Stall Space: " + str(table.loc[i, 'Stall Space']) + "<br>" +
    str(table.loc[i, 'Stall Space Description']) + "<br>" +
    "Cleanliness: " + str(table.loc[i, 'Cleanliness']) + "<br>" +
    str(table.loc[i, 'Cleanliness Description']) + "<br>" +
    "Privacy: " + str(table.loc[i, 'Privacy']) + "<br>" +
    str(table.loc[i, 'Privacy Description']) + "<br>" +
    "Smell: " + str(table.loc[i, 'Smell']) + "<br>" +
    str(table.loc[i, 'Stench Description'])
)


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
        popup = folium.Popup(description, max_width=500),
        tooltip=name
    ).add_to(map_asu)


folium.LayerControl.add_to(map_asu)

# Display the map
map_asu.save("disaster_relief.html")
