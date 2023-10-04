## [Link Aplikasi Inventoriorio](https://inventoriorio.adaptable.app/)

<details> 
<summary>Tugas 2</summary> 

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
</details>

<details> 
<summary>Tugas 3</summary>

## Apa perbedaan antara form POST dan form GET dalam Django?

| POST | GET |
| :-: | :-: | 
| Nilai variabel tidak ditampilkan di URL | Nilai variabel ditampilkan di URL |
| Dapat memodifikasi input user sebelum masuk ke database | Tidak bisa memodifikasi input user |
| Lebih aman | Kurang aman |
| Tidak dibatasi panjang string | Dibatasi panjang string sampai 2047 karakter |
| Biasanya untuk input data melalui form | Biasanya untuk input data melalui link |
| Digunakan untuk mengirim data-data penting seperti password | Digunakan untuk mengirim data-data tidak penting |

## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

HTML(Hypertext Markup Language) cenderung digunakan untuk mengatur tampilan dan struktur dari halaman web, sehingga HTML tidak terlalu cocok digunakan untuk mengirim data mentah. XML(eXtensible Markup Language) menggunakan struktur tag dalam setiap data, ini menyebabkan XML lebih kompleks dan sulit untuk dibuat dan dibaca oleh manusia. JSON(JavaScript Object Notation) menyimpan data dengan object(pasangan key - value), sehingga JSON lebih simpel, ringan, dan lebih mudah untuk dibuat dan dibaca.

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

- Sederhana dan mudah dibaca.
- Lebih ringan dibandingkan format lain, sehingga pertukaran data menjadi tidak terbebani dan lancar.
- Mendungkung banyak bahasan pemrograman.
- Struktur data yang fleksibel, mudah untuk dimodifikasi.
- Keamanan yang lebih baik dibandingkan format lain.
- Popularitasnya yang tinggi membuat banyak web modern menggunakannya, sehingga lebih mudah integrasi antar aplikasinya.

## Step by step pengimplementasian

- Menambahkan folder `template` dalam direktori utama, dan diisi dengan `base.html` sebagai template dasar untuk halaman lainnya.
- Membuat dan mengisi berkas `forms.py` pada direktori `main`, berfungsi agar dapat menginput data(object model) untuk aplikasi.
- Menambahkan fungsi baru pada berkas `views.py` di direktori `main` dengan nama `create_item` untuk menyimpan data yang diinput/disubmit dalam forms.
- Membuat dan mengisi berkas baru `create_item.html` pada direktori `main/templates` sebagai halaman/template dari fungsi `create_item` untuk menginput data.
- Memodifikasi isi berkas `main.html` untuk menampilkan data item yang telah diinput, menampilkan jumlah item yang ada(telah diinput), dan menambahkan tombol `Add New Item` yang akan redirect ke halaman form.
- Menambahkan fungsi - fungsi baru pada berkas `views.py` di direktori `main`, yaitu fungsi `show_xml` dan `show_json` yang masing - masing berfungsi untuk menampilkan data dalam bentuk `XML` dan `JSON` secara kesuluruhan. Selain itu ditambahkan juga fungsi `show_xml_by_id` dan `show_json_by_id` untuk menampilkan data dalam bentuk `XML` dan `JSON` secara spesifik tergantung id yang diberikan.
- Melakukan routing URL dari fungsi - fungsi yang baru saja dibuat di atas dengan cara memodifikasi berkas `urls.py` di direktori `main`. Pada berkas `urls.py` diimport fungsi - fungsi tersebut, lalu ditambahkan semua path yang menuju fungsi - fungsi tersebut.

## Screenshot pengaksesan kelima URL menggunakan Postman

HTML:
![html](static/images/html.png)
XML:
![xml](static/images/xml.png)
JSON:
![json](static/images/json.png)
XML by id:
![xml_by_id](static/images/xml_by_id.png)
JSON by id:
![json_by_id](static/images/json_by_id.png)

</details>

<details> 
<summary>Tugas 4</summary>

## Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

Django UserCreationForm adalah import bawaan dalam library Django yang bertujuan untuk memudahkan pembuatan formulir pendaftaran user/pengguna dalam aplikasi web. Dengan formulir ini, kelebihannya yaitu kita dapat membuat formulir pendaftaran user tanpa menulis kode dari awal lagi, karena sudah disediakan field - field input yang biasa diperlukan dalam registrasi aplikasi dan juga terdapat validasi terhadap input yang diberikan sehingga dapat membuat keamanan akun pengguna terjamin. Namun ada juga kekurangan dari UserCreationForm yaitu seperti kurangnya pilihan untuk kustomisasi dari segi visual, keterbatasan untuk kustomisasi fitur yang telah ada secara default seperti validasi input, dan lain - lain.

## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

Autentikasi adalah proses verifikasi terhadap pengguna yang ingin masuk/mengakses aplikasi, sistem akan mengecek apakah pengguna yang ingin masuk ke dalam aplikasi adalah pengguna yang berhak/memiliki akses masuk. Contohnya saat melakukan proses login sistem akan memverifikasi pengguna misalnya berdasarkan input username dan password.
Otorisasi sendiri adalah proses untuk mengatur akses pengguna yang telah berhasil di-autentikasi sebelumnya terhadap aplikasi, seperti akses untuk memodifikasi model, melakukan operasi pada aplikasi, dan sebagainya. 
Kedua hal tersebut merupakan hal yang penting dalam aplikasi Django untuk menjaga keamanan aplikasi. Dengan adanya autentikasi  maka kita mengurangi resiko bagi sembarang orang khususnya yang berniat jahat untuk dapat masuk ke dalam aplikasi kita. Selain itu pengguna yang terautentikasi juga terbatasi aksesnya sesuai yang diizinkan/sesuai perannya dalam aplikasi sehingga tidak bisa sembarangan untuk memodifikasi data dari aplikasi.

## Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

Cookies adalah data dengan ukuran kecil yang disimpan pada komputer browser web yang digunakan saat mereka mengunjungi situs web. Cookies digunakan untuk menyimpan informasi yang dapat digunakan oleh server web untuk mengenali pengguna yang telah mengunjungi situs sebelumnya atau untuk menyimpan data sesi pengguna. Cookies menyimpan session ID dalam komputer pengguna, session ID ini yang kemudian dipetakan ke struktur data di sisi server web. Saat pengguna melakukan request maka browser web akan mengirimkan session ID ke server dan kemudian server akan mencari informasi berdasarkan session ID yang diterima lalu akan mengembalikan data yang diminta.

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Secara default penggunaan cookies aman untuk pengembangan web, ini karena cookies tidak akan menyebabkan pengaruh kepada device kita seperti terkena virus atau malware. Namun karena cookies sendiri menyimpan id unik dari pengguna, make dengan cookies tersebut seseorang dapat melacak jejak browsing dari pengguna dengan cookies(id) tersebut. Hal ini dapat disalahgunakan oleh orang - orang yang tidak bertanggung jawab. Oleh karena itu kita harus menghindari mengakses situs - situs yang mencurigakan, biasanya situs - situs ilegal dimana banyak *third party* cookies yang lebih rentan untuk dipersalahgunakan oleh seseorang. 

## Step by step pengimplementasian

