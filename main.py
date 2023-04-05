import config
import telebot
from telebot import *

# from pars import parse

bot = telebot.TeleBot("6116036028:AAFIceklU-Wwz0TSC_cq9wJbrZ8NS4K_D50")

strt = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
strt.row('Розмитнити авто!')
strt.one_time_keyboard = True

re = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
re.row('Так!')
re.one_time_keyboard = True

keyboard6 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard6.row('Назад', 'На початок')
keyboard6.one_time_keyboard = True

keyboard7 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard7.row('Погоджуюсь', 'Створити запит заново')
keyboard7.one_time_keyboard = True

keyboard8 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard8.row('На початок')
keyboard8.one_time_keyboard = True

brands = ['Toyota', 'Volkswagen', 'Ford', 'Honda', 'Chevrolet', 'Nissan', 'Hyundai', 'Kia', 'Mercedes-Benz',
          'BMW', 'Audi', 'Subaru', 'Mazda', 'Jeep', 'Lexus', 'GMC', 'Dodge', 'Porsche', 'Chrysler',
          'Mitsubishi', 'Volvo', 'Fiat', 'Mini', 'Land Rover', 'Jaguar', 'Acura', 'Infiniti', 'Buick', 'Cadillac',
          'Ram', 'Alfa Romeo', 'Genesis', 'Maserati', 'Smart', 'Suzuki', 'Peugeot', 'Renault', 'Citroen', 'Dacia',
          'Skoda', 'Seat', 'Opel', 'Vauxhall', 'Lada', 'Tata', 'Mahindra', 'Proton', 'Perodua', 'Geely',
          'Scania', 'MAN', 'Iveco']

years = ['1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008',
         '2009', '2010', '2011', '2012',
         '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', 'Назад']

