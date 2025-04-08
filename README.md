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

  # Pokretanje Hadoop i YARN servisa

## 1. Kreiranje korisnika za Hadoop i YARN

Pre nego što pokrenemo Hadoop i YARN servise, potrebno je kreirati odgovarajuće korisnike:

```sh
sudo adduser hadoop
sudo adduser yarn
```

Nakon toga, prijavljujemo se na Hadoop korisnika i pokrećemo HDFS servis.

## 2. Pokretanje Hadoop Distributed File System (HDFS)

Da bismo pokrenuli **HDFS**, koristimo sledeće komande:

```sh
su - hadoop
sudo ./sbin/start-dfs.sh
```

Ovo će pokrenuti **NameNode** i **DataNode** servise, koji su ključni za distribuisano skladištenje podataka u Hadoop sistemu.

<img src="https://github.com/DajanaRadovic/BigData/blob/main/images/hadoopKorisnik.png" alt="Opis slike" width="500"/>

## 3. Pokretanje YARN servisa

**YARN (Yet Another Resource Negotiator)** se koristi za raspodelu resursa i izvršavanje zadataka u Hadoop klasteru. Da ga pokrenemo, koristimo sledeće komande:

```sh
su - yarn
sudo ./sbin/start-yarn.sh
```

Ovo će pokrenuti **ResourceManager** i **NodeManager** procese.

<img src="https://github.com/DajanaRadovic/BigData/blob/main/images/yarn.png" alt="Opis slike" width="500"/>

## 4. Provera aktivnih servisa

Da bismo proverili da li su servisi ispravno pokrenuti, koristimo komandu:

```sh
jps
```

Ako su svi servisi uspešno pokrenuti, trebalo bi da vidimo sledeći izlaz (ili sličan):

```
1234 NameNode
5678 DataNode
9101 ResourceManager
1121 NodeManager
1314 SecondaryNameNode
```

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

   <img src="https://github.com/DajanaRadovic/BigData/blob/main/images/Figure2.png" alt="Opis slike" width="500"/>

### Job3: Ukupno broj pacijenata u ICU i bolnicama po datumima

Ovaj zadatak analizira broj pacijenata na intenzivnoj nezi i u bolnicama po datumima:

1. **Učitani su podaci** o pacijentima u ICU i bolnicama, i `fillna` funkcije su korišćene za popunjavanje praznih vrednosti.
2. **Izračunat je ukupni broj pacijenata** po datumu.
3. **Rezultati su prikazani** u obliku **bar grafikona** sa najvišim brojevima pacijenata.

    <img src="https://github.com/DajanaRadovic/BigData/blob/main/images/Figure3.png" alt="Opis slike" width="500"/>

## Korišćeni alati

- **PySpark**: za rad sa velikim podacima.
- **Matplotlib**: za generisanje grafova i vizualizaciju podataka.
- **HDFS**: kao sistem za skladištenje podataka.
- **YARN**: za distribuciju resursa.


## Postavke za Spark sesiju

Za pokretanje Spark sesije koristi se sledeća konfiguracija:

`python
spark = SparkSession.builder \
    .appName("Job1") \
    .config("spark.executor.memory", "1G") \
    .config("spark.executor.cores", "1") \
    .config("spark.driver.memory", "1G") \
    .getOrCreate()`

<img src="https://github.com/DajanaRadovic/BigData/blob/main/images/hadoop.png" alt="Opis slike" width="500"/> 

<img src="https://github.com/DajanaRadovic/BigData/blob/main/images/terminal.png" alt="Opis slike" width="500"/> 

## Uputstvo za pokretanje

1. **Postavite Hadoop i Spark** u klasteru.
2. **Učitajte CSV podatke** u HDFS.
3. **Pokrenite Spark sesiju** koristeći prethodno definisane konfiguracije.
4. **Izvršite svaki od jobova** (Job1, Job2, Job3) prema uputstvima.


