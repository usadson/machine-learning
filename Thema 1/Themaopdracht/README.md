# Themaopdracht Optimalisatie: Lectoraat Energietransitie
[Projectpagina](https://techforfuture.nl/onderzoek/lopend/twomes-digital-twins-voor-de-warmtetransitie/)

**Spreker:** Ruben Cijsouw

Learn thermal inertia from time series monitoring data of 23 homes in Assendorp

2023 project wijk Assendorp
Projectdata is uit 2021/2022
Met machine learning uniek te leren hoe het huis in elkaar zit
Het project loopt nu door heel Nederland

1. Data understanding
2. Learn thermal inertia for all suitable cooling periods for each home
3. Report, summarize, visualize
4. Bonus: improve retrieval KNMI data

## Data collected, preprocessed, interpolated
Sheet bevat een grafiek
    Blauw lijn: buitentemperatuur
    Rode lijn: binnentemperatuur
    Vlakke lijn: maximumtemperatuur (setpoint van het thermostaat)

    Van 03-jan-22 tot 10-jan-22
Het doel is om een goeie lijn (naar beneden) wil hebben, moeten we interpoleren

## Doelstelling
> Kan je ervoor zorgen dat er minder energie gebruikt wordt in Nederland?

Binnen een generatie alle (verwarmingsinstalltie in) woningen van het aardgas af?

Verwarming is een groot deel van de energietransitie

## Kernpijlers
- Woning (isolatie, kierdichting, HR++glas)
- Installatie (CV-ketel, warmtepomp, biogas, waterstof, infrarood)
- Instellingen (nacht-/dagverlaging, waterzijdig inregelen, aanvoertemperatuur)
- Comformtbehoefte/gedrag (warme rrui)
- Weer (klimaatverandering)

## Architectuur Gegevensverzameling
- Huis heeft een dak en is dicht
- Boiler in het huis
- Smart Meter (P3-protocol)
- Meten met Wifi of er iemand thuis is (hoeveel)

+ OpenData van Overheid, maar ook energielabels, BAG, AHN
+ KNMI-weerdata
+ Enexis (DSO?)
+ Enelogic

Nieuw: OpenTherm Monitor (door studenten in de elektro van Windesheim)
Data wordt verstuurd naar Twomes Backoffice, gaat naar de Twomes Analysis Pipeline, verstuurt advies vanuit de 'energie dokter'

## Grafiek
- Gasverbruik
- Irradiation

## Data-analyse
> Inverse grey-box modeling as a form of machine learning

|White|Grey|Black
|-|-|-|
Deterministic equations |Prior knowledge |Databased
Physical knowledge | Data |Input-output representation
Detailed submodels |

> Hoe zo'n huis in Assendorp eruitziet, willen ze een ML-model van te maken.

**Parameters:** Building, installation, conform needs (zie hierboven)

## Model Preperation
Zorg ervoor dat als je parameters benoemd, dat je de juiste symbolen en benamingen ervan gebruikt. Deze stond in de diavoorstelling in een tabel.

- H
- Tau
- Ceff
- Aeff
- Pmax
- ETA upper;CH
- <Tset;h;d>

## Middelen
- GEKKO: ML-library (Maar hoeven we niet te gebruiken?)
- Python, pandas, numpy, scipy curve fitting

Doel: beste fit te maken voor de `thermal inertia (tau)[h]` for each of 23 Assendorp homes.

## Warmtebalans
> Kaolo veel formules, ga ik niet allemaal overtypen
### Verlies
- Transmission: warmte lekken naar buiten
- Infiltration: koude lucht naar binnen
- Ventilatie

### Winst
- Internal: mensen, apparaten, douchen/baden
- Solar irridiation
- CV-installatie (boiler + distrib)

###
Uitrekenen: de groene zinnen (mn de _specific heat loss_)

## Wat we krijgen:
> Hiervoor moet eerst een geheimhoudingsverklaring getekend voor worden.
- ZIP-bestand met CSV-bestanden en PARQUET-bestanden
- Metadata op GitHub
- Eerdere preprocessing-code mogen we gebruiken

- [edu.nl/fqjed](https://edu.nl/fqjed)

De kern van het probleem is: het huis koelt af, als je een huis hebt - vanuitgaande dat al je apparatuur uitstaat en de zon schijnt niet - stel je gaat naar huis, het is 20graden binnen, 10 buiten, als je goed geisoleerd huis hebt, is het 's ochtends 19 graden, slechtgeisoleerd, dan is het een stuk lager.

Thermische traagheid: hoeveel tijd gaat erover om het verschil tussen de binnentemperatuur en buiten- te halveren (de deltatemperatuur)
