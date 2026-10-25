# rescue_mission_solar_plane
Student Research Group Recruitment Project
Franciszek Zieba

1. Misja polega na skanowaniu przez drona pewnego obszaru poruszajac sie po wyznaczonych punktach w poszukiwaniu obiektu (target).
   Po znalezieniu obiektu dron zatrzymuje sie nad nim i upuszcza ladunek (klasa PayloadDropper) po czym przechodzi w tryb RTL i laduje
2. Dron startuje, wznosi sie na zadana wysokosc skanuje obszar poruszajac sie wzdluz zadanej siatki punktow i szuka punktu w ktorym 
   ma upuscic ladunek. po znalezieniu punktu przechodzi w tryb LOITER i upuszcza ladunek za pomoca serwa. Jezeli upusci ladunek,
   albo osiagnie ostatni punkt przechodzi w tryb RTL i wraca do startu oraz laduje
3. Rozwiazanie opiera sie na czterech plikach z klasami:
   drone_controller odpowiada za komunikacje z dronem i sterowanie jego akcjami
   payload_dropper odpowiada za zrzut ladunku przy pomocy serwa kiedy dron znajdzie sie nad celen
   target_detector odpowiada za sprawdzanie czy dron nie znajduje sie w dobrej odleglosci od celu. Jest to placeholder dla prawdziwego systemu detekcji np z kamery
   mission_executer odpowiada za zorganizowanie calej misji w jedna metode
   Plik main.py inicjuje wszystkie obiekty i uruchamia misje
5. Aby uruchomic program jest potrzebny mission planner i biblioteka pymavlink. uruchomic nalezy plik main.py w tym samym folderze co reszta plikow
   Jezeli to potrzebne zmienic connection_string aby program napewno polaczyl sie uzywajac dobrego protokolu i dobrego portu.
6. w mission plannerze nalezy uruchomic symulacje wybierajac drona. symulacja musi zostac uruchomiona przed uruchomieniem kodu.
7. Niestety moje rozwiazanie nie jest kompletne poniewaz nie zawiera testow. Sama misja nie przebiega w pelni prawidlowo sa problemy ze zmiana trybu
   lotu, dron zatrzymuje sie nad niektorymi punktami i wisi nieruchomo nad nimi. Niestety nie dokonczylem rozwiazywania tych problemow przed wyznaczonym terminem. W poleceniu jednak znalazl sie zapis aby oddac takze zadania ktore nie sa w pelni kompletne.
8. Brak
9. Brak prawdziwej kamery i wykrywania obiektu, zamiast tego zastosowany zostal staly punkt do ktorego program oblicza odleglosc i na tej podstawie
   decyduje o zrzucie ladunku, brak sprawdzania poziomu baterii, brak reakcji na czynniki atmosferyczne, brak unikania kolizji.
10. Rozwiazanie mozna napewno rozwinac o rzeczy wymienione w punkcie 9, zastosowanie rozpoznawania obrazu np. opencv, mozliwosc zmiany zbioru punktow
    na przyklad na przyjmowanie rogow prostokata i wyznaczanie samodzielne punktow siatki dla ruchu drona 

