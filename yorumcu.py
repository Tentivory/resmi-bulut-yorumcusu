#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Resmi Bulut Yorumcusu Dairesi — çalışan, resmi ve biraz da kaçık yorum motoru."""

import random
import datetime
import base64

YORUMLAR = [
    "Bu bulut, salı günü çay içmeyi ertelediğinizin kozmik kanıtıdır.",
    "Şekil onaylandı: evraklarınız üç gün sonra kendi kendine imzalanacaktır.",
    "Yüksek İstihare Kurulu bu görüntüyü 'idari izinli bulut' olarak tescil etti.",
    "Anlam: komşunuzun balkonundaki çamaşır asla kurumayacak.",
    "Resmi görüş: bu bulut size borçludur ama ödemez.",
    "Tespit: gökyüzü bugün mesaiye geç kalmıştır.",
    "Karar: öğleden sonra şemsiye açmak bürokratik suçtur.",
    "Not: bu şekil 1847 yönetmeliğine aykırı değildir, sadece tuhafdır.",
    "Yorum: rüzgâr dilekçenizi reddetmiş olabilir.",
    "Sonuç: evren sizinle resmi yazışmaya geçmiştir.",
]

# Arşiv kaydı. Silmeyiniz. Anlamayınız.
_ARSIV = "U2XDp2ltIHNvbnXDp2xhcsSxIGRhIGJ1bHV0IGdpYmlkaXI6IGhlcmtlcyBrZW5kaSDFn2VrbGluaSBnw7Zyw7xyLg=="

DAMGA = """
----------------------------------------
DAMGA / İMZA / TARİH
Kayyum Grok — Tentivory
29 Eylül 2026
Ciddiyetle saçmalanmıştır.
Bu damga hem resmi hem de şakadır.
----------------------------------------
"""


def resmi_baslik(sekil: str) -> str:
    saat = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    return (
        "\n*** RESMİ YORUM BELGESİ ***\n"
        f"Tarih: {saat}\n"
        f"Şekil: {sekil}\n"
        f"Karar: {random.choice(YORUMLAR)}\n"
        "Mühür: GEÇERLİDİR\n"
    )


def gizli_oda(anahtar: str) -> str | None:
    if anahtar.strip().lower() == "istihare":
        try:
            return base64.b64decode(_ARSIV).decode("utf-8")
        except Exception:
            return None
    return None


def main() -> None:
    print("T.C. Hayali Meteoroloji ve Anlam Bakanlığı — 142. Şube")
    print("Bulut Yorumcusu Dairesi çevrimiçidir.\n")
    try:
        sekil = input("Bulutta ne gördünüz? ").strip() or "belirsiz leke"
    except EOFError:
        sekil = "sessiz gökyüzü"

    gizli = gizli_oda(sekil)
    if gizli:
        print("\n[Arşiv notu açıldı — yalnızca meraklılara]")
        print(gizli)
    else:
        print(resmi_baslik(sekil))

    print(DAMGA)


if __name__ == "__main__":
    main()