models = [
    # Toyota
    'Corolla', 'Camry', 'RAV4', 'Highlander', 'Tundra', 'Sienna', '4Runner', 'Prius', 'Land Cruiser', 'Avalon',
    'Tacoma', 'Yaris', 'C-HR', 'Sequoia', 'Venza', 'Supra', 'Mirai', 'Celica', 'MR2', 'Solara',
    'Matrix', 'Echo', 'Previa', 'Paseo', 'Starlet', 'Terios', 'Verso', 'Avensis', 'Aygo', 'Hiace',
    'Hilux', 'Urban Cruiser', 'Century', 'Crown', 'Carina', 'Sprinter', 'Soarer', 'Altezza', 'Chaser',
    'Mark X', 'Brevis', 'Vios', 'Fortuner', 'FJ Cruiser', 'Belta', 'Blade', 'Probox', 'Succeed', 'Allion',

    # Volkswagen
    'Golf', 'Passat', 'Polo', 'Jetta', 'Tiguan', 'Beetle', 'Touran', 'Touareg', 'Caddy', 'Scirocco',
    'Arteon', 'Up!', 'Sharan', 'Amarok', 'Phaeton', 'Transporter', 'Eos', 'Fox', 'Lupo', 'Bora',
    'New Beetle', 'CC', 'Karmann Ghia', 'Corrado', 'Taro', 'T-Cross', 'Golf Sportsvan', 'Routan',
    'Atlas', 'ID.3', 'ID.4', 'Type 3', 'Type 4', 'Type 2', 'Type 181', 'Kübelwagen', 'Type 14',
    'Type 147', 'Type 3 Fastback', 'Type 3 Notchback', 'Type 34', 'Type 2 T1', 'Type 2 T2',
    'Type 2 T3', 'Type 2 T4', 'Type 2 T5', 'Type 2 T6', 'XL1', 'Lavida', 'Santana', 'Sedric',

    # Ford
    'F-150', 'Focus', 'Mustang', 'Escape', 'Explorer', 'Fusion', 'Taurus', 'Edge', 'Transit', 'Ranger',
    'Expedition', 'EcoSport', 'Bronco', 'Thunderbird', 'Flex', 'C-Max', 'Galaxie', 'Fairlane', 'Escort',
    'Excursion', 'Crown Victoria', 'Contour', 'Windstar', 'GT', 'Model T', 'Model A', 'Model B', 'Model 18',
    'Model 48', 'Model 68', 'Model 74', 'Model 79', 'Model 91', 'Model K', 'Model N', 'Model R', 'Model S',
    'Model Y', 'Model C', 'Model F', 'Model H', 'Model L', 'Model M', 'Model TT', 'Model V-8', 'Model 2GA',
    'Model 2HA', 'Model 2HB', 'Model 2N',

    # Honda
    'Civic', 'Accord', 'CR-V', 'Pilot', 'Odyssey', 'Ridgeline', 'Element', 'Fit', 'Insight', 'S2000', 'NSX',
    'Integra', 'Prelude', 'CRX', 'Passport', 'Crosstour', 'Legend', 'City', 'FR-V', 'Stream', 'Airwave', 'Orthia',
    'Domani', 'Partner', 'Concerto', 'Ascot', 'Avancier', 'Vigor', 'Inspire', 'Shuttle', 'Mobilio', 'Capa',
    'Torneo', 'Rafaga', 'Crossroad', 'Zest', 'Life', 'Today', 'S660', 'S800', 'S500', 'S600', 'Beat', 'Z', 'T360',
    'T500', 'T600', 'T700', 'T800',

    # Chevrolet
    'Silverado', 'Camaro', 'Corvette', 'Impala', 'Malibu', 'Blazer', 'Suburban', 'Equinox',
    'Traverse', 'Tahoe', 'Colorado', 'Trailblazer', 'Avalanche', 'Express', 'Nova', 'Chevelle', 'El Camino',
    'Monte Carlo', 'Cruze', 'Sonic', 'Spark', 'Cavalier', 'Cobalt', 'Beretta', 'Caprice', 'Celebrity', 'Corsica',
    'Lumina', 'Venture', 'HHR', 'SSR', 'Uplander', 'Metro', 'Prizm', 'S-10', 'Tracker', 'Astro', 'Silverado HD', 'Volt',
    'Bolt EV', 'City Express', 'Biscayne', 'Nomad', 'Bel Air', 'Del Ray', 'Brookwood', 'Yeoman', 'Kingswood',
    'Parkwood',

    # Nissan
    'Altima',
    'Sentra', 'Maxima', 'Rogue', 'Versa', 'Murano', 'Pathfinder', 'Frontier', 'Titan', 'Armada', '370Z', 'GT-R', 'Leaf',
    'Kicks', 'Versa Note', 'Juke', 'Cube', 'Quest', 'Xterra', 'Rogue Sport', 'NV200', 'NV Cargo', 'NV Passenger',
    '200SX', '240SX', '300ZX', '350Z', 'Advan', 'Almera', 'Bluebird', 'Cefiro', 'Cherry', 'Clipper', 'Datsun',
    'Fairlady', 'Figaro', 'Gloria', 'Interstar', 'Juke Nismo RS', 'Lafesta', 'Latio', 'Moco', 'Nismo', 'Note',
    'Paladin', 'Pao', 'Patrol', 'Pixo', 'President', 'Primera',

    # Hyundai
    'Elantra', 'Sonata', 'Accent', 'Tucson', 'Santa Fe', 'Palisade',
    'Kona', 'Veloster', 'Venue', 'Genesis G70', 'Genesis G80', 'Genesis G90', 'Azera', 'Creta', 'Entourage', 'Equus',
    'Excel', 'Galloper', 'Getz', 'Grand i10', 'H1', 'H100', 'HB20', 'i10', 'i20', 'i30', 'i40', 'ix20', 'ix35',
    'Lantra', 'Matrix', 'Nexo', 'Pony', 'Porter', 'Santamo', 'Scoupe', 'Solaris', 'Starex', 'Terracan', 'Trajet',
    'Tiburon', 'Tucson Fuel Cell', 'Universe', 'Verna', 'Veracruz', 'Xcent', 'Aslan', 'Avante', 'County', 'Dynasty',

    # Kia
    'Seltos', 'Sorento', 'Soul', 'Telluride', 'Sportage', 'Niro', 'Carnival', 'Rio', 'Optima', 'K5', 'Stinger', 'Ceed',
    'Picanto', 'Forte', 'Cerato', 'K900', 'Amanti', 'Borrego', 'Carens', 'Carnival/Sedona', 'Clarus', 'Joice',
    'Magentis', 'Mohave/Borrego', 'Morning', 'Opirus/Amanti', 'Pegas', 'Potentia', 'Pride', 'Ray', 'Retona', 'Sedona',
    'Shuma', 'Spectra', 'Stonic', 'Venga', 'XCeed', 'K2500/K2700', 'K2900', 'K3000', 'K3600', 'K4000', 'K4200', 'KCV4',
    'KEA Truck', 'K-Series', 'Optima PHEV', 'Sephia/Shuma II', 'Soluto', 'Telluride Hybrid',

    # Mercedes-Benz
    'C-Class', 'E-Class', 'S-Class', 'GLE-Class', 'GLC-Class', 'A-Class', 'GLA-Class', 'B-Class', 'CLA-Class',
    'SL-Class', 'AMG GT', 'GLS-Class', 'GLB-Class', 'CLS-Class', 'G-Class', 'V-Class', 'GLE Coupe', 'SLC-Class', 'EQC',
    'GLS SUV', 'Maybach S-Class', 'X-Class', 'SLS AMG', 'Metris', 'Sprinter', 'AMG GT 4-Door', 'EQS', 'EQB', 'Citan',
    'EQE', '190-Class', '240D', '280SE', '300CE', '300D', '300E', '450SEL', '500SEL', '560SEL', '600SEL', 'CLK-Class',
    'CLS63 AMG', 'E55 AMG', 'GL-Class', 'GLK-Class', 'SL550', 'SLK-Class', 'SLS-Class', 'SLS GT AMG', 'Vito', '190E',
    '200-Series',

    # BMW
    '3 Series', '5 Series', '7 Series', 'X5', 'X3', '1 Series', 'X1', '4 Series', '2 Series', '6 Series', '8 Series',
    'X7', 'Z4', 'i3', 'M4', 'M3', 'M5', 'X6', 'M2', 'X4', 'M8', 'M6', 'X2', 'Z3', 'Z8', 'i8', '325i', '325e', '325is',
    '325', '318i', '330i', '335i', '335d', '328i', '335xi', '530i', '540i', '525i', '545i', '535i', '550i', 'M550i',
    '740i', '750i', '760Li', '745Li', '740Li', '735i',

    # Audi
    'A4', 'Q5', 'A6', 'A3', 'Q7', 'A5', 'TT', 'S4', 'A8', 'RS5', 'RS3', 'RS7', 'R8', 'S5', 'Q3', 'S3', 'SQ5', 'A7',
    'A1', 'S6', 'RS6', 'Q8', 'S8', 'e-tron', 'SQ7', 'TT RS', 'RS Q8', '100', '80', '90', '200', '5000', 'V8',
    'Cabriolet', 'Coupe', 'S7', 'S2', 'S1', 'S Coupe', 'S5 Sportback', 'RS4 Avant', 'S4 Avant', 'RS5 Sportback',
    'RS3 Sportback', 'RS5 Coupe', 'S6 Avant', 'S8 Plus', 'RS6 Avant', 'S7 Sportback',

    # Subaru
    'Forester', 'Outback', 'Impreza', 'Crosstrek', 'Legacy', 'Ascent', 'WRX', 'BRZ', 'Baja', 'SVX', 'XT', 'Justy',
    'Loyale', 'GL', 'Leone', 'Rex', 'Trezia', 'Stella', 'Alcyone', 'Impreza WRX', 'Impreza WRX STI',
    'Impreza WRX STI Type RA', 'Legacy B4', 'Legacy Touring Wagon', 'Legacy Outback', 'Levorg', 'Traviq', 'Exiga',
    'Dex', 'Pleo', 'Sambar', 'Lucra', 'Impreza Anesis', 'Impreza XV', 'Impreza Sport Hybrid', 'Impreza G4',
    'Impreza Sport', 'Impreza Sport Hybrid G4', 'Impreza Cross', 'Impreza Sport Hybrid Cross', 'Impreza Sport Cross',
    'Levorg STI Sport', 'WRX S4', 'WRX STI S209', 'Viziv Performance Concept', 'Viziv Adrenaline Concept',
    'Viziv Tourer Concept', 'Viziv Adrenaline', 'Levorg STI Sport Black Selection',

    # Mazda
    'Mazda3', 'CX-5', 'Mazda6', 'MX-5 Miata', 'CX-3', 'CX-30', 'CX-9', 'RX-8', 'MX-6', 'RX-7', '626', 'Millenia',
    'Protege', 'Tribute', 'B-Series', 'MPV', 'RX-3', 'RX-4', '929', 'GLC', 'CX-7', 'Navajo', 'RX-2', '808', 'RX-5',
    'Cosmo', '323', 'Protege5', 'CX-4', 'RX-8 R3', 'Carol', 'Roadpacer', 'Proceed', 'Familia Van', 'Xedos 9',
    'Eunos 500', 'Capella', 'Bongo Friendee', 'Verisa', 'CX-8', 'AZ-1', 'Eunos 800', 'Lantis', 'Familia', 'Flair Wagon',
    'CX-6', 'Persona', 'K360', 'Eunos Cosmo',

    # Jeep
    'Wrangler', 'Grand Cherokee', 'Cherokee', 'Renegade', 'Compass', 'Gladiator', 'Commander', 'Patriot', 'Liberty',
    'Wagoneer', 'CJ', 'J-10', 'J-20', 'J-200', 'J-300', 'J-4000', 'J-4500', 'J-4600', 'J-4700', 'J-4800', 'J-550',
    'J-600', 'J-700', 'J-800', 'Scrambler', 'Honcho', 'Dispatcher', 'Forward Control', 'FC-150', 'FC-170', 'CJ-2A',
    'CJ-3A', 'CJ-3B', 'CJ-5', 'CJ-6', 'CJ-7', 'CJ-8', 'Willys MB', 'Willys MA', 'Willys MC', 'M-38', 'M-38A1', 'M-170',
    'DJ-3A', 'DJ-5', 'DJ-6', 'DJ-5A', 'DJ-6A', 'FJ', 'Jeepster', 'Commando',

    # Lexus
    'RX', 'ES', 'NX', 'GX', 'LS', 'IS', 'LX', 'RC', 'CT', 'HS', 'SC', 'GS', 'UX', 'LC', 'LF-A', 'IS F', 'ES Hybrid',
    'GS F', 'LS Hybrid', 'HS Hybrid', 'CT Hybrid', 'NX Hybrid', 'RX Hybrid', 'LS 600h L', 'LS 400', 'GX 470', 'GX 460',
    'RX 330', 'RX 300', 'RX 350', 'RX 400h', 'RX 450h', 'IS 250', 'IS 350', 'ES 330', 'ES 350', 'LS 430', 'LS 460',
    'SC 430', 'HS 250h', 'CT 200h', 'IS 300', 'GS 300', 'GS 400', 'GS 430', 'GS 450h', 'GS 460', 'LX 450', 'LX 470',

    # GMC
    'Sierra 1500', 'Yukon', 'Sierra 2500HD', 'Acadia', 'Terrain', 'Canyon', 'Envoy', 'Sierra 3500HD', 'Savana',
    'Yukon XL 1500', 'Sonoma', 'Jimmy', 'Yukon XL 2500', 'Typhoon', 'S-15', 'S-15 Jimmy', 'Rally', 'Rally Wagon',
    'Vandura', 'Caballero', 'Safari', 'Sierra 1500 Classic', 'Sierra 2500', 'Syclone', 'Suburban', 'Tracker',
    'C/K 1500', 'C/K 2500', 'C/K 3500', 'Envoy XL', 'Envoy XUV', 'Forward Control Chassis', 'G-Series Van',
    'Jimmy (S-15)', 'P-Chassis', 'R/V 3500 Series', 'S-15 Pickup', 'Safari Cargo', 'Savana Cargo', 'Savana Cutaway',
    'Sierra 1500HD', 'Sierra 1500 Limited', 'Sierra 2500HD Classic', 'Sierra 3500', 'Sierra 3500 Classic',
    'Sonoma (S-15)', 'Sonoma GT', 'Suburban 1500', 'Suburban 2500', 'T15 (S-15)',

    # Dodge
    'Ram 1500', 'Challenger', 'Grand Caravan', 'Charger', 'Durango', 'Journey', 'Ram 2500', 'Dakota', 'Avenger', 'Neon',
    'Nitro', 'Caravan', 'Magnum', 'Stratus', 'Ram 3500', 'Intrepid', 'Ram Van', 'Caliber', 'Ram 150', 'Ram Wagon',
    'Viper', 'Daytona', 'Spirit', 'Aries', 'Stealth', 'Omni', 'Shadow', 'Dynasty', 'Colt', 'SRT Viper', '600', 'Aspen',
    '600 ES', 'Mirada', 'Lancer', 'Dart', 'Conquest', 'Monaco', 'Royal Monaco', '600 SE', 'St. Regis',
    'Charger Daytona', '400', 'Polara', 'Charger SRT Hellcat', 'Custom Royal', 'D150', 'Power Wagon', 'W150',

    # Porsche
    '911', 'Cayenne', 'Panamera', 'Macan', 'Boxster', 'Carrera GT', '718 Cayman', '928', '944', '968', '959', '914',
    '356', '912', '919 Hybrid', '911 GT2', '911 GT3', '911 RSR', '917', '918 Spyder', '924', '934', '935', '962',
    '968 Turbo S', 'Carrera', 'Cayman', 'CGT', 'GTS', 'Panamera Hybrid', 'RS', 'Speedster', 'Taycan', 'Turbo',

    # Chrysler
    '300', 'Pacifica', 'Voyager', 'Crossfire', 'Sebring',
    'Concorde', 'Aspen', 'PT Cruiser', 'LHS', 'Imperial', 'New Yorker', 'Cirrus', 'LeBaron', 'Intrepid', 'TC',
    'Fifth Avenue', 'Airflow', 'Prowler', 'Royal', 'Windsor', 'Saratoga', 'Stratus', 'Crown Imperial', '300M',
    'Imperial Parade Phaeton', 'E-Class', 'Saratoga Six', 'Sunbeam', 'Phaeton', 'Vision', 'Deluxe', 'Laser', 'Newport',
    'Phantom', 'Lancer', 'Yorker', 'Conquest', 'Delta', 'Viper', 'Fury', 'Valiant', 'Newport Custom', 'Windsor Deluxe',
    'Executive', 'Imperial Crown', 'Imperial LeBaron', 'Imperial Custom', 'Dart', 'Sebring Convertible',

    # Mitsubishi
    'Lancer', 'Outlander', 'Eclipse', 'Galant', 'Mirage', 'Pajero', 'ASX', 'RVR', 'Delica', 'Colt', 'Grandis', 'Strada',
    'Chariot', 'Diamante', 'Endeavor', 'L200', '3000GT', 'Montero', 'Sigma', 'Lancer Evolution', 'Carisma',
    'Space Star', 'Tredia', 'Starion', 'GTO', 'Lancer Sportback', 'Magna', 'Raider', 'Emeraude', 'Toppo', 'FTO',
    'Pajero iO', 'Cordia', 'Debonair', 'Eterna', 'Galant Fortis', 'Pajero Mini', 'Mirage G4', 'Pajero Pinin', 'Dingo',
    'Minica', 'Pajero Sport', 'Rosa', 'Eclipse Cross', 'Challenger', 'Minicab', 'Chariot Grandis', 'Pajero Junior',
    'Grand Lancer',

    # Volvo

    'volvo xc90', 'volvo xc60', 'volvo xc40', 'volvo s60', 'volvo v60', 'volvo s90', 'volvo v90', 'volvo c70',
    'volvo v70', 'volvo s40', 'volvo v40', 'volvo 850', 'volvo 240', 'volvo 740', 'volvo 940', 'volvo s70', 'volvo c30',
    'volvo s80', 'volvo v50', 'volvo 960', 'volvo 1800', 'volvo 480', 'volvo 66', 'volvo 144', 'volvo 145', 'volvo 164',
    'volvo 242', 'volvo 244', 'volvo 262', 'volvo 264', 'volvo 265', 'volvo 343', 'volvo 345', 'volvo 360', 'volvo 440',
    'volvo 460', 'volvo 480', 'volvo 740', 'volvo 760', 'volvo 780', 'volvo 850', 'volvo 940', 'volvo 960', 'volvo c70',
    'volvo s70', 'volvo s80', 'volvo v40', 'volvo v50', 'volvo v70', 'volvo v90',

    # Fiat

    "500", "Panda", "Tipo", "Ducato", "Bravo", "Punto", "Uno", "124 Spider", "Cinquecento", "Doblo", "Stilo",
    "Seicento", "Scudo", "Barchetta", "Qubo", "Croma", "Multipla", "Grande Punto", "Talento", "124", "Marea", "Fiorino",
    "Argo", "Idea", "Dino", "Linea", "X1/9", "Regata", "Campagnola", "850", "Topolino", "Tempra", "Nuova 500", "Palio",
    "Albea", "Sedici", "Ritmo", "Turbo Daily", "Weekend", "Mobi", "Freemont", "Coupe", "Brava", "Ulysse", "Palisade",
    "Viaggio", "Elba", "Siena", "Perla",

    # Mini

]

