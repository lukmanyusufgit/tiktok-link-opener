# TikTok Link Opener

Utilitas Python sederhana untuk membuka tautan video atau profil TikTok di browser default. Proyek ini tidak melakukan login, scraping, atau otomatisasi views, likes, follows, maupun shares.

## Persyaratan

- Python 3.8 atau lebih baru
- Browser default tersedia di sistem

Tidak ada paket tambahan yang perlu dipasang; program hanya memakai standard library Python.

## Menjalankan

```powershell
python tiktok_toolkit.py
```

Masukkan URL ketika diminta. URL juga dapat diberikan langsung:

```powershell
python tiktok_toolkit.py https://www.tiktok.com/@username/video/123456789
```

Program menerima host `tiktok.com`, `www.tiktok.com`, `m.tiktok.com`, `vm.tiktok.com`, dan `vt.tiktok.com`. URL yang tidak valid ditolak.

## Lisensi

Belum ada lisensi yang ditetapkan untuk kode utilitas ini. Jangan menganggap kode dapat digunakan ulang atau didistribusikan kembali tanpa izin.
