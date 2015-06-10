Edison-KWJ

To configure the edison for Tox and Tor sensor:
	1. Flash the edison with latest image.
		http://www.intel.com/support/edison/sb/CS-035286.htm
	2. connect to wifi.
		configure_edison --wifi
	3.Install / update the mraa :
		Install first:

		echo "src mraa-upm http://iotdk.intel.com/repos/1.1/intelgalactic" > /etc/opkg/mraa-upm.conf
		opkg update
		opkg install libmraa0

		update with latest:
		
		echo "src mraa-upm http://iotdk.intel.com/repos/1.1/intelgalactic-dev" > /etc/opkg/mraa-upm.conf
		opkg update
		opkg install libmraa0
	4. git clone https://djain@stash.ndg.intel.com/scm/edisonkwj/edison-kwj.git
		

To Run the Briza for all 4 modules:

	1. Run the briza_eeprom.py to flash the eeprom with details.
		>> python briza_eeprom.py 0x53 0x55 0x56 0x57
	2. Run the briza.py to see the values from all sensors.
		>> python briza.py 0x53 0x55 0x56 0x57

NOTE: In briza.py : function other_sensor() is diasbled for now to test the Gas sensors.
      if wanted to check see the avlues of LPH, HDC sensor enable the other_sensor() in while loop.
      0x53, 0x55,0x56, 0x57 are the default board addresses. please specify the correct board address and in sequence of
      board1, board2 board3, board4

