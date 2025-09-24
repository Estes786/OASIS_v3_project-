# Panduan Mendetail Penggunaan Jupyter Notebook di Termux

Selamat datang di dunia Jupyter Notebook! Saya memahami bahwa ini mungkin terasa baru dan sedikit membingungkan pada awalnya, tetapi jangan khawatir. Jupyter Notebook adalah alat yang sangat powerful dan intuitif setelah Anda memahami dasar-dasarnya. Panduan ini akan membawa Anda langkah demi langkah melalui cara kerja Jupyter Notebook, mulai dari membuat file baru hingga menjalankan skrip, menginstal paket, dan mengintegrasikannya dengan proyek Anda.

## 1. Apa Itu Jupyter Notebook?

Jupyter Notebook adalah aplikasi web *open-source* yang memungkinkan Anda membuat dan berbagi dokumen yang berisi kode langsung, persamaan, visualisasi, dan teks naratif. Nama "Jupyter" sendiri merupakan singkatan dari tiga bahasa pemrograman inti yang didukungnya: Julia, Python, dan R. Namun, Python adalah bahasa yang paling umum digunakan di Jupyter.

**Konsep Utama Jupyter Notebook:**

*   **Notebook**: Dokumen utama di Jupyter, berekstensi `.ipynb`. Ini adalah kombinasi dari sel kode dan sel Markdown.
*   **Kernel**: "Mesin" komputasi yang menjalankan kode Anda. Setiap notebook terhubung ke sebuah kernel. Jika Anda menggunakan Python, kernelnya adalah Python.
*   **Sel (Cell)**: Unit dasar dalam notebook. Ada dua jenis utama:
    *   **Sel Kode (Code Cell)**: Tempat Anda menulis dan menjalankan kode program (misalnya, Python).
    *   **Sel Markdown (Markdown Cell)**: Tempat Anda menulis teks naratif, penjelasan, judul, daftar, dan format teks lainnya menggunakan sintaks Markdown.

**Mengapa Jupyter Notebook Sangat Berguna?**

Jupyter Notebook sangat populer di kalangan ilmuwan data, peneliti, dan pengembang karena beberapa alasan:

*   **Interaktivitas**: Anda dapat menjalankan kode sel per sel dan melihat hasilnya secara instan. Ini sangat membantu untuk eksplorasi data dan debugging.
*   **Reproducibility**: Notebook menyimpan kode, output, dan penjelasan dalam satu dokumen, membuatnya mudah untuk mereproduksi analisis atau eksperimen Anda.
*   **Komunikasi**: Anda dapat berbagi notebook dengan orang lain, dan mereka dapat melihat alur pemikiran Anda, kode Anda, dan hasilnya secara bersamaan.
*   **Fleksibilitas**: Mendukung berbagai bahasa pemrograman dan dapat digunakan untuk berbagai tugas, mulai dari analisis data, machine learning, hingga pengembangan web sederhana.

## 2. Antarmuka Jupyter Notebook

Setelah Anda berhasil mengakses Jupyter Notebook melalui browser di VNC (seperti yang sudah kita lakukan sebelumnya), Anda akan melihat antarmuka utama yang disebut **Dashboard Jupyter**. Dashboard ini adalah tempat Anda mengelola file dan folder, serta meluncurkan notebook baru atau yang sudah ada.

**Bagian-bagian Penting Dashboard:**

*   **Files**: Tab ini menampilkan daftar file dan folder di direktori kerja Anda. Anda bisa menavigasi folder, mengunggah file, membuat folder baru, dan menghapus file.
*   **Running**: Tab ini menampilkan semua notebook dan terminal yang sedang berjalan. Penting untuk mematikan kernel notebook yang tidak digunakan untuk menghemat sumber daya.
*   **Clusters (Opsional)**: Jika Anda menginstal IPython parallel, tab ini akan muncul untuk mengelola cluster komputasi paralel.

**Toolbar di Dashboard:**

