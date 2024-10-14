# MINI-PROJECT-DASAR PEMOGRAMAN 2
Nama : Aliyah Azzah Sekedang

Kelas : A

Tema : Sistem Langganan atau Membership Layanan Streaming (Netflix)

## Flowchart
![MINPRO DDP 2](https://github.com/user-attachments/assets/944b4fc4-ebea-4989-a1f0-b1905f5671fb)

## Menu Utama
![image](https://github.com/user-attachments/assets/fe040ba7-4ac8-4849-a642-dce76048e9b2)

Saat program dimulai, akan muncul Menu Utama (Main Menu). Disini, user diminta untuk memilih Login sebagai Admin atau Member.

## Menu Login
Setelah memilih 'Role', user diminta memasukkan Username dan Password.

1) Login sebagai Admin, bisa melakukan sistem CRUD (Create, Read, Update, Delete) pada database paket streaming.
   
   - Username: mba_admin
   - Password: kerjalembur
     
3) Login sebagai Member, hanya dapat melakukan transaksi dan menampilkan paket streaming yang telah dibeli.
   
   - Username: aliyahazs
   - Password: nontondulu

- Seandainya jika user menginput role mode selain Admin atau Member.

![image](https://github.com/user-attachments/assets/5a5c728e-2668-493e-89b7-7ccf94f198a7)

jika user menginput role mode selain Admin atau Member, maka otomatis akan kembali ke Menu Login.

## Menu Admin
- Jika user memasukkan Username dan Password yang tidak sesuai.
  
  ![image](https://github.com/user-attachments/assets/fa556cda-73b3-49bf-9315-4d00a306dd7b)

  maka otomatis akan kembali diminta memasukkan ulang.
  
- Jika login sebagai Admin berhasil, akan muncul Menu Admin dengan opsi:

  ![image](https://github.com/user-attachments/assets/5f0e0542-07a9-45ba-9cc3-735085a46bf3)

## Penjelasan Menu Admin

  ### 1. View a package
  Admin dapat melihat semua paket yang tersedia.
  
  ![image](https://github.com/user-attachments/assets/8d8db1bf-4e29-49f2-8b8a-394d45093aed)
  
  Untuk masuk ke opsi "View a package" inputkan angka 1.

  ![image](https://github.com/user-attachments/assets/b2fbb4f4-6f33-4706-961a-9907e3084102)

  Disini Admin akan langsung ditampilkan Paket Streaming yang tersedia beserta harganya, yaitu Paket Basic, Standart, dan Premium.
  
  ### 2. Add a package
  Admin dapat menambahkan paket baru dengan memasukkan Nama baru dan Harga baru.
  
  ![image](https://github.com/user-attachments/assets/fb138b2a-09f7-4c15-b36e-e04ffd33931e)

  Untuk masuk ke opsi "Add a package" inputkan angka 2. Lalu diminta memasukkan Nama baru dan Harga Baru.

  ![image](https://github.com/user-attachments/assets/009b0cdd-0a07-4e93-9f78-bf50bfbbfcc2)

  ### 3. Update a package
  Admin dapat mengubah atau memperbarui paket yang sudah ada.

  ![image](https://github.com/user-attachments/assets/a1691d6e-3c4b-49bd-b267-82bed2ad1268)

  Untuk masuk ke opsi "Update a package" inputkan angka 3. Lalu diminta input nomor paket yang diubah dan diminta memasukkan Nama baru serta Harga Baru.

  ![image](https://github.com/user-attachments/assets/4f6cd649-ed05-47ad-9352-a8936d821d4e)

  ### 4. Delete a package
  Admin dapat menghapus paket yang ada.

  ![image](https://github.com/user-attachments/assets/e5e4e448-7a52-4f09-9a02-b621d63f797d)

  Untuk masuk ke opsi "Delete a package" inputkan angka 4. Lalu diminta input nomor paket yang ingin dihapus.

  ![image](https://github.com/user-attachments/assets/5bbf6b86-167f-4acf-a544-469cd119c3e3)

  ### 5. View transactions
  Admin dapat melihat semua transaksi yang telah dilakukan oleh Member.
  
  - Jika belum ada transaksi yang dilakukan, ditampilkan tulisan "No transactions yet." dan kembali ditampilkan Menu Admin. 
  ![image](https://github.com/user-attachments/assets/a24ba8f0-ab49-4777-b5b5-4379469a0935)

  - Jika sudah ada transaksi yang dilakukan, ditampilkan tulisan

  ### 6. Logout
  Ketika Admin telah selesai menggunakan Menu Admin, Admin dapat memilih opsi ke 6 yaitu Logout. Setelah memasukkan opsi 6, maka user akan logout sebagai Admin. Lalu, diarahkan untuk Exit atau keluar dari program.

  ![image](https://github.com/user-attachments/assets/4eab3461-9fe7-48ea-a2ea-c5dabba2d159)

   - Ketika memilih "No" maka user diarahkan kembali ke Menu Login.

     ![image](https://github.com/user-attachments/assets/bba1c793-2c37-454b-b7fb-e39963dc8b9c)
     
   - Ketika memilih "Yes" maka user telah keluar dari program.

     ![image](https://github.com/user-attachments/assets/4e98e861-63d9-4093-a929-762c70c97646)

## Mode Member

![image](https://github.com/user-attachments/assets/edfa9e50-6c1f-41f8-bee4-803ff39ff761)

Pada mode Member, user akan diberikan 3 opsi dalam Menu Member seperti pada gambar dan user diminta untuk menginput opsi sesuai dengan angka opsi yang disediakan.

## Penjelasan Menu Member

   ### 1. View all Package

   Member dapat melihat semua paket yang tersedia.
  
   ![image](https://github.com/user-attachments/assets/ddf7e827-d0ce-44c1-ba42-0d9d3df11b62)
  
   Untuk masuk ke opsi "View a package" inputkan angka 1.

   ![image](https://github.com/user-attachments/assets/310b9c91-bce0-4312-82ba-998be8548b46)

   Disini Member akan langsung ditampilkan Paket Streaming yang tersedia beserta harganya, yaitu Paket Basic, Standart, dan Premium.
   
   ### 2. Purchase a package
   Admin dapat membeli dan berlangganan paket yang tersedia.

   ![image](https://github.com/user-attachments/assets/38b1c63c-c407-430f-9f08-bd35936914f2)
    
   Untuk masuk ke opsi "Purchase a package" inputkan angka 2. Lalu diminta input nomor paket yang ingin dibeli dan berlangganan.

   ![image](https://github.com/user-attachments/assets/afd50bcb-5832-4230-a0ff-86cb72eace0f)

   Lalu, konfirmasi pembayaran beserta harga total. User diminta memilih opsi "Yes" atau "No".
   
   - Jika user memilih opsi "Yes".
     
     ![image](https://github.com/user-attachments/assets/fb4eaf2b-fa38-41d5-a087-19666203dccf)

   - Jika user memilih opsi "No".

   Lanjut, user dapat melakukan transaksi kembali ketika memlilih opsi "Yes" dan diarahkan 
   

   

    




