#UAS Pemrograman Python
#Yoga Maulana Febriansyah 21.83.0596
#Rakhaezza Nabella 21.83.0598
#Eleazar Hendro Tri Putra 21.83.0645


import random
import array
 
MAX_PW =  10
 
ANGKA = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

HURUF_KECIL = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
HURUF_BESAR = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
 
SIMBOL = ['@', '#', '$', '%', '=', '?',  '/', '|', '~', '>',
           '*', '(', ')', '<']
 
PW = ANGKA + HURUF_KECIL + HURUF_BESAR + SIMBOL
 
rand_angka = random.choice(ANGKA)
rand_kecil = random.choice(HURUF_KECIL)
rand_besar = random.choice(HURUF_BESAR)
rand_simbol = random.choice(SIMBOL)
 
temp_pass = rand_angka + rand_kecil + rand_besar + rand_simbol
 
for x in range(MAX_PW - 4):
    temp_pass = temp_pass + random.choice(PW)
 
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)
 
password = ""
for x in temp_pass_list:
        password = password + x
         
print(password)
