import os
import json
import requests
from pathlib import Path

class AdService:
    def __init__(self):
        self.api_url = "https://tuapi.com/api/ads"
        self.local_dir = Path("assets/ads")
        self.config_path = Path("config/ads_config.json")
        self.local_dir.mkdir(parents=True, exist_ok=True)

    def sync_ads(self):
        try:
            response = requests.get(self.api_url, timeout=10)
            if response.status_code != 200:
                print("No se pudo sincronizar con el servidor")
                return

            ads = response.json()  # [{"filename": "...", "url": "...", "type": "image"|"video"}, ...]

            for ad in ads:
                local_file = self.local_dir / ad["filename"]
                if not local_file.exists():
                    print(f"Descargando {ad['filename']}...")
                    content = requests.get(ad["url"]).content
                    with open(local_file, "wb") as f:
                        f.write(content)

            # Guardar metadatos para el reproductor
            with open(self.config_path, "w") as f:
                json.dump(ads, f)

        except Exception as e:
            print("❌ Error sincronizando publicidad:", e)
