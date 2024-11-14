# Instrukcja dzialania aplikacji

## Opis aplikacji

Aplikacja jest prostym narzedziem, ktore laczy sie z API OpenAI w celu przetworzenia pliku tekstowego z artykulem i zapisania go w formacie HTML. Glowne kroki dzialania aplikacji to:

1. Odczytanie pliku tekstowego z artykulem (plik `artykul.txt`).
2. Przeslanie tresci artykulu do API OpenAI w celu wygenerowania nowego artykulu w formacie HTML.
3. Zapisanie wygenerowanego artykulu do pliku `artykul.html` oraz `podglad.html`.

Aplikacja uzywa modelu OpenAI `gpt-3.5-turbo` do wygenerowania tresci artykulu, w tym dodania miejsc na grafiki z odpowiednimi tagami HTML.

## Instrukcja uruchomienia

### Wymagania wstepne

- Python 3.7 lub nowszy.
- Zainstalowany modul OpenAI.

Aby zainstalowac modul OpenAI, uruchom ponizsze polecenie:

```bash
pip install openai
```

### Klucz API

Aby aplikacja mogla polaczyc sie z API OpenAI, potrzebny jest klucz API. Klucz nalezy ustawic w pliku `article_generator.py`, przypisujac go do zmiennej `openai.api_key`:

```python
openai.api_key = 'YOUR_OPENAI_API_KEY'
```

### Instrukcja uruchomienia aplikacji

1. Upewnij sie, ze plik `artykul.txt` znajduje sie w tym samym katalogu, co skrypt `article_generator.py`. Plik `artykul.txt` powinien zawierac tresc, ktora chcesz przetworzyc.
2. Upewnij sie, ze plik `szablon.html` jest dostepny w tym samym katalogu. Plik ten sluzy jako szablon do generowania pliku `podglad.html`.
3. Uruchom skrypt `article_generator.py` za pomoca ponizszego polecenia:

```bash
python article_generator.py
```

4. Po pomyslnym uruchomieniu skryptu, wygenerowany artykul w formacie HTML zostanie zapisany w plikach `artykul.html` oraz `podglad.html`.

### Struktura projektu

- `article_generator.py` - glowny skrypt aplikacji.
- `artykul.txt` - plik wejsciowy z trescia artykulu.
- `artykul.html` - plik wynikowy z wygenerowanym artykulem w formacie HTML.
- `szablon.html` - pusty szablon HTML do wizualizacji artykulu.
- `podglad.html` - plik wynikowy z pelnym HTML, lacznie z zawartoscia szablonu.

### Informacje dodatkowe

Wygenerowany plik `artykul.html` nie zawiera znacznikow `<html>`, `<head>` ani `<body>`, zgodnie z wymaganiami zadania. Skrypt generuje tylko zawartosc do umieszczenia wewnatrz `<body>`. Plik `podglad.html` zawiera natomiast kompletny kod HTML, wykorzystujac tresc z `szablon.html` oraz wygenerowany artykul.

W razie jakichkolwiek pytan lub problemow prosze o kontakt.