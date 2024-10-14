# MINI-PROJECT-DASAR PEMOGRAMAN 2
Nama : Aliyah Azzah Sekedang

Kelas : A

Tema : Sistem Langganan atau Membership Layanan Streaming (Netflix)

## Flowchart
![MINPRO DASPRO 2 Aliyah Azzah S drawio](https://github.com/user-attachments/assets/ca807a3d-12dd-4f7d-b1aa-be1eb60d3a35)

## Menu Utama
![image](https://github.com/user-attachments/assets/fe040ba7-4ac8-4849-a642-dce76048e9b2)

Saat program dimulai, akan muncul Menu Utama (Main Menu). Disini, user diminta untuk memilih Login sebagai Admin atau Member.

## Menu Login
Setelah memilih 'Role', user diminta memasukkan Username dan Password.

1) Login sebagai Admin, bisa melakukan sistem CRUD (Create, Read, Update, Delete) pada database paket streaming.

2) Login sebagai Member, hanya dapat melakukan transaksi dan menampilkan paket streaming yang telah dibeli.

- Seandainya jika user menginput role mode selain Admin atau Member.

![image](https://github.com/user-attachments/assets/5a5c728e-2668-493e-89b7-7ccf94f198a7)

jika user menginput role mode selain Admin atau Member, maka otomatis akan kembali ke Menu Login.

## Menu Admin
Pada mode Admin, user akan diberikan 6 opsi dalam Menu Admin seperti pada gambar dan user diminta untuk menginput opsi sesuai dengan kebutuhan.

![image](https://github.com/user-attachments/assets/10471ed8-1dba-4b17-b95b-2219f23c2847)

- Jika user memasukkan Username dan Password yang tidak sesuai.
  
  ![image](https://github.com/user-attachments/assets/fa556cda-73b3-49bf-9315-4d00a306dd7b)

  maka otomatis akan kembali diminta memasukkan ulang.
  
- Jika login sebagai Admin berhasil, akan muncul Menu Admin dengan opsi:

  ![image](https://github.com/user-attachments/assets/5f0e0542-07a9-45ba-9cc3-735085a46bf3)

## Penjelasan Menu Admin

  ### 1. View a package
  Admin dapat melihat semua paket yang tersedia.
  
  ![image](https://github.com/user-attachments/assets/21dc774f-7613-48f0-b9be-d217dc5d21c5)

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

  - Jika sudah ada transaksi yang dilakukan, ditampilkan tulisan. Seharusnya member dapat menjual 
    

  ### 6. Logout
  Ketika Admin telah selesai menggunakan Menu Admin, Admin dapat memilih opsi ke 6 yaitu Logout. Setelah memasukkan opsi 6, maka user akan logout sebagai Admin. Lalu, diarahkan untuk Exit atau keluar dari program.

  ![image](https://github.com/user-attachments/assets/4eab3461-9fe7-48ea-a2ea-c5dabba2d159)

   - Ketika memilih "no" maka user diarahkan kembali ke Menu Login.

     ![image](https://github.com/user-attachments/assets/bba1c793-2c37-454b-b7fb-e39963dc8b9c)
     
   - Ketika memilih "yes" maka user telah keluar dari program.

     ![image](https://github.com/user-attachments/assets/4e98e861-63d9-4093-a929-762c70c97646)

## Menu Member

Pada mode Member, user akan diberikan 3 opsi dalam Menu Member seperti pada gambar dan user diminta untuk menginput opsi sesuai dengan kebutuhan.

![image](https://github.com/user-attachments/assets/edfa9e50-6c1f-41f8-bee4-803ff39ff761)

- Jika user memasukkan Username dan Password yang tidak sesuai.

 ![image](https://github.com/user-attachments/assets/76a53d27-6767-41d5-9cd6-2790edd02d56)

 maka otomatis akan kembali diminta memasukkan ulang.

 - Jika login sebagai Member berhasil, akan muncul Menu Member dengan opsi:

 ![image](https://github.com/user-attachments/assets/28d60830-a36f-40a0-8f18-a14c3b2a56ae)

## Penjelasan Menu Member

   ### 1. View all Package

   Member dapat melihat semua paket yang tersedia.
  
   ![image](https://github.com/user-attachments/assets/cc0e1f23-bf8d-4af5-a6ac-336d69d6a737)
  
   Untuk masuk ke opsi "View a package" inputkan angka 1.

   ![image](https://github.com/user-attachments/assets/310b9c91-bce0-4312-82ba-998be8548b46)

   Disini Member akan langsung ditampilkan Paket Streaming yang tersedia beserta harganya, yaitu Paket Basic, Standart, dan Premium.
   
   ### 2. Purchase a package
   
   Member dapat membeli dan berlangganan paket yang tersedia.

   ![image](https://github.com/user-attachments/assets/38b1c63c-c407-430f-9f08-bd35936914f2)
    
   Untuk masuk ke opsi "Purchase a package" inputkan angka 2. Lalu diminta input nomor paket yang ingin dibeli dan berlangganan.

   ![image](https://github.com/user-attachments/assets/b673ae23-fc44-4c2f-a681-92eee6609e7b)

   Lalu, konfirmasi pembayaran dengan ditampilkan Nama paket beserta Harga total. User diminta memilih opsi "yes" atau "no".
   
   - Jika user memilih opsi "yes".
     
     ![image](https://github.com/user-attachments/assets/3910f3c1-bea5-40e7-a0dd-dfe424c20b9b)

     maka, pembayarannya telah berhasil dan user akan diarahkan kembali jika ingin melakukan transaksi ulang.

   - Jika user memilih opsi "no".
    
     ![image](https://github.com/user-attachments/assets/627263f4-dece-47db-9f52-626497b594b1)

     maka, user ditanya apakah ingin melakukan transaksi kembali atau tidak. Jika memilih opsi "yes", user akan diarahkan kembali ke opsi "Purchase a package.

     ### 3. View Transactions
     
     Member dapat melihat paket yang telah dibelinya.
     
  Admin dapat melihat semua transaksi yang telah dilakukan oleh Member.
  
  - Jika belum ada transaksi yang dilakukan, ditampilkan tulisan "No transactions yet." dan kembali ditampilkan Menu Admin.
    
  ![image](https://github.com/user-attachments/assets/a24ba8f0-ab49-4777-b5b5-4379469a0935)

  - Jika sudah ada transaksi yang dilakukan, ditampilkan tulisan. Seharusnya member dapat menjual 
    

   ### 5. Logout
  Ketika Admin telah selesai menggunakan Menu Admin, Admin dapat memilih opsi ke 6 yaitu Logout. Setelah memasukkan opsi 6, maka user akan logout sebagai Admin. Lalu, diarahkan untuk Exit atau keluar dari program.

  ![image](https://github.com/user-attachments/assets/4eab3461-9fe7-48ea-a2ea-c5dabba2d159)

   - Ketika memilih "no" maka user diarahkan kembali ke Menu Login.

     ![image](https://github.com/user-attachments/assets/bba1c793-2c37-454b-b7fb-e39963dc8b9c)
     
   - Ketika memilih "yes" maka user telah keluar dari program.

     ![image](https://github.com/user-attachments/assets/4e98e861-63d9-4093-a929-762c70c97646)


     
   
   

   

    




