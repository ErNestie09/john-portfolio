from flask import Flask, render_template

app = Flask(__name__)

# Homepage
@app.route("/")
def home():
    return render_template("index.html")

# Attractions page
@app.route("/attractions") 
def attractions():
    attractions_list = [
        # --- Beaches, Mountains, Lakes, Dive Spots & Natural Destinations ---
        {"name": "Laiya Beach", "description": "A popular white-sand beach destination in San Juan.", "image": "laiya_beach.jpg", "categories": ["Nature"], "gmap_link": "https://maps.app.goo.gl/Jq8Xefp7M5UvBRo99?g_st=ipc"},
        {"name": "Anilao (Mabini)", "description": "Diving capital of the Philippines located in Mabini/Bauan.", "image": "anilao.jpg", "categories": ["Nature"], "gmap_link": "https://maps.app.goo.gl/WchSg8Bvzz6xK5Zd8"},
        {"name": "Fortune Island", "description": "Island with Greek-style ruins and turquoise waters.", "image": "fortune_island.jpg", "categories": ["Nature"], "gmap_link": "https://maps.app.goo.gl/R4FLJnUGaEgiw2wv8"},
        {"name": "Masasa Beach", "description": "Crystal-clear waters and white sands in Tingloy.", "image": "masasa.jpg", "categories": ["Nature"], "gmap_link": "https://maps.app.goo.gl/jw5voJQrDsR5mX159"},
        {"name": "Matabungkay Beach", "description": "Calm, shallow waters and floating cottages in Lian.", "image": "matabungkay.jpg", "categories": ["Nature"], "gmap_link": "https://maps.app.goo.gl/VSziC5FSS3oa8bYA7?g_st=ipc"},
        {"name": "Stilts Calatagan Beach Resort", "description": "Maldives-style cottages on stilts in Calatagan.", "image": "stilts.jpg", "categories": ["Nature", "Leisure"], "gmap_link": "https://maps.app.goo.gl/HCeM6epbF8qWon1Q8?g_st=ipc"},
        {"name": "Pico de Loro Cove", "description": "Exclusive beachfront community in Nasugbu.", "image": "pico_de_loro.jpg", "categories": ["Nature"], "gmap_link": "https://maps.app.goo.gl/dTxVXFCyWcA3oTTt7?g_st=ipc"},
        {"name": "Layag-Layag Reef", "description": "Snorkeling and diving reef in Nasugbu.", "image": "layag_layag.jpg", "categories": ["Nature"], "gmap_link": "https://maps.app.goo.gl/y2qvQx4CxM9WkgMY7?g_st=ipc"},
        {"name": "Mount Maculot", "description": "Famous for “The Rockies” view deck in Cuenca.", "image": "mount_maculot.jpg", "categories": ["Nature"], "gmap_link": "https://maps.app.goo.gl/9F5VTumMSk7VEAWLA?g_st=ipc"},
        {"name": "Mt. Manabu", "description": "Beginner-friendly hiking trail in Sto. Tomas.", "image": "mt_manabu.jpg", "categories": ["Nature"], "gmap_link": "https://maps.app.goo.gl/gUAZtT9nJVEkVudRA"},
        {"name": "Taal Lake / Taal Volcano", "description": "Unique volcano within a lake within a volcano.", "image": "taal.jpg", "categories": ["Nature"], "gmap_link": "https://maps.app.goo.gl/RtdkqtdiR5jstgLJ7"},
        {"name": "Malaya Campsite", "description": "Nature campsite in Nasugbu.", "image": "malaya_campsite.jpg", "categories": ["Nature"], "gmap_link": "https://maps.app.goo.gl/AunU7trSiVfVGB6o9"},
        {"name": "Wakim Lake & Resort", "description": "Lake attraction in Talisay.", "image": "wakim_lake.jpg", "categories": ["Nature", "Leisure"], "gmap_link": "https://maps.app.goo.gl/PKNTXXiecCrSYfk87?g_st=ipc"},
        {"name": "Batangas Lakelands", "description": "Adventure parks and scenic lake area in Balete.", "image": "batangas_lakelands.jpg", "categories": ["Nature", "Leisure"], "gmap_link": "https://maps.app.goo.gl/C8hxmJxpHWUYsiDt6?g_st=ipc"},
        {"name": "Mountain of Salvation", "description": "Peaceful hiking and pilgrimage site in Pagkilatan.", "image": "mountain_salvation.jpg", "categories": ["Nature"], "gmap_link": "https://maps.app.goo.gl/9BGqC5wPnc2KCnwx9"},

        # --- Heritage Towns, Museums, Churches, Shrines, Landmarks ---
        {"name": "Taal Basilica (Basilica of St. Martin of Tours)", "description": "Largest Catholic church in Asia.", "image": "taal_basilica.jpg", "categories": ["Heritage"], "gmap_link": "https://maps.app.goo.gl/aqiq1PxXf3DJ9Y5j8"},
        {"name": "Cathedral Minor Basilica and Parish of the Immaculate Conception", "description": "Diving sanctuary known for cathedral-like rock structures.", "image": "cathedral.jpg", "categories": ["Heritage"], "gmap_link": "https://maps.app.goo.gl/jcu5vM4mtALJcksQ6?g_st=ipc"},
        {"name": "Montemaria Shrine", "description": "Home of the massive Virgin Mary statue in Batangas City.", "image": "montemaria_shrine.jpg", "categories": ["Heritage"], "gmap_link": "https://maps.app.goo.gl/aqiq1PxXf3DJ9Y5j8"},
        {"name": "Padre Pio Shrine", "description": "National shrine dedicated to St. Padre Pio in Sto. Tomas.", "image": "padre_pio.jpg", "categories": ["Heritage"], "gmap_link": "https://maps.app.goo.gl/ZNoKYByWNefrwzXy9"},
        {"name": "Chapel on the Hill", "description": "Circular chapel with a peaceful ambiance in Nasugbu.", "image": "chapel_on_the_hill.jpg", "categories": ["Heritage"], "gmap_link": "https://maps.app.goo.gl/mKwjT3xBwqsYw1pW6"},
        {"name": "Simbahang Bato", "description": "Church carved from rock formations in Laurel.", "image": "simbahang_bato.jpg", "categories": ["Heritage"], "gmap_link": "https://maps.app.goo.gl/rBxUN5Hx8nTHmhMs5?g_st=ipc"},
        {"name": "Taal Heritage Town", "description": "Town filled with Spanish-era houses and museums.", "image": "taal_heritage.jpg", "categories": ["Heritage"], "gmap_link": "https://maps.app.goo.gl/E1w5eZwFDTV9yB678"},
        {"name": "Mabini Shrine", "description": "Historical site dedicated to Apolinario Mabini.", "image": "mabini_shrine.jpg", "categories": ["Heritage"], "gmap_link": "https://maps.app.goo.gl/G5g82ZHyioxqFrK28"},
        {"name": "Museo de Lipa", "description": "Museum preserving the heritage of Lipa City.", "image": "museo_de_lipa.jpg", "categories": ["Heritage"], "gmap_link": "https://maps.app.goo.gl/z2cX9Punp4AsiNpa9"},
        {"name": "Plaza Mabini Park", "description": "Historical park in Batangas City.", "image": "plaza_mabini.jpg", "categories": ["Heritage"], "gmap_link": "https://maps.app.goo.gl/Aqo8kZszE2XGH5vN8"},
        {"name": "Fantasy World", "description": "Colorful fairytale-like theme park in Lemery.", "image": "fantasy_world.jpg", "categories": ["Heritage"], "gmap_link": "https://maps.app.goo.gl/Z5xtwcWaDUGHpYbA7"},

        # --- Hotels, Staycations, Leisure Destinations ---
        {"name": "Stilts Calatagan Beach Resort", "description": "Dream-like resort with cottages on stilts.", "image": "stilts.jpg", "categories": ["Nature", "Leisure"], "gmap_link": "https://maps.app.goo.gl/669sxB3DQYg5zSrm7"},
        {"name": "Acuatico Beach Resort & Hotel", "description": "Luxury resort in Laiya.", "image": "acuatico.jpg", "categories": ["Nature", "Leisure"], "gmap_link": "https://maps.app.goo.gl/ZebKn9wm1zxJ1qaAA"},
        {"name": "La Virginia Resort", "description": "Theme-inspired resort in Mataas na Kahoy.", "image": "la_virginia.jpg", "categories": ["Leisure"], "gmap_link": "https://maps.app.goo.gl/fUiHd7tEGmW7kmpY6"},
        {"name": "Aiyanar Beach and Dive Resort", "description": "Diving resort in Mabini.", "image": "aiyanar.jpg", "categories": ["Nature", "Leisure"], "gmap_link": "https://maps.app.goo.gl/ZSYGz4UTgSeQbrHKA"},
        {"name": "J Castle", "description": "Castle-themed hotel in Tanauan.", "image": "j_castle.jpg", "categories": ["Leisure"], "gmap_link": "https://maps.app.goo.gl/Hy1RcnkvL3bBKjmk8"},


        # --- Food & Dining ---
        {"name": "TAGGO Grill & Resto", "description": "Grill and Filipino-style dining in Batangas City.", "image": "taggo.jpg", "categories": ["Food & Dining"], "gmap_link": "https://maps.app.goo.gl/tqgaT1H5WioKvjT38"},
        {"name": "Cucina de Jardin", "description": "Garden-style restaurant in Taal with scenic views.", "image": "cucina_de_jardin.jpg", "categories": ["Food & Dining"], "gmap_link": "https://maps.app.goo.gl/Gap6CJ26tzjSSkFy7"},
        {"name": "Prism Restaurant Cafe", "description": "Cozy café and restaurant overlooking Taal Lake.", "image": "prism.jpg", "categories": ["Food & Dining"], "gmap_link": "https://maps.app.goo.gl/TjunTnHBJGQNq31DA"},
        {"name": "MOUSE HOLE Cheesebar X Restaurant", "description": "Cheese-inspired dining with a unique atmosphere.", "image": "mouse_hole.jpg", "categories": ["Food & Dining"], "gmap_link": "https://maps.app.goo.gl/VU2ZXnxABXDcJjLB8"},
        {"name": "El Lago Restaurante", "description": "Lakeside dining with Filipino and international cuisine.", "image": "el_lago.jpg", "categories": ["Food & Dining"], "gmap_link": "https://maps.app.goo.gl/nAhsVjyXcoxsNFcJ6"},
        {"name": "LogHouse Care", "description": "Rustic wooden café and dining in Lipa.", "image": "loghouse.jpg", "categories": ["Food & Dining"], "gmap_link": "https://maps.app.goo.gl/4cyNX14taaqtHhhU6"},
        {"name": "Butch Seafood & Grill Restaurant", "description": "Classic seafood and Filipino grilled specialties.", "image": "butch.jpg", "categories": ["Food & Dining"], "gmap_link": "https://maps.app.goo.gl/2Jj2DDDgy5SCL3ge8"},
        {"name": "Fat Grill Restaurant", "description": "Casual dining spot known for grilled dishes.", "image": "fat_grill.jpg", "categories": ["Food & Dining"], "gmap_link": "https://maps.app.goo.gl/adWfDVifi7879xPV6"},
        {"name": "Tree House Restaurant", "description": "Batangas City landmark serving Filipino favorites.", "image": "tree_house.jpg", "categories": ["Food & Dining"], "gmap_link": "https://maps.app.goo.gl/dT32ArFDXK4aq1cSA"},
        {"name": "MOGU Unlimited Hot Pot", "description": "Unlimited hot pot dining in Malvar.", "image": "mogu.jpg", "categories": ["Food & Dining"], "gmap_link": "https://maps.app.goo.gl/B3wZePdnqtQybAFRA"},
        {"name": "Johanna’s Grille", "description": "Popular grill restaurant known for hearty Filipino meals.", "image": "johannas.jpg", "categories": ["Food & Dining"], "gmap_link": "https://maps.app.goo.gl/3SDVWpxz4WGmHD4R9"},
        {"name": "Lipa Grill", "description": "Classic Filipino dishes in Lipa City.", "image": "lipa_grill.jpg", "categories": ["Food & Dining"], "gmap_link": "https://maps.app.goo.gl/q9H3RhJbtSq8pHFH9"},
        {"name": "Lolo’s Place Restaurant", "description": "Home-style Filipino comfort food in Batangas City.", "image": "lolos_place.jpg", "categories": ["Food & Dining"], "gmap_link": "https://maps.app.goo.gl/gDQsxnKjXV2bBCBP9"},
        {"name": "The Beehive", "description": "Cozy café in Lipa offering pastries and drinks.", "image": "beehive.jpg", "categories": ["Food & Dining"], "gmap_link": "https://maps.app.goo.gl/uDQh6JUwzuvBLNTXA"},
        {"name": "Wanam Sa Bukid", "description": "Nature-inspired dining experience surrounded by greenery.", "image": "wanam_sa_bukid.jpg", "categories": ["Food & Dining"], "gmap_link": "https://maps.app.goo.gl/AJzFUhJDgBBpvz4t9"},
        {"name": "Pamana Locale", "description": "Authentic Batangueño dishes and cultural ambiance.", "image": "pamana_locale.jpg", "categories": ["Food & Dining"], "gmap_link": "https://maps.app.goo.gl/5KNFD7nRDthh4S656"},
        {"name": "Rose and Grace Restaurant", "description": "Famous Filipino restaurant in Santo Tomas.", "image": "rose_and_grace.jpg", "categories": ["Food & Dining"], "gmap_link": "https://maps.app.goo.gl/47ciE92RLXGTKp9S9"},

        # --- Pasalubong & Local Products ---
        {"name": "Batangas Coffee, Grains, & Pasalubong Center", "description": "Coffee beans, pasalubong items, and local delicacies.", "image": "batangas_coffee.jpg", "categories": ["Pasalubong"], "gmap_link": "https://maps.app.goo.gl/Tg3FT6nQGAMPiu4g9"},
        {"name": "Lipa Pasalubong Center", "description": "Popular pasalubong stop offering local goods.", "image": "lipa_pasalubong.jpg", "categories": ["Pasalubong"], "gmap_link": "https://maps.app.goo.gl/tBA3bu1XikxMfHRC7"},
        {"name": "Sweet Temptations Homemade Sweets", "description": "Homemade sweets and pasalubong favorites.", "image": "sweet_temptations.jpg", "categories": ["Pasalubong"], "gmap_link": "https://maps.app.goo.gl/KTzxyZ2681Aoj2uG6"},
        {"name": "Babe’s Buko Pie", "description": "Famous Malvar-made buko pies and delicacies.", "image": "babes_buko_pie.jpg", "categories": ["Pasalubong"], "gmap_link": "https://maps.app.goo.gl/sg5p8aB32TABuEuu5"},
        {"name": "Pasalubong Souvenir and Cafe", "description": "Cafe and souvenir shop offering local products.", "image": "lobo_pasalubong.jpg", "categories": ["Pasalubong"], "gmap_link": "https://maps.app.goo.gl/jF77f7M5a6Xt1kta7"},
        {"name": "Ala Eh Sweets", "description": "Local sweets and delicacies from Lipa City.", "image": "alaeh_sweets.jpg", "categories": ["Pasalubong"], "gmap_link": "https://maps.app.goo.gl/fKzjfmMEyQDetVaP7"},
        {"name": "Gracia’s Batangas Pasalubong", "description": "Serves the best of Batangas—with bonus favorites from Baguio to Davao all in one stop.", "image": "gracias_batangas.jpg", "categories": ["Pasalubong"], "gmap_link": "https://maps.app.goo.gl/W4vTD8orz7qdriBQ8"},
    ]

    return render_template("attractions.html", attractions=attractions_list)


if __name__ == "__main__":
    app.run(debug=True)
