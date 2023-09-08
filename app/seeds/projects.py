from app.models import db, Project, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import date



def seed_projects():
    project1 = Project(
        name='Mystic Realms: Legends of Enchantoria',
        description='Embark on a mystical journey in this enchanting board game. Dive into the lore, meet magical creatures, and unravel the secrets of Enchantoria!',
        summary='''"Mystic Realms: Legends of Enchantoria" is an enchanting board game that transports players into a mystical world brimming with wonder, magic, and discovery. It is a captivating journey through the rich lore of Enchantoria, an ancient realm filled with captivating legends and hidden secrets. In this immersive game, players will encounter a diverse array of magical creatures that call Enchantoria home. From whimsical fairies to majestic dragons and enigmatic spirits, every encounter promises surprises and challenges, adding depth and unpredictability to your journey. Strategic thinking and decision-making are at the core of Mystic Realms' gameplay. Challenge your wits as you navigate the game's strategic elements, resource management, and critical decision points. Every move you make shapes the outcome, ensuring hours of engaging play. Embark on quests and missions that test your bravery and resourcefulness. Completing these quests not only advances the storyline but also unlocks hidden treasures and unravels the mysteries of Enchantoria. Customization is key in this mystical world. Tailor your adventure to your preferences by customizing your character, choosing your path, and making critical decisions that impact the course of your journey. Whether you're a fearless explorer or a cunning diplomat, your choices matter. Share the enchantment with friends and family through multiplayer modes. Form alliances, compete in challenges, or collaborate to overcome formidable obstacles, making the game a social experience filled with memorable moments. Mystic Realms features stunning artwork that brings the magical world of Enchantoria to life. Immerse yourself in breathtaking visuals that captivate players of all ages. As you progress, you'll face strategic challenges, from solving intricate puzzles to engaging in epic battles. Every moment is a test of your strategic prowess and decision-making skills. Explore an expansive and beautifully crafted world, from mystical forests to ancient ruins and bustling magical cities. Enchantoria offers a wide variety of landscapes and settings to discover and explore. This narrative-driven experience combines storytelling excellence with interactive gameplay. The game's narrative weaves a rich tapestry of stories, characters, and mysteries waiting to be uncovered. Mystic Realms: Legends of Enchantoria is more than just a board game; it's an enchanting adventure that promises endless hours of entertainment, exploration, and discovery. Whether you're a seasoned board gamer or a newcomer to the genre, this game offers a magical and unforgettable journey into the heart of Enchantoria, where legends come to life, and the mysteries of the realm await your exploration. Are you ready to embark on this extraordinary quest and become a legend in your own right?''',
        location='Enchantoria Games, San Francisco, USA',
        ownerId=1,  # Replace with the actual user ID
        categoryId=1,  # Replace with the actual category ID for board games
        bannerImg='https://pledgepaloozabucket.s3.us-east-2.amazonaws.com/MysticRealm1.png',
        endDate=date(2023, 12, 31),
    )

    project2 = Project(
        name='Virtual Oasis: The VR Adventure',
        description='Immerse yourself in a virtual oasis in this cutting-edge VR RPG. Explore lush landscapes, conquer mythical beasts, and unlock the secrets of the Oasis!',
        location='Oasis Studios, Los Angeles, USA',
        summary='''
        Virtual Oasis: The VR Adventure" invites you to step into a mesmerizing world of virtual reality, where an extraordinary RPG experience awaits. Immerse yourself in the lush landscapes and mystical realms of the Oasis, a digital paradise like no other. This cutting-edge VR game offers players the opportunity to embark on an epic journey, where they can conquer mythical beasts, unlock the secrets of the Oasis, and create their own unforgettable adventures. At the heart of this immersive experience is the groundbreaking technology that powers it. Virtual Oasis leverages the latest advancements in virtual reality to transport players to a visually stunning and highly interactive world. From the moment you don your VR headset, you'll find yourself standing at the threshold of a realm filled with wonder and awe. The gameplay of Virtual Oasis is a blend of exploration, strategy, and adventure. Traverse diverse landscapes, each more enchanting than the last, as you embark on quests, solve puzzles, and engage in epic battles against formidable foes. Whether you're a seasoned VR gamer or new to the medium, Virtual Oasis offers a user-friendly and accessible experience, ensuring that players of all levels can enjoy its immersive wonders. Located at Oasis Studios in the vibrant city of Los Angeles, USA, this project is a testament to the boundless possibilities of virtual reality in the world of gaming. As you navigate the Oasis, you'll uncover hidden treasures, forge alliances, and confront the unknown, all while pushing the boundaries of what's possible in VR gaming. Owned and developed by a passionate team, Virtual Oasis is set to redefine the future of virtual reality RPGs. Its captivating narrative, stunning visuals, and engaging gameplay promise to transport players to a realm where adventure knows no bounds. Join us on this journey to discover the limitless potential of virtual reality and experience the magic of the Oasis. Your adventure awaits, and the secrets of this virtual paradise are yours to unlock. Embark on a quest like no other with "Virtual Oasis: The VR Adventure.
        ''',
        ownerId=2,  # Replace with the actual user ID
        categoryId=2,  # Replace with the actual category ID for video games
        bannerImg='https://pledgepaloozabucket.s3.us-east-2.amazonaws.com/VRheadset.png',
        endDate=date(2024, 6, 30),
    )

    project3 = Project(
        name='Cosmic Odyssey: The Intergalactic Board Game',
        description='Embark on an epic cosmic adventure in this sci-fi board game. Command starfleets, navigate wormholes, and explore the uncharted territories of the galaxy!',
        location='Galaxy Games, Seattle, USA',
        summary='''
        Cosmic Odyssey: The Intergalactic Board Game" propels players into a thrilling sci-fi adventure where they become commanders of starfleets, navigate mysterious wormholes, and boldly explore the uncharted territories of the vast galaxy. This epic board game offers an unparalleled journey through the cosmos, where strategic thinking, resource management, and cosmic exploration collide to create an unforgettable gaming experience. At its core, Cosmic Odyssey is a testament to the limitless wonders of the universe. From the moment you step into this immersive board game, you're catapulted into a world teeming with celestial marvels, enigmatic wormholes, and untold mysteries. The game's visually captivating design and intricate gameplay mechanics ensure that every turn is filled with excitement and strategy. Your role as a starfleet commander requires you to make critical decisions, form alliances, and conquer the challenges that await in the far reaches of space. With each move, you chart a course through the galaxy, encountering cosmic phenomena, alien civilizations, and the ever-present element of the unknown. Whether you're a seasoned board game enthusiast or a newcomer to the genre, Cosmic Odyssey offers an accessible yet deeply engaging experience, promising hours of cosmic exploration and strategic conquest. Set amidst the innovation hub of Galaxy Games in Seattle, USA, this project is a testament to the boundless creativity and passion of game developers. The team behind Cosmic Odyssey has meticulously crafted a game that celebrates the grandeur of the cosmos while delivering an immersive and captivating gaming experience. As you embark on your cosmic journey, you'll forge alliances, engage in epic battles, and uncover the secrets of the galaxy. Cosmic Odyssey beckons you to explore the uncharted territories of space, where every decision shapes your destiny and every discovery adds a new layer of intrigue to your interstellar adventure. Join us on this odyssey through the cosmos and become a part of the Cosmic Odyssey legacy. The stars are your playground, and the universe is your canvas. Command your starfleet, navigate the cosmic expanse, and embark on a journey of epic proportions with "Cosmic Odyssey: The Intergalactic Board Game.
        ''',
        ownerId=3,  # Replace with the actual user ID
        categoryId=1,  # Replace with the actual category ID for board games
        bannerImg='https://pledgepaloozabucket.s3.us-east-2.amazonaws.com/Cosmic1.png',
        endDate=date(2023, 8, 15),
    )

    project4 = Project(
        name='Arcane Alchemy: The Magical Card Game',
        description='Master the art of arcane alchemy in this enchanting card game. Brew magical concoctions, summon mystical creatures, and compete in the world of spellcraft!',
        location='Mystic Games, Edinburgh, UK',
        summary='''
        Arcane Alchemy: The Magical Card Game" invites players to embark on a captivating journey into the world of mystical sorcery, where the art of arcane alchemy takes center stage. This enchanting card game weaves a spellbinding tapestry of magic, where players can brew magical concoctions, summon awe-inspiring mystical creatures, and immerse themselves in the captivating realm of spellcraft. The game unfolds in the enchanting setting of Mystic Games, nestled in the heart of Edinburgh, UK, a city steeped in history and legend. At the core of Arcane Alchemy lies a rich and intricate tapestry of magical lore, beautifully brought to life through the game's meticulously crafted cards and gameplay mechanics. As a player, you'll step into the shoes of a budding alchemist, harnessing the arcane forces to concoct powerful elixirs, summon legendary creatures, and engage in spellbinding duels. Each card in the game is a spell waiting to be cast, a potion ready to be brewed, or a creature eager to do your bidding. Whether you're a seasoned card game enthusiast or new to the world of magic, Arcane Alchemy offers a spellbinding and immersive experience for players of all levels. The game's location, Mystic Games in Edinburgh, UK, is a testament to the game's deep connection to the mystical and the magical. As you delve into the world of Arcane Alchemy, you'll explore the secrets of ancient grimoires, unlock hidden incantations, and embrace the power of the arcane. The game's captivating narrative and visually stunning artwork transport players to a realm where every card played is a step closer to mastering the arcane arts. Arcane Alchemy beckons players to immerse themselves in a world where magic knows no bounds. In the world of spellcraft and enchantment, you'll uncover ancient tomes, engage in epic duels, and brew concoctions of unparalleled potency. Join us on this mystical journey, where the cards you play and the spells you cast will determine your destiny in the world of "Arcane Alchemy: The Magical Card Game.
        ''',
        ownerId=4,  # Replace with the actual user ID
        categoryId=1,  # Replace with the actual category ID for board games
        bannerImg='https://pledgepaloozabucket.s3.us-east-2.amazonaws.com/Arcane1.png',
        endDate=date(2023, 10, 31),
    )

    project5 = Project(
        name='Cybernetica: The Futuristic VR Adventure',
        description='Dive into the futuristic world of Cybernetica in this mind-bending VR adventure. Hack cyberspace, battle cybernetic foes, and rewrite the future!',
        location='Cyber Nexus, Tokyo, Japan',
        summary='''
        Cybernetica: The Futuristic VR Adventure" thrusts players into the cutting-edge world of Cybernetica, an exhilarating VR adventure that transcends the boundaries of reality and technology. Dive headfirst into a future where the digital realm melds seamlessly with the physical, where the power to hack cyberspace, battle formidable cybernetic foes, and ultimately rewrite the future lies at your fingertips. This immersive VR experience offers a mind-bending journey through the bustling streets of Tokyo, Japan, a city known for its technological marvels and futuristic landscapes. At its core, Cybernetica is a testament to the boundless possibilities of virtual reality in the realm of gaming. As you don your VR headset, you'll find yourself transported to a world where the lines between reality and the digital domain blur. The game's stunning visuals and intricately designed environments immerse players in a future teeming with neon-lit skyscrapers, bustling metropolises, and virtual landscapes that defy imagination. The gameplay of Cybernetica is a blend of strategic hacking, intense combat, and futuristic exploration. Players take on the role of a cybernetic hacker, wielding cutting-edge technology and digital weaponry to navigate the complexities of cyberspace and confront formidable adversaries. Whether you're a seasoned VR gamer or new to the immersive medium, Cybernetica promises an accessible yet profoundly engaging experience, ensuring that players of all levels can revel in its futuristic wonders. Located at the heart of technological innovation, Cyber Nexus in Tokyo, Japan, is the ideal backdrop for a project that pushes the boundaries of VR gaming. As you delve deeper into Cybernetica, you'll uncover hidden secrets, engage in adrenaline-pumping battles, and ultimately shape the future of the digital world. The game represents a collaboration of talented developers and visionaries, striving to redefine the future of VR gaming. Join us on this futuristic odyssey as we explore the uncharted territories of cyberspace and embark on a journey to rewrite the future. Hack, battle, and transcend the boundaries of reality in "Cybernetica: The Futuristic VR Adventure," where the line between man and machine blurs, and the digital realm awaits your exploration.
        ''',
        ownerId=5,  # Replace with the actual user ID
        categoryId=2,  # Replace with the actual category ID for video games
        bannerImg='https://pledgepaloozabucket.s3.us-east-2.amazonaws.com/Cybernetica1.png',
        endDate=date(2024, 5, 15),
    )

    project6 = Project(
        name='Dragons Dominion: The Legendary Board Game',
        description='Enter Dragons Dominion, a legendary realm in this epic board game. Tame dragons, explore ancient ruins, and become a legend in a land of fantasy!',
        location='Dragonfire Studios, Dublin, Ireland',
        summary='''
        Dragons Dominion: The Legendary Board Game" invites players to embark on a mythical journey into the fabled realm of Dragons Dominion, a land steeped in legend and fantasy. This epic board game transports players to a world where they can tame majestic dragons, explore ancient ruins, and craft their own legend in a land where every turn of the board unveils new adventures and challenges. The game unfolds in the enchanting setting of Dragonfire Studios, nestled in the heart of Dublin, Ireland, a place rich in history and folklore. At its core, Dragons Dominion weaves an intricate tapestry of fantasy, where players assume the roles of daring adventurers seeking fame and fortune in a land where dragons soar and legends are born. The game's visually captivating design and immersive gameplay mechanics ensure that every moment spent in Dragons Dominion is filled with excitement, strategy, and wonder. As a player, you'll embark on quests, uncover ancient mysteries, and forge alliances as you traverse the mystical landscapes of Dragons Dominion. Whether you're a seasoned board game enthusiast or new to the world of fantasy, Dragons Dominion offers a welcoming and engaging experience suitable for players of all levels. Located in Dublin, Ireland, Dragonfire Studios serves as the perfect backdrop for a project that celebrates the timeless allure of fantasy and legend. As you delve into the game, you'll encounter magical creatures, face daunting challenges, and script your own tale of heroism and adventure. Dragons Dominion is a collaborative effort between passionate developers and storytellers, all dedicated to creating a gaming experience that transports players to a realm where legends come to life. Join us on this epic journey into Dragons Dominion, where dragons rule the skies, ancient ruins hold secrets untold, and the pursuit of legend awaits. Tame dragons, embark on quests, and become a legend in a land where fantasy knows no bounds with "Dragons Dominion: The Legendary Board Game.
        ''',
        ownerId=6,  # Replace with the actual user ID
        categoryId=1,  # Replace with the actual category ID for board games
        bannerImg='https://pledgepaloozabucket.s3.us-east-2.amazonaws.com/DragonsDomain.png',
        endDate=date(2023, 9, 30),
    )
    project7 = Project(
        name='AquaVenture: The Underwater VR Odyssey',
        description='Embark on an underwater odyssey in AquaVenture, the immersive VR experience. Dive into vibrant coral reefs, encounter marine marvels, and uncover lost treasures!',
        location='DeepSea Studios, Sydney, Australia',
        summary='''
        AquaVenture: The Underwater VR Odyssey" offers an enchanting invitation to embark on an immersive underwater odyssey like no other. Dive into the mesmerizing depths of vibrant coral reefs, encounter the wonders of the marine world, and unearth long-lost treasures hidden beneath the waves. This breathtaking VR experience takes players on a journey through the azure waters of the ocean, where the allure of the deep beckons. The game is brought to life by the creative minds at DeepSea Studios, located in the coastal city of Sydney, Australia, a place known for its stunning aquatic beauty and marine diversity. At its essence, AquaVenture plunges players into a realm of aquatic wonder, where every dive reveals a world teeming with life and mystery. The game's visually stunning graphics and immersive gameplay mechanics ensure that every moment spent exploring the underwater landscape is filled with awe and discovery. As a player, you'll find yourself amidst the colorful coral reefs, swimming alongside majestic marine creatures, and unraveling the secrets of the deep blue. Whether you're a seasoned VR enthusiast or new to the world of virtual reality, AquaVenture provides a user-friendly and engaging experience suitable for players of all levels. DeepSea Studios, situated in Sydney, Australia, serves as the perfect backdrop for a project that celebrates the breathtaking beauty of the ocean and the wonders it holds. As you embark on your underwater odyssey, you'll encounter unique marine species, navigate through stunning aquatic landscapes, and uncover hidden treasures that have long been lost to the depths. AquaVenture is a collaborative effort of passionate developers and ocean enthusiasts, all committed to creating a virtual experience that brings the enchantment of the ocean to life. Join us on this unforgettable underwater voyage, where vibrant coral reefs, marine marvels, and lost treasures await. Dive into the world of AquaVenture and immerse yourself in a realm where the mysteries of the deep are yours to discover with "AquaVenture: The Underwater VR Odyssey.
        ''',
        ownerId=7,  # Replace with the actual user ID
        categoryId=2,  # Replace with the actual category ID for video games
        bannerImg='https://pledgepaloozabucket.s3.us-east-2.amazonaws.com/aquaventure.png',
        endDate=date(2024, 4, 20),
    )

    project8 = Project(
        name='QuantumX: The Quantum Computing Breakthrough',
        description='Unlock the power of quantum computing with QuantumX. Solve complex problems faster, revolutionize cryptography, and explore the limitless potential of quantum technology!',
        location='Quantum Labs, Silicon Valley, USA',
        ownerId=8,  # Replace with the actual user ID
        categoryId=3,  # Replace with the actual category ID for tech products
        bannerImg='https://pledgepaloozabucket.s3.us-east-2.amazonaws.com/quantumx1.png',
        endDate=date(2024, 2, 28),
    )

    project9 = Project(
        name='LunaLens: The Augmented Reality Glasses',
        description='Step into augmented reality with LunaLens. Overlay digital information on your world, play immersive AR games, and redefine how you see the future!',
        location='LunaTech, New York City, USA',
        summary='''
        LunaLens: The Augmented Reality Glasses" invites you to step boldly into the exciting world of augmented reality (AR), where the boundaries between the digital and physical realms blur in a symphony of innovation. These visionary AR glasses promise to revolutionize the way you perceive and interact with the world around you. With LunaLens, you'll experience the thrill of overlaying digital information on your everyday surroundings, immerse yourself in captivating AR games, and redefine your perspective on the future. The project emanates from the vibrant tech hub of LunaTech in the heart of New York City, USA, a city known for its bustling tech scene and forward-thinking innovation. At its core, LunaLens represents a leap into the future, where the fusion of technology and reality unlocks unprecedented possibilities. The AR glasses are designed to seamlessly integrate digital elements into your daily life, offering a multifaceted experience that combines entertainment, utility, and innovation. LunaLens opens up a world of endless opportunities, from providing informative overlays in real-time to delivering immersive gaming experiences that blur the line between the virtual and the tangible. As a wearer of LunaLens, you'll find yourself on the forefront of AR innovation, navigating through a landscape where information comes to life, and entertainment takes on a new dimension. Whether you're an AR enthusiast or new to the world of augmented reality, LunaLens promises an accessible and captivating experience suitable for users of all backgrounds. Located in the bustling metropolis of New York City, LunaTech is the ideal birthplace for a project that pushes the boundaries of AR technology. LunaLens embodies the city's spirit of constant evolution and progress, offering a glimpse into the future where augmented reality is an integral part of our daily lives. LunaTech's team of dedicated innovators and creators are committed to transforming the way we see the world and experience reality. Join us on this extraordinary journey into augmented reality, where LunaLens AR glasses empower you to overlay your world with digital magic, explore immersive AR games, and shape the future of human interaction with "LunaLens: The Augmented Reality Glasses." Discover a new dimension of reality and embrace the limitless potential of AR technology.
        ''',
        ownerId=9,  # Replace with the actual user ID
        categoryId=2,  # Replace with the actual category ID for tech products
        bannerImg='https://pledgepaloozabucket.s3.us-east-2.amazonaws.com/lunalens1.png',
        endDate=date(2024, 3, 15),
    )

    project10 = Project(
        name='SkyHawk: The AI-Powered Drone',
        description='Experience the future of flight with SkyHawk, the AI-powered drone. Capture breathtaking aerial footage, enjoy autonomous flights, and redefine your perspective!',
        location='SkyTech Innovations, Los Angeles, USA',
        ownerId=10,  # Replace with the actual user ID
        categoryId=3,  # Replace with the actual category ID for tech products
        bannerImg='https://pledgepaloozabucket.s3.us-east-2.amazonaws.com/skyhawk.png',
        endDate=date(2024, 4, 10),
    )
    project11 = Project(
        name='EcoCharge: The Solar-Powered Charger',
        description='Stay charged sustainably with EcoCharge, the solar-powered charger. Harness the suns energy, charge your devices anywhere, and reduce your carbon footprint!',
        summary='''EcoCharge: The Solar-Powered Charger" is a groundbreaking and environmentally conscious solution that redefines the way we keep our devices charged. This innovative charger harnesses the boundless energy of the sun, offering a sustainable and renewable power source for all your devices. With EcoCharge, you can bid farewell to conventional charging methods and embrace a greener and cleaner future. Whether you're embarking on a wilderness adventure, relaxing in your backyard, or traveling to remote destinations, EcoCharge ensures that you stay connected, all while reducing your carbon footprint. At the heart of EcoCharge's design is its advanced solar-powered technology, ingeniously converting sunlight into electricity. This process is not only eco-friendly but also remarkably efficient, guaranteeing that your devices remain charged without relying on traditional power grids or fossil fuels. The charger's universal compatibility makes it a versatile companion, capable of charging a wide range of devices, including smartphones, tablets, cameras, and more, all simultaneously. EcoCharge's portable and compact design is tailored for adventurers and travelers alike, featuring durability that withstands the rigors of outdoor use. It's the ideal companion for camping trips, hiking expeditions, or any outdoor escapade where access to conventional power sources is limited. Developed by EcoTech Solutions, a renowned leader in eco-friendly technology, EcoCharge embodies the company's unwavering commitment to sustainability and innovation. By choosing EcoCharge, you not only benefit from the convenience of on-the-go charging but also actively contribute to a healthier planet by reducing your reliance on fossil fuels and lowering your carbon emissions. Join us in our mission to promote sustainable charging solutions and embrace a future that prioritizes environmental sustainability. Make a positive impact on the environment and stay connected wherever you go with EcoCharge: The Solar-Powered Charger.''',
        location='EcoTech Solutions, Amsterdam, Netherlands',
        ownerId=6,  # Replace with the actual user ID
        categoryId=3,  # Replace with the actual category ID for tech products
        bannerImg='https://pledgepaloozabucket.s3.us-east-2.amazonaws.com/ecocharge1.png',
        endDate=date(2024, 5, 5),
    )
    project12 = Project(
        name='EcoStyle: Sustainable Fashion Line',
        description='Introducing EcoStyle, a sustainable fashion line made from eco-friendly materials. Embrace conscious fashion, reduce your environmental footprint, and look stylish!',
        location='EcoChic Studios, Paris, France',
        summary='''
        EcoStyle: Sustainable Fashion Line" introduces a groundbreaking approach to fashion that seamlessly blends style with sustainability. This innovative fashion line is crafted from eco-friendly materials, inviting you to embrace conscious fashion and make a positive impact on the environment. With EcoStyle, you can effortlessly reduce your environmental footprint while looking effortlessly stylish. The project takes root in the artistic hub of EcoChic Studios, nestled in the enchanting city of Paris, France, a place synonymous with elegance, artistry, and a deep appreciation for both fashion and sustainability. At its essence, EcoStyle represents a transformative shift in the world of fashion, where ethical practices and eco-conscious choices take center stage. The fashion line showcases a curated collection of garments and accessories that are not only chic but also environmentally responsible. Each piece in the collection is a testament to the possibilities of sustainable fashion, combining intricate design with a commitment to reducing the fashion industry's impact on the planet. As an advocate for conscious fashion, EcoStyle empowers you to make choices that align with your values. By choosing EcoStyle, you contribute to a fashion revolution that prioritizes ethical production, eco-friendly materials, and timeless designs. Whether you're a fashion aficionado or a newcomer to sustainable clothing, EcoStyle offers a wardrobe that transcends trends and resonates with those who believe in the power of sustainable choices. EcoChic Studios, located in the fashion capital of Paris, France, serves as the perfect canvas for a project that reimagines fashion as a force for good. EcoStyle embodies the spirit of eco-conscious innovation and artistic expression, offering a glimpse into a future where fashion and sustainability harmoniously coexist. The team at EcoChic Studios is dedicated to reshaping the fashion landscape, one sustainable garment at a time. Join us on this remarkable journey into the world of EcoStyle, where sustainable fashion meets unparalleled style. Embrace a wardrobe that reflects your values, reduces your environmental footprint, and redefines fashion as a conscious choice with "EcoStyle: Sustainable Fashion Line." Elevate your style and join the movement towards a more sustainable and stylish future.
        ''',
        ownerId=5,  # Replace with the actual user ID
        categoryId=4,  # Replace with the actual category ID for fashion
        bannerImg='https://pledgepaloozabucket.s3.us-east-2.amazonaws.com/ecostyle1.png',
        endDate=date(2024, 6, 30),
    )

    project13 = Project(
        name='UrbanThreads: Streetwear Reimagined',
        description='Explore the urban culture with UrbanThreads. Elevate your street style with unique designs, quality materials, and the essence of the city streets!',
        location='UrbanX Apparel, New York City, USA',
        summary='''
        UrbanThreads: Streetwear Reimagined" invites you to dive headfirst into the vibrant tapestry of urban culture, where style meets the essence of the city streets. This dynamic streetwear collection redefines the boundaries of fashion, offering a fresh and unique take on street style that resonates with urban enthusiasts and fashion-forward individuals alike. With UrbanThreads, you have the opportunity to elevate your street style with a curated selection of designs, quality materials, and a distinctive urban flair. The project emerges from the heart of UrbanX Apparel, a creative hub situated in the bustling metropolis of New York City, USA, a city renowned for its eclectic street culture and fashion-forward spirit. At its core, UrbanThreads embodies the spirit of urban life, where fashion becomes a canvas for self-expression and creativity. The streetwear collection showcases a range of apparel and accessories that capture the pulse of the city, infusing each piece with the energy, diversity, and individuality that define urban environments. Whether you're exploring the city's bustling streets, embracing its subcultures, or simply seeking a unique style statement, UrbanThreads offers a wardrobe that empowers you to embrace the urban landscape with confidence and authenticity. As a champion of urban culture, UrbanThreads merges fashion with the ethos of the streets, celebrating the diversity and dynamism that thrive in urban settings. By choosing UrbanThreads, you become a part of a movement that celebrates individuality, creativity, and the unique spirit of urban life. Whether you're a seasoned urban explorer or a fashion enthusiast looking to make a statement, UrbanThreads offers a collection that resonates with those who embrace the urban experience. UrbanX Apparel, located in the iconic cityscape of New York City, is the ideal birthplace for a project that embodies the essence of urban culture. UrbanThreads captures the city's energy and artistic spirit, offering a fashion line that reimagines streetwear as a dynamic form of self-expression. The team at UrbanX Apparel is committed to creating a fashion movement that empowers individuals to embrace their urban identity and express themselves through style. Join us on this exciting journey into the world of UrbanThreads, where streetwear is reimagined, and the city becomes your fashion playground. Elevate your street style, celebrate urban culture, and make a bold statement with "UrbanThreads: Streetwear Reimagined." Embrace the city streets as your runway and express your unique urban identity through fashion.
        ''',
        ownerId=4,  # Replace with the actual user ID
        categoryId=4,  # Replace with the actual category ID for fashion
        bannerImg='https://pledgepaloozabucket.s3.us-east-2.amazonaws.com/urbanthreads.png',
        endDate=date(2024, 7, 15),
    )
    project14 = Project(
        name='Epic Tales: Fantasy Novel Series',
        description='Embark on a journey through epic fantasy worlds with the "Epic Tales" series. Join mythical heroes, face ancient evils, and get lost in the magic of storytelling!',
        location='MysticWords Publishing, London, UK',
        summary='''
        Embark on an enchanting journey through the realms of epic fantasy with the "Epic Tales" series, where storytelling reaches its zenith and immerses you in a world of mythical heroes, ancient evils, and boundless imagination. This exceptional novel series, poised at the intersection of adventure and mysticism, invites you to traverse the pages of epic tales that capture the essence of timeless storytelling. With "Epic Tales," you will find yourself transported to mystical worlds where the lines between reality and fiction blur, and where the magic of storytelling unfolds in all its grandeur. The project takes root in the heart of MysticWords Publishing, an esteemed literary hub nestled in the historic city of London, UK, known for its rich literary heritage and enduring love for the written word. At its core, "Epic Tales" stands as a testament to the enduring power of storytelling, where each book in the series offers a portal to uncharted territories of the imagination. The series boasts a captivating collection of novels, each filled with a rich tapestry of characters, mythical landscapes, and intricate plots that beckon readers to embark on epic adventures. Whether you're drawn to the valor of heroes, the allure of ancient mysteries, or the enchantment of magical realms, "Epic Tales" offers a literary journey that transcends time and genre, embracing the essence of epic storytelling. As a devotee of literary exploration, "Epic Tales" empowers you to traverse the realms of fantasy and lose yourself in narratives that ignite the imagination. By immersing yourself in the "Epic Tales" series, you become a part of a community of readers who share a deep appreciation for the art of storytelling and the wonder of epic adventures. Whether you're a seasoned reader of fantasy novels or embarking on your first literary quest, "Epic Tales" promises an enthralling journey that captivates the heart and mind. MysticWords Publishing, located in the literary heart of London, is the perfect backdrop for a project that celebrates the magic of storytelling. "Epic Tales" encapsulates the city's love for literature and its dedication to nurturing creativity and imagination. The team at MysticWords Publishing is dedicated to bringing epic stories to life and ensuring that the legacy of storytelling continues to inspire generations. Join us on this extraordinary voyage through the pages of "Epic Tales: Fantasy Novel Series," where storytelling transcends the ordinary, mythical heroes come to life, and the enchantment of the written word knows no bounds. Embark on an epic journey, embrace the magic of storytelling, and become a part of a timeless literary adventure with "Epic Tales."
        ''',
        ownerId=3,  # Replace with the actual user ID
        categoryId=1,  # Replace with the actual category ID for books
        bannerImg='https://pledgepaloozabucket.s3.us-east-2.amazonaws.com/epictales.png',
        endDate=date(2024, 10, 20),
    )

    project15 = Project(
        name='Cookbook Chronicles: Culinary Adventure',
        description='Indulge your taste buds with "Cookbook Chronicles." Explore diverse cuisines, savor delicious recipes, and embark on a culinary adventure!',
        location='Culinary Creations, New Orleans, USA',
        summary='''
        Embark on a delectable journey for your senses with "Cookbook Chronicles," where culinary adventure takes center stage, and the world's diverse cuisines await your exploration. This exceptional project invites you to indulge your taste buds, traverse the globe through its flavors, and savor the art of cooking like never before. "Cookbook Chronicles" is more than just a collection of recipes; it's a culinary odyssey that encapsulates the essence of culinary creativity and culinary culture. Nestled in the heart of Culinary Creations, a culinary haven situated in the vibrant city of New Orleans, USA, known for its rich culinary heritage and love for gastronomic innovation. At its core, "Cookbook Chronicles" celebrates the joy of cooking and the global tapestry of flavors that enrich our palates. The project boasts a curated collection of cookbooks, each a gateway to a world of culinary delights. Whether you're a seasoned home chef or a culinary enthusiast, you'll find inspiration in the diverse cuisines, tantalizing recipes, and culinary secrets waiting to be uncovered within these pages. "Cookbook Chronicles" encourages you to embark on a culinary adventure, experiment with flavors, and share the joy of food with loved ones. As an advocate for the culinary arts, "Cookbook Chronicles" empowers you to embrace the art of cooking as a form of self-expression and cultural exploration. By immersing yourself in these cookbooks, you become part of a community that values culinary creativity, appreciates the joy of sharing meals, and revels in the rich tapestry of global cuisine. Whether you're seeking to master a specific cuisine or simply explore new tastes, "Cookbook Chronicles" promises a journey of culinary discovery that resonates with food lovers of all backgrounds. Culinary Creations, nestled in the vibrant culinary landscape of New Orleans, serves as the perfect backdrop for a project that celebrates the magic of cooking. "Cookbook Chronicles" embodies the city's passion for food, innovation, and culinary excellence, offering a culinary adventure that transcends borders and brings people together through the universal language of food. Join us on this mouthwatering journey with "Cookbook Chronicles: Culinary Adventure," where flavors come alive, cultures unite, and the joy of cooking becomes a celebration of global gastronomy. Explore the world of cuisine, savor delicious recipes, and embrace the culinary arts with "Cookbook Chronicles."
        ''',
        ownerId=2,  # Replace with the actual user ID
        categoryId=5,  # Replace with the actual category ID for books
        bannerImg='https://pledgepaloozabucket.s3.us-east-2.amazonaws.com/cookbook1.png',
        endDate=date(2024, 11, 10),
    )

    project16 = Project(
        name='Whodunit Mysteries: Detective Series',
        description='Unravel thrilling mysteries with the "Whodunit Mysteries" series. Put on your detective hat, follow clues, and solve crimes that keep you on the edge of your seat!',
        location='Ink & Intrigue Publishing, New York City, USA',
        summary='''
        Prepare to embark on a thrilling journey into the world of mystery and intrigue with the "Whodunit Mysteries" series, where the art of deduction and the allure of suspense converge to immerse you in gripping tales of crime and investigation. This exceptional project invites you to don your detective hat, sharpen your wits, and follow the trail of clues that lead to solutions in perplexing cases that keep you on the edge of your seat. The "Whodunit Mysteries" series is not just a collection of books; it's an invitation to become a detective, to step into the shoes of brilliant investigators, and to unravel mysteries that challenge the mind. This captivating series is housed within the esteemed Ink & Intrigue Publishing, located in the bustling heart of New York City, USA, a hub of literary innovation and the perfect setting for tales of mystery and suspense. At its core, "Whodunit Mysteries" celebrates the art of storytelling through a lens of suspense, intrigue, and intellectual challenge. Each book in the series beckons readers to immerse themselves in intricately woven narratives, filled with enigmatic characters, cryptic clues, and a constant sense of anticipation. Whether you're an aficionado of classic detective fiction or a newcomer to the world of mysteries, the "Whodunit Mysteries" series promises an immersive experience that will keep you guessing until the very last page. As a champion of the detective genre, "Whodunit Mysteries" empowers you to become an active participant in solving crimes, exploring motives, and deciphering puzzles. By delving into these captivating narratives, you join a community of readers who share a passion for intellectual engagement and the thrill of the unknown. The series offers readers a chance to hone their deductive skills, appreciate the art of storytelling, and revel in the exhilaration of solving crimes alongside the most brilliant fictional detectives. Ink & Intrigue Publishing, nestled in the literary heart of New York City, provides the ideal backdrop for a project that thrives on suspense and intrigue. "Whodunit Mysteries" embodies the city's legacy of producing exceptional detective fiction, where each book in the series pays homage to the rich tradition of mystery writing and offers a fresh perspective on the genre. Join us on an enthralling journey with the "Whodunit Mysteries: Detective Series," where the line between reader and detective blurs, where suspense comes to life, and where the thrill of solving crimes awaits. Unravel the mysteries, follow the clues, and embrace the world of detective fiction with "Whodunit Mysteries."
        ''',
        ownerId=1,  # Replace with the actual user ID
        categoryId=1,  # Replace with the actual category ID for books
        bannerImg='https://pledgepaloozabucket.s3.us-east-2.amazonaws.com/mystery1.png',
        endDate=date(2024, 12, 5),
    )


    db.session.add(project1)
    db.session.add(project2)
    db.session.add(project3)
    db.session.add(project4)
    db.session.add(project5)
    db.session.add(project6)
    db.session.add(project7)
    db.session.add(project8)
    db.session.add(project9)
    db.session.add(project10)
    db.session.add(project11)
    db.session.add(project12)
    db.session.add(project13)
    db.session.add(project14)
    db.session.add(project15)
    db.session.add(project16)


    db.session.commit()


def undo_projects():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.projects RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM projects"))

    db.session.commit()