*   **Upload**: Untuk mengunggah file dari perangkat Anda ke direktori Jupyter.
*   **New**: Dropdown menu untuk membuat:
    *   **Notebook baru**: Pilih kernel (misalnya, Python 3).
    *   **Folder baru**.
    *   **Terminal baru**: Membuka sesi terminal di dalam browser, yang sangat berguna di Termux.
    *   **Text File baru**.

## 3. Membuat dan Mengelola File di Jupyter Notebook

### 3.1. Membuat Notebook Baru

1.  Di Dashboard Jupyter, klik tombol **New** di pojok kanan atas.
2.  Pilih **Python 3** (atau kernel lain yang Anda inginkan) dari dropdown menu.
3.  Sebuah tab baru akan terbuka di browser Anda, menampilkan notebook kosong yang belum diberi nama (misalnya, `Untitled.ipynb`).

### 3.2. Memberi Nama Notebook

1.  Klik pada nama `Untitled` di bagian atas halaman notebook.
2.  Ketik nama baru untuk notebook Anda (misalnya, `proyek_bdi_agent.ipynb`).
3.  Tekan `Enter` atau klik `Rename`.

### 3.3. Menyimpan Notebook

Jupyter Notebook secara otomatis menyimpan pekerjaan Anda secara berkala. Namun, Anda juga bisa menyimpannya secara manual:

1.  Klik ikon **Save and Checkpoint** (gambar disket) di toolbar.
2.  Atau, pergi ke menu **File > Save and Checkpoint**.

### 3.4. Membuka Notebook yang Sudah Ada

1.  Di Dashboard Jupyter, navigasikan ke folder tempat notebook Anda disimpan.
2.  Klik pada nama file `.ipynb` yang ingin Anda buka.
3.  Notebook akan terbuka di tab baru.

### 3.5. Menghapus, Menggandakan, atau Memindahkan File/Folder

Di Dashboard Jupyter:

1.  **Pilih** file atau folder yang ingin Anda kelola dengan mencentang kotak di samping namanya.
2.  Gunakan tombol-tombol di toolbar di atas daftar file:
    *   **Duplicate**: Membuat salinan file/folder.
    *   **Rename**: Mengganti nama file/folder.
    *   **Move**: Memindahkan file/folder ke lokasi lain.
    *   **Delete**: Menghapus file/folder (akan meminta konfirmasi).
    *   **Shutdown**: Untuk notebook yang sedang berjalan, ini akan mematikan kernelnya.

## 4. Bekerja dengan Sel (Cells) di Notebook

Setiap notebook terdiri dari urutan sel. Anda dapat memilih sel dengan mengkliknya. Saat sel dipilih, ada dua mode utama:

*   **Command Mode (Mode Perintah)**: Sel berwarna biru. Anda dapat melakukan operasi pada sel itu sendiri (misalnya, memotong, menyalin, menempel, mengubah jenis sel).
*   **Edit Mode (Mode Edit)**: Sel berwarna hijau. Anda dapat mengedit konten di dalam sel.

Untuk beralih antara mode:
*   Dari Edit Mode ke Command Mode: Tekan `Esc`.
*   Dari Command Mode ke Edit Mode: Tekan `Enter`.

### 4.1. Jenis Sel: Kode (Code) dan Markdown

Anda dapat mengubah jenis sel menggunakan dropdown menu di toolbar atau dengan shortcut keyboard di Command Mode:

*   `Y`: Mengubah sel menjadi Code Cell.
*   `M`: Mengubah sel menjadi Markdown Cell.

#### 4.1.1. Sel Kode (Code Cells)

Ini adalah tempat Anda menulis dan menjalankan kode Python (atau bahasa lain). Output dari kode akan ditampilkan tepat di bawah sel.

**Menulis Kode:**

Cukup ketik kode Python Anda di dalam sel kode.

**Menjalankan Kode:**

Ada beberapa cara untuk menjalankan sel kode:

