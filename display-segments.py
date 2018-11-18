import pygame, sys
from pygame.locals import *

pygame.init()

fileName = sys.argv[-1]
fileLines = []
with open(fileName, "r+") as fileData:
    # adds lines from file with information in order:
    # y, x, color in hex (starting with#)
    for line in fileData:
        fileLines.append(line.replace("\n", "").split("+"))

print(len(fileLines))
# order: size of segment x, size of segment y, amount segments x, amount segments y, image width, image height
segmentSizeX = int(fileLines[0][0])
segmentSizeY = int(fileLines[1][0])
amountSegmentsX = int(fileLines[2][0])
amountSegmentsY = int(fileLines[3][0])
imgWidth = int(fileLines[4][0])
imgHeight= int(fileLines[5][0])
print("segmentSizeX: "+str(segmentSizeX))
print("segmentSizeY: "+str(segmentSizeY))

for i in range(6, len(fileLines)):
    fileLines[i][2] = fileLines[i][2].split("-")

#print("############")
#print(len(fileLines[30][2]))

screen = pygame.display.set_mode((1920, 1080))

# initialize segments array
segRows = []
for  i in range(0, amountSegmentsY):
    row = []
    for j in range(0, amountSegmentsX):
        row.append("")
    segRows.append(row)

for i in range(6, len(fileLines)):
    #print(fileLines[i])
    segRows[int(fileLines[i][0])][int(fileLines[i][1])] = (int(fileLines[i][2][0]), int(fileLines[i][2][1]), int(fileLines[i][2][2]))

#print(segRows)
#print("y:"+str(len(segRows))+" x:"+str(len(segRows[0])))

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
