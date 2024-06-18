### you can open csv files in tkinter on linux by follwing the given steps
1. clone the repository
2. store the csv_viewer.py file where you feel like storing it
3. edit the csv shell script file by add the path to the csv_viewer.py file
4. give the csv shell script exectecutable permissions by running `chmod +x csv` in the same directory as the csv shell script
5. copy the csv shell script to /usr/local/bin by running `cp csv /usr/local/bin`
6. copy the csv.desktop file to /usr/share/applications by running `cp csv.desktop /usr/share/applications`
7. run the command `sudo update-desktop-database /usr/share/applications/` to update the changes and you're done

i did this stuff just coz i didn't like opening csv files on my default spreadsheet viewer or on any of my text/code editors. the csv_viewer only shows the first and the last 25 rows of a csv file having 50 or more rows.

the only problem i think which exists is that after opening a csv file, a terminal is found opened in the background and i do not know how to fix it
