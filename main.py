import requests
from bs4 import BeautifulSoup
import telebot
from telebot import *
from telebot.types import InputMediaPhoto

bot = telebot.TeleBot("6116036028:AAFIceklU-Wwz0TSC_cq9wJbrZ8NS4K_D50")

strt = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
strt.row('Старт!')
strt.one_time_keyboard = True

keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard2.row('Так', 'Ні')
keyboard2.one_time_keyboard = True

brands = ['Toyota', 'Volkswagen', 'Ford', 'Honda', 'Chevrolet', 'Nissan', 'Hyundai', 'Kia', 'Mercedes-Benz',
          'BMW', 'Audi', 'Subaru', 'Mazda', 'Jeep', 'Lexus', 'GMC', 'Dodge', 'Porsche', 'Chrysler',
          'Mitsubishi', 'Volvo', 'Fiat', 'Land Rover', 'Infiniti',
          'Peugeot', 'Renault', 'Citroen', 'Dacia', 'Skoda', 'Seat', 'Opel', 'Lada']

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
    'GLS SUV', 'Maybach S-Class', 'X-Class', 'SLS AMG', 'Metris', 'Sprinter', 'AMG GT 4-Door Coupe', 'EQS', 'EQB',
    'Citan',
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

    # Land Rover

    "Defender", "Range Rover", "Discovery", "Range Rover Sport", "Range Rover Evoque", "Range Rover Velar",
    "Freelander", "Range Rover Classic", "Discovery Sport", "Series I", "Series II", "Series III", "Range Rover P38A",
    "Range Rover L322", "Range Rover L405", "Range Rover Sport L320", "Range Rover Sport L494",
    "Range Rover Evoque L538", "Discovery L319", "Discovery 2", "Discovery 3", "Discovery 4", "Discovery 5",
    "Freelander 2", "Range Rover Evoque L551", "Range Rover Velar L560", "Range Rover Velar L550", "Defender (2020)",
    "Defender 110", "Defender 90",

    # Infiniti

    "Q50", "Q60", "Q70", "QX30", "QX50", "QX60", "QX70", "QX80", "EX", "FX", "JX", "M30", "M35", "M37",
    "M45", "M56", "G20", "G25", "G35", "G37", "I30", "I35", "J30", "Q40", "Q45", "QX4", "QX56", "QX60 Hybrid", "QX70S",
    "QX80S",

    # Peugeot

    "108", "208", "308", "408", "508", "3008", "5008", "Partner", "Rifter", "Traveller", "iOn", "206", "207",
    "307", "406", "407", "807", "106", "206+", "301", "Bipper", "Expert", "Boxer", "RCZ", "4007", "4008", "508 RXH",
    "508 SW", "508 Hybrid",

    # Renault

    "Clio", "Captur", "Megane", "Scenic", "Kadjar", "Talisman", "Koleos", "Twingo", "Espace", "Laguna", "Fluence",
    "Kangoo", "Trafic", "Master", "Modus", "Grand Scenic", "Symbol", "Sandero", "Duster", "Clio Estate", "Zoe R110",
    "Arkana", "Mégane Estate", "Kadjar RS", "Talisman Estate", "Talisman RS", "Koleos II", "Alaskan", "Kangoo II",
    "Zoe RS",

    # Citroen
    "C3", "C4", "C5", "C1", "C-Elysee", "C3 Aircross", "C4 Cactus", "C4 Picasso", "Berlingo", "SpaceTourer", "Jumpy",
    "C-Zero", "DS 3", "DS 4", "DS 5", "DS 7", "AMI", "C-Elysée WTCC", "C3 Picasso", "C4 Sedan", "C4 Spacetourer",
    "C4 Grand Picasso", "C5 Aircross", "C3 Pluriel", "Nemo", "Xsara", "Xantia", "Saxo", "BX", "ZX"
]

engine_types = ['Бензиновий', 'Дизельний']

engines = ['1.0', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '1.8', '1.9', '2.0', '2.2', '2.4', '2.5', '2.7', '2.8',
           '3.0',
           '3.5', '4.0', '4.6', '5.0', '6.2']


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Привіт, я допоможу вам розмитнити автомобіль.',
                     reply_markup=strt)


@bot.message_handler(commands=['reset'])
def reset_message(message):
    bot.send_message(message.chat.id, 'Почнемо спочатку?', reply_markup=strt)
    br = ""
    mod = ""
    yr = ""
    ent = ""
    eng = ""
    return br, mod, yr, engine, ent, eng


@bot.message_handler(content_types=["text"])
def brand(message):
    print(
        f"ID: {message.from_user.id}\nFirst name: {message.from_user.first_name}\nLast name: {message.from_user.last_name}\nUsername: {message.from_user.username}")
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
    button12 = telebot.types.InlineKeyboardButton(text="Subaru", callback_data="Subaru")
    button13 = telebot.types.InlineKeyboardButton(text="Mazda", callback_data="Mazda")
    button14 = telebot.types.InlineKeyboardButton(text="Jeep", callback_data="Jeep")
    button15 = telebot.types.InlineKeyboardButton(text="Lexus", callback_data="Lexus")
    button16 = telebot.types.InlineKeyboardButton(text="GMC", callback_data="GMC")
    button17 = telebot.types.InlineKeyboardButton(text="Dodge", callback_data="Dodge")
    button18 = telebot.types.InlineKeyboardButton(text="Porsche", callback_data="Porsche")
    button19 = telebot.types.InlineKeyboardButton(text="Chrysler", callback_data="Chrysler")
    button20 = telebot.types.InlineKeyboardButton(text="Mitsubishi", callback_data="Mitsubishi")
    button21 = telebot.types.InlineKeyboardButton(text="Land Rover", callback_data="Land Rover")
    button22 = telebot.types.InlineKeyboardButton(text="Infiniti", callback_data="Infiniti")
    button23 = telebot.types.InlineKeyboardButton(text="Peugeot", callback_data="Peugeot")
    button24 = telebot.types.InlineKeyboardButton(text="Renault", callback_data="Renault")
    button25 = telebot.types.InlineKeyboardButton(text="Citroen", callback_data="Citroen")
    button26 = telebot.types.InlineKeyboardButton(text="Skoda", callback_data="Skoda")
    button27 = telebot.types.InlineKeyboardButton(text="Opel", callback_data="Opel")
    button28 = telebot.types.InlineKeyboardButton(text="Lada", callback_data="Lada")
    mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11,
             button12, button13, button14, button15, button16, button17, button18, button19, button20, button21,
             button22, button23, button24, button25, button26, button27, button28)
    bot.send_message(message.chat.id, 'Оберіть бренд автомобіля:', reply_markup=mark)


