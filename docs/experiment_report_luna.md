# Ringkasan eksperimen A–F: 25 pertanyaan (gpt-6-luna, reasoning_effort=high, 3 repetisi)

## Proses

- **Tujuan:** membandingkan akurasi `gpt-6-luna` (reasoning_effort=high) dengan baseline `gpt-4.1` (3 repetisi) pada benchmark yang sama: 6 arm × 25 pertanyaan, snapshot `ZOMATO_DLR`.
- **Setup:** model `gpt-6-luna`, reasoning_effort=high. Setiap kombinasi 25 pertanyaan × 6 arm dijalankan **3 kali (rep1–rep3)** = **450 attempt** total. Teks pertanyaan, snapshot, dan batas query identik dengan run gpt-4.1.
- **Run:** 21 Oktober 2026; **450/450 selesai** (semua status `completed`). Attempt tersimpan di direktori `af_25_luna_rep1`, `af_25_luna_rep2`, `af_25_luna_rep3`.
- **Rubrik skor:** sama dengan run v2. Toleransi: ±INR 0,01 total uang; ±0,01 pp untuk rate/share/perubahan persen; ±0,01 untuk average dan korelasi; ±INR 0,05 per komponen dekomposisi Q20; integer dan identitas eksak. Q22–Q24 arm A–E = 0 (aturan eligibility hanya ada di F).
- **Grade:** `af_25_luna_grades.json` menyimpan skor per attempt dengan struktur `{luna_rep1, luna_rep2, luna_rep3, luna_mean, luna_std}` untuk setiap 150 kombinasi arm × pertanyaan.

## Hasil

### Perbandingan per arm — mean ± std (dari 3 repetisi)

| Arm | gpt-4.1 mean/25 (±std) | gpt-6-luna mean/25 (±std) | Delta |
| --- | ---: | ---: | ---: |
| A | 11,67 ± 0,58 | 19,33 ± 0,47 | +7,67 |
| B | 15,67 ± 0,58 | 21,00 ± 0,00 | +5,33 |
| C | 16,33 ± 0,58 | 21,67 ± 0,47 | +5,33 |
| D | 16,33 ± 0,58 | 21,67 ± 0,47 | +5,33 |
| E | 17,33 ± 1,15 | 22,00 ± 0,00 | +4,67 |
| F | 19,00 ± 0,00 | 25,00 ± 0,00 | +6,00 |
| **Total** | **96,33 ± —** | **130,67 ± 0,47** | **+34,33** |

> gpt-6-luna mendapat rata-rata **130,67/150** (130 / 131 / 131 per repetisi) vs rata-rata **96,3/150** dari gpt-4.1; kenaikan **+34,3 poin** (+36%).

### Skor per repetisi

| Arm | rep1 | rep2 | rep3 | mean | std |
| --- | ---: | ---: | ---: | ---: | ---: |
| A | 19 | 19 | 20 | 19,33 | 0,47 |
| B | 21 | 21 | 21 | 21,00 | 0,00 |
| C | 21 | 22 | 22 | 21,67 | 0,47 |
| D | 22 | 22 | 21 | 21,67 | 0,47 |
| E | 22 | 22 | 22 | 22,00 | 0,00 |
| F | 25 | 25 | 25 | 25,00 | 0,00 |
| **Total** | **130** | **131** | **131** | **130,67** | **0,47** |

## Analisis varians antar repetisi

### Pertanyaan yang konsisten (std = 0,00) — 144/150

Seluruh 150 kombinasi kecuali 6 berikut memberikan skor yang sama di ketiga repetisi. Ini mencerminkan determinisme tinggi dari gpt-6-luna reasoning_effort=high: pertanyaan-pertanyaan data murni (Q01–Q06, Q08–Q17, Q19, Q21, Q23–Q25 di arm B/E/F) menghasilkan jawaban identik.

### Pertanyaan yang bervariasi (std > 0) — 6/150

| Key | rep1 | rep2 | rep3 | mean | Deskripsi varians |
| --- | ---: | ---: | ---: | ---: | --- |
| A-Q02 | 0 | 0 | 1 | 0,33 | rep1–rep2: klarifikasi GMV (SUBTOTAL vs SALES_AMOUNT); rep3: menjawab dengan SALES_AMOUNT benar |
| A-Q07 | 1 | 0 | 1 | 0,67 | rep2: klarifikasi basis GMV sebelum menghitung % perubahan; rep1+rep3: langsung menjawab benar |
| A-Q08 | 1 | 1 | 0 | 0,67 | rep3: klarifikasi (SUBTOTAL vs SALES_AMOUNT untuk GMV kota); rep1+rep2: langsung benar |
| A-Q12 | 0 | 1 | 1 | 0,67 | rep1: klarifikasi definisi GMV; rep2+rep3: menjawab langsung dengan benar |
| C-Q07 | 0 | 1 | 1 | 0,67 | rep1: query salah (menampilkan 7.471 Jan bukan 286.712); rep2+rep3: benar |
| D-Q25 | 1 | 1 | 0 | 0,67 | rep3: query gagal (no rows), melaporkan Bangalore bukan Hyderabad; rep1+rep2: benar |

