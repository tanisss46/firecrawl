# Setting merchant category codes

## Learn about merchant category codes (MCCs) and how to set them for your connected accounts.

[MCCs](https://en.wikipedia.org/wiki/Merchant_category_code) are used to
classify businesses by the type of goods or services they provide. For example,
grocery stores, hotels, and airlines all have different MCCs. These codes are
often used for calculating interchange fees, authorizing payments, and
preventing fraud, so it’s important that your connected accounts have MCCs that
match their businesses.

Each Stripe account has exactly one MCC. To view the MCC for a specific account,
you can [retrieve](https://docs.stripe.com/api/accounts/retrieve) the
`business_profile.mcc` field on the account object.

Stripe automatically sets MCC codes for connected accounts, but you can choose
to set them manually for accounts that your platform controls. That includes
Custom and Express accounts.

## Setting MCCs automatically

Stripe automatically evaluates accounts to determine appropriate MCCs. That
means you don’t need to build and maintain any custom logic. Generally, the
industry listed in the Stripe Dashboard for the connected account is used to
determine the MCC. For accounts where Stripe collects updated information for
due or changed requirements, including Standard and Express accounts, and for
Custom accounts using [Stripe-hosted
onboarding](https://docs.stripe.com/connect/custom/hosted-onboarding), the MCC
is set during onboarding. For accounts created with the API and for Express
accounts, you can [set the MCC
manually](https://docs.stripe.com/connect/setting-mcc#mcc-manual).

If the industry that the user provides can’t be used, Stripe might use
information from the connected account’s website to determine the MCC. If this
also fails, the platform or Stripe’s default MCC (`5734` Computer Software
Stores) is used.

Sometimes accounts are flagged for manual review by Stripe. If this happens and
Stripe determines the MCC on an account is inaccurate, we might update it. The
new MCC can’t be manually changed by the platform, and an error is returned if
the API is used to update the MCC.

## Setting MCCs manually

You can set the MCC manually when you [create
accounts](https://docs.stripe.com/api/accounts/create#create_account-business_profile-mcc).
The examples below use the code for Computer Software Stores (`5734`), but you
can see a [full list](https://docs.stripe.com/connect/setting-mcc#list) in the
next section.

Typed AccountsController properties
```
curl https://api.stripe.com/v1/accounts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "controller[fees][payer]"=application \
 -d "controller[losses][payments]"=application \
 -d "controller[stripe_dashboard][type]"=none \
 -d "controller[requirement_collection]"=application \
 -d country=US \
 -d "capabilities[card_payments][requested]"=true \
 -d "capabilities[transfers][requested]"=true \
 -d "business_profile[mcc]"=5734
```

If your connected accounts share an MCC, you can provide the code using
`business_profile.mcc` when you create accounts. In
[Connect](https://docs.stripe.com/connect) Onboarding, your users won’t be asked
for an industry. If you build your own onboarding UI, you don’t need to add a UI
element for MCC.

If your connected accounts have different MCCs, Connect Onboarding will collect
that information. If you aren’t using Connect Onboarding, you can provide a list
of MCC options for users to choose from. Based on the user’s selection, you can
pass an MCC appropriate for their business. If you don’t want to pass MCCs when
you create accounts, you can [update
accounts](https://docs.stripe.com/api/accounts/update#update_account-business_profile-mcc)
with MCCs later.

Similar to an MCC that’s set automatically, Stripe can override an MCC set
manually if the connected account is flagged for review and we determine the MCC
is inaccurate.

## Merchant category code list

The following is a list of supported MCCs that you can use when creating
connected accounts. You must contact Stripe to use a restricted MCC.

CategoryMCCA/C, Refrigeration
Repair`ac_refrigeration_repair`7623Accounting/Bookkeeping
Services`accounting_bookkeeping_services`8931Advertising
Services`advertising_services`7311Agricultural
Cooperative`agricultural_cooperative`0763Airlines, Air Carriers
Restricted`airlines_air_carriers`4511Airports, Flying
Fields`airports_flying_fields`4582Ambulance Services
Restricted`ambulance_services`4119Amusement Parks/Carnivals
Restricted`amusement_parks_carnivals`7996Antique
Reproductions`antique_reproductions`5937Antique
Shops`antique_shops`5932Aquariums`aquariums`7998Architectural/Surveying
Services`architectural_surveying_services`8911Art Dealers and
Galleries`art_dealers_and_galleries`5971Artists Supply and Craft
Shops`artists_supply_and_craft_shops`5970Auto Body Repair
Shops`auto_body_repair_shops`7531Auto Paint Shops`auto_paint_shops`7535Auto
Service Shops`auto_service_shops`7538Auto and Home Supply
Stores`auto_and_home_supply_stores`5531Automated Fuel
Dispensers`automated_fuel_dispensers`5542Automobile
Associations`automobile_associations`8675Automotive Parts and Accessories
Stores`automotive_parts_and_accessories_stores`5533Automotive Tire
Stores`automotive_tire_stores`5532Bail and Bond Payments (payment to the surety
for the bond, not the actual bond paid to the government agency)
Restricted`bail_and_bond_payments`9223Bakeries`bakeries`5462Bands,
Orchestras`bands_orchestras`7929Barber and Beauty
Shops`barber_and_beauty_shops`7230Betting/Casino Gambling
Restricted`betting_casino_gambling`7995Bicycle
Shops`bicycle_shops`5940Billiard/Pool
Establishments`billiard_pool_establishments`7932Boat
Dealers`boat_dealers`5551Boat Rentals and
Leases`boat_rentals_and_leases`4457Book Stores`book_stores`5942Books,
Periodicals, and Newspapers`books_periodicals_and_newspapers`5192Bowling
Alleys`bowling_alleys`7933Bus Lines`bus_lines`4131Business/Secretarial
Schools`business_secretarial_schools`8244Buying/Shopping
Services`buying_shopping_services`7278Cable, Satellite, and Other Pay Television
and Radio`cable_satellite_and_other_pay_television_and_radio`4899Camera and
Photographic Supply Stores`camera_and_photographic_supply_stores`5946Candy, Nut,
and Confectionery Stores`candy_nut_and_confectionery_stores`5441Car Rental
Agencies`car_rental_agencies`7512Car Washes`car_washes`7542Car and Truck Dealers
(New & Used) Sales, Service, Repairs Parts and
Leasing`car_and_truck_dealers_new_used`5511Car and Truck Dealers (Used Only)
Sales, Service, Repairs Parts and
Leasing`car_and_truck_dealers_used_only`5521Carpentry
Services`carpentry_services`1750Carpet/Upholstery
Cleaning`carpet_upholstery_cleaning`7217Caterers`caterers`5811Charitable and
Social Service Organizations - Fundraising
Restricted`charitable_and_social_service_organizations_fundraising`8398Chemicals
and Allied Products (Not Elsewhere
Classified)`chemicals_and_allied_products`5169Child Care
Services`child_care_services`8351Childrens and Infants Wear
Stores`childrens_and_infants_wear_stores`5641Chiropodists, Podiatrists
Restricted`chiropodists_podiatrists`8049Chiropractors
Restricted`chiropractors`8041Cigar Stores and Stands
Restricted`cigar_stores_and_stands`5993Civic, Social, Fraternal
Associations`civic_social_fraternal_associations`8641Cleaning and
Maintenance`cleaning_and_maintenance`7349Clothing
Rental`clothing_rental`7296Colleges,
Universities`colleges_universities`8220Commercial Equipment (Not Elsewhere
Classified)`commercial_equipment`5046Commercial
Footwear`commercial_footwear`5139Commercial Photography, Art and
Graphics`commercial_photography_art_and_graphics`7333Commuter Transport,
Ferries`commuter_transport_and_ferries`4111Computer Network
Services`computer_network_services`4816Computer
Programming`computer_programming`7372Computer
Repair`computer_repair`7379Computer Software
Stores`computer_software_stores`5734Computers, Peripherals, and
Software`computers_peripherals_and_software`5045Concrete Work
Services`concrete_work_services`1771Construction Materials (Not Elsewhere
Classified)`construction_materials`5039Consulting, Public
Relations`consulting_public_relations`7392Correspondence
Schools`correspondence_schools`8241Cosmetic
Stores`cosmetic_stores`5977Counseling Services
Restricted`counseling_services`7277Country Clubs`country_clubs`7997Courier
Services`courier_services`4215Court Costs, Including Alimony and Child Support -
Courts of Law Restricted`court_costs`9211Credit Reporting
Agencies`credit_reporting_agencies`7321Cruise Lines
Restricted`cruise_lines`4411Dairy Products
Stores`dairy_products_stores`5451Dance Hall, Studios,
Schools`dance_hall_studios_schools`7911Dentists, Orthodontists
Restricted`dentists_orthodontists`8021Department
Stores`department_stores`5311Detective Agencies`detective_agencies`7393Digital
Goods Media – Books, Movies, Music`digital_goods_media`5815Digital Goods –
Applications (Excludes Games)`digital_goods_applications`5817Digital Goods –
Games`digital_goods_games`5816Digital Goods – Large Digital Goods
Merchant`digital_goods_large_volume`5818Direct Marketing - Catalog
Merchant`direct_marketing_catalog_merchant`5964Direct Marketing - Combination
Catalog and Retail
Merchant`direct_marketing_combination_catalog_and_retail_merchant`5965Direct
Marketing - Inbound Telemarketing
Restricted`direct_marketing_inbound_telemarketing`5967Direct Marketing -
Insurance Services`direct_marketing_insurance_services`5960Direct Marketing -
Other`direct_marketing_other`5969Direct Marketing - Outbound Telemarketing
Restricted`direct_marketing_outbound_telemarketing`5966Direct Marketing -
Subscription`direct_marketing_subscription`5968Direct Marketing - Travel
Restricted`direct_marketing_travel`5962Discount
Stores`discount_stores`5310Doctors Restricted`doctors`8011Door-To-Door Sales
Restricted`door_to_door_sales`5963Drapery, Window Covering, and Upholstery
Stores`drapery_window_covering_and_upholstery_stores`5714Drinking
Places`drinking_places`5813Drug Stores and Pharmacies
Restricted`drug_stores_and_pharmacies`5912Drugs, Drug Proprietaries, and
Druggist Sundries
Restricted`drugs_drug_proprietaries_and_druggist_sundries`5122Dry
Cleaners`dry_cleaners`7216Durable Goods (Not Elsewhere
Classified)`durable_goods`5099Duty Free Stores`duty_free_stores`5309Eating
Places, Restaurants`eating_places_restaurants`5812Educational
Services`educational_services`8299Electric Razor
Stores`electric_razor_stores`5997Electric Vehicle
Charging`electric_vehicle_charging`5552Electrical Parts and
Equipment`electrical_parts_and_equipment`5065Electrical
Services`electrical_services`1731Electronics Repair
Shops`electronics_repair_shops`7622Electronics
Stores`electronics_stores`5732Elementary, Secondary
Schools`elementary_secondary_schools`8211Emergency Services (GCAS) (Visa use
only)`emergency_services_gcas_visa_use_only`9702Employment/Temp
Agencies`employment_temp_agencies`7361Equipment
Rental`equipment_rental`7394Exterminating
Services`exterminating_services`7342Family Clothing
Stores`family_clothing_stores`5651Fast Food
Restaurants`fast_food_restaurants`5814Financial Institutions
Restricted`financial_institutions`6012Fines - Government Administrative Entities
Restricted`fines_government_administrative_entities`9222Fireplace, Fireplace
Screens, and Accessories
Stores`fireplace_fireplace_screens_and_accessories_stores`5718Floor Covering
Stores`floor_covering_stores`5713Florists`florists`5992Florists Supplies,
Nursery Stock, and
Flowers`florists_supplies_nursery_stock_and_flowers`5193Freezer and Locker Meat
Provisioners`freezer_and_locker_meat_provisioners`5422Fuel Dealers (Non
Automotive)`fuel_dealers_non_automotive`5983Funeral Services,
Crematories`funeral_services_crematories`7261Furniture Repair,
Refinishing`furniture_repair_refinishing`7641Furniture, Home Furnishings, and
Equipment Stores, Except
Appliances`furniture_home_furnishings_and_equipment_stores_except_appliances`5712Furriers
and Fur Shops`furriers_and_fur_shops`5681General
Services`general_services`1520Gift, Card, Novelty, and Souvenir
Shops`gift_card_novelty_and_souvenir_shops`5947Glass, Paint, and Wallpaper
Stores`glass_paint_and_wallpaper_stores`5231Glassware, Crystal
Stores`glassware_crystal_stores`5950Golf Courses -
Public`golf_courses_public`7992Government Licensed On-line Casinos (On-Line
Gambling)(US Region only)
Restricted`government_licensed_online_casions_online_gambling_us_region_only`7801Government
Services (Not Elsewhere Classified)
Restricted`government_services`9399Government-Licensed Horse/Dog Racing (US
Region only)
Restricted`government_licensed_horse_dog_racing_us_region_only`7802Government-Owned
Lotteries (Non-US
region)`government_owned_lotteries_non_us_region`9406Government-Owned Lotteries
(US Region only)
Restricted`government_owned_lotteries_us_region_only`7800Grocery Stores,
Supermarkets`grocery_stores_supermarkets`5411Hardware
Stores`hardware_stores`5251Hardware, Equipment, and
Supplies`hardware_equipment_and_supplies`5072Health and Beauty
Spas`health_and_beauty_spas`7298Hearing Aids Sales and Supplies
Restricted`hearing_aids_sales_and_supplies`5975Heating, Plumbing,
A/C`heating_plumbing_a_c`1711Hobby, Toy, and Game
Shops`hobby_toy_and_game_shops`5945Home Supply Warehouse
Stores`home_supply_warehouse_stores`5200Hospitals
Restricted`hospitals`8062Hotels, Motels, and
Resorts`hotels_motels_and_resorts`7011Household Appliance
Stores`household_appliance_stores`5722Industrial Supplies (Not Elsewhere
Classified)`industrial_supplies`5085Information Retrieval
Services`information_retrieval_services`7375Insurance Underwriting, Premiums
Restricted`insurance_underwriting_premiums`6300Intra-Company
Purchases`intra_company_purchases`9950Jewelry Stores, Watches, Clocks, and
Silverware
Stores`jewelry_stores_watches_clocks_and_silverware_stores`5944Landscaping
Services`landscaping_services`0780Laundries`laundries`7211Laundry, Cleaning
Services`laundry_cleaning_services`7210Legal Services,
Attorneys`legal_services_attorneys`8111Luggage and Leather Goods
Stores`luggage_and_leather_goods_stores`5948Lumber, Building Materials
Stores`lumber_building_materials_stores`5211Marinas, Service and
Supplies`marinas_service_and_supplies`4468Marketplaces`marketplaces`5262Masonry,
Stonework, and Plaster`masonry_stonework_and_plaster`1740Massage
Parlors`massage_parlors`7297Medical Services
Restricted`medical_services`8099Medical and Dental Labs
Restricted`medical_and_dental_labs`8071Medical, Dental, Ophthalmic, and Hospital
Equipment and Supplies
Restricted`medical_dental_ophthalmic_and_hospital_equipment_and_supplies`5047Membership
Organizations`membership_organizations`8699Mens and Boys Clothing and
Accessories Stores`mens_and_boys_clothing_and_accessories_stores`5611Mens,
Womens Clothing Stores`mens_womens_clothing_stores`5691Metal Service
Centers`metal_service_centers`5051Miscellaneous Apparel and Accessory
Shops`miscellaneous_apparel_and_accessory_shops`5699Miscellaneous Auto
Dealers`miscellaneous_auto_dealers`5599Miscellaneous Business
Services`miscellaneous_business_services`7399Miscellaneous Food Stores -
Convenience Stores and Specialty
Markets`miscellaneous_food_stores`5499Miscellaneous General
Merchandise`miscellaneous_general_merchandise`5399Miscellaneous General
Services`miscellaneous_general_services`7299Miscellaneous Home Furnishing
Specialty
Stores`miscellaneous_home_furnishing_specialty_stores`5719Miscellaneous
Publishing and Printing`miscellaneous_publishing_and_printing`2741Miscellaneous
Recreation Services`miscellaneous_recreation_services`7999Miscellaneous Repair
Shops`miscellaneous_repair_shops`7699Miscellaneous Specialty
Retail`miscellaneous_specialty_retail`5999Mobile Home
Dealers`mobile_home_dealers`5271Motion Picture
Theaters`motion_picture_theaters`7832Motor Freight Carriers and Trucking - Local
and Long Distance, Moving and Storage Companies, and Local Delivery
Services`motor_freight_carriers_and_trucking`4214Motor Homes
Dealers`motor_homes_dealers`5592Motor Vehicle Supplies and New
Parts`motor_vehicle_supplies_and_new_parts`5013Motorcycle Shops and
Dealers`motorcycle_shops_and_dealers`5571Motorcycle Shops,
Dealers`motorcycle_shops_dealers`5561Music Stores-Musical Instruments, Pianos,
and Sheet Music`music_stores_musical_instruments_pianos_and_sheet_music`5733News
Dealers and Newsstands`news_dealers_and_newsstands`5994Non-FI, Money Orders
Restricted`non_fi_money_orders`6051Non-FI, Stored Value Card Purchase/Load
Restricted`non_fi_stored_value_card_purchase_load`6540Nondurable Goods (Not
Elsewhere Classified)`nondurable_goods`5199Nurseries, Lawn and Garden Supply
Stores`nurseries_lawn_and_garden_supply_stores`5261Nursing/Personal Care
Restricted`nursing_personal_care`8050Office and Commercial
Furniture`office_and_commercial_furniture`5021Opticians, Eyeglasses
Restricted`opticians_eyeglasses`8043Optometrists, Ophthalmologist
Restricted`optometrists_ophthalmologist`8042Orthopedic Goods - Prosthetic
Devices Restricted`orthopedic_goods_prosthetic_devices`5976Osteopaths
Restricted`osteopaths`8031Package Stores-Beer, Wine, and
Liquor`package_stores_beer_wine_and_liquor`5921Paints, Varnishes, and
Supplies`paints_varnishes_and_supplies`5198Parking Lots,
Garages`parking_lots_garages`7523Passenger Railways`passenger_railways`4112Pawn
Shops`pawn_shops`5933Pet Shops, Pet Food, and
Supplies`pet_shops_pet_food_and_supplies`5995Petroleum and Petroleum
Products`petroleum_and_petroleum_products`5172Photo
Developing`photo_developing`7395Photographic
Studios`photographic_studios`7221Photographic, Photocopy, Microfilm Equipment,
and
Supplies`photographic_photocopy_microfilm_equipment_and_supplies`5044Picture/Video
Production`picture_video_production`7829Piece Goods, Notions, and Other Dry
Goods`piece_goods_notions_and_other_dry_goods`5131Plumbing, Heating Equipment,
and Supplies`plumbing_heating_equipment_and_supplies`5074Political Organizations
Restricted`political_organizations`8651Postal Services - Government Only
Restricted`postal_services_government_only`9402Precious Stones and Metals,
Watches and
Jewelry`precious_stones_and_metals_watches_and_jewelry`5094Professional
Services`professional_services`8999Public Warehousing and Storage - Farm
Products, Refrigerated Goods, Household Goods, and
Storage`public_warehousing_and_storage`4225Quick , Repro, and
Blueprint`quick_copy_repro_and_blueprint`7338Railroads`railroads`4011Real Estate
Agents and Managers - Rentals`real_estate_agents_and_managers_rentals`6513Record
Stores`record_stores`5735Recreational Vehicle
Rentals`recreational_vehicle_rentals`7519Religious Goods
Stores`religious_goods_stores`5973Religious Organizations
Restricted`religious_organizations`8661Roofing/Siding, Sheet
Metal`roofing_siding_sheet_metal`1761Secretarial Support
Services`secretarial_support_services`7339Security Brokers/Dealers
Restricted`security_brokers_dealers`6211Service
Stations`service_stations`5541Sewing, Needlework, Fabric, and Piece Goods
Stores`sewing_needlework_fabric_and_piece_goods_stores`5949Shoe Repair/Hat
Cleaning`shoe_repair_hat_cleaning`7251Shoe Stores`shoe_stores`5661Small
Appliance Repair`small_appliance_repair`7629Snowmobile
Dealers`snowmobile_dealers`5598Special Trade
Services`special_trade_services`1799Specialty
Cleaning`specialty_cleaning`2842Sporting Goods
Stores`sporting_goods_stores`5941Sporting/Recreation
Camps`sporting_recreation_camps`7032Sports
Clubs/Fields`sports_clubs_fields`7941Sports and Riding Apparel
Stores`sports_and_riding_apparel_stores`5655Stamp and Coin
Stores`stamp_and_coin_stores`5972Stationary, Office Supplies, Printing and
Writing
Paper`stationary_office_supplies_printing_and_writing_paper`5111Stationery
Stores, Office, and School Supply
Stores`stationery_stores_office_and_school_supply_stores`5943Swimming Pools
Sales`swimming_pools_sales`5996TUI Travel -
Germany`t_ui_travel_germany`4723Tailors, Alterations`tailors_alterations`5697Tax
Payments - Government Agencies
Restricted`tax_payments_government_agencies`9311Tax Preparation
Services`tax_preparation_services`7276Taxicabs/Limousines`taxicabs_limousines`4121Telecommunication
Equipment and Telephone
Sales`telecommunication_equipment_and_telephone_sales`4812Telecommunication
Services Restricted`telecommunication_services`4814Telegraph
Services`telegraph_services`4821Tent and Awning
Shops`tent_and_awning_shops`5998Testing
Laboratories`testing_laboratories`8734Theatrical Ticket
Agencies`theatrical_ticket_agencies`7922Timeshares
Restricted`timeshares`7012Tire Retreading and
Repair`tire_retreading_and_repair`7534Tolls/Bridge
Fees`tolls_bridge_fees`4784Tourist Attractions and
Exhibits`tourist_attractions_and_exhibits`7991Towing
Services`towing_services`7549Trailer Parks,
Campgrounds`trailer_parks_campgrounds`7033Transportation Services (Not Elsewhere
Classified)`transportation_services`4789Travel Agencies, Tour
Operators`travel_agencies_tour_operators`4722Truck/Utility Trailer
Rentals`truck_utility_trailer_rentals`7513Typesetting, Plate Making, and Related
Services`typesetting_plate_making_and_related_services`2791Typewriter
Stores`typewriter_stores`5978U.S. Federal Government Agencies or Departments
Restricted`u_s_federal_government_agencies_or_departments`9405Uniforms,
Commercial Clothing`uniforms_commercial_clothing`5137Used Merchandise and
Secondhand
Stores`used_merchandise_and_secondhand_stores`5931Utilities`utilities`4900Variety
Stores`variety_stores`5331Veterinary Services`veterinary_services`0742Video
Amusement Game Supplies`video_amusement_game_supplies`7993Video Game
Arcades`video_game_arcades`7994Video Tape Rental
Stores`video_tape_rental_stores`7841Vocational/Trade
Schools`vocational_trade_schools`8249Watch/Jewelry
Repair`watch_jewelry_repair`7631Welding Repair`welding_repair`7692Wholesale
Clubs`wholesale_clubs`5300Wig and Toupee Stores`wig_and_toupee_stores`5698Wires,
Money Orders Restricted`wires_money_orders`4829Womens Accessory and Specialty
Shops`womens_accessory_and_specialty_shops`5631Womens Ready-To-Wear
Stores`womens_ready_to_wear_stores`5621Wrecking and Salvage
Yards`wrecking_and_salvage_yards`5935

## Links

- [MCCs](https://en.wikipedia.org/wiki/Merchant_category_code)
- [retrieve](https://docs.stripe.com/api/accounts/retrieve)
- [Stripe-hosted
onboarding](https://docs.stripe.com/connect/custom/hosted-onboarding)
- [create
accounts](https://docs.stripe.com/api/accounts/create#create_account-business_profile-mcc)
- [Connect](https://docs.stripe.com/connect)
- [update
accounts](https://docs.stripe.com/api/accounts/update#update_account-business_profile-mcc)