@bot.callback_query_handler(func=lambda call: call.data in brands)
def query_brand(call):
    bot.answer_callback_query(callback_query_id=call.id)
    global br
    br = call.data
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
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19, button20,
                 button21, button22, button23, button24, button25, button26, button27, button28)
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
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19, button20,
                 button21, button22, button23, button24, button25, button26, button27, button28)
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
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19, button20,
                 button21, button22, button23, button24, button25, button26, button27, button28)
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
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19, button20,
                 button21, button22, button23, button24, button25, button26, button27, button28)
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
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19,
                 button20,
                 button21, button22, button23, button24, button25, button26, button27, button28)
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
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19,
                 button20,
                 button21, button22, button23, button24, button25, button26, button27, button28)
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
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19,
                 button20,
                 button21, button22, button23, button24, button25, button26, button27, button28)
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
        button25 = telebot.types.InlineKeyboardButton(text="AMG GT 4-Door Coupe", callback_data="AMG GT 4-Door Coupe")
        button26 = telebot.types.InlineKeyboardButton(text="190-Class", callback_data="190-Class")
        button27 = telebot.types.InlineKeyboardButton(text="240D", callback_data="240D")
        button28 = telebot.types.InlineKeyboardButton(text="280SE", callback_data="280SE")
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19,
                 button20,
                 button21, button22, button23, button24, button25, button26, button27, button28)
        bot.send_message(message.chat.id, 'Оберіть модель авто:', reply_markup=mark)

    if br == "BMW":
        mark = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="3 Series", callback_data="3 Series")
        button2 = telebot.types.InlineKeyboardButton(text="5 Series", callback_data="5 Series")
        button3 = telebot.types.InlineKeyboardButton(text="7 Series", callback_data="7 Series")
        button4 = telebot.types.InlineKeyboardButton(text="X5", callback_data="X5")
        button5 = telebot.types.InlineKeyboardButton(text="X3", callback_data="X3")
        button6 = telebot.types.InlineKeyboardButton(text="1 Series", callback_data="1 Series")
        button7 = telebot.types.InlineKeyboardButton(text="X1", callback_data="X1")
        button8 = telebot.types.InlineKeyboardButton(text="4 Series", callback_data="4 Series")
        button9 = telebot.types.InlineKeyboardButton(text="2 Series", callback_data="2 Series")
        button10 = telebot.types.InlineKeyboardButton(text="6 Series", callback_data="6 Series")
        button11 = telebot.types.InlineKeyboardButton(text="8 Series", callback_data="8 Series")
        button12 = telebot.types.InlineKeyboardButton(text="X7", callback_data="X7")
        button13 = telebot.types.InlineKeyboardButton(text="Z4", callback_data="Z4")
        button14 = telebot.types.InlineKeyboardButton(text="M4", callback_data="M4")
        button15 = telebot.types.InlineKeyboardButton(text="M3", callback_data="M3")
        button16 = telebot.types.InlineKeyboardButton(text="M5", callback_data="M5")
        button17 = telebot.types.InlineKeyboardButton(text="X6", callback_data="X6")
        button18 = telebot.types.InlineKeyboardButton(text="M2", callback_data="M2")
        button19 = telebot.types.InlineKeyboardButton(text="X4", callback_data="X4")
        button20 = telebot.types.InlineKeyboardButton(text="M8", callback_data="M8")
        button21 = telebot.types.InlineKeyboardButton(text="M6", callback_data="M6")
        button22 = telebot.types.InlineKeyboardButton(text="X2", callback_data="X2")
        button23 = telebot.types.InlineKeyboardButton(text="Z3", callback_data="Z3")
        button24 = telebot.types.InlineKeyboardButton(text="Z8", callback_data="Z8")
        button25 = telebot.types.InlineKeyboardButton(text="325i", callback_data="325i")
        button26 = telebot.types.InlineKeyboardButton(text="325e", callback_data="325e")
        button27 = telebot.types.InlineKeyboardButton(text="325is", callback_data="325is")
        button28 = telebot.types.InlineKeyboardButton(text="325", callback_data="325")
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19,
                 button20,
                 button21, button22, button23, button24, button25, button26, button27, button28)
        bot.send_message(message.chat.id, 'Оберіть модель авто:', reply_markup=mark)

    if br == "Audi":
        mark = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="A4", callback_data="A4")
        button2 = telebot.types.InlineKeyboardButton(text="Q5", callback_data="Q5")
        button3 = telebot.types.InlineKeyboardButton(text="A6", callback_data="A6")
        button4 = telebot.types.InlineKeyboardButton(text="A3", callback_data="A3")
        button5 = telebot.types.InlineKeyboardButton(text="Q7", callback_data="Q7")
        button6 = telebot.types.InlineKeyboardButton(text="A5", callback_data="A5")
        button7 = telebot.types.InlineKeyboardButton(text="X1", callback_data="X1")
        button8 = telebot.types.InlineKeyboardButton(text="TT", callback_data="TT")
        button9 = telebot.types.InlineKeyboardButton(text="S4", callback_data="S4")
        button10 = telebot.types.InlineKeyboardButton(text="A8", callback_data="A8")
        button11 = telebot.types.InlineKeyboardButton(text="RS5", callback_data="RS5")
        button12 = telebot.types.InlineKeyboardButton(text="RS3", callback_data="RS3")
        button13 = telebot.types.InlineKeyboardButton(text="RS7", callback_data="RS7")
        button14 = telebot.types.InlineKeyboardButton(text="R8", callback_data="R8")
        button15 = telebot.types.InlineKeyboardButton(text="S5", callback_data="S5")
        button16 = telebot.types.InlineKeyboardButton(text="Q3", callback_data="Q3")
        button17 = telebot.types.InlineKeyboardButton(text="S3", callback_data="S3")
        button18 = telebot.types.InlineKeyboardButton(text="SQ5", callback_data="SQ5")
        button19 = telebot.types.InlineKeyboardButton(text="A7", callback_data="A7")
        button20 = telebot.types.InlineKeyboardButton(text="A1", callback_data="A1")
        button21 = telebot.types.InlineKeyboardButton(text="S6", callback_data="S6")
        button22 = telebot.types.InlineKeyboardButton(text="RS6", callback_data="RS6")
        button23 = telebot.types.InlineKeyboardButton(text="Q8", callback_data="Q8")
        button24 = telebot.types.InlineKeyboardButton(text="S8", callback_data="S8")
        button25 = telebot.types.InlineKeyboardButton(text="SQ7", callback_data="SQ7")
        button26 = telebot.types.InlineKeyboardButton(text="TT RS", callback_data="TT RS")
        button27 = telebot.types.InlineKeyboardButton(text="RS Q8", callback_data="RS Q8")
        button28 = telebot.types.InlineKeyboardButton(text="100", callback_data="100")
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19,
                 button20,
                 button21, button22, button23, button24, button25, button26, button27, button28)
        bot.send_message(message.chat.id, 'Оберіть модель авто:', reply_markup=mark)

    if br == "Subaru":
        mark = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="Forester", callback_data="Forester")
        button2 = telebot.types.InlineKeyboardButton(text="Outback", callback_data="Outback")
        button3 = telebot.types.InlineKeyboardButton(text="Impreza", callback_data="Impreza")
        button4 = telebot.types.InlineKeyboardButton(text="Crosstrek", callback_data="Crosstrek")
        button5 = telebot.types.InlineKeyboardButton(text="Legacy", callback_data="Legacy")
        button6 = telebot.types.InlineKeyboardButton(text="Ascent", callback_data="Ascent")
        button7 = telebot.types.InlineKeyboardButton(text="WRX", callback_data="WRX")
        button8 = telebot.types.InlineKeyboardButton(text="BRZ", callback_data="BRZ")
        button9 = telebot.types.InlineKeyboardButton(text="Baja", callback_data="Baja")
        button10 = telebot.types.InlineKeyboardButton(text="SVX", callback_data="SVX")
        button11 = telebot.types.InlineKeyboardButton(text="XT", callback_data="XT")
        button12 = telebot.types.InlineKeyboardButton(text="Justy", callback_data="Justy")
        button13 = telebot.types.InlineKeyboardButton(text="Loyale", callback_data="Loyale")
        button14 = telebot.types.InlineKeyboardButton(text="GL", callback_data="GL")
        button15 = telebot.types.InlineKeyboardButton(text="Leone", callback_data="Leone")
        button16 = telebot.types.InlineKeyboardButton(text="Rex", callback_data="Rex")
        button17 = telebot.types.InlineKeyboardButton(text="Trezia", callback_data="Trezia")
        button18 = telebot.types.InlineKeyboardButton(text="Stella", callback_data="Stella")
        button19 = telebot.types.InlineKeyboardButton(text="Alcyone", callback_data="Alcyone")
        button20 = telebot.types.InlineKeyboardButton(text="Impreza WRX", callback_data="Impreza WRX")
        button21 = telebot.types.InlineKeyboardButton(text="Impreza WRX STI", callback_data="Impreza WRX STI")
        button22 = telebot.types.InlineKeyboardButton(text="Legacy B4", callback_data="Legacy B4")
        button23 = telebot.types.InlineKeyboardButton(text="Levorg", callback_data="Levorg")
        button24 = telebot.types.InlineKeyboardButton(text="Traviq", callback_data="Traviq")
        button25 = telebot.types.InlineKeyboardButton(text="Exiga", callback_data="Exiga")
        button26 = telebot.types.InlineKeyboardButton(text="Dex", callback_data="Dex")
        button27 = telebot.types.InlineKeyboardButton(text="Pleo", callback_data="Pleo")
        button28 = telebot.types.InlineKeyboardButton(text="Sambar", callback_data="Sambar")
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19,
                 button20,
                 button21, button22, button23, button24, button25, button26, button27, button28)
        bot.send_message(message.chat.id, 'Оберіть модель авто:', reply_markup=mark)

    if br == "Mazda":
        mark = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="Mazda3", callback_data="Mazda3")
        button2 = telebot.types.InlineKeyboardButton(text="CX-5", callback_data="CX-5")
        button3 = telebot.types.InlineKeyboardButton(text="Mazda6", callback_data="Mazda6")
        button4 = telebot.types.InlineKeyboardButton(text="MX-5 Miata", callback_data="MX-5 Miata")
        button5 = telebot.types.InlineKeyboardButton(text="CX-3", callback_data="CX-3")
        button6 = telebot.types.InlineKeyboardButton(text="CX-30", callback_data="CX-30")
        button7 = telebot.types.InlineKeyboardButton(text="CX-9", callback_data="CX-9")
        button8 = telebot.types.InlineKeyboardButton(text="RX-8", callback_data="RX-8")
        button9 = telebot.types.InlineKeyboardButton(text="MX-6", callback_data="MX-6")
        button10 = telebot.types.InlineKeyboardButton(text="RX-7", callback_data="RX-7")
        button11 = telebot.types.InlineKeyboardButton(text="626", callback_data="626")
        button12 = telebot.types.InlineKeyboardButton(text="Millenia", callback_data="Millenia")
        button13 = telebot.types.InlineKeyboardButton(text="Protege", callback_data="Protege")
        button14 = telebot.types.InlineKeyboardButton(text="Tribute", callback_data="Tribute")
        button15 = telebot.types.InlineKeyboardButton(text="B-Series", callback_data="B-Series")
        button16 = telebot.types.InlineKeyboardButton(text="MPV", callback_data="MPV")
        button17 = telebot.types.InlineKeyboardButton(text="RX-3", callback_data="RX-3")
        button18 = telebot.types.InlineKeyboardButton(text="RX-4", callback_data="RX-4")
        button19 = telebot.types.InlineKeyboardButton(text="929", callback_data="929")
        button20 = telebot.types.InlineKeyboardButton(text="GLC", callback_data="GLC")
        button21 = telebot.types.InlineKeyboardButton(text="CX-7", callback_data="CX-7")
        button22 = telebot.types.InlineKeyboardButton(text="Navajo", callback_data="Navajo")
        button23 = telebot.types.InlineKeyboardButton(text="RX-2", callback_data="RX-2")
        button24 = telebot.types.InlineKeyboardButton(text="808", callback_data="808")
        button25 = telebot.types.InlineKeyboardButton(text="RX-5", callback_data="RX-5")
        button26 = telebot.types.InlineKeyboardButton(text="Cosmo", callback_data="Cosmo")
        button27 = telebot.types.InlineKeyboardButton(text="323", callback_data="323")
        button28 = telebot.types.InlineKeyboardButton(text="Protege5", callback_data="Protege5")
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19,
                 button20,
                 button21, button22, button23, button24, button25, button26, button27, button28)
        bot.send_message(message.chat.id, 'Оберіть модель авто:', reply_markup=mark)

    if br == "Jeep":
        mark = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="Wrangler", callback_data="Wrangler")
        button2 = telebot.types.InlineKeyboardButton(text="Grand Cherokee", callback_data="Grand Cherokee")
        button3 = telebot.types.InlineKeyboardButton(text="Cherokee", callback_data="Cherokee")
        button4 = telebot.types.InlineKeyboardButton(text="Renegade", callback_data="Renegade")
        button5 = telebot.types.InlineKeyboardButton(text="Compass", callback_data="Compass")
        button6 = telebot.types.InlineKeyboardButton(text="Gladiator", callback_data="Gladiator")
        button7 = telebot.types.InlineKeyboardButton(text="Commander", callback_data="Commander")
        button8 = telebot.types.InlineKeyboardButton(text="Patriot", callback_data="Patriot")
        button9 = telebot.types.InlineKeyboardButton(text="Liberty", callback_data="Liberty")
        button10 = telebot.types.InlineKeyboardButton(text="Wagoneer", callback_data="Wagoneer")
        button11 = telebot.types.InlineKeyboardButton(text="CJ", callback_data="CJ")
        button12 = telebot.types.InlineKeyboardButton(text="J-10", callback_data="J-10")
        button13 = telebot.types.InlineKeyboardButton(text="J-20", callback_data="J-20")
        button14 = telebot.types.InlineKeyboardButton(text="J-200", callback_data="J-200")
        button15 = telebot.types.InlineKeyboardButton(text="J-300", callback_data="J-300")
        button16 = telebot.types.InlineKeyboardButton(text="J-4000", callback_data="J-4000")
        button17 = telebot.types.InlineKeyboardButton(text="J-4500", callback_data="J-4500")
        button18 = telebot.types.InlineKeyboardButton(text="J-4600", callback_data="J-4600")
        button19 = telebot.types.InlineKeyboardButton(text="J-4700", callback_data="J-4700")
        button20 = telebot.types.InlineKeyboardButton(text="J-4800", callback_data="J-4800")
        button21 = telebot.types.InlineKeyboardButton(text="J-550", callback_data="J-550")
        button22 = telebot.types.InlineKeyboardButton(text="J-600", callback_data="J-600")
        button23 = telebot.types.InlineKeyboardButton(text="J-700", callback_data="J-700")
        button24 = telebot.types.InlineKeyboardButton(text="J-800", callback_data="J-800")
        button25 = telebot.types.InlineKeyboardButton(text="Scrambler", callback_data="Scrambler")
        button26 = telebot.types.InlineKeyboardButton(text="Honcho", callback_data="Honcho")
        button27 = telebot.types.InlineKeyboardButton(text="Dispatcher", callback_data="Dispatcher")
        button28 = telebot.types.InlineKeyboardButton(text="Forward Control", callback_data="Forward Control")
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19,
                 button20,
                 button21, button22, button23, button24, button25, button26, button27, button28)
        bot.send_message(message.chat.id, 'Оберіть модель авто:', reply_markup=mark)

    if br == "Lexus":
        mark = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="RX", callback_data="RX")
        button2 = telebot.types.InlineKeyboardButton(text="ES", callback_data="ES")
        button3 = telebot.types.InlineKeyboardButton(text="NX", callback_data="NX")
        button4 = telebot.types.InlineKeyboardButton(text="GX", callback_data="GX")
        button5 = telebot.types.InlineKeyboardButton(text="LS", callback_data="LS")
        button6 = telebot.types.InlineKeyboardButton(text="IS", callback_data="IS")
        button7 = telebot.types.InlineKeyboardButton(text="LX", callback_data="LX")
        button8 = telebot.types.InlineKeyboardButton(text="RC", callback_data="RC")
        button9 = telebot.types.InlineKeyboardButton(text="CT", callback_data="CT")
        button10 = telebot.types.InlineKeyboardButton(text="HS", callback_data="HS")
        button11 = telebot.types.InlineKeyboardButton(text="SC", callback_data="SC")
        button12 = telebot.types.InlineKeyboardButton(text="GS", callback_data="GS")
        button13 = telebot.types.InlineKeyboardButton(text="UX", callback_data="UX")
        button14 = telebot.types.InlineKeyboardButton(text="LC", callback_data="LC")
        button15 = telebot.types.InlineKeyboardButton(text="LF-A", callback_data="LF-A")
        button16 = telebot.types.InlineKeyboardButton(text="IS F", callback_data="IS F")
        button17 = telebot.types.InlineKeyboardButton(text="GS F", callback_data="GS F")
        button18 = telebot.types.InlineKeyboardButton(text="LS 600h L", callback_data="LS 600h L")
        button19 = telebot.types.InlineKeyboardButton(text="LS 400", callback_data="LS 400")
        button20 = telebot.types.InlineKeyboardButton(text="GX 470", callback_data="GX 470")
        button21 = telebot.types.InlineKeyboardButton(text="GX 460", callback_data="GX 460")
        button22 = telebot.types.InlineKeyboardButton(text="RX 330", callback_data="RX 330")
        button23 = telebot.types.InlineKeyboardButton(text="RX 300", callback_data="RX 300")
        button24 = telebot.types.InlineKeyboardButton(text="RX 350", callback_data="RX 350")
        button25 = telebot.types.InlineKeyboardButton(text="RX 400h", callback_data="RX 400h")
        button26 = telebot.types.InlineKeyboardButton(text="RX 450h", callback_data="RX 450h")
        button27 = telebot.types.InlineKeyboardButton(text="IS 250", callback_data="IS 250")
        button28 = telebot.types.InlineKeyboardButton(text="IS 350", callback_data="IS 350")
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19,
                 button20,
                 button21, button22, button23, button24, button25, button26, button27, button28)
        bot.send_message(message.chat.id, 'Оберіть модель авто:', reply_markup=mark)

    if br == "GMC":
        mark = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="Sierra 1500", callback_data="Sierra 1500")
        button2 = telebot.types.InlineKeyboardButton(text="Yukon", callback_data="Yukon")
        button3 = telebot.types.InlineKeyboardButton(text="Sierra 2500HD", callback_data="Sierra 2500HD")
        button4 = telebot.types.InlineKeyboardButton(text="Acadia", callback_data="Acadia")
        button5 = telebot.types.InlineKeyboardButton(text="Terrain", callback_data="Terrain")
        button6 = telebot.types.InlineKeyboardButton(text="Canyon", callback_data="Canyon")
        button7 = telebot.types.InlineKeyboardButton(text="Envoy", callback_data="Envoy")
        button8 = telebot.types.InlineKeyboardButton(text="Sierra 3500HD", callback_data="Sierra 3500HD")
        button9 = telebot.types.InlineKeyboardButton(text="Savana", callback_data="Savana")
        button10 = telebot.types.InlineKeyboardButton(text="Yukon XL 1500", callback_data="Yukon XL 1500")
        button11 = telebot.types.InlineKeyboardButton(text="Sonoma", callback_data="Sonoma")
        button12 = telebot.types.InlineKeyboardButton(text="Jimmy", callback_data="Jimmy")
        button13 = telebot.types.InlineKeyboardButton(text="Yukon XL 2500", callback_data="Yukon XL 2500")
        button14 = telebot.types.InlineKeyboardButton(text="Typhoon", callback_data="Typhoon")
        button15 = telebot.types.InlineKeyboardButton(text="S-15", callback_data="S-15")
        button16 = telebot.types.InlineKeyboardButton(text="S-15 Jimmy", callback_data="S-15 Jimmy")
        button17 = telebot.types.InlineKeyboardButton(text="Rally", callback_data="Rally")
        button18 = telebot.types.InlineKeyboardButton(text="Rally Wagon", callback_data="Rally Wagon")
        button19 = telebot.types.InlineKeyboardButton(text="Vandura", callback_data="Vandura")
        button20 = telebot.types.InlineKeyboardButton(text="Caballero", callback_data="Caballero")
        button21 = telebot.types.InlineKeyboardButton(text="Safari", callback_data="Safari")
        button22 = telebot.types.InlineKeyboardButton(text="Sierra 1500 Classic", callback_data="Sierra 1500 Classic")
        button23 = telebot.types.InlineKeyboardButton(text="Sierra 2500", callback_data="Sierra 2500")
        button24 = telebot.types.InlineKeyboardButton(text="Syclone", callback_data="Syclone")
        button25 = telebot.types.InlineKeyboardButton(text="Suburban", callback_data="Suburban")
        button26 = telebot.types.InlineKeyboardButton(text="RX 450h", callback_data="RX 450h")
        button27 = telebot.types.InlineKeyboardButton(text="Tracker", callback_data="Tracker")
        button28 = telebot.types.InlineKeyboardButton(text="C/K 1500", callback_data="C/K 1500")
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19,
                 button20,
                 button21, button22, button23, button24, button25, button26, button27, button28)
        bot.send_message(message.chat.id, 'Оберіть модель авто:', reply_markup=mark)

    if br == "Dodge":
        mark = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="Ram 1500", callback_data="Ram 1500")
        button2 = telebot.types.InlineKeyboardButton(text="Challenger", callback_data="Challenger")
        button3 = telebot.types.InlineKeyboardButton(text="Grand Caravan", callback_data="Grand Caravan")
        button4 = telebot.types.InlineKeyboardButton(text="Charger", callback_data="Charger")
        button5 = telebot.types.InlineKeyboardButton(text="Durango", callback_data="Durango")
        button6 = telebot.types.InlineKeyboardButton(text="Journey", callback_data="Journey")
        button7 = telebot.types.InlineKeyboardButton(text="Ram 2500", callback_data="Ram 2500")
        button8 = telebot.types.InlineKeyboardButton(text="Dakota", callback_data="Dakota")
        button9 = telebot.types.InlineKeyboardButton(text="Avenger", callback_data="Avenger")
        button10 = telebot.types.InlineKeyboardButton(text="Neon", callback_data="Neon")
        button11 = telebot.types.InlineKeyboardButton(text="Nitro", callback_data="Nitro")
        button12 = telebot.types.InlineKeyboardButton(text="Caravan", callback_data="Caravan")
        button13 = telebot.types.InlineKeyboardButton(text="Magnum", callback_data="Magnum")
        button14 = telebot.types.InlineKeyboardButton(text="Stratus", callback_data="Stratus")
        button15 = telebot.types.InlineKeyboardButton(text="Ram 3500", callback_data="Ram 3500")
        button16 = telebot.types.InlineKeyboardButton(text="Intrepid", callback_data="Intrepid")
        button17 = telebot.types.InlineKeyboardButton(text="Ram Van", callback_data="Ram Van")
        button18 = telebot.types.InlineKeyboardButton(text="Caliber", callback_data="Caliber")
        button19 = telebot.types.InlineKeyboardButton(text="Ram 150", callback_data="Ram 150")
        button20 = telebot.types.InlineKeyboardButton(text="Ram Wagon", callback_data="Ram Wagon")
        button21 = telebot.types.InlineKeyboardButton(text="Viper", callback_data="Viper")
        button22 = telebot.types.InlineKeyboardButton(text="Daytona", callback_data="Daytona")
        button23 = telebot.types.InlineKeyboardButton(text="Spirit", callback_data="Spirit")
        button24 = telebot.types.InlineKeyboardButton(text="Aries", callback_data="Aries")
        button25 = telebot.types.InlineKeyboardButton(text="Stealth", callback_data="Stealth")
        button26 = telebot.types.InlineKeyboardButton(text="Omni", callback_data="Omni")
        button27 = telebot.types.InlineKeyboardButton(text="Shadow", callback_data="Shadow")
        button28 = telebot.types.InlineKeyboardButton(text="Dynasty", callback_data="Dynasty")
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19,
                 button20,
                 button21, button22, button23, button24, button25, button26, button27, button28)
        bot.send_message(message.chat.id, 'Оберіть модель авто:', reply_markup=mark)

    if br == "Porsche":
        mark = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="911", callback_data="911")
        button2 = telebot.types.InlineKeyboardButton(text="Cayenne", callback_data="Cayenne")
        button3 = telebot.types.InlineKeyboardButton(text="Panamera", callback_data="Panamera")
        button4 = telebot.types.InlineKeyboardButton(text="Macan", callback_data="Macan")
        button5 = telebot.types.InlineKeyboardButton(text="Boxster", callback_data="Boxster")
        button6 = telebot.types.InlineKeyboardButton(text="Carrera GT", callback_data="Carrera GT")
        button7 = telebot.types.InlineKeyboardButton(text="718 Cayman", callback_data="718 Cayman")
        button8 = telebot.types.InlineKeyboardButton(text="928", callback_data="928")
        button9 = telebot.types.InlineKeyboardButton(text="944", callback_data="944")
        button10 = telebot.types.InlineKeyboardButton(text="968", callback_data="968")
        button11 = telebot.types.InlineKeyboardButton(text="959", callback_data="959")
        button12 = telebot.types.InlineKeyboardButton(text="914", callback_data="914")
        button13 = telebot.types.InlineKeyboardButton(text="356", callback_data="356")
        button14 = telebot.types.InlineKeyboardButton(text="912", callback_data="912")
        button15 = telebot.types.InlineKeyboardButton(text="911 GT2", callback_data="911 GT2")
        button16 = telebot.types.InlineKeyboardButton(text="911 GT3", callback_data="911 GT3")
        button17 = telebot.types.InlineKeyboardButton(text="911 RSR", callback_data="911 RSR")
        button18 = telebot.types.InlineKeyboardButton(text="917", callback_data="917")
        button19 = telebot.types.InlineKeyboardButton(text="918 Spyder", callback_data="918 Spyder")
        button20 = telebot.types.InlineKeyboardButton(text="924", callback_data="924")
        button21 = telebot.types.InlineKeyboardButton(text="934", callback_data="934")
        button22 = telebot.types.InlineKeyboardButton(text="935", callback_data="935")
        button23 = telebot.types.InlineKeyboardButton(text="962", callback_data="962")
        button24 = telebot.types.InlineKeyboardButton(text="968 Turbo S", callback_data="968 Turbo S")
        button25 = telebot.types.InlineKeyboardButton(text="Carrera", callback_data="Carrera")
        button26 = telebot.types.InlineKeyboardButton(text="Cayman", callback_data="Cayman")
        button27 = telebot.types.InlineKeyboardButton(text="CGT", callback_data="CGT")
        button28 = telebot.types.InlineKeyboardButton(text="Turbo", callback_data="Turbo")
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19,
                 button20,
                 button21, button22, button23, button24, button25, button26, button27, button28)
        bot.send_message(message.chat.id, 'Оберіть модель авто:', reply_markup=mark)

    if br == "Chrysler":
        mark = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="300", callback_data="300")
        button2 = telebot.types.InlineKeyboardButton(text="Pacifica", callback_data="Pacifica")
        button3 = telebot.types.InlineKeyboardButton(text="Voyager", callback_data="Voyager")
        button4 = telebot.types.InlineKeyboardButton(text="Crossfire", callback_data="Crossfire")
        button5 = telebot.types.InlineKeyboardButton(text="Concorde", callback_data="Concorde")
        button6 = telebot.types.InlineKeyboardButton(text="Aspen", callback_data="Aspen")
        button7 = telebot.types.InlineKeyboardButton(text="PT Cruiser", callback_data="PT Cruiser")
        button8 = telebot.types.InlineKeyboardButton(text="LHS", callback_data="LHS")
        button9 = telebot.types.InlineKeyboardButton(text="Imperial", callback_data="Imperial")
        button10 = telebot.types.InlineKeyboardButton(text="New Yorker", callback_data="New Yorker")
        button11 = telebot.types.InlineKeyboardButton(text="Cirrus", callback_data="Cirrus")
        button12 = telebot.types.InlineKeyboardButton(text="LeBaron", callback_data="LeBaron")
        button13 = telebot.types.InlineKeyboardButton(text="Intrepid", callback_data="Intrepid")
        button14 = telebot.types.InlineKeyboardButton(text="TC", callback_data="TC")
        button15 = telebot.types.InlineKeyboardButton(text="Fifth Avenue", callback_data="Fifth Avenue")
        button16 = telebot.types.InlineKeyboardButton(text="Airflow", callback_data="Airflow")
        button17 = telebot.types.InlineKeyboardButton(text="Prowler", callback_data="Prowler")
        button18 = telebot.types.InlineKeyboardButton(text="Royal", callback_data="Royal")
        button19 = telebot.types.InlineKeyboardButton(text="Windsor", callback_data="Windsor")
        button20 = telebot.types.InlineKeyboardButton(text="Saratoga", callback_data="Saratoga")
        button21 = telebot.types.InlineKeyboardButton(text="Stratus", callback_data="Stratus")
        button22 = telebot.types.InlineKeyboardButton(text="Crown Imperial", callback_data="Crown Imperial")
        button23 = telebot.types.InlineKeyboardButton(text="300M", callback_data="300M")
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19,
                 button20,
                 button21, button22, button23)
        bot.send_message(message.chat.id, 'Оберіть модель авто:', reply_markup=mark)

    if br == "Mitsubishi":
        mark = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="Lancer", callback_data="Lancer")
        button2 = telebot.types.InlineKeyboardButton(text="Outlander", callback_data="Outlander")
        button3 = telebot.types.InlineKeyboardButton(text="Eclipse", callback_data="Eclipse")
        button4 = telebot.types.InlineKeyboardButton(text="Galant", callback_data="Galant")
        button5 = telebot.types.InlineKeyboardButton(text="Mirage", callback_data="Mirage")
        button6 = telebot.types.InlineKeyboardButton(text="Pajero", callback_data="Pajero")
        button7 = telebot.types.InlineKeyboardButton(text="ASX", callback_data="ASX")
        button8 = telebot.types.InlineKeyboardButton(text="RVR", callback_data="RVR")
        button9 = telebot.types.InlineKeyboardButton(text="Delica", callback_data="Delica")
        button10 = telebot.types.InlineKeyboardButton(text="Colt", callback_data="Colt")
        button11 = telebot.types.InlineKeyboardButton(text="Grandis", callback_data="Grandis")
        button12 = telebot.types.InlineKeyboardButton(text="Strada", callback_data="Strada")
        button13 = telebot.types.InlineKeyboardButton(text="Chariot", callback_data="Chariot")
        button14 = telebot.types.InlineKeyboardButton(text="Diamante", callback_data="Diamante")
        button15 = telebot.types.InlineKeyboardButton(text="Endeavor", callback_data="Endeavor")
        button16 = telebot.types.InlineKeyboardButton(text="L200", callback_data="L200")
        button17 = telebot.types.InlineKeyboardButton(text="3000GT", callback_data="3000GT")
        button18 = telebot.types.InlineKeyboardButton(text="Montero", callback_data="Montero")
        button19 = telebot.types.InlineKeyboardButton(text="Sigma", callback_data="Sigma")
        button20 = telebot.types.InlineKeyboardButton(text="Lancer Evolution", callback_data="Lancer Evolution")
        button21 = telebot.types.InlineKeyboardButton(text="Carisma", callback_data="Carisma")
        button22 = telebot.types.InlineKeyboardButton(text="Space Star", callback_data="Space Star")
        button23 = telebot.types.InlineKeyboardButton(text="Tredia", callback_data="Tredia")
        button24 = telebot.types.InlineKeyboardButton(text="Starion", callback_data="Starion")
        button25 = telebot.types.InlineKeyboardButton(text="GTO", callback_data="GTO")
        button26 = telebot.types.InlineKeyboardButton(text="Lancer Sportback", callback_data="Lancer Sportback")
        button27 = telebot.types.InlineKeyboardButton(text="Magna", callback_data="Magna")
        button28 = telebot.types.InlineKeyboardButton(text="Raider", callback_data="Raider")
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19,
                 button20,
                 button21, button22, button23, button24, button25, button26, button27, button28)
        bot.send_message(message.chat.id, 'Оберіть модель авто:', reply_markup=mark)

    if br == "Volvo":
        mark = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="volvo xc90", callback_data="volvo xc90")
        button2 = telebot.types.InlineKeyboardButton(text="volvo xc60", callback_data="volvo xc60")
        button3 = telebot.types.InlineKeyboardButton(text="volvo xc40", callback_data="volvo xc40")
        button4 = telebot.types.InlineKeyboardButton(text="volvo s60", callback_data="volvo s60")
        button5 = telebot.types.InlineKeyboardButton(text="volvo v60", callback_data="volvo v60")
        button6 = telebot.types.InlineKeyboardButton(text="volvo s90", callback_data="volvo s90")
        button7 = telebot.types.InlineKeyboardButton(text="volvo v90", callback_data="volvo v90")
        button8 = telebot.types.InlineKeyboardButton(text="volvo c70", callback_data="volvo c70")
        button9 = telebot.types.InlineKeyboardButton(text="volvo v70", callback_data="volvo v70")
        button10 = telebot.types.InlineKeyboardButton(text="volvo s40", callback_data="volvo s40")
        button11 = telebot.types.InlineKeyboardButton(text="volvo v40", callback_data="volvo v40")
        button12 = telebot.types.InlineKeyboardButton(text="volvo 850", callback_data="volvo 850")
        button13 = telebot.types.InlineKeyboardButton(text="volvo 240", callback_data="volvo 240")
        button14 = telebot.types.InlineKeyboardButton(text="volvo 740", callback_data="volvo 740")
        button15 = telebot.types.InlineKeyboardButton(text="volvo 940", callback_data="volvo 940")
        button16 = telebot.types.InlineKeyboardButton(text="volvo s70", callback_data="volvo s70")
        button17 = telebot.types.InlineKeyboardButton(text="volvo c30", callback_data="volvo c30")
        button18 = telebot.types.InlineKeyboardButton(text="volvo s80", callback_data="volvo s80")
        button19 = telebot.types.InlineKeyboardButton(text="volvo v50", callback_data="volvo v50")
        button20 = telebot.types.InlineKeyboardButton(text="volvo 960", callback_data="volvo 960")
        button21 = telebot.types.InlineKeyboardButton(text="volvo 1800", callback_data="volvo 1800")
        button22 = telebot.types.InlineKeyboardButton(text="volvo 480", callback_data="volvo 480")
        button23 = telebot.types.InlineKeyboardButton(text="volvo 66", callback_data="volvo 66")
        button24 = telebot.types.InlineKeyboardButton(text="volvo 144", callback_data="volvo 144")
        button25 = telebot.types.InlineKeyboardButton(text="volvo 145", callback_data="volvo 145")
        button26 = telebot.types.InlineKeyboardButton(text="volvo 164", callback_data="volvo 164")
        button27 = telebot.types.InlineKeyboardButton(text="volvo 242", callback_data="volvo 242")
        button28 = telebot.types.InlineKeyboardButton(text="volvo 244", callback_data="volvo 244")
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19,
                 button20,
                 button21, button22, button23, button24, button25, button26, button27, button28)
        bot.send_message(message.chat.id, 'Оберіть модель авто:', reply_markup=mark)

    if br == "Fiat":
        mark = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="500", callback_data="500")
        button2 = telebot.types.InlineKeyboardButton(text="Panda", callback_data="Panda")
        button3 = telebot.types.InlineKeyboardButton(text="Tipo", callback_data="Tipo")
        button4 = telebot.types.InlineKeyboardButton(text="Ducato", callback_data="Ducato")
        button5 = telebot.types.InlineKeyboardButton(text="Bravo", callback_data="Bravo")
        button6 = telebot.types.InlineKeyboardButton(text="Punto", callback_data="Punto")
        button7 = telebot.types.InlineKeyboardButton(text="Uno", callback_data="Uno")
        button8 = telebot.types.InlineKeyboardButton(text="124 Spider", callback_data="124 Spider")
        button9 = telebot.types.InlineKeyboardButton(text="Cinquecento", callback_data="Cinquecento")
        button10 = telebot.types.InlineKeyboardButton(text="Doblo", callback_data="Doblo")
        button11 = telebot.types.InlineKeyboardButton(text="Stilo", callback_data="Stilo")
        button12 = telebot.types.InlineKeyboardButton(text="Seicento", callback_data="Seicento")
        button13 = telebot.types.InlineKeyboardButton(text="Scudo", callback_data="Scudo")
        button14 = telebot.types.InlineKeyboardButton(text="Barchetta", callback_data="Barchetta")
        button15 = telebot.types.InlineKeyboardButton(text="Qubo", callback_data="Qubo")
        button16 = telebot.types.InlineKeyboardButton(text="Croma", callback_data="Croma")
        button17 = telebot.types.InlineKeyboardButton(text="Multipla", callback_data="Multipla")
        button18 = telebot.types.InlineKeyboardButton(text="Grande Punto", callback_data="Grande Punto")
        button19 = telebot.types.InlineKeyboardButton(text="Talento", callback_data="Talento")
        button20 = telebot.types.InlineKeyboardButton(text="124", callback_data="124")
        button21 = telebot.types.InlineKeyboardButton(text="Marea", callback_data="Marea")
        button22 = telebot.types.InlineKeyboardButton(text="Fiorino", callback_data="Fiorino")
        button23 = telebot.types.InlineKeyboardButton(text="Argo", callback_data="Argo")
        button24 = telebot.types.InlineKeyboardButton(text="Idea", callback_data="Idea")
        button25 = telebot.types.InlineKeyboardButton(text="Dino", callback_data="Dino")
        button26 = telebot.types.InlineKeyboardButton(text="Linea", callback_data="Linea")
        button27 = telebot.types.InlineKeyboardButton(text="X1/9", callback_data="X1/9")
        button28 = telebot.types.InlineKeyboardButton(text="Regata", callback_data="Regata")
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19,
                 button20,
                 button21, button22, button23, button24, button25, button26, button27, button28)
        bot.send_message(message.chat.id, 'Оберіть модель авто:', reply_markup=mark)

    if br == "Land Rover":
        mark = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="Defender", callback_data="Defender")
        button2 = telebot.types.InlineKeyboardButton(text="Range Rover", callback_data="Range Rover")
        button3 = telebot.types.InlineKeyboardButton(text="Discovery", callback_data="Discovery")
        button4 = telebot.types.InlineKeyboardButton(text="Range Rover Sport", callback_data="Range Rover Sport")
        button5 = telebot.types.InlineKeyboardButton(text="Range Rover Evoque", callback_data="Range Rover Evoque")
        button6 = telebot.types.InlineKeyboardButton(text="Range Rover Velar", callback_data="Range Rover Velar")
        button7 = telebot.types.InlineKeyboardButton(text="Freelander", callback_data="Freelander")
        button8 = telebot.types.InlineKeyboardButton(text="Range Rover Classic", callback_data="Range Rover Classic")
        button9 = telebot.types.InlineKeyboardButton(text="Discovery Sport", callback_data="Discovery Sport")
        button10 = telebot.types.InlineKeyboardButton(text="Series I", callback_data="Series I")
        button11 = telebot.types.InlineKeyboardButton(text="Series II", callback_data="Series II")
        button12 = telebot.types.InlineKeyboardButton(text="Series III", callback_data="Series III")
        button13 = telebot.types.InlineKeyboardButton(text="Range Rover P38A", callback_data="Range Rover P38A")
        button14 = telebot.types.InlineKeyboardButton(text="Range Rover L322", callback_data="Range Rover L322")
        button15 = telebot.types.InlineKeyboardButton(text="Range Rover L405", callback_data="Range Rover L405")
        button16 = telebot.types.InlineKeyboardButton(text="Range Rover Sport L320",
                                                      callback_data="Range Rover Sport L320")
        button17 = telebot.types.InlineKeyboardButton(text="Range Rover Sport L494",
                                                      callback_data="Range Rover Sport L494")
        button18 = telebot.types.InlineKeyboardButton(text="Range Rover Evoque L538",
                                                      callback_data="Range Rover Evoque L538")
        button19 = telebot.types.InlineKeyboardButton(text="Discovery L319", callback_data="Discovery L319")
        button20 = telebot.types.InlineKeyboardButton(text="Discovery 2", callback_data="Discovery 2")
        button21 = telebot.types.InlineKeyboardButton(text="Discovery 3", callback_data="Discovery 3")
        button22 = telebot.types.InlineKeyboardButton(text="Discovery 4", callback_data="Discovery 4")
        button23 = telebot.types.InlineKeyboardButton(text="Discovery 5", callback_data="Discovery 5")
        button24 = telebot.types.InlineKeyboardButton(text="Freelander 2", callback_data="Freelander 2")
        button25 = telebot.types.InlineKeyboardButton(text="Range Rover Evoque L551",
                                                      callback_data="Range Rover Evoque L551")
        button26 = telebot.types.InlineKeyboardButton(text="Range Rover Velar L560",
                                                      callback_data="Range Rover Velar L560")
        button27 = telebot.types.InlineKeyboardButton(text="Range Rover Velar L550",
                                                      callback_data="Range Rover Velar L550")
        button28 = telebot.types.InlineKeyboardButton(text="Defender (2020)", callback_data="Defender (2020)")
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19,
                 button20,
                 button21, button22, button23, button24, button25, button26, button27, button28)
        bot.send_message(message.chat.id, 'Оберіть модель авто:', reply_markup=mark)

    if br == "Infiniti":
        mark = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="Q50", callback_data="Q50")
        button2 = telebot.types.InlineKeyboardButton(text="Q60", callback_data="Q60")
        button3 = telebot.types.InlineKeyboardButton(text="Q70", callback_data="Q70")
        button4 = telebot.types.InlineKeyboardButton(text="QX30", callback_data="QX30")
        button5 = telebot.types.InlineKeyboardButton(text="QX50", callback_data="QX50")
        button6 = telebot.types.InlineKeyboardButton(text="QX60", callback_data="QX60")
        button7 = telebot.types.InlineKeyboardButton(text="QX70", callback_data="QX70")
        button8 = telebot.types.InlineKeyboardButton(text="QX80", callback_data="QX80")
        button9 = telebot.types.InlineKeyboardButton(text="EX", callback_data="EX")
        button10 = telebot.types.InlineKeyboardButton(text="FX", callback_data="FX")
        button11 = telebot.types.InlineKeyboardButton(text="JX", callback_data="JX")
        button12 = telebot.types.InlineKeyboardButton(text="M30", callback_data="M30")
        button13 = telebot.types.InlineKeyboardButton(text="M35", callback_data="M35")
        button14 = telebot.types.InlineKeyboardButton(text="M37", callback_data="M37")
        button15 = telebot.types.InlineKeyboardButton(text="M45", callback_data="M45")
        button16 = telebot.types.InlineKeyboardButton(text="M56", callback_data="M56")
        button17 = telebot.types.InlineKeyboardButton(text="G20", callback_data="G20")
        button18 = telebot.types.InlineKeyboardButton(text="G25", callback_data="G25")
        button19 = telebot.types.InlineKeyboardButton(text="G35", callback_data="G35")
        button20 = telebot.types.InlineKeyboardButton(text="G37", callback_data="G37")
        button21 = telebot.types.InlineKeyboardButton(text="I30", callback_data="I30")
        button22 = telebot.types.InlineKeyboardButton(text="I35", callback_data="I35")
        button23 = telebot.types.InlineKeyboardButton(text="J30", callback_data="J30")
        button24 = telebot.types.InlineKeyboardButton(text="Q40", callback_data="Q40")
        button25 = telebot.types.InlineKeyboardButton(text="Q45", callback_data="Q45")
        button26 = telebot.types.InlineKeyboardButton(text="QX4", callback_data="QX4")
        button27 = telebot.types.InlineKeyboardButton(text="QX56", callback_data="QX56")
        button28 = telebot.types.InlineKeyboardButton(text="QX70S", callback_data="QX70S")
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19,
                 button20,
                 button21, button22, button23, button24, button25, button26, button27, button28)
        bot.send_message(message.chat.id, 'Оберіть модель авто:', reply_markup=mark)

    if br == "Peugeot":
        mark = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="108", callback_data="108")
        button2 = telebot.types.InlineKeyboardButton(text="208", callback_data="208")
        button3 = telebot.types.InlineKeyboardButton(text="308", callback_data="308")
        button4 = telebot.types.InlineKeyboardButton(text="408", callback_data="408")
        button5 = telebot.types.InlineKeyboardButton(text="508", callback_data="508")
        button6 = telebot.types.InlineKeyboardButton(text="3008", callback_data="3008")
        button7 = telebot.types.InlineKeyboardButton(text="5008", callback_data="5008")
        button8 = telebot.types.InlineKeyboardButton(text="Partner", callback_data="Partner")
        button9 = telebot.types.InlineKeyboardButton(text="Rifter", callback_data="Rifter")
        button10 = telebot.types.InlineKeyboardButton(text="Traveller", callback_data="Traveller")
        button11 = telebot.types.InlineKeyboardButton(text="iOn", callback_data="iOn")
        button12 = telebot.types.InlineKeyboardButton(text="206", callback_data="206")
        button13 = telebot.types.InlineKeyboardButton(text="207", callback_data="207")
        button14 = telebot.types.InlineKeyboardButton(text="307", callback_data="307")
        button15 = telebot.types.InlineKeyboardButton(text="406", callback_data="406")
        button16 = telebot.types.InlineKeyboardButton(text="407", callback_data="407")
        button17 = telebot.types.InlineKeyboardButton(text="807", callback_data="807")
        button18 = telebot.types.InlineKeyboardButton(text="106", callback_data="106")
        button19 = telebot.types.InlineKeyboardButton(text="206+", callback_data="206+")
        button20 = telebot.types.InlineKeyboardButton(text="301", callback_data="301")
        button21 = telebot.types.InlineKeyboardButton(text="Bipper", callback_data="Bipper")
        button22 = telebot.types.InlineKeyboardButton(text="Expert", callback_data="Expert")
        button23 = telebot.types.InlineKeyboardButton(text="Boxer", callback_data="Boxer")
        button24 = telebot.types.InlineKeyboardButton(text="RCZ", callback_data="RCZ")
        button25 = telebot.types.InlineKeyboardButton(text="4007", callback_data="4007")
        button26 = telebot.types.InlineKeyboardButton(text="4008", callback_data="4008")
        button27 = telebot.types.InlineKeyboardButton(text="508 RXH", callback_data="508 RXH")
        button28 = telebot.types.InlineKeyboardButton(text="508 SW", callback_data="508 SW")
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19,
                 button20,
                 button21, button22, button23, button24, button25, button26, button27, button28)
        bot.send_message(message.chat.id, 'Оберіть модель авто:', reply_markup=mark)

    if br == "Renault":
        mark = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="Clio", callback_data="Clio")
        button2 = telebot.types.InlineKeyboardButton(text="Captur", callback_data="Captur")
        button3 = telebot.types.InlineKeyboardButton(text="Megane", callback_data="Megane")
        button4 = telebot.types.InlineKeyboardButton(text="Scenic", callback_data="Scenic")
        button5 = telebot.types.InlineKeyboardButton(text="Kadjar", callback_data="Kadjar")
        button6 = telebot.types.InlineKeyboardButton(text="Talisman", callback_data="Talisman")
        button7 = telebot.types.InlineKeyboardButton(text="Koleos", callback_data="Koleos")
        button8 = telebot.types.InlineKeyboardButton(text="Zoe", callback_data="Zoe")
        button9 = telebot.types.InlineKeyboardButton(text="Twingo", callback_data="Twingo")
        button10 = telebot.types.InlineKeyboardButton(text="Espace", callback_data="Espace")
        button11 = telebot.types.InlineKeyboardButton(text="Laguna", callback_data="Laguna")
        button12 = telebot.types.InlineKeyboardButton(text="Fluence", callback_data="Fluence")
        button13 = telebot.types.InlineKeyboardButton(text="Kangoo", callback_data="Kangoo")
        button14 = telebot.types.InlineKeyboardButton(text="Trafic", callback_data="Trafic")
        button15 = telebot.types.InlineKeyboardButton(text="Master", callback_data="Master")
        button16 = telebot.types.InlineKeyboardButton(text="Modus", callback_data="Modus")
        button17 = telebot.types.InlineKeyboardButton(text="Grand Scenic", callback_data="Grand Scenic")
        button18 = telebot.types.InlineKeyboardButton(text="Symbol", callback_data="Symbol")
        button19 = telebot.types.InlineKeyboardButton(text="Sandero", callback_data="Sandero")
        button20 = telebot.types.InlineKeyboardButton(text="Duster", callback_data="Duster")
        button21 = telebot.types.InlineKeyboardButton(text="Clio Estate", callback_data="Clio Estate")
        button22 = telebot.types.InlineKeyboardButton(text="Zoe R110", callback_data="Zoe R110")
        button23 = telebot.types.InlineKeyboardButton(text="Arkana", callback_data="Arkana")
        button24 = telebot.types.InlineKeyboardButton(text="Megane Estate", callback_data="Megane Estate")
        button25 = telebot.types.InlineKeyboardButton(text="Kadjar RS", callback_data="Kadjar RS")
        button26 = telebot.types.InlineKeyboardButton(text="Talisman Estate", callback_data="Talisman Estate")
        button27 = telebot.types.InlineKeyboardButton(text="Talisman RS", callback_data="Talisman RS")
        button28 = telebot.types.InlineKeyboardButton(text="Koleos II", callback_data="Koleos II")
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19,
                 button20,
                 button21, button22, button23, button24, button25, button26, button27, button28)
        bot.send_message(message.chat.id, 'Оберіть модель авто:', reply_markup=mark)

        # Citroen
        "C3", "C4", "C5", "C1", "C-Elysee", "C3 Aircross", "C4 Cactus", "C4 Picasso", "Berlingo", "SpaceTourer", "Jumpy",
        "C-Zero", "DS 3", "DS 4", "DS 5", "DS 7", "AMI", "C-Elysee WTCC", "C3 Picasso", "C4 Sedan", "C4 Spacetourer",
        "C4 Grand Picasso", "C5 Aircross", "C3 Pluriel", "Nemo", "Xsara", "Xantia", "Saxo", "BX", "ZX"

    if br == "Citroen":
        mark = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="C3", callback_data="C3")
        button2 = telebot.types.InlineKeyboardButton(text="C4", callback_data="C4")
        button3 = telebot.types.InlineKeyboardButton(text="C5", callback_data="C5")
        button4 = telebot.types.InlineKeyboardButton(text="C1", callback_data="C1")
        button5 = telebot.types.InlineKeyboardButton(text="C-Elysee", callback_data="C-Elysee")
        button6 = telebot.types.InlineKeyboardButton(text="C3 Aircross", callback_data="C3 Aircross")
        button7 = telebot.types.InlineKeyboardButton(text="C4 Cactus", callback_data="C4 Cactus")
        button8 = telebot.types.InlineKeyboardButton(text="C4 Picasso", callback_data="C4 Picasso")
        button9 = telebot.types.InlineKeyboardButton(text="Berlingo", callback_data="Berlingo")
        button10 = telebot.types.InlineKeyboardButton(text="SpaceTourer", callback_data="SpaceTourer")
        button11 = telebot.types.InlineKeyboardButton(text="Jumpy", callback_data="Jumpy")
        button12 = telebot.types.InlineKeyboardButton(text="C-Zero", callback_data="C-Zero")
        button13 = telebot.types.InlineKeyboardButton(text="DS 3", callback_data="DS 3")
        button14 = telebot.types.InlineKeyboardButton(text="DS 4", callback_data="DS 4")
        button15 = telebot.types.InlineKeyboardButton(text="DS 5", callback_data="DS 5")
        button16 = telebot.types.InlineKeyboardButton(text="DS 7", callback_data="DS 7")
        button17 = telebot.types.InlineKeyboardButton(text="AMI", callback_data="AMI")
        button18 = telebot.types.InlineKeyboardButton(text="C-Elysee WTCC", callback_data="C-Elysee WTCC")
        button19 = telebot.types.InlineKeyboardButton(text="C3 Picasso", callback_data="C3 Picasso")
        button20 = telebot.types.InlineKeyboardButton(text="C4 Sedan", callback_data="C4 Sedan")
        button21 = telebot.types.InlineKeyboardButton(text="C4 Spacetourer", callback_data="C4 Spacetourer")
        button22 = telebot.types.InlineKeyboardButton(text="C4 Grand Picasso", callback_data="C4 Grand Picasso")
        button23 = telebot.types.InlineKeyboardButton(text="C5 Aircross", callback_data="C5 Aircross")
        button24 = telebot.types.InlineKeyboardButton(text="C3 Pluriel", callback_data="C3 Pluriel")
        button25 = telebot.types.InlineKeyboardButton(text="Nemo", callback_data="Nemo")
        button26 = telebot.types.InlineKeyboardButton(text="Xsara", callback_data="Xsara")
        button27 = telebot.types.InlineKeyboardButton(text="Xantia", callback_data="Xantia")
        button28 = telebot.types.InlineKeyboardButton(text="Saxo", callback_data="Saxo")
        mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                 button11, button12, button13, button14, button15, button16, button17, button18, button19,
                 button20,
                 button21, button22, button23, button24, button25, button26, button27, button28)
        bot.send_message(message.chat.id, 'Оберіть модель авто:', reply_markup=mark)