engine_types = ['Бензиновий', 'Дизельний']

engines = ['1.0', '1.2', '1.3', '1.4', '1.5', '1.6', '1.8', '1.9', '2.0', '2.2', '2.4', '2.5', '2.7', '2.8', '3.0',
           '3.5', '4.0', '4.6', '5.0', '6.2']


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Привіт, я допоможу вам розмитнити автомобіль.',
                     reply_markup=strt)


@bot.message_handler(commands=['reset'])
def reset_message(message):
    bot.send_message(message.chat.id, 'Почнемо спочатку', reply_markup=re)
    br = ""
    mod = ""
    yr = ""
    ent = ""
    eng = ""
    return br, mod, yr, engine, ent, eng
    brand(message)

@bot.message_handler(content_types=["text"])
def brand(message):
    print('ID:', message.from_user.id, '\n', 'First name:', message.from_user.first_name, '\n', 'Last name:',
          message.from_user.last_name,
          '\n', 'Username:', message.from_user.username)
    mark = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton(text="Toyota", callback_data="Toyota")
    button2 = telebot.types.InlineKeyboardButton(text="Volkswagen", callback_data="Volkswagen")
    button3 = telebot.types.InlineKeyboardButton(text="Ford", callback_data="Ford")
    button4 = telebot.types.InlineKeyboardButton(text="Honda", callback_data="Honda")
    button5 = telebot.types.InlineKeyboardButton(text="Chevrolet", callback_data="Chevrolet")
    button6 = telebot.types.InlineKeyboardButton(text="Nissan", callback_data="Nissan")
    button7 = telebot.types.InlineKeyboardButton(text="Hyundai", callback_data="Hyundai")
    button8 = telebot.types.InlineKeyboardButton(text="Kia", callback_data="Kia")
    button9 = telebot.types.InlineKeyboardButton(text="Mercedes-Benz", callback_data="Mercedes-Benz")
    button10 = telebot.types.InlineKeyboardButton(text="BMW", callback_data="BMW")
    button11 = telebot.types.InlineKeyboardButton(text="Audi", callback_data="Audi")
    button12 = telebot.types.InlineKeyboardButton(text="Інший бренд", callback_data="Інший бренд")
    mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11,
             button12)
    bot.send_message(message.chat.id, 'Оберіть бренд автомобіля:', reply_markup=mark)


