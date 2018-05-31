# ipod2title

This tool renames media files by their title. This was written to make it easier to identify media moved from an iPod Classic to a PC. However, you can use this on any folder with media in it.

In that specific example, this is how you would use the tool.

1. Connect your iPod Classic to your PC. Open it as a mass storage device (like a USB drive).
2. After having made sure that you can view hidden files, open the iPod_Control/ folder.
3. Copy the Music/ folder to your desktop or whatever.
4. Right click the folder, properties, uncheck read-only and hidden. Click apply (use the all subdirectories and files option).
5. Run the ipod2title.py file as follows:
    ```
    python ipod2mp3.py /path/to/Music
    or
    python ipod2mp3.py C:\\Path\\to\\Music
     ```
     
Newly titled songs will be placed in the `/path/to/Music/titled/` directory.

The program will let you know at the end what files it could not rename. Typically this means that the file either:
- has no title
- is a duplicate

In the second case, you can just move the newly created `/path/to/Music/titled/` directory somewhere outside of the `/path/to/Music/` directory and run the program again.