*   Klik tombol **Run** (gambar segitiga) di toolbar.
*   Tekan `Shift + Enter`: Menjalankan sel dan memilih sel berikutnya.
*   Tekan `Ctrl + Enter`: Menjalankan sel dan tetap di sel yang sama.
*   Tekan `Alt + Enter`: Menjalankan sel dan menyisipkan sel kode baru di bawahnya.

**Contoh:**

```python
# Ini adalah sel kode
print("Halo, Jupyter!")
a = 10
b = 20
c = a + b
print(f"Hasil penjumlahan: {c}")
```

#### 4.1.2. Sel Markdown (Markdown Cells)

Ini adalah tempat Anda menulis teks naratif, penjelasan, dan dokumentasi menggunakan sintaks Markdown. Setelah dijalankan, Markdown akan dirender menjadi teks yang diformat dengan indah.

**Menulis Markdown:**

Ketik teks Anda menggunakan sintaks Markdown. Beberapa sintaks dasar:

*   `# Judul 1`
*   `## Judul 2`
*   `**Teks Tebal**`
*   `*Teks Miring*`
*   `- Item Daftar`
*   `1. Item Bernomor`
*   `` `kode` `` (untuk kode inline)
*   ````python
    # blok kode
    print("Hello")
    ```` (untuk blok kode)

**Menjalankan Markdown:**

Sama seperti sel kode, Anda menjalankan sel Markdown dengan `Shift + Enter` atau tombol `Run`. Ini akan merender teks Markdown menjadi tampilan yang diformat.

**Contoh:**

```markdown
# Pengantar Proyek BDI Agent

Proyek ini bertujuan untuk mengembangkan **BDI Agent** yang cerdas dan efisien.

## Modul Utama

*   Belief Management System
*   Free Tier Optimization
*   Edge Computing

Silakan lihat `belief_manager.py` untuk detail lebih lanjut.
```

### 4.2. Menambah, Memotong, Menyalin, dan Menempel Sel

Di Command Mode (sel berwarna biru):

*   **A**: Sisipkan sel baru **di atas** sel yang dipilih.
*   **B**: Sisipkan sel baru **di bawah** sel yang dipilih.
*   **X**: Potong (cut) sel yang dipilih.
*   **C**: Salin (copy) sel yang dipilih.
*   **V**: Tempel (paste) sel di bawah sel yang dipilih.
*   **DD** (tekan `D` dua kali): Hapus sel yang dipilih.

## 5. Menjalankan Skrip Python di Jupyter Notebook

Anda dapat menjalankan skrip Python yang sudah ada di dalam Jupyter Notebook dengan beberapa cara:

### 5.1. Menjalankan Kode Langsung di Sel Kode

Ini adalah cara paling umum. Anda bisa menyalin dan menempelkan kode dari skrip `.py` Anda langsung ke sel kode di Jupyter dan menjalankannya.

### 5.2. Mengimpor Modul Python

Jika Anda memiliki skrip Python yang berfungsi sebagai modul (misalnya, `belief_manager.py` dari proyek Anda), Anda dapat mengimpornya ke dalam notebook dan menggunakan fungsi atau kelas yang ada di dalamnya.

Misalnya, jika Anda memiliki file `my_script.py` dengan isi:

```python
# my_script.py
def greet(name):
    return f"Halo, {name}!"

class Calculator:
    def add(self, a, b):
        return a + b
```

Anda bisa mengimpornya di Jupyter:

```python
# Di Jupyter Notebook
from my_script import greet, Calculator

print(greet("Dunia"))

calc = Calculator()
print(calc.add(5, 3))
```

**Penting**: Jika Anda mengedit file `my_script.py` setelah mengimpornya, Anda perlu me-reload modul di Jupyter agar perubahan diterapkan. Gunakan magic command `%load_ext autoreload` dan `%autoreload 2`:

```python
# Di awal Jupyter Notebook Anda
%load_ext autoreload
%autoreload 2

from my_script import greet, Calculator
# ... kode Anda ...
```

