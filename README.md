Assalamualaikum,

Sekarang kita coba main script python lagi..

sayagunakan Python 2.7

kita mau send data random di python script ke channel Thingspeak.. 

sebelah kiri adalah tampilan channel saya..

1. kita copy dulu API KEY nya. 
"API Keys">  copy key di kolom "write api key".

punya saya : 467HQZ2548W1G8LS

2. buka terminal/bash..

3. buka text editor. saya kali ini memakai nano,

untuk langsung bikin file baru.. maka tuliskan

"nano yourscript.py"
saya akan tulis
"nano send_data_thingspeak.py"

4. import modul requests, json, time, random..
	jika belum ada silakan download dulu melalui python-pip.
	
5. masukkan variabel "api_key"

6. masukkan variabel "hosts" 

7. masukkan variabel "URL"

* step 5 - 7 variabel string yaa.. jadi perlu tanda petik atau petik tunggal

8. masukkan variabel "HEADER" berbentuk json

9. buat variabel yang akan dikirim. misal disini saya bikin variabel "data_1" dan "data_2"

10. bikin variable "sleep_time"

11. selanjutnya kita bikin fungsi untuk generate dummy data.

random.randint(56,97) akan mengacak nomor dari 56 - 97.

12. oke selanjutnya bikin fungsi "send_data"

13. generate json data payload yang dikirim , lalu gunakan "requests" "post method" untuk mengirim data

14. buat looping "while True"

15. panggil fungsi generate_dummy_data() dan send_data() di dalam loop.


16. save python script dengan CTRL+O lalu exit dengan CTRL+X

17. coba jalankan script dengan memanggil "python send_data_thingspeak.py"

OOPS bad requests..coba kita teliti lagi...
disini "field1": 89"field2" : 38 kurang koma (,)

data pertama adalah 93 dan 13.. kita coba cek di thingspeak...

oke masuk..



data sudah masuk 20 detik sekali..

sekian tutorial saya.. terimakasih...

Wassalamualaikum...





