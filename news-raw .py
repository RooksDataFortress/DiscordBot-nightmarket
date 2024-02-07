import sys
import random

#The structure should align with the following pattern
#Intro with and ending that can lead to a noun.
#Section one being a noun or something that can go "indicate X ""is"
#Section two being a sentence around what that noun is doing
#Section three being ????

preamble = ["My sources indicate", "A little birdie told me", "Don't be surprised when it goes public that", "Now you didn't hear it from me but", "This just in", "Its time you wake up to the truth that", "Just klepped some data and it strongly suggests"]
cata = ["Pick-a-corp", "a local Senator", "the Mayor", "a gang of corpos", "the Night City Local Council", "an unnamed Cyberpsycho", "a recent suspected serial killer", "the NCPD", "some anonymous Fixer", "a gang of rich investors"]
catb = ["is negotiating an offer with", "is threatening", "is making a compromise", "murdered", "killed", "died", "is praising", "is about to make an announcement about", "have been revealed", "wont stop"]
catc = ["the Corporations.", "The city", "a compromise.", "Warning", "Plan", "Scandal", "Woman", "Man", "Accident", "Hope"]
closing = ["You gonna let them get away with that?", "I'll be dead in the ground before I let that happen.", "Just think about what that means for us!", "Then again, Maybe thats just what they want you to think?", "Sounds to me like it is all part of a bigger picture.", "I'm not too sure if this source is realiable though.", "I'd Love to see Network54 get the guts to run that story."]


corps = ["Biotechnica", "Arasaka", "Millitech", "Budget arms", "Cactus Water", "Constitutional Arms", "Continental Brands", "Dai Lung", "Danger Gal", "Dynalar Technologies", "Federated Arms", "GunMart", "Kendachi", "Makigai", "Malorian Arms", "Network54", "PetroChem", "Quadra", "Rocklin Augmetics", "Raven Microcybernetics", "Sanroo", "Segotari", "SovOil", "Torrel and Chiang", "WorldSat", "Zhirafa", "Ziggurat"]

intro = random.choice(preamble)
topica = random.choice(cata)
topicb = random.choice(catb)
topicc = random.choice(catc)
outro  = random.choice(closing)

if topica == "Pick-a-corp":
    newsa = random.choice(corps)
else:
    newsa = topica
newsb = topicb
newsc = topicc

print("The intro is", intro)
print("The first category is", topica)
print("The Second category is", topicb)
print("The Third category is", topicc)
print("The Outro is", outro)

print("The News is")
print(intro, newsa, newsb, newsc, outro)
