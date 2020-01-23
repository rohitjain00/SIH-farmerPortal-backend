import pymongo


from app.main import db


"""
    Script for adding all major crops and districts in Database 
        (new collection for 'districts'  needs to be added) 
"""


crop = ['Cotton','Soyabean','Red Grams','Ground Nut Seed','Groundnut','Paddy(Dhan)','Bengal Grams(Gram)','Coriander','Tamarind Fruit','Sunflower','Coconut','Gur(Jaggery)','Tomato','Groundnut (Split)','Sunflower Seed','Groundnut pods (raw)','Gwar','Jowar(Sorgham)','Moath Dal','Mustard','Turmeric','Banana - Green','Papaya','Gingelly (Sesamum, Sesame, Til) ','Banana','Orange','Lemon','Copra','Cashewnuts','Dry Chillies','Bajra(Pearl Millet)','Black Grams (Urd Beans)','Rice','Apple','Grapes','Guava','Karbuja','Mousambi','Pomegranate','Water Melon','Beetroot','Bhindi(Ladies Finger)','Bitter gourd','Bottle gourd','Brinjal','Cabbage','Capsicum','Carrot','Cauliflower','Cluster beans','Cucumbar','Drumstick','Green Chilly','Potato','Pumpkin','Raddish','Ridgeguard','Onion','Field Pea','French Beans (Frasbean)','Snakeguard','Maize','Green Grams (Moong)','Yam','Castor Seed','Ajwan','Safflower','Ox','Jute','Ginger','Ragi (Finger Millet)',
'Beans','Green Gram Dal','Masur Dal','Mustard Oil','Wheat Atta','Arecanut(Betelnut/Supari)','Indian Beans (Seam)','Other Vegetable','Arhar (Tur)','Beaten Rice','Betal Leaves','Garlic','Green Peas','Squash(Chappal Kadoo)','Mahua','Other Oil Seed','Peas(Dry)','Linseed','Wheat','Niger Seed (Ramtil)','Tobacco','Amla','Chilly Capsicum','Elephant Yam (Suran)','Green ginger','Onion Green','Papaya (Raw)','Pointed gourd (Parval)','Rat Tail Radish (Mogari)','Surat Beans (Papadi)','Sweet Potato','Toria','Turmeric (raw)','Yam (Ratalu)','Amaranthus','Methi','Mint(Pudina)','Spinach','Big Gram','Corriander seed','Cummin Seed(Jeera)','MethiSeeds','Sesamum(Sesame,Gingelly,Til)',
'Marygold(Calcutta)','Rose(Loose)','Rajgir','Soanf','Cowpea(Veg)','Tinda','Barley (Jau)','Cowpea (Lobia)(Asparagus)','Lime','Little gourd (Kundru)','Mango','Pegeon Pea (Arhar Fali)','Horses Gram','Sponge gourd','Raya','Isabgul (Psyllium)','Cucumber (Long Melon)','Peas Wet','Chili Red','Peas cod','Chikoos(Sapota)','Kinnow','Fish','Pears','Leafy Vegetable','Pine Apple','Seetapal','Ber (Zizyphus)','Indian Colza(Sarson)','Turnip','Knool Khol','Mashrooms','Suram','Lotus Sticks','Sugar','Dalda','Maida Atta','Soji','Alasande Gram','Avare Dal','Black pepper','Chennangidal','Alsandikai','Bunch Beans','Chapparad Avare','Green Avare (W)','Seemebadnekai','Suvarna Gadde','Thondekai','Sheep','Navane','Tender Coconut','Soapnut','Tamarind Seed','Sweet Pumpkin','Amphophalus','Ashgourd','Coconut Oil','Colacasia','Gingelly Oil','Mango (Raw-Ripe)','Tapioca','Galgal(Lemon)','Round gourd','Cardamoms','Cloves','Cocoa','Coffee','Mace','Nutmeg','Rubber','Tea','Coconut Seed','Pepper ungarbled','Duster Beans','Millets','Lentil(Masur)','Kabuli Chana(Chickpeas-White)','Sweet Lime','Mataki','Cock','Hen','Karamani','Gram Raw(Chholia)','Season Leaves','Musk Melon','Taramira','T.V. Cumbu','Thinai (Italian Millet)','Varagu','Same/Savi','Ghee','Jack Fruit']

