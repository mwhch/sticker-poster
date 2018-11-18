# sticker-poster
converts picture from sticker-poster.html via JavaScript, the console of your browser and a python script into a picture with 39x29 segments by calculating the average RGB color of the segments (which are no more than rectangles) and converting them into a string that contains the segments x,y position and color.
the process:
1. open dev-tools in your browser (inspect element)
2. go to console
3. enable persist logs (otherwise the log is sometimes shortened, it is supposed to start with the first 6 lines as basic information about the amount of segments, their width and height, and the images width and height)
4. copy all the lines into a file (be carefull that you don't also copy the consoles additional info like line number, etc. - if you cant copy it without, just replace the additional info which should be able with every decent text editor)
5. call >python3 display-segments.py filename.txt
