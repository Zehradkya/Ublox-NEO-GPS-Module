int deger = 0;
float voltaj = 0.0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  deger = analogRead(A0);  // A0 pininden analog değer oku
  voltaj = deger * 0.0048;  // Voltajı hesapla
  Serial.print("Okunan Deger: ");
  Serial.print(deger);
  Serial.print(" - Voltaj: ");
  Serial.print(voltaj);
  Serial.println(" V");
  delay(1000);
}
