# Ringkasan eksperimen A–F: 25 pertanyaan

## Proses

- **Tujuan:** mengukur perubahan akurasi jawaban saat akses agent ditambah bertahap: A = source/staging, B = +intermediate, C = +core, D = +marts, E = +19 metric MetricFlow, F = +business glossary. Akses SQL sebelumnya tetap tersedia di setiap arm.
- **Setup:** satu model `gpt-4.1`, temperature 0, satu attempt untuk tiap kombinasi 25 pertanyaan × 6 arm = **150 attempt**. Semua memakai snapshot `ZOMATO_DLR`, teks pertanyaan yang sama, maksimal tiga query, dan batas 40 baris per hasil.
- **Run:** 21 Oktober 2026, 06:31–07:03 WIB; **150/150 selesai**. Agent tidak menerima [jawaban referensi](../experiments/answers_25.md). [Desain](experiment_design.md), [pertanyaan](../experiments/questions_25.md), dan [runner](../scripts/run_experiment.py) memuat detailnya.
- **Skor revisi:** jawaban akhir harus benar pada *semua* angka, populasi, unit, dan interpretasi. Toleransi numerik diperbesar menjadi ±0,01 percentage point untuk persentase dan ±0,01 unit untuk average/korelasi; count dan identitas tetap eksak. Q01–Q21 dan Q25 adalah pertanyaan data; Q22–Q24 memerlukan aturan bisnis yang hanya diberikan ke F. Seluruh 150 jawaban lama dinilai ulang tanpa menjalankan model lagi.

## Hasil

| Arm | Data benar | Kebijakan benar | Total benar |
| --- | ---: | ---: | ---: |
| A | 5/22 | 0/3 | 5/25 |
| B | 9/22 | 0/3 | 9/25 |
| C | 9/22 | 0/3 | 9/25 |
| D | 10/22 | 0/3 | 10/25 |
| E | **11/22** | 0/3 | **11/25** |
| F | 9/22 | **2/3** | **11/25** |

- **Tidak ada kenaikan bertahap yang konsisten.** E tertinggi untuk pertanyaan data; F turun dari E pada data, meski unggul pada dua pertanyaan kebijakan.
- E mencoba MetricFlow pada 18/25 pertanyaan; F pada 17/25. Dari 44 panggilan MetricFlow, 22 berhasil. Sebagian besar sisanya melewati batas 40 baris. Semua attempt tetap menghasilkan jawaban akhir.
- Tidak satu pun dari 15 attempt A–E untuk Q22–Q24 meminta klarifikasi aturan bisnis yang belum tersedia; semuanya memberi angka. F benar pada Q23 dan Q24.

## Pembelajaran

1. **Core membantu label dan grain, tetapi mart tetap perlu dibaca dengan tepat.** Pada Q18, C–F memakai label age segment yang benar; A/B salah memilih atribut. Pada Q19, D merata-ratakan baris mart kota-hari, bukan total order per hari.
2. **Kesalahan hitung di jawaban akhir dominan.** Semua arm gagal pada pertumbuhan Q07, unit share Q14, dekomposisi Q20, dan korelasi Q21. Q12 menunjukkan hasil query yang berguna masih bisa berubah menjadi total/share yang salah saat dijelaskan model.
3. **Glossary harus terhubung ke eksekusi.** Pada Q22, F menyebut aturan `rating_count >= 100` tetapi memakai hasil MetricFlow pasar penuh tanpa filter. Pada Q23 dan Q24, F menerapkan aturan bisnis dan menghasilkan jawaban yang masuk toleransi revisi.
4. **Beberapa pertanyaan perlu diperjelas sebelum eksperimen berikutnya.** Frasa “during 2025, by recorded order date” pada Q02–Q05 sering dibaca sebagai permintaan deret harian/bulanan, sementara kunci meminta satu agregat tahunan. Pertanyaannya sengaja tidak diubah selama run.
5. **Toleransi yang wajar mengubah sebagian skor.** Share Q15 yang benar adalah 70,005686%; `70%` dan `70,01%` kini diterima. Lima sel berubah menjadi benar dibanding skor awal: B-Q15, D-Q13, D-Q15, E-Q15, dan F-Q23. Kesalahan populasi, ranking, atau persentase yang meleset lebih dari 0,01 poin tetap gagal.

## Kesimpulan dan batas

- Pada **satu model, satu dataset, dan satu run per kombinasi**, hasil ini belum mendukung klaim bahwa penambahan layer A→F otomatis meningkatkan ketepatan jawaban. Belum ada estimasi repeatability atau uncertainty. Toleransi revisi dipilih setelah melihat hasil awal, sehingga skor revisi bersifat eksploratif, bukan hasil rubric yang ditetapkan sebelum run.
- Langkah berikut yang paling langsung diuji: perjelas Q02–Q05, hitung rasio/korelasi/dekomposisi lewat query atau calculation tool, dan buat aturan eligibility bisa diterapkan oleh metric/query—lalu ulangi run dengan beberapa repetisi.
- Trace dan catatan skor lengkap tersimpan lokal di `experiments/run.local/af_25/` (Git-ignored). Skor awal disimpan terpisah sebagai `grades_strict.local.json`; skor pada tabel memakai `grades.local.json` untuk **150 jawaban akhir yang sama**.
- [Audit per pertanyaan](experiment_answer_audit.md) menampilkan kunci, skor dan alasannya, serta jawaban akhir asli A–F untuk seluruh 25 pertanyaan.