district_name = ['Adilabad','Anantapur','Chittor','Cuddapah','East Godavari','Guntur','Hyderabad','Karimnagar','Khammam','Krishna','Kurnool','Mahbubnagar','Medak','Nalgonda','Nellore','Nizamabad','Prakasam',
'Ranga Reddy Dist.','Srikakulam','Vijayanagaram','Visakhapatnam','Warangal','WestGodavari','Barpeta','Cachar','Darrang','Hailakandi','Kamrup','Bastar','Bilaspur','Dhamtari','Janjgir','Jashpur','Kawardha','Mahasamund','North Bastar','Raigarh','Raipur','Rajnandgaon','Surguja',
'Ahmedabad','Amreli','Banaskanth','Bharuch','Dahod','Gandhinagar','Jamnagar','Junagarh','Kachchh',
'Mehsana','Narmada','Navsari','Patan','Rajkot','Sabarkantha','Surat','Surendranagar',
'Vadodara(Baroda)','Bhiwani','Faridabad','Fatehabad','Gurgaon','Hissar','Jhajar','Karnal',
'Kurukshetra','Mahendragarh-Narnaul','Mewat','Sirsa','Yamuna Nagar','Kangra',
'Kangra (at Dharmashala)','Kullu','Mandi','Una','Jammu','Udhampur','Dumka','Giridih','Godda','Hazaribagh','Lohardaga','Pakur','Palamu','Ranchi','Saraikela(Kharsanwa)','Bagalkot','Bangalore','Belgaum','Bellary','Bidar','Bijapur','Chamrajnagar','Chikmagalur','Chitradurga','Davangere','Dharwad',
                 'Gadag','Gulbarga','Hassan','Haveri','Karwar(Uttar Kannad)','Kolar','Koppal','Madikeri(Kodagu)','Mandya',
                 'Mangalore(Dakshin Kannad)','Mysore','Raichur','Shimoga','Tumkur','Udupi','Alappuzha','Ernakulam',
                 'Idukki','Kannur','Kasargod','Kollam','Kottayam','Kozhikode(Calicut)','Malappuram','Palakad','Thirssur',
                 'Thiruvananthapuram','Alirajpur','Balaghat','Chhindwara','Dewas','Dindori','Guna','Hoshangabad','Khandwa',
                 'Mandsaur','Narsinghpur','Rajgarh','Sagar','Shajapur','Ahmednagar','Buldhana','Hingoli','Jalgaon','Kolhapur',
                 'Latur','Mumbai','Nagpur','Nanded','Nashik','Pune','Raigad','Ratnagiri','Sangli','Satara','Sholapur',
                 'Imphal East','Imphal West','East Khasi Hills','Delhi','Balasore','Jajpur','Pondicherry','Amritsar','Barnala',
                 'Bhatinda','Faridkot','Fatehgarh','Fazilka','Ferozpur','Gurdaspur','Hoshiarpur','Jalandhar','kapurthala',
                 'Ludhiana','Mansa','Moga','Mohali','Muktsar','Nawanshahr','Patiala','Ropar (Rupnagar)','Sangrur','Tarntaran',
                 'Ajmer','Baran','Barmer','Bhilwara','Bikaner','Chittorgarh','Churu','Dausa','Dholpur','Ganganagar',
                 'Hanumangarh','Jaipur','Jalore','Jhunjunu','Jodhpur','Kota','Rajasamand','Sikar','Swai Madhopur','Tonk',
                 'Chennai','Coimbatore','Cuddalore','Dharmapuri','Dindigul','Erode','Kancheepuram','Krishnagiri','Madurai',
                 'Namakkal','Pudukkottai','Ramanathapuram','Salem','Sivaganga','Thanjavur','Theni','Thiruchirappalli',
                 'Thirunelveli','Thiruvallur','Thiruvannamalai','Tuticorin','Vellore','Virudhunagar','Agra','Aligarh',
                 'Allahabad','Azamgarh','Bahraich','Ballia','Bareilly','Basti','Bulandshahar','Chandauli','Etah','Etawah',
                 'Farukhabad','Fatehpur','Ghaziabad','Gonda','Hardoi','Jalaun (Orai)','Kanpur','Lucknow','Maharajganj',
                 'Mau(Maunathbhanjan)','Meerut','Mirzapur','Muradabad','Pratapgarh','Saharanpur','Shahjahanpur','Shravasti',
                 'Siddharth Nagar','Sitapur','Unnao','Haridwar','Nanital','UdhamSinghNagar','24 Parganas','Bankura','Burdwan',
                 'Coochbehar','Darjeeling','Kolkatta (R)','Malda','Nadia','Puruliya']

#For adding Crops:
for i in crop:
    crops = {
        "crop_name" : i
    }
    db.crop.insert_one(crops)

#For adding Districts: 
for i in district_name:
    district = {
        "district" : i
    }
    db.district.insert_one(district)
    
    