@bot.callback_query_handler(func=lambda call: call.data in brands)
def query_brand(call):
    bot.answer_callback_query(callback_query_id=call.id)
    global br
    br = call.data

    if br == 'Інший бренд':
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        other(call.message)
    else:
        bot.send_message(call.message.chat.id, 'Обраний бренд: ' + br)
        print(br)
        model(call.message)


@bot.message_handler(content_types=["text"])
def model(message):
    if br == "Toyota":
        mark = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="Corolla", callback_data="Corolla")
        button2 = telebot.types.InlineKeyboardButton(text="Camry", callback_data="Camry")
        button3 = telebot.types.InlineKeyboardButton(text="RAV4", callback_data="RAV4")
        button4 = telebot.types.InlineKeyboardButton(text="Highlander", callback_data="Highlander")
        button5 = telebot.types.InlineKeyboardButton(text="Tundra", callback_data="Tundra")
        button6 = telebot.types.InlineKeyboardButton(text="Sienna", callback_data="Sienna")
        button7 = telebot.types.InlineKeyboardButton(text="4Runner", callback_data="4Runner")
        button8 = telebot.types.InlineKeyboardButton(text="Prius", callback_data="Prius")
        button9 = telebot.types.InlineKeyboardButton(text="Land Cruiser", callback_data="Land Cruiser")
        button10 = telebot.types.InlineKeyboardButton(text="Avalon", callback_data="Avalon")
        button11 = telebot.types.InlineKeyboardButton(text="Tacoma", callback_data="Tacoma")
        button12 = telebot.types.InlineKeyboardButton(text="Yaris", callback_data="Yaris")
        button13 = telebot.types.InlineKeyboardButton(text="C-HR", callback_data="C-HR")
        button14 = telebot.types.InlineKeyboardButton(text="Sequoia", callback_data="Sequoia")
        button15 = telebot.types.InlineKeyboardButton(text="Venza", callback_data="Venza")
        button16 = telebot.types.InlineKeyboardButton(text="Supra", callback_data="Supra")
        button17 = telebot.types.InlineKeyboardButton(text="Mirai", callback_data="Mirai")
        button18 = telebot.types.InlineKeyboardButton(text="Celica", callback_data="Celica")
        button19 = telebot.types.InlineKeyboardButton(text="MR2", callback_data="MR2")
        button20 = telebot.types.InlineKeyboardButton(text="Solara", callback_data="Solara")
        button21 = telebot.types.InlineKeyboardButton(text="Matrix", callback_data="Matrix")
        button22 = telebot.types.InlineKeyboardButton(text="Echo", callback_data="Echo")
        button23 = telebot.types.InlineKeyboardButton(text="Previa", callback_data="Previa")
        button24 = telebot.types.InlineKeyboardButton(text="Paseo", callback_data="Paseo")
        button25 = telebot.types.InlineKeyboardButton(text="Starlet", callback_data="Starlet")
        button26 = telebot.types.InlineKeyboardButton(text="Terios", callback_data="Terios")
        button27 = telebot.types.InlineKeyboardButton(text="Verso", callback_data="Verso")
        button28 = telebot.types.InlineKeyboardButton(text="Avensis", callback_data="Avensis")
        button29 = telebot.types.InlineKeyboardButton(text="Інша модель", callback_data="Інша модель")
        button30 = telebot.types.InlineKeyboardButton(text="Назад", callback_data="Назад")
        button31 = telebot.types.InlineKeyboardButton(text="На початок", callback_data="На початок")
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19, button20,
                 button21, button22, button23, button24, button25, button26, button27, button28, button29, button30,
                 button31)
        bot.send_message(message.chat.id, 'Оберіть модель авто:', reply_markup=mark)

    if br == "Volkswagen":
        mark = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="Golf", callback_data="Golf")
        button2 = telebot.types.InlineKeyboardButton(text="Passat", callback_data="Passat")
        button3 = telebot.types.InlineKeyboardButton(text="Polo", callback_data="Polo")
        button4 = telebot.types.InlineKeyboardButton(text="Jetta", callback_data="Jetta")
        button5 = telebot.types.InlineKeyboardButton(text="Tiguan", callback_data="Tiguan")
        button6 = telebot.types.InlineKeyboardButton(text="Beetle", callback_data="Beetle")
        button7 = telebot.types.InlineKeyboardButton(text="Touran", callback_data="Touran")
        button8 = telebot.types.InlineKeyboardButton(text="Touareg", callback_data="Touareg")
        button9 = telebot.types.InlineKeyboardButton(text="Caddy", callback_data="Caddy")
        button10 = telebot.types.InlineKeyboardButton(text="Scirocco", callback_data="Scirocco")
        button11 = telebot.types.InlineKeyboardButton(text="Arteon", callback_data="Arteon")
        button12 = telebot.types.InlineKeyboardButton(text="Up!", callback_data="Up!")
        button13 = telebot.types.InlineKeyboardButton(text="Sharan", callback_data="Sharan")
        button14 = telebot.types.InlineKeyboardButton(text="Amarok", callback_data="Amarok")
        button15 = telebot.types.InlineKeyboardButton(text="Phaeton", callback_data="Phaeton")
        button16 = telebot.types.InlineKeyboardButton(text="Transporter", callback_data="Transporter")
        button17 = telebot.types.InlineKeyboardButton(text="Eos", callback_data="Eos")
        button18 = telebot.types.InlineKeyboardButton(text="Fox", callback_data="Fox")
        button19 = telebot.types.InlineKeyboardButton(text="Lupo", callback_data="Lupo")
        button20 = telebot.types.InlineKeyboardButton(text="Bora", callback_data="Bora")
        button21 = telebot.types.InlineKeyboardButton(text="New Beetle", callback_data="New Beetle")
        button22 = telebot.types.InlineKeyboardButton(text="CC", callback_data="CC")
        button23 = telebot.types.InlineKeyboardButton(text="Karmann Ghia", callback_data="Karmann Ghia")
        button24 = telebot.types.InlineKeyboardButton(text="Corrado", callback_data="Corrado")
        button25 = telebot.types.InlineKeyboardButton(text="Taro", callback_data="Taro")
        button26 = telebot.types.InlineKeyboardButton(text="T-Cross", callback_data="T-Cross")
        button27 = telebot.types.InlineKeyboardButton(text="Golf Sportsvan", callback_data="Golf Sportsvan")
        button28 = telebot.types.InlineKeyboardButton(text="Routan", callback_data="Routan")
        button29 = telebot.types.InlineKeyboardButton(text="Інша модель", callback_data="Інша модель")
        button30 = telebot.types.InlineKeyboardButton(text="Назад", callback_data="Назад")
        button31 = telebot.types.InlineKeyboardButton(text="На початок", callback_data="На початок")
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19, button20,
                 button21, button22, button23, button24, button25, button26, button27, button28, button29, button30,
                 button31)
        bot.send_message(message.chat.id, 'Оберіть модель авто:', reply_markup=mark)

    if br == "Ford":
        mark = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="F-150", callback_data="F-150")
        button2 = telebot.types.InlineKeyboardButton(text="Focus", callback_data="Focus")
        button3 = telebot.types.InlineKeyboardButton(text="Mustang", callback_data="Mustang")
        button4 = telebot.types.InlineKeyboardButton(text="Escape", callback_data="Escape")
        button5 = telebot.types.InlineKeyboardButton(text="Explorer", callback_data="Explorer")
        button6 = telebot.types.InlineKeyboardButton(text="Fusion", callback_data="Fusion")
        button7 = telebot.types.InlineKeyboardButton(text="Taurus", callback_data="Taurus")
        button8 = telebot.types.InlineKeyboardButton(text="Edge", callback_data="Edge")
        button9 = telebot.types.InlineKeyboardButton(text="Transit", callback_data="Transit")
        button10 = telebot.types.InlineKeyboardButton(text="Ranger", callback_data="Ranger")
        button11 = telebot.types.InlineKeyboardButton(text="Expedition", callback_data="Expedition")
        button12 = telebot.types.InlineKeyboardButton(text="EcoSport", callback_data="EcoSport")
        button13 = telebot.types.InlineKeyboardButton(text="Bronco", callback_data="Bronco")
        button14 = telebot.types.InlineKeyboardButton(text="Thunderbird", callback_data="Thunderbird")
        button15 = telebot.types.InlineKeyboardButton(text="Flex", callback_data="Flex")
        button16 = telebot.types.InlineKeyboardButton(text="C-Max", callback_data="C-Max")
        button17 = telebot.types.InlineKeyboardButton(text="Galaxie", callback_data="Galaxie")
        button18 = telebot.types.InlineKeyboardButton(text="Fairlane", callback_data="Fairlane")
        button19 = telebot.types.InlineKeyboardButton(text="Escort", callback_data="Escort")
        button20 = telebot.types.InlineKeyboardButton(text="Excursion", callback_data="Excursion")
        button21 = telebot.types.InlineKeyboardButton(text="Crown Victoria", callback_data="Crown Victoria")
        button22 = telebot.types.InlineKeyboardButton(text="Contour", callback_data="Contour")
        button23 = telebot.types.InlineKeyboardButton(text="Windstar", callback_data="Windstar")
        button24 = telebot.types.InlineKeyboardButton(text="GT", callback_data="GT")
        button25 = telebot.types.InlineKeyboardButton(text="Model T", callback_data="Model T")
        button26 = telebot.types.InlineKeyboardButton(text="Model A", callback_data="Model A")
        button27 = telebot.types.InlineKeyboardButton(text="Model B", callback_data="Model B")
        button28 = telebot.types.InlineKeyboardButton(text="Model 18", callback_data="Model 18")
        button29 = telebot.types.InlineKeyboardButton(text="Інша модель", callback_data="Інша модель")
        button30 = telebot.types.InlineKeyboardButton(text="Назад", callback_data="Назад")
        button31 = telebot.types.InlineKeyboardButton(text="На початок", callback_data="На початок")
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19, button20,
                 button21, button22, button23, button24, button25, button26, button27, button28, button29, button30,
                 button31)
        bot.send_message(message.chat.id, 'Оберіть модель авто:', reply_markup=mark)

    if br == "Honda":
        mark = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="Civic", callback_data="Civic")
        button2 = telebot.types.InlineKeyboardButton(text="Accord", callback_data="Accord")
        button3 = telebot.types.InlineKeyboardButton(text="CR-V", callback_data="CR-V")
        button4 = telebot.types.InlineKeyboardButton(text="Pilot", callback_data="Pilot")
        button5 = telebot.types.InlineKeyboardButton(text="Odyssey", callback_data="Odyssey")
        button6 = telebot.types.InlineKeyboardButton(text="Ridgeline", callback_data="Ridgeline")
        button7 = telebot.types.InlineKeyboardButton(text="Element", callback_data="Element")
        button8 = telebot.types.InlineKeyboardButton(text="Fit", callback_data="Fit")
        button9 = telebot.types.InlineKeyboardButton(text="Insight", callback_data="Insight")
        button10 = telebot.types.InlineKeyboardButton(text="S2000", callback_data="S2000")
        button11 = telebot.types.InlineKeyboardButton(text="NSX", callback_data="NSX")
        button12 = telebot.types.InlineKeyboardButton(text="Integra", callback_data="Integra")
        button13 = telebot.types.InlineKeyboardButton(text="Prelude", callback_data="Prelude")
        button14 = telebot.types.InlineKeyboardButton(text="CRX", callback_data="CRX")
        button15 = telebot.types.InlineKeyboardButton(text="Passport", callback_data="Passport")
        button16 = telebot.types.InlineKeyboardButton(text="Crosstour", callback_data="Crosstour")
        button17 = telebot.types.InlineKeyboardButton(text="Legend", callback_data="Legend")
        button18 = telebot.types.InlineKeyboardButton(text="City", callback_data="City")
        button19 = telebot.types.InlineKeyboardButton(text="FR-V", callback_data="FR-V")
        button20 = telebot.types.InlineKeyboardButton(text="Stream", callback_data="Stream")
        button21 = telebot.types.InlineKeyboardButton(text="Airwave", callback_data="Airwave")
        button22 = telebot.types.InlineKeyboardButton(text="Orthia", callback_data="Orthia")
        button23 = telebot.types.InlineKeyboardButton(text="Domani", callback_data="Domani")
        button24 = telebot.types.InlineKeyboardButton(text="Partner", callback_data="Partner")
        button25 = telebot.types.InlineKeyboardButton(text="Concerto", callback_data="Concerto")
        button26 = telebot.types.InlineKeyboardButton(text="Ascot", callback_data="Ascot")
        button27 = telebot.types.InlineKeyboardButton(text="Avancier", callback_data="Avancier")
        button28 = telebot.types.InlineKeyboardButton(text="Vigor", callback_data="Vigor")
        button29 = telebot.types.InlineKeyboardButton(text="Інша модель", callback_data="Інша модель")
        button30 = telebot.types.InlineKeyboardButton(text="Назад", callback_data="Назад")
        button31 = telebot.types.InlineKeyboardButton(text="На початок", callback_data="На початок")
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19, button20,
                 button21, button22, button23, button24, button25, button26, button27, button28, button29, button30,
                 button31)
        bot.send_message(message.chat.id, 'Оберіть модель авто:', reply_markup=mark)

    if br == "Chevrolet":
        mark = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="Silverado", callback_data="Silverado")
        button2 = telebot.types.InlineKeyboardButton(text="Camaro", callback_data="Camaro")
        button3 = telebot.types.InlineKeyboardButton(text="Corvette", callback_data="Corvette")
        button4 = telebot.types.InlineKeyboardButton(text="Impala", callback_data="Impala")
        button5 = telebot.types.InlineKeyboardButton(text="Malibu", callback_data="Malibu")
        button6 = telebot.types.InlineKeyboardButton(text="Blazer", callback_data="Blazer")
        button7 = telebot.types.InlineKeyboardButton(text="Suburban", callback_data="Suburban")
        button8 = telebot.types.InlineKeyboardButton(text="Equinox", callback_data="Equinox")
        button9 = telebot.types.InlineKeyboardButton(text="Traverse", callback_data="Traverse")
        button10 = telebot.types.InlineKeyboardButton(text="Tahoe", callback_data="Tahoe")
        button11 = telebot.types.InlineKeyboardButton(text="Colorado", callback_data="Colorado")
        button12 = telebot.types.InlineKeyboardButton(text="Trailblazer", callback_data="Trailblazer")
        button13 = telebot.types.InlineKeyboardButton(text="Avalanche", callback_data="Avalanche")
        button14 = telebot.types.InlineKeyboardButton(text="Express", callback_data="Express")
        button15 = telebot.types.InlineKeyboardButton(text="Nova", callback_data="Nova")
        button16 = telebot.types.InlineKeyboardButton(text="Chevelle", callback_data="Chevelle")
        button17 = telebot.types.InlineKeyboardButton(text="El Camino", callback_data="El Camino")
        button18 = telebot.types.InlineKeyboardButton(text="Monte Carlo", callback_data="Monte Carlo")
        button19 = telebot.types.InlineKeyboardButton(text="Cruze", callback_data="Cruze")
        button20 = telebot.types.InlineKeyboardButton(text="Sonic", callback_data="Sonic")
        button21 = telebot.types.InlineKeyboardButton(text="Spark", callback_data="Spark")
        button22 = telebot.types.InlineKeyboardButton(text="Cavalier", callback_data="Cavalier")
        button23 = telebot.types.InlineKeyboardButton(text="Cobalt", callback_data="Cobalt")
        button24 = telebot.types.InlineKeyboardButton(text="Beretta", callback_data="Beretta")
        button25 = telebot.types.InlineKeyboardButton(text="Caprice", callback_data="Caprice")
        button26 = telebot.types.InlineKeyboardButton(text="Celebrity", callback_data="Celebrity")
        button27 = telebot.types.InlineKeyboardButton(text="Corsica", callback_data="Corsica")
        button28 = telebot.types.InlineKeyboardButton(text="Lumina", callback_data="Lumina")
        button29 = telebot.types.InlineKeyboardButton(text="Інша модель", callback_data="Інша модель")
        button30 = telebot.types.InlineKeyboardButton(text="Назад", callback_data="Назад")
        button31 = telebot.types.InlineKeyboardButton(text="На початок", callback_data="На початок")
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19,
                 button20,
                 button21, button22, button23, button24, button25, button26, button27, button28, button29,
                 button30,
                 button31)
        bot.send_message(message.chat.id, 'Оберіть модель авто:', reply_markup=mark)

    if br == "Nissan":
        mark = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="Altima", callback_data="Altima")
        button2 = telebot.types.InlineKeyboardButton(text="Sentra", callback_data="Sentra")
        button3 = telebot.types.InlineKeyboardButton(text="Maxima", callback_data="Maxima")
        button4 = telebot.types.InlineKeyboardButton(text="Rogue", callback_data="Rogue")
        button5 = telebot.types.InlineKeyboardButton(text="Versa", callback_data="Versa")
        button6 = telebot.types.InlineKeyboardButton(text="Murano", callback_data="Murano")
        button7 = telebot.types.InlineKeyboardButton(text="Pathfinder", callback_data="Pathfinder")
        button8 = telebot.types.InlineKeyboardButton(text="Frontier", callback_data="Frontier")
        button9 = telebot.types.InlineKeyboardButton(text="Titan", callback_data="Titan")
        button10 = telebot.types.InlineKeyboardButton(text="Armada", callback_data="Armada")
        button11 = telebot.types.InlineKeyboardButton(text="370Z", callback_data="370Z")
        button12 = telebot.types.InlineKeyboardButton(text="GT-R", callback_data="GT-R")
        button13 = telebot.types.InlineKeyboardButton(text="Versa Note", callback_data="Versa Note")
        button14 = telebot.types.InlineKeyboardButton(text="Juke", callback_data="Juke")
        button15 = telebot.types.InlineKeyboardButton(text="Cube", callback_data="Cube")
        button16 = telebot.types.InlineKeyboardButton(text="Quest", callback_data="Quest")
        button17 = telebot.types.InlineKeyboardButton(text="Xterra", callback_data="Xterra")
        button18 = telebot.types.InlineKeyboardButton(text="Rogue Sport", callback_data="Rogue Sport")
        button19 = telebot.types.InlineKeyboardButton(text="NV200", callback_data="NV200")
        button20 = telebot.types.InlineKeyboardButton(text="NV Cargo", callback_data="NV Cargo")
        button21 = telebot.types.InlineKeyboardButton(text="NV Passenger", callback_data="NV Passenger")
        button22 = telebot.types.InlineKeyboardButton(text="200SX", callback_data="200SX")
        button23 = telebot.types.InlineKeyboardButton(text="240SX", callback_data="240SX")
        button24 = telebot.types.InlineKeyboardButton(text="300ZX", callback_data="300ZX")
        button25 = telebot.types.InlineKeyboardButton(text="350Z", callback_data="350Z")
        button26 = telebot.types.InlineKeyboardButton(text="Advan", callback_data="Advan")
        button27 = telebot.types.InlineKeyboardButton(text="Almera", callback_data="Almera")
        button28 = telebot.types.InlineKeyboardButton(text="Bluebird", callback_data="Bluebird")
        button29 = telebot.types.InlineKeyboardButton(text="Інша модель", callback_data="Інша модель")
        button30 = telebot.types.InlineKeyboardButton(text="Назад", callback_data="Назад")
        button31 = telebot.types.InlineKeyboardButton(text="На початок", callback_data="На початок")
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19,
                 button20,
                 button21, button22, button23, button24, button25, button26, button27, button28, button29,
                 button30,
                 button31)
        bot.send_message(message.chat.id, 'Оберіть модель авто:', reply_markup=mark)

    if br == "Kia":
        mark = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="Seltos", callback_data="Seltos")
        button2 = telebot.types.InlineKeyboardButton(text="Sorento", callback_data="Sorento")
        button3 = telebot.types.InlineKeyboardButton(text="Soul", callback_data="Soul")
        button4 = telebot.types.InlineKeyboardButton(text="Telluride", callback_data="Telluride")
        button5 = telebot.types.InlineKeyboardButton(text="Sportage", callback_data="Sportage")
        button6 = telebot.types.InlineKeyboardButton(text="Niro", callback_data="Niro")
        button7 = telebot.types.InlineKeyboardButton(text="Carnival", callback_data="Carnival")
        button8 = telebot.types.InlineKeyboardButton(text="Rio", callback_data="Rio")
        button9 = telebot.types.InlineKeyboardButton(text="Optima", callback_data="Optima")
        button10 = telebot.types.InlineKeyboardButton(text="K5", callback_data="K5")
        button11 = telebot.types.InlineKeyboardButton(text="Stinger", callback_data="Stinger")
        button12 = telebot.types.InlineKeyboardButton(text="Ceed", callback_data="Ceed")
        button13 = telebot.types.InlineKeyboardButton(text="Picanto", callback_data="Picanto")
        button14 = telebot.types.InlineKeyboardButton(text="Forte", callback_data="Forte")
        button15 = telebot.types.InlineKeyboardButton(text="Cerato", callback_data="Cerato")
        button16 = telebot.types.InlineKeyboardButton(text="K900", callback_data="K900")
        button17 = telebot.types.InlineKeyboardButton(text="Amanti", callback_data="Amanti")
        button18 = telebot.types.InlineKeyboardButton(text="Borrego", callback_data="Borrego")
        button19 = telebot.types.InlineKeyboardButton(text="Carens", callback_data="Carens")
        button20 = telebot.types.InlineKeyboardButton(text="Carnival/Sedona", callback_data="Carnival/Sedona")
        button21 = telebot.types.InlineKeyboardButton(text="Clarus", callback_data="Clarus")
        button22 = telebot.types.InlineKeyboardButton(text="Joice", callback_data="Joice")
        button23 = telebot.types.InlineKeyboardButton(text="Magentis", callback_data="Magentis")
        button24 = telebot.types.InlineKeyboardButton(text="Mohave/Borrego", callback_data="Mohave/Borrego")
        button25 = telebot.types.InlineKeyboardButton(text="Morning", callback_data="Morning")
        button26 = telebot.types.InlineKeyboardButton(text="Opirus/Amanti", callback_data="Opirus/Amanti")
        button27 = telebot.types.InlineKeyboardButton(text="Pegas", callback_data="Pegas")
        button28 = telebot.types.InlineKeyboardButton(text="Potentia", callback_data="Potentia")
        button29 = telebot.types.InlineKeyboardButton(text="Інша модель", callback_data="Інша модель")
        button30 = telebot.types.InlineKeyboardButton(text="Назад", callback_data="Назад")
        button31 = telebot.types.InlineKeyboardButton(text="На початок", callback_data="На початок")
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19,
                 button20,
                 button21, button22, button23, button24, button25, button26, button27, button28, button29,
                 button30,
                 button31)
        bot.send_message(message.chat.id, 'Оберіть модель авто:', reply_markup=mark)

    if br == "Mercedes-Benz":
        mark = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="C-Class", callback_data="C-Class")
        button2 = telebot.types.InlineKeyboardButton(text="E-Class", callback_data="E-Class")
        button3 = telebot.types.InlineKeyboardButton(text="S-Class", callback_data="S-Class")
        button4 = telebot.types.InlineKeyboardButton(text="GLE-Class", callback_data="GLE-Class")
        button5 = telebot.types.InlineKeyboardButton(text="GLC-Class", callback_data="GLC-Class")
        button6 = telebot.types.InlineKeyboardButton(text="A-Class", callback_data="A-Class")
        button7 = telebot.types.InlineKeyboardButton(text="GLA-Class", callback_data="GLA-Class")
        button8 = telebot.types.InlineKeyboardButton(text="B-Class", callback_data="B-Class")
        button9 = telebot.types.InlineKeyboardButton(text="CLA-Class", callback_data="CLA-Class")
        button10 = telebot.types.InlineKeyboardButton(text="SL-Class", callback_data="SL-Class")
        button11 = telebot.types.InlineKeyboardButton(text="AMG GT", callback_data="AMG GT")
        button12 = telebot.types.InlineKeyboardButton(text="GLS-Class", callback_data="GLS-Class")
        button13 = telebot.types.InlineKeyboardButton(text="GLB-Class", callback_data="GLB-Class")
        button14 = telebot.types.InlineKeyboardButton(text="CLS-Class", callback_data="CLS-Class")
        button15 = telebot.types.InlineKeyboardButton(text="G-Class", callback_data="G-Class")
        button16 = telebot.types.InlineKeyboardButton(text="V-Class", callback_data="V-Class")
        button17 = telebot.types.InlineKeyboardButton(text="GLE Coupe", callback_data="GLE Coupe")
        button18 = telebot.types.InlineKeyboardButton(text="SLC-Class", callback_data="SLC-Class")
        button19 = telebot.types.InlineKeyboardButton(text="GLS SUV", callback_data="GLS SUV")
        button20 = telebot.types.InlineKeyboardButton(text="Maybach S-Class", callback_data="Maybach S-Class")
        button21 = telebot.types.InlineKeyboardButton(text="X-Class", callback_data="X-Class")
        button22 = telebot.types.InlineKeyboardButton(text="SLS AMG", callback_data="SLS AMG")
        button23 = telebot.types.InlineKeyboardButton(text="Metris", callback_data="Metris")
        button24 = telebot.types.InlineKeyboardButton(text="Sprinter", callback_data="Sprinter")
        button25 = telebot.types.InlineKeyboardButton(text="AMG GT 4-Door", callback_data="AMG GT 4-Door")
        button26 = telebot.types.InlineKeyboardButton(text="190-Class", callback_data="190-Class")
        button27 = telebot.types.InlineKeyboardButton(text="240D", callback_data="240D")
        button28 = telebot.types.InlineKeyboardButton(text="280SE", callback_data="280SE")
        button29 = telebot.types.InlineKeyboardButton(text="Інша модель", callback_data="Інша модель")
        button30 = telebot.types.InlineKeyboardButton(text="Назад", callback_data="Назад")
        button31 = telebot.types.InlineKeyboardButton(text="На початок", callback_data="На початок")
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19,
                 button20,
                 button21, button22, button23, button24, button25, button26, button27, button28, button29,
                 button30,
                 button31)
        bot.send_message(message.chat.id, 'Оберіть модель авто:', reply_markup=mark)


