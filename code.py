import csv

rows = []

with open ("data.csv", "r") as f:
    a = csv.reader(f)
    for row in a:
        rows.append(row)


headers = rows[0]
planet_data_rows = rows[1:]

# print(headers)
# print(planet_data_rows[0])


headers[0] = "row_num" 


solar_system_planet_count = {}

for planet_data in planet_data_rows:
    if solar_system_planet_count.get(planet_data[11]) :
        solar_system_planet_count[planet_data[11]] += 1
    else:
        solar_system_planet_count[planet_data[11]] = 1

max_ss = max(solar_system_planet_count, key = solar_system_planet_count.get)

print("The solar system " , max_ss , ", has maximun planets -" , solar_system_planet_count[max_ss]) 


temp_planet_data_rows = list(planet_data_rows)

for planet_data in temp_planet_data_rows:
    planet_mass = planet_data[3]
    if planet_mass.lower() == "unknown":
        planet_data_rows.remove(planet_data)
        continue
    else:
        planet_mass_value = planet_mass.split(" ")[0]
        planet_mass_ref = planet_mass.split(" ")[1]
        if planet_mass_ref == "Jupiters":
            planet_mass_value = float(planet_mass_value) * 317.8
        planet_data[3] = planet_mass_value

    planet_radius = planet_data[7]
    if planet_radius.lower() == "unknown":
        planet_data_rows.remove(planet_data)
        continue
    else:
        planet_radius_value = planet_radius.split(" ")[0]
        planet_radius_ref = planet_radius.split(" ")[2]
    if planet_radius_ref == "Jupiter":
        planet_radius_value = float(planet_radius_value) * 11.2
    planet_data[7] = planet_radius_value

print(len(planet_data_rows))


# 19.4 Jupiters

# 1.08 x Jupiter


















