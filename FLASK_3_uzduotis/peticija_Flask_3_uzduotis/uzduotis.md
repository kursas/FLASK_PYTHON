# Užduotis

Parašykite vienos peticijos puslapį:

- Puslapio navigacijoje turi būti nuorodos į pagrindinį puslapį ir /about.
  - Sukurti marsruta i pagrindini puslapi
  - Sukurti marsruta i about
  - Sukurti navigacija/navbar visuose puslapiuose
- Pagrindiniame puslapyje turi būti forma, kurioje reikia įvesti vardą, pavardę ir komentarą. Po ja - pasirašiusiųjų 
 sąrašas:  eil.nr, vardas pavardė, data ir komentaras 
  - Pagrindinis puslapis turi GET ir POST
  - Sukurti forma HTML'e su vardu, pavarde, komentaru
  - Israsyti sarasa su pasirasiusiais po forma
- Naudokite sqlite duomenų bazę įrašams saugoti. 
  - importuojam flask sqlalchemy
  - susikurti sqlite duomenu baze
  - Sukurti duomenu baze / lentele su formos duomenimis: vardas, pavarde, komentaras, data
- Jeigu forma užpildyta sėkmingai, sąrašas papildomas paskutiniu įrašu, o vietoje formos atsiranda padėkos žinutė.
  - Patikrinti formos duomenis
  - Is karto papildyti sarasa (kviesti nauja uzklausa)
  - Paslepti forma kai ji uzpildyta sekmingai
  - Parodyti vietoj formos padekos zinute
- Jums reikės atrasti būdą, kaip prieš sugeneruojant šabloną į duomenų bazę perkelti formos duomenis 
  - issaugoti formos duomenis irasant i duomenu baze
  - perduoti formos duomenis i HTML sablona
- Pavienės wtf-formos reikšmės traukiamos taip, pvz: form.name.data 
- Formos validacijas palikite pabaigai, jeigu liks laiko.