### 5.3. Menjalankan Skrip dari Terminal Jupyter

Jupyter juga memungkinkan Anda membuka terminal langsung di browser. Ini sangat berguna untuk menjalankan skrip seperti yang biasa Anda lakukan di Termux.

1.  Di Dashboard Jupyter, klik **New > Terminal**.
2.  Sebuah tab baru akan terbuka dengan terminal Linux. Anda bisa menggunakan perintah seperti `python nama_skrip.py` di sini.

## 6. Menginstal Paket Python di Jupyter (Termux)

Saat Anda bekerja dengan proyek yang kompleks seperti BDI Agent FMAA, Anda akan membutuhkan banyak library Python eksternal (misalnya, `numpy`, `pandas`, `scikit-learn`, `matplotlib`, `aiohttp`, dll.). Anda bisa menginstalnya langsung dari dalam Jupyter Notebook.

Ada dua cara utama:

### 6.1. Menggunakan Terminal Jupyter

Ini adalah cara yang paling direkomendasikan karena lebih konsisten dengan lingkungan Termux Anda.

1.  Buka **Terminal baru** dari Dashboard Jupyter (New > Terminal).
2.  Gunakan perintah `pip` seperti biasa:
    ```bash
    pip install nama_paket
    ```
    Atau, jika Anda memiliki `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

### 6.2. Menggunakan Sel Kode dengan `!` (Bang)

Anda juga bisa menjalankan perintah shell langsung dari sel kode Jupyter dengan menambahkan tanda seru (`!`) di awal perintah. Ini akan menjalankan perintah di shell yang mendasari kernel Jupyter.

```python
# Menginstal satu paket
!pip install numpy

# Menginstal dari requirements.txt
!pip install -r requirements.txt

