Project 1- Local QT based UI by Anay Gondhalekar
For Course Embedded Interface Design 5053-002 

This project demonstrates development of a rapid prototype of a stand-alone temperature and humidity monitoring device with a local user interface.The project also lets you create the standard class setup for RPi3 and other hardware and system elements, DHT22 Temp/Hum Sensor, Raspbian (Debian) Linux, QT5, Python 3.x and your display (direct OR a laptop via a Remote Desktop or VNC connection)

Name of Owner: Anay Gondhalekar

Installation Instructions: 
1. Download the Project 1 on your Raspberry Pi machine with Raspbian loaded on it.
2. Connect the Rpi and set it up. Connect the DHT22 to Vcc/ Ground and 4th pin of Rpi. Make sure you put a 4.7k to 10k resistor across the pins of DHT22 sensor.
3. Make sure Python3 is installed on your device.
4. Fromt the downloaded folder ,go to the Sources folder and run the Login.py file with the command- python3 Login.py
5. A Login authentication window will open up, if put the correct password; i.e. anayanay, a new window will open up to see the temperature and humidity values.
6. If an incorrect password is shown, the prompt shows a warning and exits gracefully. 
7. Once a correct password is put and the main window opens, click the refresh button to get values of temperature and humidity.
8. Use Cel/Fah conversion button to convert between Celcius and Fahrenheit.
9. You can observe the Sensor connectivity and Alerts as change of various parameters.
10. Close the window when done to gracefully exit the application.

Project Work: Entire work by Anay Gondhalekar

Project Additions:
1. Login window to access the application with a secure password.
2. Celcius to Fahrenheit conversion with one click button.
3. Alarm for High and Low Temperature as well as extreme Humidity conditions.

Citations:
Adafruit DHT library: https://github.com/adafruit/Adafruit_Python_DHT
ProgrammingKnowledge Youtube channel: https://www.youtube.com/watch?v=Sf-Vr-1q5UA
For PyQt5 widgets: http://zetcode.com/gui/pyqt5/widgets/
Professor Bruce R Montgomary's Lecture slides and files for subject EID 5053-002 at University of Colorado,Boulder.
