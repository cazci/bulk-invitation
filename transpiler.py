import csv
from PIL import Image, ImageFont, ImageDraw 
 
with open('invitations.csv', mode ='r') as file:
  names = csv.reader(file)
  font = ImageFont.truetype('Lato/Lato-Italic.ttf', 34)

  for name in names:
    invitation = Image.open("invitation.png")
    editable = ImageDraw.Draw(invitation)

    cutoff
    cutoffOffset = (0, 0)

    if (name[1] == "m"):
      cutoff = "__________________"
      cutoffOffset = (0, 0)
    elif (name[1] == "f"):
      cutoff = "______________"
      cutoffOffset = (0, 0)
    elif (name[1] == "b"):
      cutoff = "_______            ________"
      cutoffOffset = (0, 0)

    editable.text((0, 0), name[0], (0, 0, 0), font=font)

    if (cutoff != "_"):
      editable.text(cutoffOffset, cutoff, (0, 0, 0), font=font)

    invitation.save("exports/" + name[2] + "/"+ name[0] + ".png")