@bot.callback_query_handler(func=lambda call: call.data in models)
def query_model(call):
    bot.answer_callback_query(callback_query_id=call.id)
    global mod
    mod = call.data
    if br == 'Інший бренд':
        mod = 'Інша модель'
        year(call.message)
    if mod == 'Назад':
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        brand(call.message)

    elif mod == 'На початок':
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        reset_message(call.message)

    else:
        bot.send_message(call.message.chat.id, 'Обрана модель: ' + mod)
        print(mod)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        year(call.message)


@bot.message_handler(content_types=["text"])
def year(message):
    mark = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton(text="1995", callback_data="1995")
    button2 = telebot.types.InlineKeyboardButton(text="1996", callback_data="1996")
    button3 = telebot.types.InlineKeyboardButton(text="1997", callback_data="1997")
    button4 = telebot.types.InlineKeyboardButton(text="1998", callback_data="1998")
    button5 = telebot.types.InlineKeyboardButton(text="1999", callback_data="1999")
    button6 = telebot.types.InlineKeyboardButton(text="2000", callback_data="2000")
    button7 = telebot.types.InlineKeyboardButton(text="2001", callback_data="2001")
    button8 = telebot.types.InlineKeyboardButton(text="2002", callback_data="2002")
    button9 = telebot.types.InlineKeyboardButton(text="2003", callback_data="2003")
    button10 = telebot.types.InlineKeyboardButton(text="2004", callback_data="2004")
    button11 = telebot.types.InlineKeyboardButton(text="2005", callback_data="2005")
    button12 = telebot.types.InlineKeyboardButton(text="2006", callback_data="2006")
    button13 = telebot.types.InlineKeyboardButton(text="2007", callback_data="2007")
    button14 = telebot.types.InlineKeyboardButton(text="2008", callback_data="2008")
    button15 = telebot.types.InlineKeyboardButton(text="2009", callback_data="2009")
    button16 = telebot.types.InlineKeyboardButton(text="2010", callback_data="2010")
    button17 = telebot.types.InlineKeyboardButton(text="2011", callback_data="2011")
    button18 = telebot.types.InlineKeyboardButton(text="2012", callback_data="2012")
    button19 = telebot.types.InlineKeyboardButton(text="2013", callback_data="2013")
    button20 = telebot.types.InlineKeyboardButton(text="2014", callback_data="2014")
    button21 = telebot.types.InlineKeyboardButton(text="2015", callback_data="2015")
    button22 = telebot.types.InlineKeyboardButton(text="2016", callback_data="2016")
    button23 = telebot.types.InlineKeyboardButton(text="2017", callback_data="2017")
    button24 = telebot.types.InlineKeyboardButton(text="2018", callback_data="2018")
    button25 = telebot.types.InlineKeyboardButton(text="2019", callback_data="2019")
    button26 = telebot.types.InlineKeyboardButton(text="2020", callback_data="2020")
    button27 = telebot.types.InlineKeyboardButton(text="2021", callback_data="2021")
    button28 = telebot.types.InlineKeyboardButton(text="2022", callback_data="2022")
    button29 = telebot.types.InlineKeyboardButton(text="2023", callback_data="2023")
    button30 = telebot.types.InlineKeyboardButton(text="Назад", callback_data="Назад")
    button31 = telebot.types.InlineKeyboardButton(text="На початок", callback_data="На початок")
    mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11,
             button12, button13, button14, button15, button16, button17, button18, button19, button20, button21,
             button22, button23, button24, button25, button26, button27, button28, button29, button30, button31)
    bot.send_message(message.chat.id, 'Оберіть рік випуску автомобіля', reply_markup=mark)


