import serial

# Seri port ayarları
SERIAL_PORT = "/dev/cu.usbserial-130"  # port no
BAUD_RATE = 9600
OUTPUT_FILE = "gps_data.txt"

def gps_verisi_yaz():
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print("GPS verisi alınıyor... (Çıkış için Ctrl+C)")

        while True:
            line = ser.readline().decode('utf-8').strip()
            if "LAT:" in line and "LNG:" in line:  # GPS verisini ayrıştırma
                lat_start = line.find("LAT:") + 4
                lng_start = line.find("LNG:") + 4
                latitude = line[lat_start:line.find(",", lat_start)]
                longitude = line[lng_start:]

                # gps_data.txt dosyasına yazma
                with open(OUTPUT_FILE, "w") as file:
                    file.write(f"{latitude},{longitude}")
                print(f"Güncellendi: Enlem={latitude}, Boylam={longitude}")
    except KeyboardInterrupt:
        print("İşlem durduruldu.")
    except serial.SerialException as e:
        print(f"Seri port hatası: {e}")
    finally:
        if 'ser' in locals():
            ser.close()

if __name__ == "__main__":
    gps_verisi_yaz()
