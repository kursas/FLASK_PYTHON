PUNKTAI:
- Svetainė turi tris puslapius: 
  - pagrindinis (biudžeto overview, pajamų ir išlaidų istorija), balansas
  - Forma pajamų puslapyje: siuntėjas, extra info, suma
  - Forma išlaidų puslapyje: atsiskaitymo būdas, prekė/paslauga, suma
- Flask:
  - maršrutai į pagrindinį, pajamų, išlaidų puslapius
- HTML:
  - base šablonas su navigacija
  - flask_wtf forma pajamų ir išlaidų puslapyje (siųsti per argumentą return_template)
- Duomenų bazė: 
  - dvi lentelės:
    - pajamos: siuntėjas, extra info, data, suma
    - išlaidos: atsiskaitymo būdas, comment, data, suma
  - ARBA (sunkesnis būdas) viena lentelė
    - irašas: siuntėjas (nullable), atsiskaitymo būdas (nullable), comment, data, suma, argumento tipas (pajamos ar išlaidos)

UZDUOTIS:

Perdaryti prieš tai kurtą biudžeto programą, kad ji būtų su grafine vartotojo sąsaja (Flask), duomenų baze (SQLAlchemy).
  
Seno biudžeto užduotis:

Padaryti minibiudžeto programą, kuri:

- Leistų vartotojui įvesti pajamas
- Leistų vartotojui įvesti išlaidas
- Leistų vartotojui parodyti pajamų/išlaidų balansą
- Leistų vartotojui parodyti biudžeto ataskaitą (visus pajamų ir išlaidų įrašus su sumomis)
- Leistų vartotojui išeiti iš programos

Rekomendacija:
- Programa turi turėti klasę Irasas, kuri turėtų argumentus tipas (Pajamos arba Išlaidos) ir suma. Galima prirašyti str metodą, kuris gražintų, kaip bus atvaizduojamas spausdinamas objektas.
- Programa turi turėti klasę Biudzetas, kurioje būtų:
  - Metodas init, kuriame sukurtas tuščias sąrašas zurnalas, į kurį bus dedami sukurti pajamų ir išlaidų objektai 
  - Metodas prideti_pajamu_irasa(self, suma), kuris priimtų paduotą sumą, sukurtų pajamų objektą ir įdėtų jį į biudžeto žurnalą 
  - Metodas prideti_islaidu_irasa(self, suma), kuris priimtų paduotą sumą, sukurtų išlaidų objektą ir įdėtų jį į biudžeto žurnalą 
  - Metodas gauti_balansą(self), kuris gražintų žurnale laikomų pajamų ir išlaidų balansą. 
  - Metodas parodyti_ataskaita(self), kuris atspausdintų visus pajamų ir išlaidų įrašus (nurodydamas kiekvieno įrašo tipą ir sumą).

