import requests
from bs4 import BeautifulSoup
import serial
import time

def get_temperature_dubai():
    # URL of the weather website to scrape
    url = "https://www.timeanddate.com/weather/united-arab-emirates/dubai"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Find the temperature data in the HTML (adjust selector if necessary)
        temp_element = soup.find("div", class_="h2")
        temperature = temp_element.text.strip()
        
        # Extract only the temperature as an integer (e.g., "34°C" -> "34")
        temperature_value = int("".join(filter(str.isdigit, temperature)))
        return temperature_value
    
    except Exception as e:
        print(f"Error retrieving temperature: {e}")
        return None

if __name__ == "__main__":
    
    # Set up serial communication on COM4
    ser = serial.Serial('COM5', 9600) # Replace COM4 with your own serial port number where Arduino is connected
    time.sleep(2)  # Wait for the serial connection to initialize
    
    try:
        while True:
            # Get the fields value
            temperature = get_temperature_dubai()
            if temperature is not None:
                # Send field_value to serial port as string with newline and carriage return
                ser.write((f'Dubai: {temperature}' + '\r\n').encode())
                print(f'Dubai: {temperature}')
            else:
                print("Failed to retrieve data.")
            
            time.sleep(5)  # Wait for 5 seconds before the next request

    except KeyboardInterrupt:
        print("Program interrupted by user.")
        
    finally:
        ser.close()  # Close the serial connection when done
    

