import openai

# Ustaw swój klucz API OpenAI
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Ścieżka do pliku z artykułem
plik_artykulu = 'artykul.txt'

# Funkcja do odczytu pliku z artykułem
def odczytaj_plik(plik):
    try:
        with open(plik, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Nie znaleziono pliku: {plik}")
        return None

# Funkcja do przetwarzania treści przez API OpenAI
def przetworz_artykul_z_AI(tresc):
    if not tresc:
        return None

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Utwórz artykuł w formacie HTML na podstawie poniższego tekstu. "
                        "Użyj odpowiednich znaczników HTML takich jak <h1>, <h2>, <p>. "
                        "Dodaj miejsca na grafiki z tagiem <img src=\"image_placeholder.jpg\" alt=\"opis grafiki\"> "
                        "w odpowiednich miejscach w artykule. Nie dodawaj elementów <html>, <head> ani <body>."
                    )
                },
                {"role": "user", "content": tresc}
            ],
            max_tokens=1500,
            temperature=0.7
        )
        return response.choices[0].message['content']
    except openai.error.OpenAIError as e:
        print(f"Błąd połączenia z API OpenAI: {e}")
        return None

# Funkcja do zapisania wygenerowanego artykułu do pliku HTML
def zapisz_do_pliku(nazwa_pliku, tresc):
    try:
        with open(nazwa_pliku, 'w', encoding='utf-8') as f:
            f.write(tresc)
            print(f"Artykuł został zapisany w pliku {nazwa_pliku}")
    except IOError as e:
        print(f"Nie udało się zapisać pliku: {e}")

# Główna funkcja programu
def main():
    tresc_artykulu = odczytaj_plik(plik_artykulu)
    przetworzona_tresc = przetworz_artykul_z_AI(tresc_artykulu)
    if przetworzona_tresc:
        zapisz_do_pliku('artykul.html', przetworzona_tresc)

if __name__ == "__main__":
    main()