@bot.callback_query_handler(func=lambda call: call.data in years)
def query_year(call):
    bot.answer_callback_query(callback_query_id=call.id)
    global yr
    yr = call.data

    if yr == 'Назад':
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        model(call.message)
    elif yr == 'На початок':
        reset_message(call.message)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    else:
        print(yr)
        bot.send_message(call.message.chat.id, 'Обраний рік випуску: ' + yr)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        engine_type(call.message)


@bot.message_handler(content_types=["text"])
def engine_type(message):
    mark = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton(text="Бензиновий", callback_data="Бензиновий")
    button2 = telebot.types.InlineKeyboardButton(text="Дизельний", callback_data="Дизельний")
    button3 = telebot.types.InlineKeyboardButton(text="Назад", callback_data="Назад")
    button4 = telebot.types.InlineKeyboardButton(text="На початок", callback_data="На початок")
    mark.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id, 'Оберіть тип двигуна', reply_markup=mark)


@bot.callback_query_handler(func=lambda call: call.data in engine_types)
def query_enginetype(call):
    bot.answer_callback_query(callback_query_id=call.id)
    global ent
    ent = call.data
    if ent == 'Назад':
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        yr(call.message)
    elif yr == 'На початок':
        reset_message(call.message)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    else:
        print(ent)
        bot.send_message(call.message.chat.id, 'Обраний тип двигуна: ' + ent)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        engine(call.message)


