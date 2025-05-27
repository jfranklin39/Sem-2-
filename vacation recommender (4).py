import random
from PIL import Image
import requests
from io import BytesIO

# Name of each city
Places = [
    "New York City", "Los Angeles", "San Francisco", "Vancouver", "Montreal", "Cancun", "Boston",
    "Toronto", "New Orleans", "San Jose", "Paris", "Rome", "Barcelona", "Amsterdam", "London",
    "Berlin", "Madrid", "Lisbon", "Edinburgh", "Zurich", "Milan", "Geneva", "Munich", "Brussels",
    "Tokyo", "Bali", "Hong Kong", "Seoul", "Dubai", "Ho Chi Minh City", "Hanoi", "Buenos Aires",
    "Rio de Janeiro", "Sydney", "Auckland"
]
#The average weather throughout the year
weather = [
    "cold", "warm", "medium", "cold", "cold", "warm", "cold", "cold", "warm", "warm", "medium",
    "medium", "warm", "cold", "cold", "cold", "warm", "warm", "cold", "cold", "medium", "cold",
    "cold", "cold", "cold", "medium", "warm", "warm", "medium", "warm", "warm", "warm", "warm",
    "warm", "warm"
]
#Average cost it takes to fly from a major city in the United States
cost = [
    300, 250, 270, 350, 380, 450, 280, 320, 200, 500, 600, 650, 700, 700, 650, 750, 700, 750, 750,
    800, 700, 800, 750, 700, 1200, 1000, 850, 950, 1000, 950, 900, 1200, 1100, 1200, 1300
]

# The links to an image of each city
images = ["https://media.cntravellerme.com/photos/648c35b151562a659243e075/16:9/w_1920%2Cc_limit/New%2520York%2520City_GettyImages-1347979016.jpg","https://www.extraspace.com/blog/wp-content/uploads/2018/11/living-in-los-angeles-670x450.jpg","https://cdn.britannica.com/51/178051-050-3B786A55/San-Francisco.jpg","https://media.timeout.com/images/106148123/image.jpg","https://www.usatoday.com/gcdn/authoring/authoring-images/2024/08/14/USAT/74794361007-36472-credit-fr-loic-romer-tourisme-montreal-en-credit-loic-romer-tourisme-montreal.jpg?crop=3988,2989,x0,y0","https://www.delphinusworld.com/hubfs/Hint-Blogs%20Octubre%202021/panoramica-cancun.jpg","https://www.travelandleisure.com/thmb/_aMbik8KZYsUKc_6_XNeAOzPi84=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/boston-massachusetts-BOSTONTG0221-719aef2eeb1c4929b6c839715e34a69e.jpg","https://www.toronto.ca/wp-content/uploads/2024/08/9693-Local-Services-Tile-960x560-1.jpg","https://i.natgeofe.com/n/54ed439a-13e9-4e8e-aaac-19df3289bb4e/neworleans_dsc2493_hr.jpg","https://delivery.gfobcontent.com/api/public/content/04607f00586c498e8913eb881e39bd90?v=4b65f644","https://media-cdn.tripadvisor.com/media/photo-c/1280x250/17/15/6d/d6/paris.jpg","https://cdn.audleytravel.com/4008/2863/79/1018521-rome-skyline-italy.jpg","https://img1.10bestmedia.com/Images/Photos/378847/GettyImages-1085317916_54_990x660.jpg?auto=webp&width=3840&quality=75","https://worldjewishtravel.org/wp-content/uploads/amsterdam_city.jpg","https://www.visitlondon.com/-/media/images/london/visit/things-to-do/sightseeing/london-attractions/tower-bridge/towerbridge-640x360.jpg?mw=800&rev=8bf9c817401a4d4bb7f3a63d62e0778b&hash=F1ADED12BEE11589534511887D6BFEA9","https://i.natgeofe.com/n/b234ec7d-a988-4b75-9e65-749ddcbea7a0/citylife_berlin_2B4H3T1_web_2x1.jpg","https://img.static-kl.com/images/media/65848EF5-2848-4EA7-BE113130180A0A55","https://images.goway.com/production/styles/hero_s1_2xl/s3/hero/iStock-1137863101.jpg?h=08f4e768&itok=_EdrR9FN","https://media.cntraveller.com/photos/611be9e3d5b6f5a4a3def392/16:9/w_2560%2Cc_limit/Mountain-view-over-city-Edinburgh-scotland-conde-nast-traveller-28july17-iStock.jpg","https://lp-cms-production.imgix.net/2021-08/shutterstockRF_314150237.jpg?w=1095&fit=crop&crop=faces%2Cedges&auto=format&q=75","https://afar.brightspotcdn.com/dims4/default/4b8536a/2147483647/strip/true/crop/3800x2016+209+0/resize/1440x764!/quality/90/?url=https%3A%2F%2Fk3-prod-afar-media.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fb6%2Ff6%2Fa962dc37472c96f3220c5cc761df%2Fmilan-travel-guide-lede-michelle-heimerman.jpg","https://www.grayline.com/wp-content/uploads/2025/02/Gray-Line-Geneva-Switzerland-2-scaled.jpg","https://a.travel-assets.com/findyours-php/viewfinder/images/res70/501000/501501-munich.jpg","https://statemag.state.gov/wp-content/uploads/2024/01/0224POM-4-scaled.jpg","https://www.gotokyo.org/en/plan/tokyo-outline/images/main.jpg","https://www.outlooktravelmag.com/media/bali-tg.png","https://ik.imgkit.net/3vlqs5axxjf/external/ik-seo/http://images.ntmllc.com/v4/destination/Hong-Kong/Hong-Kong-city/112086_SCN_HongKong_iStock466733790_Z8C705/Hong-Kong-Scenery.jpg?tr=w-656%2Ch-390%2Cfo-auto","https://silversea-discover.imgix.net/2022/12/QCRUa0gV-2asunsetinSeoulskyline_1490190263.jpg?auto=compress%2Cformat&ixlib=php-3.3.1","https://cdn.britannica.com/15/189715-050-4310222B/Dubai-United-Arab-Emirates-Burj-Khalifa-top.jpg","https://lp-cms-production.imgix.net/2021-01/shutterstockRF_718619590.jpg","https://images.travelandleisureasia.com/wp-content/uploads/sites/3/2024/07/03150728/Hanoi-Itinerary-9.jpg","https://images.squarespace-cdn.com/content/v1/52efc94ae4b01409c74273d6/1585836711975-N7XHQ1OEB1VT1Q28Y0NP/BuenosAires-1815x1200.jpg","https://southquestsafaris.com/wp-content/uploads/2023/10/shutterstock_421013719.jpg","https://content.r9cdn.net/rimg/dimg/12/98/b1e36771-city-2258-163f4d7f814.jpg?crop=true&width=1020&height=498","https://www.travelandleisure.com/thmb/dQxH74Jlg6DggoHbo-ZMEvMhIFA=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/auckland-city-AUCKLANDTG0621-c9f8c81db1274fd99821dd508cc7aff8.jpg"]  # keep full list of URLs

