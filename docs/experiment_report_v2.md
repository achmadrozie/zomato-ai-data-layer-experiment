# Ringkasan eksperimen A–F: 25 pertanyaan (run v2, 3 repetisi)

## Proses

- **Tujuan:** mengukur perubahan akurasi jawaban saat akses agent ditambah bertahap: A = source/staging, B = +intermediate, C = +core, D = +marts, E = +19 metric MetricFlow, F = +business glossary. Akses SQL dari layer sebelumnya tetap tersedia di setiap arm.
- **Setup:** satu model `gpt-4.1`, temperature 0, seed 20261021. Setiap kombinasi 25 pertanyaan × 6 arm dijalankan **3 kali (repetisi)** = **450 attempt** total. Semua memakai snapshot `ZOMATO_DLR`, teks pertanyaan yang sama, dan batas query yang konsisten.
- **Run:** 21 Oktober 2026; **450/450 selesai** (status `completed`). Repetisi disimpan di direktori `af_25_v2_rep1`, `af_25_v2_rep2`, `af_25_v2_rep3`. Agent tidak menerima [jawaban referensi](../experiments/answers_25.md).
- **Rubrik skor:** jawaban akhir harus benar pada *semua* angka, populasi, unit, dan interpretasi. Toleransi: ±INR 0,01 untuk total uang; ±0,01 percentage point untuk rate, share, dan perubahan persen; ±0,01 unit untuk average dan korelasi; ±INR 0,05 untuk tiap komponen dekomposisi Q20; integer count dan identitas eksak. Q01–Q21 dan Q25 adalah pertanyaan data; Q22–Q24 memerlukan aturan bisnis yang hanya diberikan ke F. Arm A–E di Q22–Q24 dinilai 0 karena tidak memiliki aturan eligibility standard market.
- **Skor mean ±std** dihitung dari 3 nilai (0 atau 1) tiap arm×pertanyaan di atas tiga repetisi.

## Hasil

| Arm | Data benar (mean±std / 22) | Kebijakan benar (mean±std / 3) | Total benar (mean±std / 25) |
| --- | ---: | ---: | ---: |
| A | 11,67 ± 0,58 | 0,00 ± 0,00 | 11,67 ± 0,58 |
| B | 15,67 ± 0,58 | 0,00 ± 0,00 | 15,67 ± 0,58 |
| C | 16,33 ± 0,58 | 0,00 ± 0,00 | 16,33 ± 0,58 |
| D | 16,33 ± 0,58 | 0,00 ± 0,00 | 16,33 ± 0,58 |
| E | **17,33 ± 1,15** | 0,00 ± 0,00 | **17,33 ± 1,15** |
| F | 16,00 ± 0,00 | **3,00 ± 0,00** | **19,00 ± 0,00** |

**Catatan per arm:**

- **A (source/staging):** 11–12 benar per repetisi. Gagal pada Q08 (menggunakan granular city bukan kota agregat), Q09 (Bikaner bukan Hyderabad), Q10 (tidak menemukan data delivery duration), Q13 (total order salah, hanya Delivered), Q14 (share unit salah), Q18 (pakai usia numerik, bukan label segmen), Q25 (Bikaner).
- **B (+intermediate):** 15–16 benar. Mengalami inkonsistensi di Q13 (total order masih salah), Q14 (share unit), Q16 (filter INR menghasilkan 14.321 bukan 21.466 perbedaan), Q18 (beberapa rep menggunakan segmen income bukan age).
- **C (+core):** 16–17 benar. Core membawa label age segment yang benar (Q18). Q16 gagal karena filter INR. Q20 hanya benar di rep3 (dekomposisi eksak dengan AOV presisi tinggi).
- **D (+marts):** 16–17 benar. Marts membawa label segmen yang tepat dan Q13 benar (memakai total order benar). Q19 gagal semua rep karena merata-ratakan data mart city-hari bukan total order per hari.
- **E (+MetricFlow):** 16–18 benar. Arm terbaik untuk pertanyaan data. Q05 gagal di rep3 (query error). Q09 gagal di rep3 (timeout). Variasi antar-rep tertinggi (std 1,15).
- **F (+glossary):** 16 data benar + 3 kebijakan benar = total terbaik 19/25. Sempurna di Q22–Q24 berkat aturan `rating_count >= 100`. Q19 gagal semua rep (salah hitung rata-rata per hari weekday), Q20 gagal (dekomposisi dengan AOV tidak presisi), Q25 gagal (delivery Hyderabad tidak dikueri secara eksplisit di rep1 dan rep3).