@bot.callback_query_handler(func=lambda call: call.data in models)
def query_model(call):
    bot.answer_callback_query(callback_query_id=call.id)
    global mod
    mod = call.data
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
    mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11,
             button12, button13, button14, button15, button16, button17, button18, button19, button20, button21,
             button22, button23, button24, button25, button26, button27, button28, button29)
    bot.send_message(message.chat.id, 'Оберіть рік випуску автомобіля', reply_markup=mark)


@bot.callback_query_handler(func=lambda call: call.data in years)
def query_year(call):
    bot.answer_callback_query(callback_query_id=call.id)
    global yr
    yr = call.data
    print(yr)
    bot.send_message(call.message.chat.id, 'Обраний рік випуску: ' + yr)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    engine_type(call.message)


@bot.message_handler(content_types=["text"])
def engine_type(message):
    mark = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton(text="Бензиновий", callback_data="Бензиновий")
    button2 = telebot.types.InlineKeyboardButton(text="Дизельний", callback_data="Дизельний")
    mark.add(button1, button2)
    bot.send_message(message.chat.id, 'Оберіть тип двигуна', reply_markup=mark)


@bot.callback_query_handler(func=lambda call: call.data in engine_types)
def query_enginetype(call):
    bot.answer_callback_query(callback_query_id=call.id)
    global ent
    ent = call.data
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
    button7 = telebot.types.InlineKeyboardButton(text="1.7", callback_data="1.7")
    button8 = telebot.types.InlineKeyboardButton(text="1.8", callback_data="1.8")
    button9 = telebot.types.InlineKeyboardButton(text="1.9", callback_data="1.9")
    button10 = telebot.types.InlineKeyboardButton(text="2.0", callback_data="2.0")
    button11 = telebot.types.InlineKeyboardButton(text="2.2", callback_data="2.2")
    button12 = telebot.types.InlineKeyboardButton(text="2.4", callback_data="2.4")
    button13 = telebot.types.InlineKeyboardButton(text="2.5", callback_data="2.5")
    button14 = telebot.types.InlineKeyboardButton(text="2.7", callback_data="2.7")
    button15 = telebot.types.InlineKeyboardButton(text="2.8", callback_data="2.8")
    button16 = telebot.types.InlineKeyboardButton(text="3.0", callback_data="3.0")
    button17 = telebot.types.InlineKeyboardButton(text="3.5", callback_data="3.5")
    button18 = telebot.types.InlineKeyboardButton(text="4.0", callback_data="4.0")
    button19 = telebot.types.InlineKeyboardButton(text="4.6", callback_data="4.6")
    button20 = telebot.types.InlineKeyboardButton(text="5.0", callback_data="5.0")
    button21 = telebot.types.InlineKeyboardButton(text="6.2", callback_data="6.2")
    mark.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11,
             button12, button13, button14, button15, button16, button17, button18, button19, button20, button21)
    bot.send_message(message.chat.id, "Оберіть об'єм двигуна", reply_markup=mark)


