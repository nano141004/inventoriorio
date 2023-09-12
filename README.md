## [Link Aplikasi Inventoriorio](https://inventoriorio.adaptable.app/)

## Step by step pengimplementasian

- Membuat direktori(utama) baru bernama ``inventoriorio``, lalu membuat virtual environment didalamnya dan kemudian diaktifkan
- Membuat berkas ``requirements.txt`` yang diisi dependencies dan kemudian diinstal
- Menetapkan nilai ``["*"]`` pada ``ALLOWED_HOST`` dalam berkas ``settings.py``
- Menambahkan berkas ``.gitignore``
- Membuat aplikasi baru bernama ``main`` dalam direktori
- Menambahkan ``main`` pada ``INSTALLED_APPS`` dalam berkas ``setting.py`` di direktori proyek
- Membuat model bernama ``Item`` dalam ``models.py`` dengan atribut ``name, description, dan amount``
- Melakukan migrasi model
- Mengisi berkas ``views.py``
- Membuat direktori ``templates`` dalam direktori ``main`` dan diisi berkas ``main.html``
- Membuat dan mengisi berkas ``urls.py`` dalam direktori ``main``
- Menambahkan rute url (yang mengarah ke ``main``) baru pada ``urlpatterns`` dalam berkas ``urls.py`` di direktori proyek
- Membuat unit test pada berkas ``tests.py``
- Membuat repo baru pada github dengan nama ``inventoriorio``
- Menghubungkan repo lokal dengan repo pada github
- Melakukan add, commit, dan push ke repo github
- Melakukan deployment aplikasi di ``Adaptable.io``

## Bagan request client dan kaitan diantaranya



