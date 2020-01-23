# Fejlesztői dokumentáció
## Vonal követő robot
#### Raboczki Csongor (Neptun kód: HFJQX4)


## Tervezési fázis: 
Tervezési fázis első lépése az volt hogy, kiválasszam a small board computert ami az egészet irányitani fogja. 
A választásom egy Raspberry Pi 3 B+ modell-re esett. Nemes egyszerűség miatt, mert ezt tudtam leggyorsabban beszerezni. 
Alkatrészek melyek még szükségesek voltak a projekt elkészítéséhez az két motor, egy motor vezérlő modul, egy négy darab AA elem 
 sorban való összekötésére szolgáló tartó és kettő optikai érzékelő 
mely figyelni fogja a pályaként lehelyezett vonalat. Ezeket az alkatrészeket Kínából szereztem be Aliexpressen keresztül. Lehet venni erre 
létrehozott csomagokat(úgynevezett kiteket) de mivel számomra belőle csak pár alkatrészre volt szükség egyesével szereztem be őket.
Ebböl késöbb problémáim is akadtak, hiszen nem teljesen megbízható a nagy távú csomag szállítés ebböl kifolyólag el is veszett egy csomagom. A robot vázát elöször műanyagból képzeltem el, amelyet megtervezek és egy 3D nyomtató segítségével kinyomtatok végül vastag karton lapok összeragasztásánal maradtam az egyszerübb kezelhetőség miatt.

## Felmerülő problémák: 
 -Elveszett csomag problémája: Az egyik csomagom mely tartalmazta az elem tartót elveszett az úton Magyarország fele. Ez abból okozott problémát, hogy a motor vezérlő elektronika 12V segítségével műkodik tökéletesen. Raspberry Pi 3 Modell B+ kimenetein a legnagyobb feszültség 5V. De a modul képes működni csak 5V segítségével is. Így ez a probléma elhárult.
 
 -Váz problémája: Nem várt szállítási időtartamok miatt (átlagosan 2 hónap volt) megnehezítette a végleges váz megtervezését. Ennek megoldására erős karton lapokból építettem meg a kocsi alvázát és a tetejére ragasztottam falakat melyek a helyükön tartják az ott elhelyezett modulokat. Ezáltal könyebben kezelhetőbb lett a váz, és esetleges módosítás könnyebben végrehajtható.
 

## Áramköri rajzok, felhasznált elemek:

Felhasznált elemek: 
- Raspberry Pi 3 Modell B+
- Kettő DC motor
- Motor vezérlő modul
- Kettő optikai érzékelő
- Kettő bútorkerék (az első tengely szabadon futása miatt)

#### Kötési rajz:

![KötésiRajz (1)](https://user-images.githubusercontent.com/54138095/72931790-cd5f0c80-3d5e-11ea-9a2a-c68847e85022.PNG)

#### Motor vezérlő áramköri rajza:
![motorvezerlomodul](https://user-images.githubusercontent.com/54138095/72931934-0b5c3080-3d5f-11ea-92d8-66d677714a82.png)

## Hardver specifikációk:
#### Raspberry Pi 3 Model B+: 
- Broadcom 1.4GHz 64-bit quad-core processzorral rendelkezik
- Broadcom Videocore-IV grafikai egység
- 1GB LPDDR2 SDRAM
- 40 GPIO pin output és input lehetőség

#### TT DC motor:
- 3V-12V között üzemel
- 3 Volton 70mA
#### Motor vezérlő modul:
- Fő kontroller chip: L298N
- Logikai feszültség: 5V
- Maximális teljesítmény 25W

#### Vonal követő szenzor:
- Digitális output jel
- 5V szükséges a működtetéséhez
- 1-3 cm érzékelési távolság
- Led, amely segíti a fejlesztést(Fekete felület: 0 jelet ad, fehér felületen 1 jelet ad)
- Potenciométer az érzékenység állításához

## Szoftver specifikációk:
A robot szoftverét Python nyelven írtam meg. Python IDLE környezetbe futtatok egy while ciklust ami folyton fut és control+C billenytyű kombinációval szakítható meg.


## Fejlesztett kódok részletezése:
Elöször is azonosítom a bemeneteket, hogy melyik GPIO pin-re kötöttem az adott motort és infra érzékelőt.
```python
import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(20,IO.IN) #GPIO 20 -> Bal infra erzekelo
IO.setup(26,IO.IN) #GPIO 26 -> Jobb infra erzeklo

IO.setup(8,IO.OUT) #GPIO 8 -> Jobb motor terminal A
IO.setup(7,IO.OUT) #GPIO 7 -> Jobb motor terminal B

IO.setup(9,IO.OUT) #GPIO 9 -> Bal motor terminal A
IO.setup(10,IO.OUT) #GPIO 10 -> Bal motor terminal B
Végtelen ciklusba működtetem a robotot.
```python
while 1:
```
Ha mindkettő érzékelő fekete felületet lát akkor mindkettő motor áll. Pálya végeken elhelyezet keresztbe lévő fekete csík jelzi a pálya végét.
```python
if(IO.input(20)==True and IO.input(26)==True): #mindketto motor all    
        IO.output(8,True) #1A+
        IO.output(7,True) #1B-

        IO.output(9,True) #2A+
        IO.output(10,True) #2B-
```
Jobbra fordulás: Forduláshoz mindkettő motort működtetem. Ellentétes irányba forgatom őket. Ezzel megkönnyítve a fordulást. Ellenkező esetben szűk fordulókkal problémái adódhatnak.

```python
elif(IO.input(2)==False and IO.input(3)==True): #jobbra fordul 
        IO.output(4,False) #1A+
        IO.output(14,True) #1B-

        IO.output(17,True) #2A+
        IO.output(18,False) #2B-
```

Balra fordulás, ugyanazon az elven mint a jobbra iránynál csak most ellentétesen.

```python
elif(IO.input(2)==True and IO.input(3)==False): #Balra fordul
        IO.output(4,True) #1A+
        IO.output(14,False) #1B-

        IO.output(17,False) #2A+
        IO.output(18,True) #2B-
```
Előre irány megvalósítása:
```python
else:  #megy elore
        IO.output(4,True) #1A+
        IO.output(14,False) #1B-

        IO.output(17,True) #2A+
        IO.output(18,False) #2B-
 ```
 

## Képek a kész projektről:
