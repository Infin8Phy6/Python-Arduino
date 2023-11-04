import tkinter as tk
import serial

# Define the serial port and baud rate (adjust these values to match your Arduino setup)
port = "COM16"  # Replace with the actual serial port
baud_rate = 9600  # Match the baud rate set in your Arduino sketch

# Open the serial connection
ser = serial.Serial(port, baud_rate, timeout=1)

# Function to toggle the state of pin 13
def toggle_led():
    ser.write(b"TOGGLE_PIN13")  # Send a command to toggle pin 13
    response = ser.readline().decode().strip()  # Read the response
    status_label.config(text=f"LED Status: {response}")

# Create the Tkinter window
window = tk.Tk()
window.title('Arduino Control')

# Create a toggle button
toggle_button = tk.Button(window, text='Toggle LED', command=toggle_led)
toggle_button.pack(pady=20)

# Create a label to display LED status
status_label = tk.Label(window, text='LED Status: OFF')
status_label.pack()

# Function to close the serial connection and exit the application
def close_serial_and_exit():
    ser.close()
    window.destroy()

# Create an exit button
exit_button = tk.Button(window, text='Exit', command=close_serial_and_exit)
exit_button.pack()

window.mainloop()

#copy and paste it to your arduino coding platform then upload to the module

int ledPin = 13;
bool isLedOn = false;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    command.trim();

    if (command == "TOGGLE_PIN13") {
      isLedOn = !isLedOn;  // Toggle the LED state
      digitalWrite(ledPin, isLedOn ? HIGH : LOW);  // Turn on or off based on the state
      Serial.println(isLedOn ? "ON" : "OFF");
    }
  }
}