# Contoh lain: melihat daftar paket yang terinstal
!pip list
```

**Catatan Penting:**
*   Saat menginstal paket, pastikan Anda menginstal ke lingkungan Python yang sama dengan yang digunakan oleh kernel Jupyter Anda. Di Termux, ini biasanya lingkungan default Anda.
*   Setelah menginstal paket baru, kadang-kadang Anda perlu me-restart kernel Jupyter agar paket tersebut dikenali. Anda bisa melakukannya dari menu **Kernel > Restart** atau **Kernel > Restart & Clear Output**.

## 7. Integrasi Proyek BDI Agent FMAA dengan Jupyter Notebook

Sekarang, mari kita bahas bagaimana semua ini terhubung dengan proyek BDI Agent FMAA Anda. Ingat, tujuan utama menggunakan Jupyter di sini adalah untuk memfasilitasi pengembangan, pengujian, dan visualisasi setiap komponen proyek secara interaktif.

### 7.1. Struktur Proyek dan Navigasi

Asumsikan Anda telah mengkloning atau menempatkan folder proyek BDI Agent FMAA Anda di direktori `home` Termux Anda. Saat Anda membuka Jupyter Notebook, Anda akan melihat folder-folder proyek Anda (misalnya, `core`, `enterprise`, `android`, dll.).

Anda bisa menavigasi ke dalam folder-folder ini dari Dashboard Jupyter untuk membuka atau membuat notebook di dalamnya. Misalnya, Anda bisa membuat folder `notebooks` di dalam proyek Anda untuk menyimpan semua file `.ipynb` yang Anda buat.

### 7.2. Mengembangkan Modul per Modul

Seperti yang dijelaskan dalam panduan sebelumnya, Anda dapat membuat notebook terpisah untuk setiap modul utama proyek Anda. Contoh:

*   `notebooks/belief_manager_dev.ipynb`: Untuk mengembangkan dan menguji `core/belief_manager.py`.
*   `notebooks/free_tier_optimization_tests.ipynb`: Untuk menguji `optimization/free_tier_maximizer.py`.
*   `notebooks/termux_orchestrator_testing.ipynb`: Untuk mengembangkan dan menguji `android/super_orchestrator.py`.

Di setiap notebook, Anda akan:

1.  **Mengimpor** kelas atau fungsi yang relevan dari file `.py` modul Anda.
2.  **Menulis kode** untuk menginisialisasi objek, memanggil fungsi, dan menjalankan logika modul.
3.  **Menambahkan sel Markdown** untuk menjelaskan apa yang Anda lakukan, mengapa, dan apa hasilnya.
4.  **Membuat visualisasi** untuk memahami data atau performa modul.
5.  **Menguji skenario** yang berbeda dan melihat outputnya secara langsung.

### 7.3. Mengelola Dependensi Proyek

Proyek Anda akan memiliki banyak dependensi. Penting untuk mengelolanya dengan baik:

1.  **Buat `requirements.txt`**: Pastikan Anda memiliki file `requirements.txt` di root proyek Anda yang mencantumkan semua library Python yang dibutuhkan. Contoh isinya:
    ```
    numpy
    pandas
    scikit-learn
    matplotlib
    aiohttp
    asyncio
    # ... dan seterusnya
    ```
2.  **Instal dari Terminal Jupyter**: Kapan pun Anda memulai proyek baru atau jika ada dependensi yang hilang, buka Terminal Jupyter dan jalankan `pip install -r requirements.txt`.

### 7.4. Menggunakan Terminal Jupyter untuk Tugas Spesifik Termux

Beberapa bagian proyek Anda (terutama `Termux Super-Orchestrator`) mungkin perlu berinteraksi langsung dengan sistem Termux atau menjalankan perintah shell. Terminal Jupyter adalah tempat yang tepat untuk ini.

Misalnya, Anda mungkin perlu menjalankan perintah `termux-api` atau `apt` untuk menginstal utilitas sistem. Anda bisa melakukannya di Terminal Jupyter.

## 8. Tips Lanjutan untuk Produktivitas di Jupyter

*   **Keyboard Shortcuts**: Pelajari shortcut keyboard untuk mempercepat alur kerja Anda. Tekan `H` di Command Mode untuk melihat daftar lengkap.
*   **Magic Commands**: Jupyter memiliki "magic commands" yang dimulai dengan `%` atau `%%`. Contoh:
    *   `%timeit`: Mengukur waktu eksekusi baris kode.
    *   `%%timeit`: Mengukur waktu eksekusi seluruh sel kode.
    *   `%who`: Menampilkan semua variabel yang didefinisikan.
    *   `%matplotlib inline`: Untuk menampilkan plot Matplotlib langsung di notebook.
*   **Debugging**: Jika Anda mengalami error, Anda bisa menggunakan `%debug` di sel kode setelah error terjadi untuk masuk ke debugger Python.
*   **Clear Output**: Sebelum menyimpan atau berbagi notebook, Anda bisa membersihkan semua output sel dari menu **Cell > All Output > Clear** atau **Kernel > Restart & Clear Output**.

## Kesimpulan

Jupyter Notebook adalah alat yang sangat serbaguna yang akan menjadi aset berharga dalam pengembangan proyek BDI Agent FMAA Anda. Dengan memahami cara membuat dan mengelola notebook, menjalankan kode, menginstal paket, dan mengintegrasikannya dengan struktur proyek Anda, Anda akan dapat bekerja secara lebih efisien dan interaktif.

Ingatlah bahwa praktik terbaik adalah memulai dari yang kecil, menguji setiap komponen secara terpisah di notebook, dan secara bertahap mengintegrasikannya ke dalam proyek yang lebih besar. Jangan ragu untuk bereksperimen dan menjelajahi fitur-fitur Jupyter lainnya.

Saya harap panduan mendetail ini membantu Anda merasa lebih nyaman dan percaya diri dalam menggunakan Jupyter Notebook untuk proyek Anda. Jika ada pertanyaan lebih lanjut atau Anda ingin saya menjelaskan topik tertentu secara lebih mendalam, jangan sungkan untuk bertanya!

