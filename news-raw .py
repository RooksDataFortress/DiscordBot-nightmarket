import sys
import random

#The structure should align with the following pattern
#Intro with and ending that can lead to a noun.
#Section one being a noun or something that can go "indicate X ""is"
#Section two being a sentence around what that noun is doing
#Section three being ????

preamble = ["My sources indicate", "A little birdie told me", "Don't be surprised when it goes public that", "Now you didn't hear it from me but", "This just in", "Its time you wake up to the truth that", "Just klepped some data and it strongly suggests", "Word on the street is", "Would you believe me if I told you", "You might wanna take a seat for this because"]
cata = ["Pick-a-corp", "a local Senator", "the Mayor", "a gang of corpos", "the Night City Local Council", "an unnamed Cyberpsycho", "a recent suspected serial killer", "the NCPD", "some anonymous Fixer", "a gang of rich investors", "a gang"]
catb = ["is negotiating an offer with", "is threatening", "is making a compromise with", "is praising", "is about to make an announcement about", "has been revealed to be mixed up with", "wont stop their current plans, in defiance of"]
catc = ["the Corporations.", "the city.", "a compromise.", "a warning.", "a plan.", "a scandal.", "a mysterious woman.", "a mysterious man.", "an accident.", "a total loss of hope."]
closing = ["You gonna let them get away with that?", "I'll be dead in the ground before I let that happen.", "Just think about what that means for us!", "Then again, Maybe thats just what they want you to think?", "Sounds to me like it is all part of a bigger picture.", "I'm not too sure if this source is reliable though.", "I'd Love to see Network54 get the guts to run that story."]


corps = ["Biotechnica", "Arasaka", "Millitech", "Budget arms", "Cactus Water", "Constitutional Arms", "Continental Brands", "Dai Lung", "Danger Gal", "Dynalar Technologies", "Federated Arms", "GunMart", "Kendachi", "Makigai", "Malorian Arms", "Network54", "PetroChem", "Quadra", "Rocklin Augmetics", "Raven Microcybernetics", "Sanroo", "Segotari", "SovOil", "Torrel and Chiang", "WorldSat", "Zhirafa", "Ziggurat"]
gangs = ["the Tyger claws gang", "Maelstrom", "a Mox representitive", "the Animals gang's current enforcer", "one of the Voodoo boys"]


intro = random.choice(preamble)
topica = random.choice(cata)
topicb = random.choice(catb)
topicc = random.choice(catc)
outro  = random.choice(closing)

if topica == "Pick-a-corp":
    newsa = random.choice(corps)
elif topica == "a gang":
    newsa = random.choice(gangs)
elif topica == "a gang of rich investors":
    newsa = ("a gang of rich investors from " + random.choice(corps))
else:
    newsa = topica

if topicb == "is threatening":
    newsb = ("is threatening " + random.choice(cata) + " with")
else:
    newsb = topicb

newsc = topicc

print("The intro is", intro)
print("The first category is", topica)
print("The Second category is", topicb)
print("The Third category is", topicc)
print("The Outro is", outro)

print("The News is")
print(intro, newsa, newsb, newsc, outro)
