/**
 * Serial Duplex 
 * by Tom Igoe. 
 * 
 * Sends a byte out the serial port when you type a key
 * listens for bytes received, and displays their value. 
 * This is just a quick application for testing serial data
 * in both directions. 
 */


import processing.serial.*;

Serial myPort;      // The serial port
int whichKey = -1;  // Variable to hold keystoke values
int inByte = -1;    // Incoming serial data
byte init[] = new byte[4];
byte frame[] = new byte[4];

void setup() {
  size(400, 300);
  // create a font with the third font available to the system:
  PFont myFont = createFont(PFont.list()[2], 14);
  textFont(myFont);

  // List all the available serial ports:
  println(Serial.list());

  // I know that the first port in the serial list on my mac
  // is always my  FTDI adaptor, so I open Serial.list()[0].
  // In Windows, this usually opens COM1.
  // Open whatever port is the one you're using.
  String portName = Serial.list()[0];
  myPort = new Serial(this, portName, 19200);
  
  init[0] = 1;
  /*init[1] = ;
  init[2] = ;
  init[3] = ;*/
  
  frame[0] = 3;
  frame[1] = 0;
  frame[2] = 102;
  frame[3] = 96;
  //frame[3] = byte(frame[0] | frame[1] | frame[2]);
  
  myPort.write(init);
}

void draw() {
  background(0);
  text("Last Received: " + inByte, 10, 130);
}

void serialEvent(Serial myPort) {
  inByte = myPort.read();
}

void keyPressed() {
  // Send the keystroke out:
  if (key == 49 ){
  frame[0] = 3;
  frame[1] = 0;
  frame[2] = 1;
  frame[3] = 2;
  }
  if (key == 50 ){
  frame[0] = 3;
  frame[1] = 0;
  frame[2] = 2;
  frame[3] = 1;
  }
  if (key == 51 ){
  frame[0] = 3;
  frame[1] = 0;
  frame[2] = 4;
  frame[3] = 7;
  }
  if (key == 52 ){
  frame[0] = 3;
  frame[1] = 0;
  frame[2] = 8;
  frame[3] = 11;
  }
  if (key == 53 ){
  frame[0] = 3;
  frame[1] = 0;
  frame[2] = 16;
  frame[3] = 19;
  }
  if (key == 54 ){
  frame[0] = 3;
  frame[1] = 0;
  frame[2] = 32;
  frame[3] = 35;
  }
  if (key == 55 ){
  frame[0] = 3;
  frame[1] = 0;
  frame[2] = 64;
  frame[3] = 67;
  }
  if (key == 56 ){
  frame[0] = 3;
  frame[1] = 0;
  frame[2] = byte(128);
  frame[3] = byte(131);
  }
  myPort.write(frame);
  println(key);
}

