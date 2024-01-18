# Projekta darbs

## Uzdevuma apraksts

Izmantojot Selenium bibliotēku automatizēt automašīnu meklēšanu tīmekļvietnēs, terminālī ievadot jums nepieciešamos automasīnas meklēšanas filtrus(parametrus), kā arī salīdzināt 2 auto tīmekļvietņu izdotos rezultātus. Šajā projektā tika izmantotas https://www.ss.com/ un https://lv.m.autoplius.lt/ tīmekļvietnes. Lai iegūtu vēlamos automašīnu sarakstus no šīm tīmekļvietnēm, ir nepieciešams terminālī ierakstīt nepieciešamos meklēšanas filtrus (automašīnas marku, modeli, izlaiduma gadu, degvielas tipu, ātrumkārbas tipu un virsbūves tipu), kā rezultātā tiks automātiski ievadīti šie filtri un izdoti saraksti no auto tīmekļvietnēm. Lai tiktu izvadīti saraksti ar automašīnām no tīmekļvietnēm, ir jāpievērš uzmanību dažiem nosacījumiem:

- automāšīnas meklēšanas filtri(parametri), kuri tika izmantoti šajā projektā un parādīsies terminālī, visos ir jaievada vertības, piemēram, nedrīkst ievadīt tikai automašīnas marku un modeli, bet izlaist izlaiduma gadu vai pārējos parametrus. Lai tiktu izvadīti saraksti ar automašīnām, terminālī OBLIGĀTI ir jāievada vērtības pie katra parametra;
- vērtības, kuras jūs ievadīsiet pie automašīnas parametriem atbilst tādām pašām vērtībām kā https://www.ss.com/ tīmekļvietnē, tādējādi ievadot vērtības terminālī pie automašīnu parametriem, ir japārbauda, vai vērtības tikai ierakstītas pareizi, piemēram, ja pie automašīnas markas jūs gribat ievadīt automašīnu 'Audi', tad jāraksta 'Audi', lielākai daļai automašīnu marku nosaukumi jāraksta pirmais markas burts ar lielo un pārējie ar mazu (tāpat arī degvielas tips, ātrumkārbas tips un virsbūves tips), tomēr rakstot automašīnas markas nosaukumu terminālī, ir daži izņēmumi, piemēram ja jūs gribat ievadīt BMW automašīnu, tad jums ir jāievada 'BMW' nevis 'Bmw'. Lai pārbaudītu vai vērtība tika ievadīti korekti, var apskatīt to https://www.ss.com/ tīmekļvietnē.

### Uzlabojumi, kurus varētu izdarīt, lai uzlabotu šo projektu:

- mūsu projektā, pēc parametru ievadīšanas terminālī, sākumā tiks izdots saraksts ar vēlāmajām automašīnām no https://www.ss.com/ tīmekļvietnes un tikai piespiežot terminālī pogu Enter, tikai tad tiks izdots tas pats saraksts ar automašīnām jau no https://lv.m.autoplius.lt/ tīmekļvietnes. Tādēļ šajā projektā varētu uzlabot rezultātu iegušanu, lai pēc ievadīšanas programma uzreiz vienlaicīgi izdotu 2 sarakstus ar automašīnām (gan no vienas, gan no otras tīmekļvietnes), līdz ar to vieglāk būtu salīdzināt automašīnas un preces starp 2 auto tīmekļvietnēm.


## Projekta izstrādes laikā izmantotās bibliotēkas 

### Selenium

- *Apraksts*: Selenium bibliotēka ir bibliotēka, kas ļauj veikt automatizētas pārlūkprogrammu vai tīmekļa lietojumprogrammu pārbaudes gadījumus. Tā tiek izmantota, lai simulētu darbības, piemēram, pieskaroties pogai, ievadot saturu struktūrās, pārmeklējot visu vietni utt.
- *Izmantošana mūsu projektā*: Mūsu projektā Selenium bibliotēka tika izmantota pārlūkprogrammas automatizacijai un vietņu darbības simulācijai.

### Time

- *Apraksts*: Time bibliotēka ir bibliotēka, kas nodrošina dažādas ar laiku saistītas funkcijas. Šis modulis ietilpst Python standarta utilītu moduļos. Tā ļauj izmērīt laika intervālus un izsekot ar laiku saistītus datus programmās.
- *Izmantošana mūsu projektā*: Mūsu projektā Time bibliotēka tika izmantota, lai pievienotu programmas izpildes aizkavi, apturētu programmas izpildi uz noteiktu laiku sekundēs. 


## Programmatūras izmantošanas metodes

### input()

- Projekta izstrādes laikā tika izmantotas vairākas input() funkcijas, lai saņemtu ievadi no lietotāja terminālī.

### nosacījums if

- Projekta izstrādes laikā tika izmantoti nosacījumi if, lai izveidotu nosacījumu paziņojumus, kas ļauj izpildīt koda bloku tikai tad, ja nosacījums ir patiess.
