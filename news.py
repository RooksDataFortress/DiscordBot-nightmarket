import random
preamble = ["My sources indicate", "A little birdie told me", "Don't be surprised when it goes public that", "Now you didn't hear it from me but", "This just in", "Its time you wake up to the truth that", "Just klepped some data and it strongly suggests", "Word on the street is", "Would you believe me if I told you", "You might wanna take a seat for this because"]
cata = ["An undisclosed corp", "a local Senator", "the Mayor", "an alliance of corpos", "the Night City Local Council", "an unnamed Cyberpsycho", "a recent suspected serial killer", "the NCPD", "some anonymous Fixer", "a gang of rich investors", "a gang"]
catb = ["is negotiating an offer with", "is threatening", "is making a compromise with", "is praising", "is about to make an announcement about", "has been revealed to be mixed up with", "wont stop their current plans, in defiance of"]
catc = ["the Corporations.", "the city.", "a compromise.", "a warning.", "a plan.", "a scandal.", "a mysterious woman.", "a mysterious man.", "an accident."]
closing = ["You gonna let them get away with that?", "I'll be dead in the ground before I let that happen.", "Just think about what that means for us!", "Then again, Maybe thats just what they want you to think?", "Sounds to me like it is all part of a bigger picture.", "I'm not too sure if this source is reliable though.", "I'd Love to see Network54 get the guts to run that story.", "I never thought i'd see the day...", "Talk about a new low.", "I know better than to dig any further into that.", "Better them than me.", "I'm not saying I agree, but I can see where they are coming from."]

corps = ["Biotechnica", "Arasaka", "Millitech", "Budget arms", "Cactus Water", "Constitutional Arms", "Continental Brands", "Dai Lung", "Danger Gal", "Dynalar Technologies", "Federated Arms", "GunMart", "Kendachi", "Makigai", "Malorian Arms", "Network54", "PetroChem", "Quadra", "Rocklin Augmetics", "Raven Microcybernetics", "Sanroo", "Segotari", "SovOil", "Torrel and Chiang", "WorldSat", "Zhirafa", "Ziggurat"]
gangs = ["the Tyger claws gang", "Maelstrom", "a Mox representitive", "the Animals gang's current enforcer", "one of the Voodoo boys"]
areas= ["the badlands","Heywood","Pacifica", "Watson", "Santo Domingo", "Japantown", "Charter Hill", "Charter Hill", "Little China", "Kabuki", "Northside", "North Oak", "Arroyo", "Rancho Coronado", "The Glen", "Wellsprings", "the Corpo Plaza", "Jackson Plains", "the Biotechnica Flats", "Coastview", "Downtown"]
plans = ["beef up their security.", "hire some Solos.", "invest some eddies into their latest scheme.", "buy up a bunch of weapons.", "take out the competition.", "invent some newtech.", "klep a prototype from " + random.choice(corps) + ".", "buy up property in " + random.choice(areas) + ".", "Fake their death."]
accidents = ["in which someone died.", "that let some thieves get away with one of their access passes.", "that was revealed to be an inside job.", "that they themselves caused in the first place.", "that started riots in "+ random.choice(areas) + ".", "that really pissed off " + random.choice(gangs) + "."]
mysteries = ["has a clean shaven head.", "has short black hair.", "is one chipped implant away from going over the edge", "used to run in a chromer band.", "lives somewhere around " + random.choice(areas) + ".", "has connections with " + random.choice(gangs) + ".", "hates corpos with a passion.", "cannot be bought at any cost.", "is a netrunner.", "fought in the 4th corporate war.", "despises edgerunners.", "graduated from Arasaka academyy.", "drives a brand new Quadra.", "is seeking out a long lost twin."]