**Pertanyaan yang tidak bisa dijawab oleh semua arm:**
- **Q07:** Seluruh arm melaporkan perubahan count ~33,73%–33,75%, sementara kunci membutuhkan 33,7684% (±0,01pp). Selisih terkecil masih ~0,018pp di luar toleransi. Semua arm membuat kesalahan hitung aritmetika saat menghitung perubahan persentase count.
- **Q14:** Semua arm melaporkan share Veg ~72,57%–72,63%, sementara kunci 72,584811%. Sebagian besar meleset ~0,04–0,04pp di luar toleransi ±0,01pp.
- **Q20:** Hampir semua arm membuat kesalahan aritmetika pada perkalian komponen dekomposisi (melaporkan −8.771.964 alih-alih −8.768.368 untuk count effect). Hanya C-rep3 yang mendapat nilai tepat.

## Pembelajaran

1. **Akses layer yang lebih tinggi membantu secara bertahap untuk sebagian pertanyaan.** Q08 (kota order), Q13 (total order per cuisine), Q18 (label age segment) menunjukkan kenaikan yang jelas dari A ke C/D. Arm A gagal pada pertanyaan yang membutuhkan join dimensi atau label dari mart.
2. **Kesalahan hitung di jawaban akhir tetap dominan.** Q07, Q14, Q20 gagal di semua arm karena kesalahan aritmetika numerik, bukan karena akses data. Ini menunjukkan limitasi model dalam melakukan kalkulasi presisi tinggi pada saat merangkum jawaban.
3. **MetricFlow (E) memberi manfaat terbesar pada data, glossary (F) penting untuk kebijakan.** E memiliki akurasi data tertinggi (17,33/22); F tidak kalah di data tetapi unggul di Q22–Q24 yang membutuhkan aturan bisnis.
4. **Variabilitas lintas repetisi mengungkap instabilitas.** E memiliki std tertinggi (1,15) karena rep3 mengalami dua kegagalan query (Q05, Q09). F paling stabil (std 0) karena pertanyaannya lebih konsisten menghasilkan jawaban sama. Tiga repetisi sangat membantu mengidentifikasi pertanyaan yang bersifat acak (Q21 untuk C dan D).
5. **Pertanyaan "satu angka tambahan" paling sulit.** Q07 (perubahan % count yang tepat), Q14 (share unit dengan dua angka presisi tinggi), Q20 (dekomposisi dengan toleransi ±0,05 INR) mengharuskan rantai kalkulasi yang presisi. Lebih baik menggunakan tool kalkulasi terpisah daripada mengandalkan model untuk aritmetika presisi.
6. **Kegagalan Q19 pada D dan F.** D menggunakan rata-rata data mart kota-hari (bukan total order per hari), F melakukan pembagian total/count secara manual tetapi menghasilkan nilai yang sedikit salah untuk beberapa hari (Sunday, Friday, Tuesday, Wednesday).

## Kesimpulan dan batas

- Pada **satu model, satu dataset, dan tiga repetisi per kombinasi**, ada tren kenaikan A→E untuk pertanyaan data, tetapi kenaikan tidak selalu konsisten di setiap layer. C dan D memiliki mean data yang sama (16,33/22). Penambahan glossary di F memberikan lompatan besar pada pertanyaan kebijakan (0→3/3) tanpa mengorbankan akurasi data.
- **Keterbatasan:** (1) Hanya satu model (gpt-4.1); (2) Tiga repetisi belum cukup untuk estimasi ketidakpastian yang robust; (3) Rubrik ±0,01pp untuk perubahan persentase sangat ketat dan membutuhkan kalkulasi presisi tinggi yang sulit bagi model bahasa.
- Langkah selanjutnya: perjelas Q07 (minta SQL eksplisit untuk perubahan persen), gunakan calculation tool untuk Q14/Q20/Q07, uji model lain, dan tambah repetisi untuk pertanyaan dengan variasi tinggi.
- Trace lengkap tersimpan lokal di `experiments/run.local/af_25_v2_rep{1,2,3}/` (Git-ignored). Grade tersimpan di [`af_25_v2_grades.json`](../experiments/run.local/af_25_v2_grades.json).
- [Audit per pertanyaan v2](experiment_answer_audit_v2.md) menampilkan kunci, skor per arm×rep, dan jawaban akhir untuk seluruh 25 pertanyaan.
