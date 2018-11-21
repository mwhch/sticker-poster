import pygame, sys
from pygame.locals import *

pygame.init()

fileName = sys.argv[-1]
fileLines = []
with open(fileName, "r+") as fileData:
    # split output file with & for individual segment info (what used to be done with a new line to indicate a new segment)
    for line in fileData:
        fileLines = line.split("&")

# store info that is gained from input file in segmentInfo array
segmentInfo = []
for line in fileLines:
    # adds lines from file with information in order:
    # y+x+r-g-b
    segmentInfo.append(line.split("+"))

# remove last cell from array because for whatever reason this is an empty cell
# only do this of course if it actually is the empy cell so there is no data deleted
if len(segmentInfo[-1]) == 1:
    del segmentInfo[-1]

# order: size of segment x, size of segment y, amount segments x, amount segments y, image width, image height
segmentSizeX = int(segmentInfo[0][0])
segmentSizeY = int(segmentInfo[1][0])
amountSegmentsX = int(segmentInfo[2][0])
amountSegmentsY = int(segmentInfo[3][0])
imgWidth = int(segmentInfo[4][0])
imgHeight= int(segmentInfo[5][0])
print("segmentSizeX: "+str(segmentSizeX))
print("segmentSizeY: "+str(segmentSizeY))

for i in range(6, len(segmentInfo)):
    segmentInfo[i][2] = segmentInfo[i][2].split("-")

screen = pygame.display.set_mode((1920, 1080))

# initialize segments array
segRows = []
for  i in range(0, amountSegmentsY):
    row = []
    for j in range(0, amountSegmentsX):
        row.append("")
    segRows.append(row)

for i in range(6, len(segmentInfo)):
    segRows[int(segmentInfo[i][0])][int(segmentInfo[i][1])] = (int(segmentInfo[i][2][0]), int(segmentInfo[i][2][1]), int(segmentInfo[i][2][2]))

# draw segments
for i in range(0, amountSegmentsY):
    for j in range(0, amountSegmentsX):
        color = segRows[i][j]
        pygame.draw.rect(screen, color, (j*segmentSizeX,i*segmentSizeY,segmentSizeX,segmentSizeY), 0)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
