# sticker-poster
converts picture from sticker-poster.html via JavaScript, the console of your browser and a python script into a picture with 39x29 segments by calculating the average RGB color of the segments (which are no more than rectangles) and converting them into a string that contains the segments x,y position and color.
the process:
1. click on image
2. save generated .txt file (thanks to https://github.com/eligrey/FileSaver.js for allowing us to keep things simple)
3. call: python3 display-segments.py output.txt

Further detail:
The information contained in the output file contains basic information about the picture and how it was devided:
1. one segments width,
2. one segments height, 
3. amount of segments in x direction
4. amount of segments in y direction
5. image width,
6. image height

everything that follows these 6 lines is a segments y and x coordinate and average (decimal) rgb color in the format:
y+x+r-g-b 