**Pola varians:**
- 5 dari 6 pertanyaan bervariansi berada di Arm A (arm dengan layer paling minimal: hanya SQL source/staging). Ini menunjukkan bahwa ambiguitas GMV (SUBTOTAL vs SALES_AMOUNT) di layer staging menyebabkan gpt-6-luna kadang meminta klarifikasi dan kadang mengasumsikan SALES_AMOUNT.
- C-Q07 dan D-Q25 menunjukkan kegagalan query stokastik: query mengenai subpopulasi yang salah (rep1 C-Q07) atau query mengembalikan no rows (rep3 D-Q25), bukan karena pilihan interpretasi model.
- Arm B, E, F: **nol varians** — seluruh 25 × 3 = 75 attempt menghasilkan skor identik.

## Detail per arm

**A (source/staging) — mean 19,33 ± 0,47:**
- Luna konsisten gagal di Q18 (tidak ada label segmen usia) dan Q22–Q24 (tanpa aturan bisnis).
- Luna **tidak konsisten** di Q02, Q07, Q08, Q12 — tergantung apakah model memilih mengklarifikasi definisi GMV atau langsung menggunakan SALES_AMOUNT.
- Luna **berhasil** di Q03 (AOV pakai SALES_AMOUNT), Q09, Q10, Q13, Q14, Q16, Q19, Q20, Q25.

**B (+intermediate) — mean 21,00 ± 0,00 (sempurna konsisten):**
- Luna gagal di Q18, Q22–Q24 di semua repetisi.
- **Nol varians** di semua 25 pertanyaan.

**C (+core) — mean 21,67 ± 0,47:**
- rep1 gagal di Q07 (query anomali). rep2+rep3 benar.
- Luna gagal di Q22–Q24 di semua repetisi.

**D (+marts) — mean 21,67 ± 0,47:**
- rep3 gagal di Q25 (query no rows). rep1+rep2 benar.
- Luna gagal di Q22–Q24 di semua repetisi.

**E (+MetricFlow) — mean 22,00 ± 0,00 (sempurna konsisten):**
- Luna gagal di Q22–Q24 di semua repetisi.
- **Nol varians** di semua 25 pertanyaan.

**F (+business glossary) — mean 25,00 ± 0,00 (sempurna di semua repetisi):**
- **Sempurna di ketiga repetisi.** 25/25 di rep1, rep2, dan rep3.
- **Nol varians** di semua 25 pertanyaan.

## Analisis per pertanyaan: perbedaan signifikan

### Luna menang (mean ≥ 0,67) di mana gpt-4.1 selalu gagal (mean 0,00)

| Key | Pertanyaan | Luna mean | Catatan |
| --- | --- | ---: | --- |
| A-Q07, B-Q07, C-Q07, D-Q07, E-Q07, F-Q07 | Perubahan % count Jan→Des | 0,67–1,00 | Luna menghitung +33,7684% persis; gpt-4.1 gagal di semua arm |
| A-Q08, A-Q09, A-Q10, A-Q25 | Kota order, cancellation rate, delivery time | 0,67–1,00 | Arm A: luna menemukan data di layer source/staging |
| A/B/C/D/E-Q13 | Cuisine label dengan total order | 1,00 | Luna menggunakan semua order sebagai denominator cancellation |
| A/B/C/D/E/F-Q14 | Veg share 72,584811% | 1,00 | Luna menghitung dengan denominator tiga kelompok |
| B/C/D-Q16 | Reconciliasi item amount | 1,00 | Luna melaporkan 21.466 baris, INR 23.791 |
| A/B/C/D/E/F-Q20 | Dekomposisi GMV Jan→Feb | 1,00 | Luna menghitung count effect −8.768.368,61 dan AOV effect −390.829,39 persis |
| D-Q19, F-Q19 | Rata-rata Delivered per hari weekday | 1,00 | Luna benar di semua repetisi |
| A/D/E/F-Q25 | Hyderabad vs overall delivery time | 0,67–1,00 | Luna selalu menyertakan nilai delivery time |

### Luna kalah (mean < 1,00) di mana gpt-4.1 berhasil (mean > 0,5)