#This is the function to open an image
def open_image(url):
    try:
        response = requests.get(url, timeout=5)
        img = Image.open(BytesIO(response.content))
        img.show()
    except Exception as e:
        print(f"Could not open image from URL: {url}\nError: {e}")
#This filters searches for the weather type and prints it
def filter_places_by_weather(weather_condition):
    # Print a header message
    print("\nCities with '" + weather_condition + "' weather:")

    # Keep track of whether we find any matching cities
    found = False

    # Loop through the lists together
    for i in range(len(Places)):
        place = Places[i]
        weather_type = weather[i]
        img = images[i]

        # Check if the weather matches (ignoring upper/lower case)
        if weather_type.lower() == weather_condition.lower():
            found = True
            print("\n" + place)
            open_image(img)

    # If no city was found, print a message
    if found == False:
        print("No cities found with that weather condition.")

#This filter shows information about each city
def view_all_cities():
    # Print a title
    print("\nAll Cities:")

    # Go through each city one by one using a basic loop
    for i in range(len(Places)):
        place = Places[i]
        img = images[i]
        temp = weather[i]
        price = cost[i]

        # Print the city info
        print("\nPlace: " + place)
        print("Weather: " + temp)
        print("Cost: $" + str(price))

        # Show the city image
        open_image(img)

        # Pause before showing the next city
        input("Press Enter to see next city...")

#This is the main menu for the program
def menu():
    while True:
        print("\n Travel Destination Menu")
        print("1. Search by City")
        print("2. Filter by Weather (Warm, Cold, Medium)")
        print("3. View All Cities")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            city = input("Enter city name: ").strip()
            if city in Places:
                index = Places.index(city)
                print(f"\n{city}")
                open_image(images[index])
                print(f"Weather: {weather[index]}")
                print(f"Cost (approx.): ${cost[index]}")
            else:
                print("City not found.")
        elif choice == "2":
            weather_condition = input("Enter weather (cold, warm, medium): ").strip().lower()
            if weather_condition in {"cold", "warm", "medium"}:
                filter_places_by_weather(weather_condition)
            else:
                print("Invalid weather condition.")
        elif choice == "3":
            view_all_cities()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-4.")

# --- Run the program ---

menu()
