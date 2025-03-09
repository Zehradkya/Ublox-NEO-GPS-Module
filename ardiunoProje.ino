#include <SoftwareSerial.h>
#include <TinyGPS++.h>

SoftwareSerial gpsSerial(4, 3); // RX, TX
TinyGPSPlus gps;

void setup() {
  Serial.begin(9600);       // Arduino seri port hızı
  gpsSerial.begin(9600);    // GPS modülü seri port hızı
}

void loop() {
  while (gpsSerial.available() > 0) {
    if (gps.encode(gpsSerial.read())) {
      if (gps.location.isUpdated()) {
        float latitude = gps.location.lat();
        float longitude = gps.location.lng();
        Serial.print("LAT: ");
        Serial.print(latitude, 6);
        Serial.print(", LNG: ");
        Serial.println(longitude, 6);
      }
    }
  }
}
