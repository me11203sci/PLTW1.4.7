#!/usr/bin/env python

# Import dependencies.
import matplotlib.pyplot as plt
import os.path
from PIL import Image, ImageDraw

# Delcare variables.
currentDirectory = os.path.dirname(os.path.abspath(__file__))
outputDirectory = os.path.join(currentDirectory, "Output\\")
os.makedirs(outputDirectory)
workingDirectory = os.path.join(currentDirectory, "Input\\")
crest = Image.open(currentDirectory + "\\crest.png")

# Modify crest.
crest = crest.resize((157,200))

# Loop through input directory.
for fileName in os.listdir("Input/"):

    # Load valid file(s).
    if fileName.endswith(".png") or fileName.endswith(".jpg"):
         currentImage = Image.open(workingDirectory + fileName)
    else:
        continue

    # Determine padding based on image size.
    borderWidth = currentImage.width * 0.025
    paddingRight = int((currentImage.width - crest.width) - borderWidth)
    paddingTop = int(currentImage.height - crest.height - borderWidth)
    sideTriangeHieght = (currentImage.height-(borderWidth*2))/20

    # Paste watermark and border.
    currentImage.paste(crest, (paddingRight, paddingTop), mask = crest)

    # Generate border.
    draw = ImageDraw.Draw(currentImage)
    for i in range (0,41):
            draw.polygon([(borderWidth*i,0),(borderWidth+(borderWidth*i),0),(borderWidth*i,borderWidth)],"blue","white")
            draw.polygon([(borderWidth+(borderWidth*i),0),(borderWidth+(borderWidth*i),borderWidth),(borderWidth*i,borderWidth)],"lightblue","white")
    for i in range (0,41):
            draw.polygon([(borderWidth*i,currentImage.height-borderWidth),(borderWidth+(borderWidth*i),currentImage.height-borderWidth),(borderWidth*i,currentImage.height)],"blue","white")
            draw.polygon([(borderWidth+(borderWidth*i),currentImage.height-borderWidth),(borderWidth+(borderWidth*i),currentImage.height),(borderWidth*i,currentImage.height)],"lightblue","white")
    for i in range (0,20):
            draw.polygon([(0,borderWidth+sideTriangeHieght*i),(borderWidth,borderWidth+sideTriangeHieght*i),(0,borderWidth+sideTriangeHieght+(sideTriangeHieght*i))],"blue","white")
            draw.polygon([(borderWidth,borderWidth+sideTriangeHieght*i),(borderWidth,borderWidth+sideTriangeHieght+(sideTriangeHieght*i)),(0,borderWidth+sideTriangeHieght+(sideTriangeHieght*i))],"lightblue","white")
    for i in range (0,20):
            draw.polygon([(currentImage.width-borderWidth,borderWidth+sideTriangeHieght*i),(currentImage.width,borderWidth+sideTriangeHieght*i),(currentImage.width-borderWidth,borderWidth+sideTriangeHieght+(sideTriangeHieght*i))],"blue","white")
            draw.polygon([(currentImage.width,borderWidth+sideTriangeHieght*i),(currentImage.width,borderWidth+sideTriangeHieght+(sideTriangeHieght*i)),(currentImage.width-borderWidth,borderWidth+sideTriangeHieght+(sideTriangeHieght*i))],"lightblue","white")
    del draw

    # Output image(s).
    currentImage.save(outputDirectory + "modified_" + fileName)
