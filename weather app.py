import requests
import ipywidgets as widgets
from IPython.display import display

cities = [
    "Anantapur", "Chittoor", "East Godavari", "Ahmedabad", "Amreli", "Bharuch",
    "Kheda (Nadiad)", "Vadodara", "Valsad", "Surendranagar", "Surat", "Rajkot", "Patan",
    "Navsari", "Narmada", "Morbi", "Mehsana", "Junagadh", "Jamnagar", "Gir Somnath",
    "Dahod", "Dang", "Devbhoomi Dwarka", "Gandhinagar", "Botad", "Bhavn", "Bilaspur",
    "Chamba", "Hamirpur", "Kangra", "Kinnaur", "Kullu", "Lahaul and Spiti", "Mandi",
    "Shimla", "Sirmaur", "Solan", "Una", "Bokaro", "Chatra", "Deoghar", "Dhanbad",
    "Dumka", "Garhwa", "Giridih", "Godda", "Gumla", "Hazaribagh", "Jamtara", "Khunti",
    "Koderma", "Latehar", "Lohardaga", "Pakur", "Palamu", "Ramgarh", "Ranchi", "Sahibganj",
    "Seraikela Kharsawan", "Simdega", "West Singhbhum", "Bagalkot", "Bangalore Rural",
    "Bangalore Urban", "Belgaum", "Bellary", "Bidar", "Vijayapura", "Chamarajanagar",
    "Chikmagalur", "Chitradurga", "Dakshina Kannada", "Davanagere", "Dharwad", "Gadag",
    "Gulbarga", "Hassan", "Haveri", "Kodagu", "Kolar", "Koppal", "Mandya", "Mysore", "Raichur",
    "Ramanagara", "Shimoga", "Tumkur", "Udupi", "Uttara Kannada", "Yadgir", "Alappuzha",
    "Ernakulam", "Idukki", "Kannur", "Kasaragod", "Kollam", "Kottayam", "Kozhikode",
    "Malappuram", "Palakkad", "Pathanamthitta", "Thiruvananthapuram", "Thrissur", "Wayanad",
    "Agar Malwa", "Alirajpur", "Anuppur", "Ashoknagar", "Balaghat", "Barwani", "Betul",
    "Bhind", "Bhopal", "Burhanpur", "Chhatarpur", "Chhindwara", "Damoh", "Datia", "Dewas",
    "Dhar", "Dindori", "Guna", "Gwalior", "Harda", "Hoshangabad", "Indore", "Jabalpur",
    "Jhabua", "Katni", "Khandwa", "Khargone", "Mandla", "Mandsaur", "Morena", "Narsinghpur",
    "Neemuch", "Panna", "Raisen", "Rajgarh", "Ratlam", "Rewa", "Sagar", "Satna", "Sehore",
    "Seoni", "Kota", "Sikar", "Sirohi", "Sri Ganganagar", "Tonk", "Udaipur", "Ajmer", "Alwar",
    "Banswara", "Baran", "Barmer", "Bharatpur", "Bhilwara", "Bikaner", "Bundi", "Chittorgarh",
    "Churu", "Dausa", "Dholpur", "Dungarpur", "Hanumangarh", "Jaipur", "Jaisalmer", "Jalore",
    "Jhalawar", "Jhunjhunu", "Jodhpur", "Karauli", "Nagaur", "Pali", "Pratapgarh", "Rajsamand",
    "Sawai Madhopur", "Sikar", "Sirohi", "Sri Ganganagar", "Tonk", "Udaipur", "East Sikkim",
    "North Sikkim", "South Sikkim", "West Sikkim", "Ariyalur", "Chengalpattu", "Chennai",
    "Coimbatore", "Cuddalore", "Dharmapuri", "Dindigul", "Erode", "Kallakurichi", "Kanchipuram",
    "Kanyakumari", "Karur", "Krishnagiri", "Madurai", "Mayiladuthurai", "Nagapattinam",
    "Namakkal", "Nilgiris", "Perambalur", "Pudukkottai", "Ramanathapuram", "Ranipet", "Salem",
    "Sivaganga", "Tenkasi", "Thanjavur", "Theni", "Thoothukudi", "Tiruchirappalli", "Tirunelveli",
    "Tirupattur", "Tiruppur", "Tiruvallur", "Tiruvannamalai", "Vellore", "Viluppuram", "Virudhunagar",
    "Dhalai", "Gomati", "Khowai", "North Tripura", "Sepahijala", "South Tripura", "Unakoti",
    "West Tripura", "Agra", "Aligarh", "Ambedkar Nagar", "Amethi", "Amroha", "Auraiya", "Ayodhya",
    "Azamgarh", "Baghpat", "Bahraich", "Ballia", "Balrampur", "Banda", "Barabanki", "Bareilly",
    "Basti", "Bhadohi", "Bijnor", "Budaun", "Bulandshahr", "Chandauli", "Chitrakoot", "Deoria",
    "Etah", "Etawah", "Farrukhab"
]

def get_weather(change):
    city = com.value
    if not city:
        result_label.value = "Please select a city."
        return
    
    api_key = '253682c0bd759acfb4255d4aa08c3dd7'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        temperature_kelvin = data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        temperature_fahrenheit = (temperature_kelvin - 273.15) * 9/5 + 32
        humidity = data['main']['humidity']
        weather_condition = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        pressure = data['main']['pressure']
        country_code = data['sys']['country']
        city_with_country = f"{city}, {country_code}"
        
        result_label.value = f"City: {city_with_country}\nTemperature: {temperature_celsius:.2f} °C / {temperature_fahrenheit:.2f} °F\nHumidity: {humidity}%\nWeather Condition: {weather_condition}\nWind Speed: {wind_speed} m/s\nPressure: {pressure} hPa"
    except requests.exceptions.RequestException as e:
        result_label.value = f"Error: {e}"
    except KeyError as e:
        result_label.value = "Error: Data format incorrect, please try again."

def on_key_release(change):
    value = change.new
    if value:
        matches = [city for city in cities if value.lower() in city.lower()]
        listbox_update(matches)
    else:
        listbox_update([])

def listbox_update(matches):
    listbox.options = matches

def on_select(change):
    selected_city = listbox.value
    if selected_city:
        com.value = selected_city
        listbox_update([])

com = widgets.Combobox(options=cities)
com.observe(on_key_release, names='value')

listbox = widgets.Select()
listbox.observe(on_select, names='value')

done_button = widgets.Button(description="Get Weather")
done_button.on_click(get_weather)

result_label = widgets.Label()

display(com, listbox, done_button, result_label)
