import sys
import random
from news import preamble, cata, catb, catc, closing, corps, gangs, areas, plans, accidents, mysteries

intro = random.choice(preamble)
topica = random.choice(cata)
topicb = random.choice(catb)
topicc = random.choice(catc)
outro  = random.choice(closing)

if topica == "An undisclosed corp":
    newsa = random.choice(corps)
elif topica == "a gang":
    newsa = random.choice(gangs)
elif topica == "a gang of rich investors":
    newsa = ("a gang of rich investors from " + random.choice(corps))
elif topica == "some anonymous Fixer":
    newsa = ("some anonymous Fixer based in " + random.choice(areas))
elif topica == "an alliance of corpos":
    corpgang = random.sample(corps, 2)
    tidiedcorpgang = (corpgang[0] + " and " + corpgang[1])
    newsa = ("an alliance of corpos from " + tidiedcorpgang)
else:
    newsa = topica

if topicb == "is threatening":
    newsb = ("is threatening " + random.choice(cata) + " with")
else:
    newsb = topicb

if topicc == "a plan.":
    newsc = ("a plan to " + random.choice(plans))
elif topicc == "a compromise.":
    newsc = ("a compromise by agreeing to " + random.choice(plans))
elif topicc == "an accident.":
    newsc = ("an accident " + random.choice(accidents))
elif topicc == "a mysterious man.":
    newsc = ("a mysterious man, all we know about him is he " + random.choice(mysteries))
elif topicc == "a mysterious woman.":
    newsc = ("a mysterious woman, all we know about her is she " + random.choice(mysteries))
else:
    newsc = topicc

print("The intro is", intro)
print("The first category is", topica)
print("The Second category is", topicb)
print("The Third category is", topicc)
print("The Outro is", outro)

print("The News is")
print(intro, newsa, newsb, newsc, outro)