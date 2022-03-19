# Projekt zespołowy

## Hero Realms

Aplikacja ta jest przeglądarkową pomocą do karcianej gry Hero Realms. Dzieki której nie bedziesz musiał/a już zapisywać wszystkiego na papierze.

### Lokalne uruchomienie aplikacji

1. Aby uruchomić aplikacje lokalnie wystarczy mieć zainstalowanego dockera <br /> <https://docs.docker.com/engine/install/>

2. Startujemy aplikcje:<br />
	`docker run -p 5000:5000 -d madpele/hero_realms`

3. Dzięki czemu w przeglądarce możemy ją wywołać pod adresem:<br />
	`0.0.0.0:5000`
	
### Aby lepiej zrozumieć aplikacje polecam poczytać:
Docker <https://docs.docker.com/get-started/overview/> <br />
Makefile <https://makefiletutorial.com> <br />
Travis CI <https://travis-ci.org> <br />