@bot.callback_query_handler(func=lambda call: call.data in engines)
def query_enginetype(call):
    bot.answer_callback_query(callback_query_id=call.id)
    global eng
    eng = call.data
    print(eng)
    bot.send_message(call.message.chat.id, "Обраний об'єм двигуна: " + eng)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    info(call.message)


def stepinit(message):
    i = message.text
    if i == 'Так':
        url = f"https://auto.ria.com/uk/legkovie/{br}/{mod}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        prices = []
        for item in soup.select(".ticket-item"):
            price_element = item.select_one(".price-ticket .green")
            if price_element is not None:
                price = int(price_element.get_text(strip=True).replace(" ", ""))
                prices.append(price)

        if prices:
            avg_price = sum(prices) / len(prices)
            bot.send_message(message.chat.id,
                             f"Середня ціна на <a href='{url}'>{br.upper()} {mod.upper()}</a>: {avg_price:.2f} $ \n<i>Ціна вказана незалежно від року випуску</i>",
                             parse_mode='HTML')
            reset_message(message)
        else:
            bot.send_message(message.chat.id, f"Автомобілів {br.upper()} {mod.upper()} на сайті не знайдено.")
            reset_message(message)

    if i == 'Ні':
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
    elif eng == '1.7':
        engv = 1.7
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
    rik = (2023 - int(yr))
    if rik == 0:
        vartist_rozm = stavka * engv * 1
    else:
        vartist_rozm = stavka * engv * rik
    print(vartist_rozm)
    bot.send_message(message.chat.id,
                     'Отже ви вибрали:\n' + 'Бренд: ' + br + '\n' + 'Модель: ' + mod + '\n' + 'Рік випуску: ' + yr + '\n' + 'Тип двигуна: ' + ent.lower() + '\n' + "Об'єм двигуна: " + eng + '\n' + 'Вартість розмитнення: {:.2f}'.format(
                         vartist_rozm) + '$')
    bot.send_message(message.chat.id,
                     f"Натисніть 'Так', якщо бажаєте дізнатися середню ціну на {br.upper()} {mod.upper()} в Україні, або натисніть 'Ні'",
                     reply_markup=keyboard2)
    bot.register_next_step_handler(message, stepinit)


bot.polling()
