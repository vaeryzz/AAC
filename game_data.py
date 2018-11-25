characters = {
	"THE_PLAYER": {
		"name": "Lurco",
		"equipped": [None] * 6,  # armor, weapon
		"inventory": ["copper_sword", "hpot0"],
		"coin": 12,
		"stats": [
			[7, 7], 1, 10, 0, 1, 0,  # HP AP Dodge, D, A, EXP
			60, 15, 25, 25, 0  # HC IA CC CD BD
		],
		"mods": {
			# HC IA CC CD BD
			"sword": [10, -15, -5, 25, 0],
			"axe": [0, 0, -10, 75, 0],
			"mace": [-25, 30, -15, 75, 0],
		},
		"perks": [],
		"avatar": "bw-man0-ava",
		"image": "bw-man0",
		"map_image": "map_lurco-35x35",
		"place_image": "bw-man0",
		"place_indoor_image": "bw-man0",
		#"location": None,  
		"location_coords": [50, 50],  # location of player in map
	},
	# NPCs -------------------------------------
	"ferrec": {  # merchant,
		"name": "Ferrec",
		"coin": 475,
		"inventory": ["book", "book", "hpot0"],
		"avatar": "czferrec_ava-100x105",
		# default inv? to reset auto, optional
	},
	"innkeeper": {  # merchant and ?quest giver
		"name": "Innlady",
		"coin": 12,
		"inventory": ["hpot0", "hpot0", "hpot0", "copper_sword"],
		"avatar": "czinnkeeper_ava-100x105",
		# default inv? to reset auto, optional, not implemented yet
		#"default_inventory": (12, ["hpot0"] * 5),
	},
	# Enemies ----------------------------------
	"bandit99": {  # Bandit that attacks the player in MQ00
		"name": "Bandit Thug",
		"inventory": [],
		"coin": 250,
		"stats": [ [35, 35], 1, 5, 1, 5, 1000, 75, 0, 15, 25 ],  # HP AP Dodge D A EXP HC IA CC CD BD
		"avatar": "bw-man0c-ava",
		"image": "bw-man0c-f",
	},
	"plant0": {
		"name": "Cinder Plant",
		"inventory": [],
		"coin": 0,
		"stats": [
			[5, 5], 2, 1, 0, 1, 100,
			70, 15, 15, 25, 0
		],
		"avatar": "bw-t-fmonster0-ava",
		"image": "bw-t-fmonster0",
	},
	## -- Camp Bandits -- ##
	"camp_bandit0": {
		"name": "Bandit",
		"inventory": [],
		"coin": 25,
		"stats": [
			[35, 35], 2, 0, 1, 2, 100,
			60, 15, 15, 25, 0
		],
		"avatar": "bw-man0b-ava",
		"image": "bw-man0b-f",
	},
	"camp_bandit1": {
		"name": "Bandit",
		"inventory": [],
		"coin": 25,
		"stats": [
			[35, 35], 1, 0, 2, 4, 200,
			60, 15, 15, 25, 0
		],
		"avatar": "bw-man0g-ava",
		"image": "bw-man0g-f",
	},
	"camp_bandit2": {
		"name": "Bandit",
		"inventory": [],
		"coin": 30,
		"stats": [
			[38, 38], 1, 0, 1, 5, 300,
			60, 15, 15, 25, 0
		],
		"avatar": "bw-man0c-ava",
		"image": "bw-man0c-f",
	},
	"camp_bandit3": {
		"name": "Bandit",
		"inventory": [],
		"coin": 30,
		"stats": [
			[38, 38], 1, 0, 0, 5, 300,
			60, 15, 15, 25, 0
		],
		"avatar": "bw-man0h-ava",
		"image": "bw-man0h-f",
	},
	"camp_bandit4": {
		"name": "Bandit",
		"inventory": [],
		"coin": 50,
		"stats": [
			[40, 40], 2, 0, 5, 2.5, 500,
			60, 15, 15, 25, 0
		],
		"avatar": "bw-man0f-ava",
		"image": "bw-man0f-f",
	},
	"camp_bandit5": {
		"name": "Bandit",
		"inventory": [],
		"coin": 50,
		"stats": [
			[40, 40], 1, 0, 5, 5, 500,
			60, 15, 15, 25, 0
		],
		"avatar": "bw-man0e-ava",
		"image": "bw-man0e-f",
	},
	"camp_bandit_boss": {
		"name": "Bandit",
		"inventory": [],
		"coin": 1000,
		"stats": [
			[45, 45], 1, 0, 10, 4, 1000,
			60, 15, 15, 25, 0
		],
		"avatar": "bw-man0d-ava",
		"image": "bw-man0d-f",
	},
	
	
	"cave_lookout": {
		"name": "Weak Bandit",
		"inventory": [],
		"coin": 25,
		"stats": [
			[17, 17], 2, 5, 1, 2, 100,
			60, 15, 15, 25, 0
		],
		"avatar": "bw-man0i-ava",
		"image": "bw-man0i-f",
	},
	"cave_bandit1": {
		"name": "Weak Bandit",
		"inventory": [],
		"coin": 35,
		"stats": [
			[24, 24], 1, 5, 1, 3, 100,
			60, 15, 15, 25, 0
		],
		"avatar": "bw-man0g-ava",
		"image": "bw-man0g-f",
	},
	"cave_bandit2": {
		"name": "Bandit",
		"inventory": [],
		"coin": 125,
		"stats": [
			[35, 35], 1, 5, 5, 5, 100,
			60, 15, 15, 25, 0
		],
		"avatar": "bw-man0b-ava",
		"image": "bw-man0b-f",
	},
	"cultist0": {
		"name": "Cultist",
		"inventory": [],
		"coin": 200,
		"stats": [
			[50, 50], 1, 1, 0, 4, 100,
			75, 15, 15, 25, 0
		],
		"avatar": "bw-man0b-ava",
		"image": "bw-man0b-f",
	},
	"bandit0": {
		"name": "Weak Bandit",
		"inventory": [],
		"coin": 25,
		"stats": [
			[17, 17], 1, 5, 1, 2, 100,
			60, 15, 15, 25, 0
		],
		"avatar": "bw-man0i-ava",
		"image": "bw-man0i-f",
	},
	"mplant0": {
		"name": "Cinder Plant",
		"inventory": [],
		"coin": 0,
		"stats": [
			[5, 5], 2, 1, 0, 1, 100,
			70, 15, 15, 25, 0
		],
		"avatar": "bw-t-fmonster0-ava",
		"image": "bw-t-fmonster0",
	},
	"pondcrab0": {
		"name": "Pondcrab",
		"inventory": [],
		"coin": 50,
		"stats": [
			[12, 25], 1, 1, 1, 3, 100,
			70, 15, 15, 25, 0
		],
		"avatar": "bw-t-npc-pondcrab0-ava",
		"image": "bw-t-npc-pondcrab0",
	},
	"treasure_hunter": {
		"name": "Treasure Hunter",
		"inventory": [],
		"coin": 375,
		"stats": [
			[48, 48], 1, 1, 7, 6, 0,
			75, 15, 35, 50, 0
		],
		"avatar": "bw-t-npc-treasurehunter-ava",
		"image": "bw-t-npc-treasurehunter-f",
	},
}
containers = {
	"cabin_chest": {  # Player House 0 Chest
		"name": "Chest",
		"inventory": ["book"],
		"coin": 1000,
		"avatar": "czchest_ava-100x105",
	},
}
items = {
	# armor ------------------------------------
	"cloak_shield0": {
		"name": "Cloak and Shield",
		"type": "armor",
		"image": "invi_cloaknshield",
		"descr": None,
		"price": [61, 30],
		# unique variables
		"defense_value": 1,
	},
	# potion -----------------------------------
	"hpot0": {
		"name": "Health Potion",
		"type": "potion",
		"image": "bw-t-pot-hp0",
		"descr": "A bitter potion of healing.",
		"price": [47, 27],
		#"quality": ("Uncommon", "#776611"),
		# unique variables
		"heal_value": 7,
	},
	"plant0_extract": {
		"name": "Cinder Extract",
		"type": "potion",
		"image": "bw-t-pot-cintract",
		"descr": "A powerful potion of healing.",
		"price": [127, 67],
		"heal_value": 20,
	},
	# treasure ---------------------------------
	"book": {  # make quality list later
		"name": "Book",
		"type": "treasure",
		"image": "bw-t-trs-book",
		"descr": "Valuable to the wealthy and few.",
		# buy/sell
		"price": [250, 125],
	},
	"book_special": {
		"name": "Special Book",
		"type": "treasure",
		"image": "bw-t-trs-book-special",
		"descr": "It's special.",
		"quality": ("Uncommon", "#776611"),
		# buy/sell
		"price": [500, 385],
	},
	# OLD
	"books": {  # make quality list later
		"name": "Books",
		"type": "treasure",
		"image": "invi_books",
		"descr": "Valuable to the wealthy and few.",
		"quality": ("Uncommon", "#776611"),
		# buy/sell
		"price": [250, 125],
	},
	# weapon -----------------------------------
	"sword_steel_rusty": {
		"name": "Rusty Sword",
		"type": "weapon",
		"image": "bw-t-wpn-sword-steel-rusty",
		"descr": "A rusty steel sword. Deadly nonetheless.",
		"price": [300, 150],
		"weapon_type": "sword",
		"attack_value": 7,
	},
	"axe_epic": {
		"name": "Epic Axe",
		"type": "weapon",
		"image": "bw-t-axe-copper1",
		"descr": "An instrument of death.",
		"price": [750, 500],
		"weapon_type": "axe",
		"attack_value": 12,
	},
	# OLD
	"copper_axe": {
		"name": "Copper Axe",
		"type": "weapon",
		"image": "bw-t-axe-copper",
		"descr": "A brittle axe.",
		"price": [107, 49],
		# unique variables
		"weapon_type": "axe",
		"attack_value": 3,
	},
	"copper_mace": {
		"name": "Copper Mace",
		"type": "weapon",
		"image": "bw-t-wpn-mace-copper",
		"descr": "A tool for breaking bones.",
		"price": [149, 75],
		# unique variables
		"weapon_type": "mace",
		"attack_value": 5,
	},
	"copper_sword": {
		"name": "Copper Sword",
		"type": "weapon",
		"image": "invi_swordc",
		"descr": "A useful tool for slicing paper.",
		"price": [87, 45],
		# unique variables
		"weapon_type": "sword",
		"attack_value": 1,
	},
	"iron_sword": {
		"name": "Iron Sword",
		"type": "weapon",
		"image": "invi_swordi",
		"descr": "A popular weapon for killing peasants.",
		"price": [261, 129],
		# unique variables
		"weapon_type": "sword",
		"attack_value": 6
	},
}
perks = {
	# % % r r r
	# "HP", "AP", "Dodge%", "Def", "Atk"
	# %/raw for each type, not both to avoid errors
	#"sym": ["HP", "AP", "Dodge%", "Def", "Atk"],
	"swordDMG0": {
		"name": "Sword Mastery I",
		"desc": "Increases sword damage by 13.5%",
		"level": [0, 10],
		"affects": ["swordDB"], 
		"change": ["13.5raw"],
		"prerequisite": None,
		"img": "perk_swordi-40x40",
	},
	"swordHC0": {
		"name": "Fruit Slicer",
		"desc": "Increases sword hit chance by 4.5%",
		"level": [0, 5],
		"affects": ["swordHC"], 
		"change": ["4.5raw"],
		"prerequisite": ("swordDMG0", 3),
		"img": "perk_fruitslicer-40x40",
	},
	"swordCC0": {
		"name": "Piercing Strike",
		"desc": "Increase sword critical hit chance by 7.5%",
		"level": [0, 4],
		"affects": ["swordCC"], 
		"change": ["7.5raw"],
		"prerequisite": ("swordDMG0", 2),
		"img": "perk_piercingstrike-40x40",
	},
	"swordMX0": {
		"name": "Sword Adept",
		"desc": "Increases sword damage by 75%",
		"level": [0, 1],
		"affects": ["swordDB"], 
		"change": ["75raw"],
		"prerequisite": ("swordHC0", 5),
		"img": "perk_swordadept-40x40",
	},
	"dodge0": {
		"name": "Fast Reflexes",
		"desc": "Increases dodge by 2.9%",
		"level": [0, 9],
		"affects": ["Dodge%"], 
		"change": ["2.9raw"],
		"prerequisite": None,
		"img": "perk_fastreflex-40x40",
	},
	"dodgeMX0": {
		"name": "Faster Reflexes",
		"desc": "Increases dodge by 7.5%",
		"level": [0, 1],
		"affects": ["Dodge%"], 
		"change": ["7.5raw"],
		"prerequisite": ("dodge0", 9),
		"img": "perk_fasterreflex-40x40",
	},
}
map_markers = {  # appears on map
	"cabin": { "name": "Cabin", "image": "bw-cabin-35x35", "coords": (150, 400), },
	"cave": { "name": "Cave", "image": "bw-cave-35x35", "coords": (110, 200), },
	"forest": { "name": "", "image": "bw-forest-30x30", "coords": (417, 195), },
	"forest1": { "name": "", "image": "bw-forest-30x30", "coords": (455, 200), },
	"forest2": { "name": "", "image": "bw-forest-30x30", "coords": (425, 220), },
	"village": { "name": "Village", "image": "bw-village-40x40", "coords": (355, 250), },
	"cultist_house": { "name": "House", "image": "bw-house-30x30", "coords": (475, 350), },
	"ruin": { "name": "Ruin", "image": "bw-fhouse-30x30", "coords": (250, 150), },
	"forest3": { "name": "", "image": "bw-forest-30x30", "coords": (160, 130), },
}
'''
	"vhouse": {
		"name": "?????",
		"image": "bw-vhouse-37x37",
		"coords": (725, 100),
		"condition": None,
		#"event": "place|cabin",  # future
		#"place": "cabin", redundant as key is the parameter
	},
	"fhouse": {
		"name": "?????",
		"image": "bw-fhouse-30x30",
		"coords": (120, 60),
		"condition": None,
		#"event": "place|cabin",  # future
		#"place": "cabin", redundant as key is the parameter
	},
	"hillfort": {
		"name": "?????",
		"image": "bw-hillfort-40x40",
		"coords": (585, 50),
		"condition": None,
		#"event": "place|cabin",  # future
		#"place": "cabin", redundant as key is the parameter
	},
	"church": {
		"name": "?????",
		"image": "bw-church-35x35",
		"coords": (720, 200),
		"condition": None,
		#"event": "place|cabin",  # future
		#"place": "cabin", redundant as key is the parameter
	},
	"house": {
		"name": "House",
		"image": "bw-house-30x30",
		"coords": (530, 180),
		"condition": None,
		#"event": "place|cabin",  # future
		#"place": "cabin", redundant as key is the parameter
	},
	"camp": {
		"name": "Camp",
		"image": "bw-tent-30x30",
		"coords": (630, 300),
		"condition": None,
		#"event": "place|cabin",  # future
		#"place": "cabin", redundant as key is the parameter
	},
'''
world_places = {  # list of places
	"cabin": {  # Player House 0
		"name": "Cabin",
		"type": ["outdoors", "bw-bg_top1", "bw-bg_bot1"],
		"entry_coords": (625, 317),
		"walk_range": "default",
		"events": [
			("Qdormant|MQ01", None, "bw-house0|250,170"),
			("Qdormant|MQ01", "place|cabin_indoors", "bw-hdoor0|270,253"),
			("Qstarted|MQ01", None, "bw-house0-z|250,170"),
			("Qdormant|MQ01", "dialg|maiden00", "bw-t-hotgirl0|180,185"),  # change image size to 80x175, 100x185 for males
			(None, "leave|", "bw-arrow_up|555,270"),
		],
	},
	"cabin_indoors": {  # Player House 0 Indoors
		"name": "Cabin",
		"type": ["indoors", "bw-wall0", "bw-floor0"],
		"entry_coords": (480, 285),
		"walk_range": "default",
		"events": [
			(None, "place|cabin*312,320", "bw-door0|412,157"),
			(None, None, "bw-bed0|60, 267"),
			(None, None, "bw-closet0|275, 180"),
			(None, "chest|cabin_chest", "bw-chest0|630,450"),
		],
	},
	"cave": {
		"name": "Cave",
		"type": ["outdoors", "bw-bg_top1", "bw-bg_bot1"],
		"entry_coords": (675, 317),
		"walk_range": "default",
		"events": [
			("Qdormant|MQ02", "place|cave_inner", "bw-cave|100,175"),
			("Qstage1|MQ02", "dialg|MQ02-1", "bw-cave|100,175"),
			("Qstage+2|MQ02", "place|cave_inner", "bw-cave|100,175"),
			(None, "leave|", "bw-arrow_up|705,270"),
		],
	},
	"cave_inner": {
		"name": "Cave",
		"type": ["outdoors", "bw-bg_top3", "bw-bg_bot3"],
		"entry_coords": (275, 317),
		"walk_range": "default",
		"events": [  # "Qstage2|MQ02"
			("Qstage2|MQ02", "dialg|MQ02-4", "bw-man0g-f|650,175"),
			("Qstage2|MQ02", "dialg|MQ02-4", "bw-man0i|500,160"),
			("Qstage2|MQ02", "dialg|MQ02-4", "bw-man0b|480,200"),
			("Qstage3|MQ02", "dialg|MQ02-8", "bw-t-girl0-f|650,200", "Qcomplete|MQ02"),
			(None, "place|cave", "bw-arrow_up|105,270"),
		],
	},
	"cultist_house": {
		"name": "House",
		"type": ["outdoors", "bw-bg_top1", "bw-bg_bot1"],
		"entry_coords": (275, 317),
		"walk_range": "default",
		"events": [
			(None, None, "bw-house1|350,170"),
			(None, "dialg|cultist_house", "bw-hdoor0|445,268"),
			(None, "leave|", "bw-arrow_up|205,270"),
		],
	},
	"forest": {
		"name": "Forest",
		"type": ["outdoors", "bw-bg_top1", "bw-bg_bot2"],
		"entry_coords": (145, 417),
		"walk_range": "default",
		"events": [
			#("Qstarted|MQ01", "place|forest_inner0*155,345", "bw-arrow_up|700,275"),
			#(None, "dialg|plant0", "bw-t-fmonster0|590,180"),
			("Qstage1|sq07", "dialg|sq07-1", "bw-t-npc-pondcrab0-ava|350,250"),
			(None, "leave|", "bw-arrow_down|100,545"),
		],
	},
	"forest_inner0": {
		"name": "Forest",
		"type": ["outdoors", "bw-bg_top1", "bw-bg_bot1"],
		"entry_coords": (425, 417),
		"walk_range": "default",
		"events": [
			(None, "dialg|plant0", "bw-t-fmonster0|590,180"),
			(None, "place|forest", "bw-arrow_up|100,275"),
		],
	},
	"forest1": {
		"name": "Forest",
		"type": ["outdoors", "bw-bg_top1", "bw-bg_bot1"],
		"entry_coords": (425, 417),
		"walk_range": "default",
		"events": [
			#("Qstarted|MQ01", "place|forest_inner0*155,345", "bw-arrow_up|700,275"),
			#(None, "dialg|plant0", "bw-t-fmonster0|590,180"),
			(None, "leave|", "bw-arrow_down|445,545"),
		],
	},
	"forest2": {
		"name": "Forest",
		"type": ["outdoors", "bw-bg_top1", "bw-bg_bot1"],
		"entry_coords": (425, 417),
		"walk_range": "default",
		"events": [
			#("Qstarted|MQ01", "place|forest_inner0*155,345", "bw-arrow_up|700,275"),
			(None, "dialg|plant0", "bw-t-fmonster0|590,180"),
			(None, "leave|", "bw-arrow_down|445,545"),
		],
	},
	"forest3": {
		"name": "Forest",
		"type": ["outdoors", "bw-bg_top1", "bw-bg_bot1"],
		"entry_coords": (425, 417),
		"walk_range": "default",
		"events": [
			("Qcompleted|MQ05", "place|forest3_camp_entrance", "bw-arrow_up|552,275"),
			("Qstage1|MQ05", "dialg|MQ05-0", "bw-arrow_up|552,275"),
			(None, "leave|", "bw-arrow_down|445,545"),
		],
	},
	"forest3_camp_entrance": {
		"name": "Bandit Camp",
		"type": ["outdoors", "bw-bg_top2", "bw-bg_bot1"],
		"entry_coords": (325, 417),
		"walk_range": "default",
		"events": [
			("Qcompleted|MQ05", "place|forest3_camp", "bw-gate0|340,212"),
			("Qstage1|MQ05", "dialg|MQ05-3", "bw-gate0|340,212"),
			(None, "place|forest3", "bw-arrow_down|345,545"),
		],
	},
	"forest3_camp": {
		"name": "Bandit Camp",
		"type": ["outdoors", "bw-bg_top2", "bw-bg_bot1"],
		"entry_coords": (325, 450),
		"walk_range": (75, 330, 725, 430),
		"events": [
			("Qcompleted|MQ05", "place|forest3_camp_tent0", "bw-t-obj-tent0|300,170"),
			("Qcompleted|MQ05", "place|forest3_camp_tent1", "bw-t-obj-tent1|550,190"),
			("Qcompleted|MQ05", "place|forest3_camp_tent1", "bw-t-obj-tent1|50,190"),
			("Qstage1|MQ05", None, "bw-t-obj-tent0|300,170"),
			("Qstage1|MQ05", None, "bw-t-obj-tent1|550,190"),
			("Qstage1|MQ05", None, "bw-t-obj-tent1|50,190"),
			("Qstage1|MQ05", "dialg|MQ05-6", "bw-man0f-f|250,200"),
			("Qstage1|MQ05", "dialg|MQ05-6", "bw-man0e|450,200"),
			("Qcompleted|MQ05", "place|forest3_camp_entrance", "bw-arrow_down|245,545"),
		],
	},
	"forest3_camp_tent0": {
		"name": "Tent",
		"type": ["outdoors", "bw-t-bg-top5", "bw-t-bg-bot5"],
		"entry_coords": (225, 320),
		"walk_range": (75, 300, 725, 470),
		"events": [
			(None, "place|forest3_camp*350,400", "bw-arrow_up|383,235"),
		],
	},
	"forest3_camp_tent1": {
		"name": "Tent",
		"type": ["outdoors", "bw-t-bg-top4", "bw-t-bg-bot4"],
		"entry_coords": (225, 320),
		"walk_range": (75, 300, 725, 470),
		"events": [
			(None, "place|forest3_camp*350,400", "bw-arrow_up|383,235"),
		],
	},
	"village": {
		"name": "Village",
		"type": ["outdoors", "bw-bg_top0", "bw-bg_bot1"],
		"entry_coords": (625, 317),
		"walk_range": "default",
		"events": [
			# Tavern
			(None, None, "bw-house0|160,170"),
			(None, None, "bw-t-obj-storesign|195,224"),
			#(None, "store|ferrec", "bw-hdoor0|180,253"),
			(None, "place|village_store", "bw-hdoor0|180,253"),
			(None, None, "bw-house1|-50,160"),
			(None, None, "bw-tavern|245,135"),
			(None, "place|village_tavern", "bw-hdoor0|388,259"),
			# Empty House
			(None, None, "bw-house0|705,170"),
			(None, "dialg|village-empty_house", "bw-hdoor0|722,253"),
			(None, "leave|", "bw-gate0|585,213"),  # Gate
		],
	},
	"village_store": {
		"name": "Store",
		"type": ["indoors", "bw-wall0", "bw-floor0"],
		"entry_coords": (480, 317),
		"walk_range": (75, 310, 725, 430),
		"events": [
			(None, "place|village*312,320", "bw-door0|587,162"),
			(None, None, "bw-t-shelf0|215,127"),
			(None, None, "bw-t-shelf0|415,127"),
			(None, "dialg|village_merchant", "bw-t-npc-merchant|330,202"),
			(None, None, "bw-counter|205,287"),
		],
	},
	"village_tavern": {
		"name": "Tavern",
		"type": ["indoors", "bw-wall0", "bw-floor0"],
		"entry_coords": (480, 285),
		"walk_range": "default",
		"events": [
			(None, "place|village*312,320", "bw-door0f|432,157"),
			(None, "place|village*312,320", "bw-door0|565,157"),
			(None, "dialg|tavernkeeper00", "bw-woman0|180,190"),
			(None, None, "bw-counter|65,270"),
			(None, None, "bw-table|80,450"),
			("Qstage1|MQ04", None, "bw-t-npc-treasurehunter-f|654,340"),
			(None, None, "bw-table|538,450"),
		],
	},
	"ruin": {
		"name": "Ruin",
		"type": ["outdoors", "bw-bg_top1", "bw-bg_bot1"],
		"entry_coords": (275, 295),
		"walk_range": "default",
		"events": [
			(None, "leave|", "bw-gate0|100,213"),
			(None, None, "bw-t-obj-fort-destroyed|435,150"),
			(None, None, "bw-house0-z|-75,180"),
			(None, None, "bw-house0-z|325,180"),
			(None, None, "bw-house0-z-f|685,180"),
			(None, None, "bw-house0-z-f|195,190"),
			("Qstage2|MQ04", None, "bw-t-chest0|600,315"),
			("Qstage2|MQ04", "dialg|MQ04-2", "bw-t-npc-treasurehunter-f|475,203"),
			
		],
	},
	
	
	"vhouse": {
		"name": "Camp",
		"type": ["outdoors", "bw-bg_top2", "bw-bg_bot1"],
		"entry_coords": (425, 417),
		"walk_range": "default",
		"events": [
			(None, None, "bw-gate0|245,210"),
			(None, "leave|", "bw-arrow_down|445,545"),
		],
	},
	"fhouse": {
		"name": "Camp",
		"type": ["outdoors", "bw-bg_top2", "bw-bg_bot1"],
		"entry_coords": (425, 417),
		"walk_range": "default",
		"events": [
			(None, None, "bw-gate0|245,210"),
			(None, "leave|", "bw-arrow_down|445,545"),
		],
	},
	"hillfort": {
		"name": "Camp",
		"type": ["outdoors", "bw-bg_top2", "bw-bg_bot1"],
		"entry_coords": (425, 417),
		"walk_range": "default",
		"events": [
			(None, None, "bw-gate0|245,210"),
			(None, "leave|", "bw-arrow_down|445,545"),
		],
	},

	"church": {
		"name": "Camp",
		"type": ["outdoors", "bw-bg_top2", "bw-bg_bot1"],
		"entry_coords": (425, 417),
		"walk_range": "default",
		"events": [
			(None, None, "bw-gate0|245,210"),
			(None, "leave|", "bw-arrow_down|445,545"),
		],
	},
	#
	
	
	"house": {
		"name": "House",
		"type": ["outdoors", "bw-bg_top1", "bw-bg_bot1"],
		"entry_coords": (625, 317),
		"walk_range": "default",
		"events": [
			(None, None, "bw-house1|250,160"),
			(None, "leave|", "bw-arrow_up|705,270"),
		],
	},
	"camp": {
		"name": "Camp",
		"type": ["outdoors", "bw-bg_top2", "bw-bg_bot1"],
		"entry_coords": (425, 417),
		"walk_range": "default",
		"events": [
			(None, None, "bw-gate0|245,210"),
			(None, "leave|", "bw-arrow_down|445,545"),
		],
	},

}
quests = {  # Quest added to fertigql if reward is given
	# MAIN QUESTS ACT 1  10k EXP 3k GOLD
	"MQ00": {  # COMPLETED
		"name": "Maiden In Illness",
		"stage": [0, 2],
		"stage1": ["    My recent maiden is ill and needs a tonic."],
		"stage2": ["    I was attacked right after I gave her the potion."],
		"reward": [1000, 0, ["hpot0"]],  # exp, gold, items
	},
	"MQ01": {  # COMPLETED
		"name": "Gathering The Pieces",
		"stage": [0, 3],
		"stage1": ["    I need time to recover. Once I am able to, I should go to the village for answers. Some of the villagers may have information about the attack. I am too wounded to fight the bandits and I need time to rest and recover."],
		"stage2": ["    The mute boy who is gravely ill needs a special plant extract that can only be found near the village. He can give us significant details about the bandits. The plants are said to be dangerous and deadly. I need a sword, armor and some tonics in order to be sucessful."],
		"stage3": ["    I delivered the plant extract just in time. The mute boy is still in bed but the tavernkeeper said that he is recovering and that he would have died if it was not for me. I should hone my fighting skills while the boy recovers."],
		"reward": [1500, 100, ["hpot0", "hpot0"]],
	},
	"MQ02": {  # COMPLETED
		"name": "Descending The Void",
		"stage": [0, 4],
		"stage1": ["    The mute boy tells of a cave to the north west. There a group of bandits rest after their raiding and pillaging. They might be the ones that have destroyed the cabin."],
		"stage2": ["    I have killed the lookout. I should go further down the cave."],
		"stage3": ["    I have killed the bandits."],
		"stage4": ["    The bandits are dead. I had rescued a girl, somehow related to the mute boy. She gave me useful information. She is in the village now."],
		"reward": [2000, 750, ["cloak_shield0", "copper_sword", "hpot0", "hpot0", "hpot0", "hpot0", "hpot0", "iron_sword"]],
	},
	"MQ03": {  # COMPLETED
		"name": "Cultist In Retreat",
		"stage": [0, 2],
		"stage1": ["    This cultist has been trading and helping these bandits. The rogue bandits from the cave planned to rob him. He knows the location of the bandits that took my maiden. His abode lies somewhere to the west."],
		"stage2": ["    I have recovered his journal but it is written in another language. Its writing is other wordly. I will need something to decode its contents."],
		"reward": [750, 350, ["book", "book", "book", "book"]],
	},
	"MQ04": {  # COMPLETED
		"name": "Decoding The Script",
		"stage": [0, 3],
		"stage1": ["    I should ask around the village for answers. The tavernkeeper likes books. She might know something"],
		"stage2": ["    While talking to the tavernkeeper, I was approached by a man who claims to know a book that can decrypt the journal. He tells of a place far from here. I should meet him there."],
		"stage3": ["    I have decoded the journal. I now know the location of the bandit camp."],
		"reward": [1750, 300, ["hpot0", "copper_mace"]],
	},
	"MQ05": {  # COMPLETED
		"name": "Showdown In Camp",
		"stage": [0, 2],
		"stage1": ["    I now know the location of the bandits. I should ready myself. Hoard. Prepare. Train. There will be no going back. This will be the end."],
		"stage2": ["    I have managed it. I have recovered the sword that they have stolen. I have avenged the cabin they have razed. Many questions still lie unanswered. My maiden is missing. One day, answers will come and when it comes, I will be prepared."],
		"reward": [3000, 1500, ["hpot0", "hpot0", "axe_epic", "copper_mace", "copper_sword", "book_special", "book_special", "book_special", "book_special", "book_special"]],
	},
	# SIDE QUESTS ACT 1  5k EXP 2k GOLD
	"sq00": {
		"name": "Desire For Books",
		"stage": [0, 2],
		"stage1": ["    The tavernkeeper wants books. She'll pay a decent amount of gold for it."],
		"stage2": ["    I gave the books to the tavernkeeper."],
		"reward": [250, 300, ["hpot0"]],  # , "copper_axe" no image
	},
	"sq01": {
		"name": "Need For Gold",
		"stage": [0, 2],
		"stage1": ["    The young lady needs gold to rebuild her life."],
		"stage2": ["    I gave the young lady gold."],
		"reward": [250, 0, ["hpot0"]],
	},
	"sq02": {
		"name": "Man To Kill",
		"stage": [0, 2],
		"stage1": ["    They need a man dead. They'll pay good money. really good money."],
		"stage2": ["    The job is done. I received the gold."],
		"reward": [2500, 700, []],
	},
	"sq03": {
		"name": "Lost Special Item",
		"stage": [0, 2],
		"stage1": ["    They have a lost an item of special value. They will pay good gold for it."],
		"stage2": ["    I have given them their special item."],
		"reward": [750, 500, ["hpot0", "hpot0"]],
	},
	"sq04": {
		"name": "Bandit To Kill",
		"stage": [0, 2],
		"stage1": ["    An infamous bandit needs to die. They will pay good gold."],
		"stage2": ["    I killed the bandit and received the gold."],
		"reward": [1250, 500, []],
	},
	# MORE SIDE QUESTS  5k EXP 3k GOLD
	"sq05": {  # Tavern Keeper
		"name": "Debt Collection",
		"stage": [0, 3],
		"stage1": ["    A drunk hasn't paid his tab for a while. The tavernkeeper has sent you to collect 5000 gold. She said you'll get a quarter of it as a reward. It seems easy. The man is drunk. He is around the village."],
		"stage2": ["    I got the gold from the man. All 5000 of it. I should head back now to the tavernkeeper."],
		"stage3": ["    I got some money after giving it all back to the tavernkeeper. It's nice to be honest."],
		"reward": [750, 1250, []],
	},
	"sq06": {  # Strange Woman
		"name": "The Three Books",
		"stage": [0, 2],
		"stage1": ["    The strange woman likes books. She wants three Special books this time. She'll pay good money."],
		"stage2": ["    I gave her three special books and she gave me gold for it. She said it was a fair deal."],
		"reward": [1000, 950, []],
	},
	"sq07": {  # Merchant - Completed
		"name": "Missing Sword",
		"stage": [0, 3],
		"stage1": ["    The merchant used to be a soldier. He lost his sword somewhere near a pond. He wants it back for old time's sake."],
		"stage2": ["    I got the sword. It's rusty, old, and smells."],
		"stage3": ["    The merchant didn't like it and told me to keep it instead. I received some few gold coins for my efforts."],
		"reward": [2250, 50, ["sword_steel_rusty"]],
	},
	"sq08": {  # Odd Man
		"name": "Lost Item",
		"stage": [0, 3],
		"stage1": ["    An odd man lost a lucky horseshoe somewhere near a pond. He wants you to find it."],
		"stage2": ["    I found his lucky horseshoe. I should go back to the man."],
		"stage3": ["    A man lost a lucky horseshoe somewhere near a pond"],
		"reward": [500, 300, []],
	},
	"sq09": {  # Sly Girl
		"name": "A Lesson",
		"stage": [0, 3],
		"stage1": ["    The village thief needs to be thought a lesson. Beat him up and bring his teeth as a reward."],
		"stage3": ["    I got his teeth. I should go back and collect my reward."],
		"stage2": ["    The thief promised to live a new life of good. He fled the village. I got my reward."],
		"reward": [500, 450, ["book"]],
	},
}

















