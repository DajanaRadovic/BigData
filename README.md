# Spark COVID-19 Analiza

**Ovaj projekat je razvijen korišćenjem Apache Spark-a za analizu COVID-19 podataka.**  
Podaci su preuzeti sa *Our World in Data* i učitani u HDFS za dalju obradu. Korišćenje Apache Spark-a omogućava brzu i efikasnu analizu velikih količina podataka, a aplikacija se koristi za obavljanje različitih analiza u vezi sa brojem slučajeva, brojem testova i brojem pacijenata na intenzivnoj nezi i u bolnicama. Podaci su obrađeni pomoću YARN za raspodelu resursa i paralelno izvršavanje poslova.

## Okruženje

- **Apache Spark**: Ver. 3.x
- **Hadoop**: Ver. 3.x
- **YARN**: Za raspodelu resursa
- **Python**: 3.x
- **Matplotlib**: Za vizualizaciju podataka
- **HDFS**: Za skladištenje podataka

## Postavke

- Hadoop i YARN korisnici su kreirani za upravljanje podacima u HDFS-u i raspodelu resursa.
- Spark aplikacija je postavljena da koristi resurse sa YARN-a za paralelno izvršavanje zadataka.
- Podaci su smešteni u HDFS direktorijum: 
  - `hdfs://localhost:9000/user/hadoop/owid-covid-data.csv`

## Spark Aplikacija

### Job1: Analiza ukupnog broja slučajeva po kontinentima

U ovom zadatku analizirani su podaci o broju COVID-19 slučajeva po kontinentima. Izvršen je sledeći proces:

1. **Učitani su podaci** sa CSV fajla smeštenog na HDFS-u.
2. **Filtrirani su podaci** kako bi se eliminisale NULL vrednosti u kolonama `total_cases` i `continent`.
3. **Određen je najnoviji datum** za analizu.
4. **Podaci su grupisani po kontinentima**, sumirani su ukupni brojevi slučajeva po kontinentima i rezultat je prikazan u obliku **bar grafikona** pomoću Matplotlib.

   <img src="https://github.com/DajanaRadovic/BigData/blob/main/images/Figure1.png" alt="Opis slike" width="500"/>

### Job2: Prosečan broj novih testova po lokacijama

Za ovaj zadatak, analiziran je prosečan broj novih testova po lokacijama:

1. **Učitani su podaci** sa HDFS-a i korišćene su `fillna` funkcije kako bi se popunile NULL vrednosti u kolonama `new_tests`.
2. **Izračunat je prosečan broj novih testova** po lokacijama.
3. **Rezultati su predstavljeni** u obliku **bar grafikona**.

### Job3: Ukupno broj pacijenata u ICU i bolnicama po datumima

Ovaj zadatak analizira broj pacijenata na intenzivnoj nezi i u bolnicama po datumima:

1. **Učitani su podaci** o pacijentima u ICU i bolnicama, i `fillna` funkcije su korišćene za popunjavanje praznih vrednosti.
2. **Izračunat je ukupni broj pacijenata** po datumu.
3. **Rezultati su prikazani** u obliku **bar grafikona** sa najvišim brojevima pacijenata.

## Korišćeni alati

- **PySpark**: za rad sa velikim podacima.
- **Matplotlib**: za generisanje grafova i vizualizaciju podataka.
- **HDFS**: kao sistem za skladištenje podataka.
- **YARN**: za distribuciju resursa.

## Uputstvo za pokretanje

1. **Postavite Hadoop i Spark** u klasteru.
2. **Učitajte CSV podatke** u HDFS.
3. **Pokrenite Spark sesiju** koristeći prethodno definisane konfiguracije.
4. **Izvršite svaki od jobova** (Job1, Job2, Job3) prema uputstvima.

## Postavke za Spark sesiju

Za pokretanje Spark sesije koristi se sledeća konfiguracija:

```python
spark = SparkSession.builder \
    .appName("Job1") \
    .config("spark.executor.memory", "1G") \
    .config("spark.executor.cores", "1") \
    .config("spark.driver.memory", "1G") \
    .getOrCreate()