| Key | Luna mean | gpt-4.1 mean | Catatan |
| --- | ---: | ---: | --- |
| A-Q02 | 0,33 | ~1,00 (B/C/D) | Luna meminta klarifikasi definisi GMV di Arm A (2/3 repetisi) |
| A-Q07 | 0,67 | 1,00 (D/E/F) | Luna meminta klarifikasi GMV di rep2 |
| A-Q08 | 0,67 | ~0 (arm A) | Luna klarifikasi di rep3 (tapi gpt-4.1 juga gagal di arm A) |
| A-Q12 | 0,67 | ~0 (arm A) | Luna klarifikasi di rep1 (tapi gpt-4.1 juga gagal di arm A) |

## Efisiensi langkah (steps)

| Metrik | gpt-4.1 (estimasi) | gpt-6-luna (mean 3 rep) |
| --- | --- | --- |
| Attempt dengan 1 langkah (klarifikasi) | ~0 | ~14 per rep |
| Semua 1-langkah = klarifikasi? | N/A | Ya, 100% |
| Attempt dengan 2 langkah | Sebagian besar | Mayoritas pertanyaan data |
| Attempt dengan 3+ langkah | Sebagian besar kompleks | Q20, Q21, Q25, beberapa lainnya |

**Konsistensi klarifikasi:** Pattern permintaan klarifikasi luna stabil antar repetisi kecuali di Arm A Q02/Q07/Q08/Q12 (definisi GMV), yang menunjukkan stokastisitas marginal di batas ambiguitas. Q18 (tidak ada label segmen) dan Q22–Q24 (tidak ada aturan bisnis) selalu menghasilkan klarifikasi.

## Pembelajaran

1. **gpt-6-luna (reasoning_effort=high) sangat stabil antar repetisi.** Dari 150 kombinasi arm × pertanyaan, hanya 6 (4%) menunjukkan varians di 3 repetisi. Std keseluruhan hanya 0,47 poin/repetisi.

2. **Arm F sempurna dan deterministik.** 25/25 di ketiga repetisi — nol variasi. Kombinasi business glossary + reasoning_effort=high sepenuhnya menyelesaikan benchmark.

3. **Varians Arm A terpusat pada ambiguitas definisi GMV.** 4 dari 6 pertanyaan bervariansi adalah Arm A Q02/Q07/Q08/Q12, di mana model kadang mengklarifikasi "SUBTOTAL vs SALES_AMOUNT?" dan kadang langsung menggunakan SALES_AMOUNT. Ini bukan kesalahan data — justru perilaku yang tepat dalam konteks ambiguitas. Untuk produksi, prompt Arm A perlu mendefinisikan GMV secara eksplisit.

4. **C-Q07 dan D-Q25 adalah kegagalan query stokastik, bukan interpretasi.** Masing-masing muncul hanya 1 dari 3 kali. Anomali ini sulit dideteksi tanpa repetisi — justifikasi utama untuk menjalankan ≥3 repetisi.

5. **Kenaikan total vs gpt-4.1 adalah +34,3 poin (+36%).** Luna mencapai 130,67/150 mean vs 96,3/150 gpt-4.1. Keunggulan konsisten di semua arm.

6. **gpt-6-luna secara substansial lebih akurat pada pertanyaan presisi tinggi.** Q07 (±0,01pp), Q14 (denominator tiga kelompok), Q20 (dekomposisi ±INR 0,05) — yang gagal di hampir semua arm gpt-4.1 — berhasil dengan mean 0,67–1,00 di luna.

## Kesimpulan

- **gpt-6-luna (reasoning_effort=high) secara substansial mengungguli gpt-4.1** pada benchmark 25-pertanyaan × 6-arm ini: mean 130,67/150 vs 96,3/150, kenaikan +34,3 poin.
- **Reprodusibilitas tinggi:** std hanya 0,47 poin/repetisi dari 3 run. Model ini sangat deterministik untuk pertanyaan data.
- **Arm F sempurna** (25/25 × 3 rep = 75/75): tidak ada pertanyaan yang gagal saat business glossary tersedia, di satu pun repetisi.
- **Satu-satunya variasi bermakna** ada di Arm A (definisi GMV ambigu) dan kegagalan query stokastik di C-Q07/D-Q25. Ini dapat diatasi dengan: (a) mendefinisikan GMV eksplisit di prompt Arm A, (b) memvalidasi query sebelum menjawab.
- Grade tersimpan di [`af_25_luna_grades.json`](../experiments/run.local/af_25_luna_grades.json) dengan struktur `{luna_rep1, luna_rep2, luna_rep3, luna_mean, luna_std}` per kombinasi.
