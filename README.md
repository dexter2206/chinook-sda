# Ćwiczenia z SQLAlchemy na bazie Chinook

Link do zrzutu bazy danych (można zaimportować np. z Workbencha): https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_MySql.sql

Opis bazy danych: https://www.sqlitetutorial.net/sqlite-sample-database/


## Ćwiczenia

### Tworzenie mapowania obiektowo relacyjnego dla wybranych tabel bazy Chinook

Proszę utworzyć mapowanie obiektowo relacyjne dla tabel: artists, albums, playlists, tracks, genres, media_types.
Należy zwrócić uwagę, że relacja pomiędzy tracks i playlists jest typu wiele do wielu!

### Kwerendy

Napisać programu realizujące następujące kwerendy.

1. Wyszukać wszystkie gatunki utworów.
2. Wyszukać wszystkie albumy wybranego artysty.
3. Wyszukać wszystkie utwory z zadanego albumu.
4. Wyszukać wszystkie utwory z zadanej playlisty.
5. Wyszukać wszystkie playlisty na których znajduje się zadany utwór.

### Wstawianie i modyfikacja rekordów

1. Dodać nowego artystę.
2. Dla dodanego artysty dodać nowy album wraz z kilkoma trackami. Zaawansowane: zastanowić się jak wykonać tę operację
   hurtowo (tzw. bulk insert)
3. Utworzyć nową playlistę z kilkoma utworami.
4. Zmienić tytuł wybraneog przez siebie utworu.
5. Remix! Zmienić gatunek wszystkich rockowych utworów na pop. Zaawansowane: użycie metody update obiektu query.
