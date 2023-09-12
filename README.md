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

![Bagan](static/images/bagan_request_client.png)

Client ingin masuk ke url web kita, sehingga browser melakukan HTTP request. Request tersebut kemudian akan diterima dan diproses oleh `urls.py`. Setelah request di proses dalam `urls.py`, kemudian akan dipanggil function yang sesuai yang ada dalam `views.py`.Akan dilakukan operasi dalam `views.py` seperti transaksi data dari/ke `models.py`. Kemudian setelah itu `views.py` akan mengembalikan respon template HTML yang sesuai kembali kepada client.

## Mengapa venv dibutuhkan 

Virtual environment(venv) adalah lingkungan terisolasi. Virtual environment berguna agar setiap proyek yang berbeda memiliki lingkungan terisolasi sehinga masing - masing proyek dapat memiliki dependensinya masing - masing.
Kita dapat membuat aplikasi berbasis django tanpa menggunakan virtual environment, namun tentunya jika kita bekerja dalam beberapa proyek berbeda bisa saja terjadi konflik antar proyek tersebut yang disebabkan oleh dependensi yang berbeda.

## MVC, MVT, dan MVVM

- MVC (Model View Controller)
    - Model: Mengurusi bagian logika, data, dan berhubungan dengan database
    - View: Mengurusi UI, dengan menampilkan data dari model dan menerima pembaruan dari controller
    - Controller: Perantara model dan view, mengatur aliran aplikasi dan sinkronisasi antara model dan view
- MVT (Model View Template)
    - Model: Mengurusi bagian logika, data, dan berhubungan dengan database; tidak berhubungan langsung dengan view
    - View: Mengurusi UI, bergantung terhadap pembaruan dari controller 
    - Template: Menjembatani antara model dan view, menerima data dari model dan melakukan pembaruan ke view
- MVVM (Model View - ViewModel)
    - Model: Mengurusi bagian logika, data, dan berhubungan dengan database
    - View: Mengurusi UI, menampilkan data dari model
    - ViewModel: Menjembatani antara model dan view, menyediakan dan memanipulasi data untuk ditampilkan