- Membuat fungsi `register` dalam berkas `views.py` di direktori `main` yang berfungsi untuk membuat form registrasi untuk membuat akun pengguna baru. Setelah itu membuat berkas baru bernama `register.html` di direktori `main/templates` yang memuat halaman untuk form registrasi tersebut.
- Membuat fungsi `login_user` dalam berkas `views.py` di direktori `main` yang berfungsi untuk melakukan autentikasi pengguna yang ingin login. Setelah itu membuat berkas baru bernama `login.html` di direktori `main/templates` yang memuat halaman untuk login pengguna.
- Membuat fungsi `logout_user` dalam berkas `views.py` di direktori `main` yang berfungsi untuk mekanisme saat pengguna melakukan logout dari aplikasi.
- Melakukan routing URL dari semua fungsi yang baru saja dibuat di atas dengan cara memodifikasi berkas `urls.py` di direktori `main`. Pada berkas `urls.py` diimport fungsi - fungsi tersebut, lalu ditambahkan semua path yang menuju fungsi - fungsi tersebut.
- Memodifikasi isi berkas `main.html` di direktori `main/templates` dengan menambahkan button untuk logout.
- Melakukan restriksi terhadap fungsi `show_main` pada berkas `view.py` di direktori `main` agar halaman *main* hanya bisa diakses oleh pengguna yang telah ter-autentikasi.
- Mencoba membuat 2 akun pengguna baru pada aplikasi dengan menggunakan localhost dan kemudian menambahkan 3 dummy data pada setiap akun tersebut.
- Menambahkan fungsi untuk menambahkan *cookie* yang bernama `last_login` pada fungsi `login_user` dalam berkas `views.py` di direktori `main` untuk menampilkan `datetime` atau waktu terakhir kali pengguna login pada aplikasi. Dalam berkas yang sama, memodifikasi fungsi `show_main` dengan menambahkan kode `'last_login': request.COOKIES['last_login']` pada variabel `context`. Setelah itu memodifikasi fungsi `logout_user` untuk menghapus *cookie* `last_login` setelah pengguna logout. Terakhir, memodifikasi berkas `main.html` di direktori `main/templates` dengan menambahkan kode yang menunjukkan data `last_login`.
- Menghubungkan model `Item` dengan pengguna dengan cara memodifikasi berkas `models.py` di direktori `main` dengan menambahkan `ForeignKey` yang bertujuan untuk membuat *relationship* antara satu `Item` dengan satu pengguna. Kemudian memodifikasi fungsi `create_item` pada berkas `views.py` di direktori `main` untuk mencegah Django langsung menyimpan objek yang dibuat ke dalam database. Setelah itu memodifikasi isi variabel `context` pada fungsi `show_main` dalam berkas `views.py` di direktori `main` yaitu mengubah *value* 'name' menjadi sesuai dengan username pengguna yang login. Terakhir adalah melakukan migrasi model.
##### Bonus
- Membuat fungsi - fungsi baru dalam berkas `views.py` di direktori `main`, yaitu fungsi `plus` yang berfungsi untuk menambahkan `amount` sebanyak 1 dari item yg dipilih, fungsi `minus` yang berfungsi untuk mengurangi `amount` sebanyak 1 dari item yg dipilih(jika setelah dikurang 1 `amount` menjadi 0, maka item akan di hapus), dan fungsi `remove` yang berfungsi untuk menghapus item yang dipilih. 
- Melakukan routing URL semua fungsi tersebut pada berkas `urls.py` di direktori `main`.
- Memodifikasi berkas `main.html` di direktori `main/templates` dengan menambahkan button `plus 1` (untuk fungsi `plus`), button `minus 1` (untuk fungsi `minus`), dan button `remove` (untuk fungsi `remove`) di sebelah setiap item yang ada dalam table.

</details>

<details> 
<summary>Tugas 5</summary> 

## Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.

- Element selector : Untuk mengubah properti pada semua element dengan tag yang sama, berguna untuk mengubah properti pada element dengan tag yang ditentukan pada satu proyek.
- ID selector : Untuk mengubah properti pada element dengan dengan id yang unik, berguna untuk mengubah properti pada element secara spesifik tergantung id yang ditentukan.
- Class selector : Untuk mengelompokkan beberapa element dengan suatu karakteristik yang sama, berguna untuk mengubah properti element secara kesuluruhan dengan class yang ditentukan.

## Jelaskan HTML5 Tag yang kamu ketahui.

- `<nav>` : untuk menandai bagian navigasi dari halaman web
- `<header>` : menandai bagian kepala dari dari halaman web
- `<body>` : menandai badan dari halaman web
- `<dev>`: menandai suatu bagian dari halaman web
- `<footer>` : menandai bagian kaki/bawah dari halaman web
- `<time>` : menandari waktu 

## Jelaskan perbedaan antara margin dan padding.

- Margin : adalah ruang di luar batas elemen, biasanya transparan, membatasi ruang antar elemen
- Paddding : adalah ruang di dalam batas elemen, menandai ruang antara isi konten dengan batas ruang element, biasanya memiliki background warna atau gambar

## Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

| Tailwind | Bootstrap |
| :-: | :-: | 
| Ukuran file yang lebih kecil | Ukuran file lebih besar karena termasuk komponen yang telah didefinisikan |
| Fleksibilitas dan adaptasi yang tinggi | Tampilan yang lebih konsisten pada seluruh proyek |
| Lebih sulit karena harus memahami banyak kelas yang ada | Lebih mudah karena sudah disediakan banyak komponen |

Kita menggunakan bootstrap jika memerlukan pengembangan yang cepat, konsistensi keseluruhan proyek, dan tidak memerlukan kustomisasi yang banyak.
Sebaliknya, kita menggunakan tailwind saat memerlukan kustomisasi yang banyak dan lebih fleksibel.

## Step by step pengimplementasian

- Menambahkan bootstrap pada proyek kita.
- Menambahkan navigation bar pada halaman `main`, yang berisi username dari pengguna yang login, lalu tombol logout.
- Memodifikasi halaman `login`, `register`, dan `create_item`, dengan memosisikan content ke tengah, lalu button - button yang ada diganti menjadi *layout button*. 
- Memodifikasi halaman `main`, mengubah `background color`, mengubah button - button yang ada menjadi *layout button*, lalu juga mengganti warna dari item terakhir yang ada pada aplikasi menjadi warna merah.

</details>