@bot.message_handler(content_types=["text"])
def engine(message):
    mark = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton(text="1.0", callback_data="1.0")
    button2 = telebot.types.InlineKeyboardButton(text="1.2", callback_data="1.2")
    button3 = telebot.types.InlineKeyboardButton(text="1.3", callback_data="1.3")
    button4 = telebot.types.InlineKeyboardButton(text="1.4", callback_data="1.4")
    button5 = telebot.types.InlineKeyboardButton(text="1.5", callback_data="1.5")
    button6 = telebot.types.InlineKeyboardButton(text="1.6", callback_data="1.6")
    button7 = telebot.types.InlineKeyboardButton(text="1.8", callback_data="1.8")
    button8 = telebot.types.InlineKeyboardButton(text="1.9", callback_data="1.9")
    button9 = telebot.types.InlineKeyboardButton(text="2.0", callback_data="2.0")
    button10 = telebot.types.InlineKeyboardButton(text="2.2", callback_data="2.2")
    button11 = telebot.types.InlineKeyboardButton(text="2.4", callback_data="2.4")
    button12 = telebot.types.InlineKeyboardButton(text="2.5", callback_data="2.5")
    button13 = telebot.types.InlineKeyboardButton(text="2.7", callback_data="2.7")
    button14 = telebot.types.InlineKeyboardButton(text="2.8", callback_data="2.8")
    button15 = telebot.types.InlineKeyboardButton(text="3.0", callback_data="3.0")
    button16 = telebot.types.InlineKeyboardButton(text="3.5", callback_data="3.5")
    button17 = telebot.types.InlineKeyboardButton(text="4.0", callback_data="4.0")
    button18 = telebot.types.InlineKeyboardButton(text="4.6", callback_data="4.6")
    button19 = telebot.types.InlineKeyboardButton(text="5.0", callback_data="5.0")
    button20 = telebot.types.InlineKeyboardButton(text="6.2", callback_data="6.2")
    button21 = telebot.types.InlineKeyboardButton(text="Назад", callback_data="Назад")
    button22 = telebot.types.InlineKeyboardButton(text="На початок", callback_data="На початок")
    mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11,
             button12, button13, button14, button15, button16, button17, button18, button19, button20, button21,
             button22)
    bot.send_message(message.chat.id, "Оберіть об'єм двигуна", reply_markup=mark)


