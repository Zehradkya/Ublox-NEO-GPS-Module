import time

# Dosya yolları
input_file = "gps_data.txt"
output_file = "gps_coordinates.js"

def gps_verilerini_js_olarak_yaz():
    try:
        while True:
            with open(input_file, "r") as file:
                lines = file.readlines()
                if lines:
                    last_line = lines[-1].strip()
                    if "LAT:" in last_line and "LNG:" in last_line:
                        try:
                            # Enlem ve boylamı ayrıştır
                            lat_start = last_line.find("LAT:") + 4
                            lng_start = last_line.find("LNG:") + 4
                            latitude = float(last_line[lat_start:last_line.find(",", lat_start)])
                            longitude = float(last_line[lng_start:])

                            # JavaScript dosyasına yaz
                            with open(output_file, "w") as js_file:
                                js_file.write(f"var currentLatitude = {latitude};\n")
                                js_file.write(f"var currentLongitude = {longitude};\n")
                            print(f"Güncel konum yazıldı: Enlem={latitude}, Boylam={longitude}")
                            time.sleep(5)  # Her 5 saniyede bir güncelle
                        except ValueError:
                            print("Hatalı GPS verisi atlandı.")
    except KeyboardInterrupt:
        print("GPS veri güncelleme işlemi durduruldu.")

if __name__ == "__main__":
    gps_verilerini_js_olarak_yaz()
