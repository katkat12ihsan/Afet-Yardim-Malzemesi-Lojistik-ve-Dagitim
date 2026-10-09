"""Veri erişim katmanı - veritabanı bağlantısı.

Hafta 3: yalnızca bağlantı noktası hazır.
Hafta 4: tablolar (şema scripti), ilişkiler/kısıtlar ve CRUD repository'leri
bu pakete eklenecek.
"""

import sqlite3

from backend import config


def baglanti_ac() -> sqlite3.Connection:
    """SQLite bağlantısı açar; yabancı anahtar kısıtlarını etkinleştirir."""
    config.VERI_KLASORU.mkdir(parents=True, exist_ok=True)
    baglanti = sqlite3.connect(config.VERITABANI_YOLU)
    baglanti.execute("PRAGMA foreign_keys = ON")  # SQLite'ta varsayılan kapalıdır
    baglanti.row_factory = sqlite3.Row
    return baglanti
