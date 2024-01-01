# History-candle-figure-of-Specific-Stock
A program provides the history data of a specific stock serial. And it automatically creates a candle figure to show the trend.
It uses Selenium and tkinter, the former is to get the history data from TWSE(Taiwan Stock Exchange Corporation) website and 
the latter is the UI to enter the Year、Month、Serial number you want.
The TWSE website itself and there are two comboboxes to select the year and month and one enter column to type the stock serial you want.  
![image](https://github.com/Yorkxe/History-candle-figure-of-Specific-Stock/blob/main/TWSE.PNG)
After entering the Year、Month、Serial, the data we want show up.
![image](https://github.com/Yorkxe/History-candle-figure-of-Specific-Stock/blob/main/Data.PNG)
The program will auotmatically get these data and making the candle figure.

Procedure:
1.
The tkinter UI will show and it simulates the enter gird like TWSE website to enter the year/month/stock serial.
![image](https://github.com/Yorkxe/History-candle-figure-of-Specific-Stock/blob/main/Procedure%201.PNG)
2.
After sending the year/month/stock serial, the program will make the candle figure according the year/month/stock serial
we have sended.
![image](https://github.com/Yorkxe/History-candle-figure-of-Specific-Stock/blob/main/The%20candle%20figure.PNG)
What if you send the wrong serial number the data the stocked hasn't listed, an alert UI will pop out to remind you that the info you
typed is wrong.

![image](https://github.com/Yorkxe/History-candle-figure-of-Specific-Stock/blob/main/No%20such%20data!!.PNG)
