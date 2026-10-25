# Ringkasan eksperimen A–F: 25 pertanyaan (gpt-4.1, 3 repetisi)

## Proses

- **Tujuan:** mengukur perubahan akurasi jawaban saat akses agent ditambah bertahap: A = source/staging, B = +intermediate, C = +core, D = +marts, E = +19 metric MetricFlow, F = +business glossary. Akses SQL dari layer sebelumnya tetap tersedia di setiap arm.
- **Setup:** satu model `gpt-4.1`, temperature 0, seed 20261021. Setiap kombinasi 25 pertanyaan × 6 arm dijalankan **3 kali (repetisi)** = **450 attempt**. Semua memakai snapshot `ZOMATO_DLR`, teks pertanyaan yang sama, dan batas query yang sama.
- **Run:** 21 Oktober 2026; **450/450 selesai** (status `completed`). Repetisi disimpan di `af_25_v2_rep1`, `af_25_v2_rep2`, `af_25_v2_rep3`. Agent tidak menerima [jawaban referensi](../experiments/answers_25.md).
- **Penilaian:** skor resmi berasal dari [`scripts/autograde.py`](../scripts/autograde.py), yang memeriksa jawaban akhir terhadap nilai referensi di [`gold_25_results.json`](../experiments/gold_25_results.json) (hasil menjalankan ulang gold SQL pada 25 Oktober 2026; sama dengan `answers_25.md`). Aturan yang sama dipakai untuk semua attempt. Toleransi: ±INR 0,01 untuk total uang; ±0,01 percentage point untuk rate, share, dan perubahan persen; ±0,01 unit untuk average dan korelasi; ±INR 0,05 untuk tiap komponen dekomposisi Q20; integer count dan identitas eksak. Klarifikasi dan query gagal bernilai 0. Q22–Q24 memerlukan aturan bisnis yang hanya diberikan ke F, sehingga bernilai 0 di A–E.
- **Koreksi atas penilaian manual awal:** 13 dari 450 nilai manual berbeda dari skor ini dan sudah diganti (daftar di [`experiments/README.md`](../experiments/README.md)). Sebelas nilai manual terlalu longgar dan dua terlalu ketat.
- **Statistik:** mean ± simpangan baku **sampel** (n−1) dari 3 total per repetisi.

## Hasil

| Arm | Data benar (mean ± std / 22) | Kebijakan benar (mean ± std / 3) | Total benar (mean ± std / 25) |
| --- | ---: | ---: | ---: |
| A | 11,33 ± 0,58 | 0,00 ± 0,00 | 11,33 ± 0,58 |
| B | 14,00 ± 1,00 | 0,00 ± 0,00 | 14,00 ± 1,00 |
| C | 16,67 ± 1,15 | 0,00 ± 0,00 | 16,67 ± 1,15 |
| D | 16,33 ± 0,58 | 0,00 ± 0,00 | 16,33 ± 0,58 |
| E | 16,67 ± 0,58 | 0,00 ± 0,00 | 16,67 ± 0,58 |
| F | 15,33 ± 0,58 | 3,00 ± 0,00 | **18,33 ± 0,58** |

Total semua arm: **93,33 / 150** (92, 94, 94 per repetisi; std 1,15).

Pertanyaan data yang tidak dijawab benar di setiap repetisi. Angka dalam kurung adalah skor rep1 rep2 rep3:

| Arm | Pertanyaan yang gagal |
| --- | --- |
| A | Q07, Q08, Q09, Q10, Q12, Q13, Q14, Q18, Q20, Q25 (000); Q15 (010) |
| B | Q07, Q12, Q13, Q14, Q16, Q18, Q20 (000); Q09 (101), Q15 (011), Q17 (101) |
| C | Q07, Q13, Q14, Q16 (000); Q09 (011), Q20 (001), Q21 (101) |
| D | Q07, Q14, Q19, Q20, Q25 (000); Q21 (010) |
| E | Q07, Q14, Q20, Q25 (000); Q05 (110), Q08 (101), Q09 (110), Q12 (011) |
| F | Q07, Q12, Q14, Q15, Q19, Q20 (000); Q25 (010) |

## Pola yang terlihat

- **Q07 dan Q14 gagal di semua 18 attempt masing-masing; Q20 gagal di 17 dari 18.** Dalam jawaban akhir model menghitung persentase dan share dengan hitungan manual, bukan dari hasil SQL. Contohnya Q07 melaporkan kenaikan count 33,732% (benar 33,7684%) dan Q14 melaporkan share Veg 72,5739% (benar 72,5848%). Ini kesalahan aritmetika model, bukan kekurangan akses data.
- **Q12 gagal di 10 attempt** (A, B, dan F di semua repetisi; E di satu repetisi). Contoh: model menulis top-ten GMV 3.552.107 padahal sepuluh nilai yang ia tulis sendiri berjumlah 3.552.103.
- **Q13 gagal di A, B, dan C di semua repetisi:** total order dan cancellation rate per cuisine tidak sesuai kunci; D, E, dan F memperbaikinya.
- **Q18 gagal di A dan B** karena label age segment ada di `DIM_CUSTOMER` (layer core), yang belum tersedia di kedua arm itu.
- **Q22–Q24:** hanya F yang menjawab benar (3/3 di semua repetisi), berkat aturan `rating_count >= 100`, geografi restoran, dan definisi repeat customer. Tidak ada jawaban A–E yang cocok dengan kunci walau skor 0 tidak dipaksakan.
- **Variasi antar repetisi** terbesar ada di C (std 1,15) dan B (std 1,00), terutama dari Q09, Q15, Q17, Q20, dan Q21.

## Kesimpulan dan batas

- Pada **satu model, satu dataset, dan tiga repetisi**, skor total naik dari A (11,33) ke B (14,00) ke C (16,67), lalu datar di D dan E (16,33 dan 16,67). F menambah 3 poin dari pertanyaan kebijakan, sementara skor data F (15,33) lebih rendah daripada C–E karena Q12, Q15, dan Q19 gagal di F di semua repetisi.
- Selisih C, D, dan E (0,33 poin) lebih kecil daripada simpangan baku antar repetisi (0,58–1,15), jadi urutan ketiganya tidak dapat disimpulkan.
- **Keterbatasan:** (1) satu model; (2) tiga repetisi belum cukup untuk estimasi ketidakpastian yang kuat; (3) rubrik ±0,01 pp untuk persentase menuntut aritmetika presisi tinggi yang sulit bagi model tanpa alat hitung; (4) kunci referensi dan pertanyaan berasal dari penulis yang sama.
- Langkah lanjutan yang masuk akal: alat kalkulasi atau instruksi agar menghitung persentase di SQL (Q07, Q12, Q14, Q20), uji model lain, dan tambah repetisi untuk pertanyaan yang bervariasi.
- Trace lengkap ada di `experiments/run.local/af_25_v2_rep{1,2,3}/`. Skor tersimpan di [`af_25_v2_grades.json`](../experiments/run.local/af_25_v2_grades.json).
