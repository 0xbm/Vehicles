# APLIKACJA WEBOWA DO WSPOMAGANIA FLOTY POJAZDÓW
## _AutoMobile_


[![Build Progrss](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## 1. PRZEZNACZENIE

Projektowana aplikacja webowa przeznaczona jest dla właścicieli flot , logistyków oraz dla  osób, które zajmują się zarządzaniem pojazdami w firmach. Aplikacja będzie zapisywać dane dotyczące każdego pojazdu wpisywanego w programie. Głównym przeznaczeniem aplikacji jest zsumowanie wszystkich informacji na temat pojazdów w jednym miejscu co poprawi i zautomatyzuje pracę z osobom zajmującym się tym procesem. Projekt zakłada możliwość rozbudowy oprogramowania o kolejne moduły tak, aby finalnie był to pełen pakiet wszelkich programów obliczeniowych wykorzystywanych w pracy osób zajmujących się gospodarką magazynową oraz paliwową floty. 



## 2. OPIS DZIAŁANIA APLIKACJI 
Aplikacja webowa działa w oparciu o usługę chmurową, do której następuje dostęp przez klienta – przeglądarkę internetową. Użytkownik ma do dyspozycji kafelki (grid) nawigacyjne, z których wybiera odpowiednie moduły aplikacji. 

W widoku głównym, dla osób niezarejestrowanych, czeka nas tylko podgląd na wszystkie dodane pojazdy do floty. Po zarejestrowaniu się jako użytkownik platformy, dostajemy możliwość dodawania, edycji oraz usuwania pojazdów (C.R.U.D) oraz niezbędnych informacji użytych podczas tworzenia elementu takich jak:


- Brand
- Model 
- Model 
- Model 
- Model 
- Model 

Po wybraniu modułu „Add Vehicle” zostaje przekierowany na stronę , która umożliwi dodawania pojazdów do bazy danych. 
Moduł „Add Vehicle” przedstawia poniższa grafika:


Po wybraniu modułu „List Vehicle” wsyświetla się lista wszystkich pojazdów w stosie z możliwościa edycji lub usunięcia. Sytuacja wygląda tak samo w odniesieniu do modułów „List Brand”, „List Model” czy  „List Driver”.  
W aplikacji wykorzystałem możliwość wyświetlania stron (pagination) na liście pojazdów. 
W stopcje jest możliwość wysłania wiadomości mail a także ikony z linkiem prawdzacym na: Github, LinkedIn czy Twitter. 

## 3. Tech

Dillinger uses a number of open source projects to work properly:
- [git-repo-url] 
- [Python 3.11] 
- [Markdown]
- [Bootstrap] 
- [HTML]
- [CSS]
- [Java Script]

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

## 4. INSTALACJA

Instalowanie zależności wpisując w konsoli:
```sh
pip install -r requirements.txt
```

## 5. ROZPOCZECIE PRACY

```sh
127.0.0.1:8000
```

### Licencja

MIT
**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [git-repo-url]: <https://github.com/0xmb/vehicles.git>
   [markdown]: <https://www.markdownguide.org/>
   [python 3.11]: <https://www.python.org/>
   [Bootstrap]: <http://twitter.github.com/bootstrap/>
   [html]: <https://html.com/>
   [css]: <https://css.com/>
   [java script]: <https://javascript.com/>