@bot.callback_query_handler(func=lambda call: call.data in engines)
def query_enginetype(call):
    bot.answer_callback_query(callback_query_id=call.id)
    global eng
    eng = call.data
    if eng == 'Назад':
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        engine_type(call.message)
    elif eng == 'На початок':
        reset_message(call.message)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    else:
        print(eng)
        bot.send_message(call.message.chat.id, "Обраний об'єм двигуна: " + eng)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        info(call.message)


def stepinit(message):
    i = message.text
    if i == 'Погоджуюсь':
        pass
        # finder(message)
    if i == 'Створити запит заново':
        reset_message(message)


@bot.message_handler(content_types=["text"])
def info(message):
    stavka = 0
    engv = 0
    if ent == 'Бензиновий':
        if eng == '1.0' or eng == '1.2' or eng == '1.3' or eng == '1.4' or eng == '1.5' or eng == '1.6' or eng == '1.8' or eng == '1.9' or eng == '2.0' or eng == '2.2' or eng == '2.4' or eng == '2.5' or eng == '2.7' or eng == '2.8' or eng == '3.0':
            stavka = 50
        else:
            stavka = 100
    elif ent == 'Дизельний':
        if eng == '1.0' or eng == '1.2' or eng == '1.3' or eng == '1.4' or eng == '1.5' or eng == '1.6' or eng == '1.8' or eng == '1.9' or eng == '2.0' or eng == '2.2' or eng == '2.4' or eng == '2.5' or eng == '2.7' or eng == '2.8' or eng == '3.0' or eng == '3.5':
            stavka = 75
        else:
            stavka = 150
    if eng == '1.0':
        engv = 1
    elif eng == '1.2':
        engv = 1.2
    elif eng == '1.3':
        engv = 1.3
    elif eng == '1.4':
        engv = 1.4
    elif eng == '1.5':
        engv = 1.5
    elif eng == '1.6':
        engv = 1.6
    elif eng == '1.8':
        engv = 1.8
    elif eng == '1.9':
        engv = 1.9
    elif eng == '2.0':
        engv = 2.0
    elif eng == '2.0':
        engv = 2.0
    elif eng == '2.2':
        engv = 2.2
    elif eng == '2.4':
        engv = 2.4
    elif eng == '2.5':
        engv = 2.5
    elif eng == '2.7':
        engv = 2.7
    elif eng == '2.8':
        engv = 2.8
    elif eng == '3.0':
        engv = 3.0
    elif eng == '3.5':
        engv = 3.5
    elif eng == '4.0':
        engv = 4.0
    elif eng == '4.6':
        engv = 4.6
    elif eng == '5.0':
        engv = 5.0
    elif eng == '6.2':
        engv = 6.2
    vartist_rozm = stavka * engv * (2023 - int(yr))
    print(vartist_rozm)
    bot.send_message(message.chat.id,
                     'Отже ви вибрали:\n' + 'Бренд: ' + br + '\n' + 'Модель: ' + mod + '\n' + 'Рік випуску: ' + yr + '\n' + 'Тип двигуна: ' + ent.lower() + '\n' + "Об'єм двигуна: " + eng + '\n' + 'Вартість розмитнення: {:.2f}'.format(
                         vartist_rozm) + '$')


bot.polling()
