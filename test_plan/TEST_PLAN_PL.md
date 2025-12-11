# VodQA Mobile App - Test Plan

## Informacje o aplikacji

| Właściwość | Wartość |
|------------|---------|
| Aplikacja | VodQA.apk |
| Package | com.vodqareactnative |
| Platforma | Android |
| Automatyzacja | UiAutomator2 + Appium |

---

## Scenariusze testowe

### TC-00: Logowanie do aplikacji

| ID | TC-00 |
|----|-------|
| **Nazwa** | Logowanie użytkownika do aplikacji VodQA |
| **Priorytet** | P0 - Krytyczny |
| **Warunki wstępne** | Aplikacja zainstalowana, urządzenie podłączone |

**Kroki:**
1. Uruchom aplikację VodQA
2. Poczekaj na załadowanie strony logowania
3. Wprowadź login: `admin`
4. Wprowadź hasło: `admin`
5. Kliknij przycisk 'LOG IN'

**Oczekiwany rezultat:**
- Użytkownik zostaje zalogowany
- Wyświetla się strona "Samples List"

---

### TC-01: Native View (Chained View)

| ID | TC-01 |
|----|-------|
| **Nazwa** | Nawigacja w widoku natywnym |
| **Priorytet** | P2 |
| **Content Descriptor** | `chainedView` |
| **Warunki wstępne** | Użytkownik zalogowany |

**Kroki:**
1. Na liście Samples List znajdź opcję 'Native View'
2. Kliknij na 'Native View'
3. Zweryfikuj elementy na ekranie
4. Kliknij przycisk 'Back'

**Oczekiwany rezultat:**
- Ekran Native View otwiera się poprawnie
- Elementy UI są widoczne
- Powrót do Samples List działa prawidłowo

---

### TC-02: Slider

| ID | TC-02 |
|----|-------|
| **Nazwa** | Interakcja z suwakiem |
| **Priorytet** | P3 |
| **Content Descriptor** | `slider1` |
| **Warunki wstępne** | Użytkownik zalogowany |

**Kroki:**
1. Na liście Samples List znajdź opcję 'Slider'
2. Kliknij na 'Slider'
3. Przeciągnij suwak w różne pozycje (0%, 50%, 100%)
4. Zweryfikuj zmianę wartości
5. Kliknij przycisk 'Back'

**Oczekiwany rezultat:**
- Suwak reaguje na gesty przeciągania
- Wartość suwaka zmienia się poprawnie
- Nawigacja wstecz działa prawidłowo

---

### TC-03: Vertical Swiping

| ID | TC-03 |
|----|-------|
| **Nazwa** | Przewijanie pionowe |
| **Priorytet** | P3 |
| **Content Descriptor** | `verticalSwiping` |
| **Warunki wstępne** | Użytkownik zalogowany |

**Kroki:**
1. Na liście Samples List znajdź opcję 'Vertical Swiping'
2. Kliknij na 'Vertical Swiping'
3. Wykonaj gest przewijania w górę
4. Wykonaj gest przewijania w dół
5. Kliknij przycisk 'Back'

**Oczekiwany rezultat:**
- Zawartość przewija się płynnie w górę i w dół
- Gesty swipe są rozpoznawane poprawnie

---

### TC-04: Drag and Drop

| ID | TC-04 |
|----|-------|
| **Nazwa** | Przeciągnij i upuść |
| **Priorytet** | P4 |
| **Content Descriptor** | `dragAndDrop` |
| **Warunki wstępne** | Użytkownik zalogowany |

**Kroki:**
1. Na liście Samples List znajdź opcję 'Drag and Drop'
2. Kliknij na 'Drag and Drop'
3. Zidentyfikuj elementy do przeciągania
4. Przeciągnij element do strefy upuszczania
5. Zweryfikuj nową pozycję elementu
6. Kliknij przycisk 'Back'

**Oczekiwany rezultat:**
- Elementy można przeciągać
- Strefa upuszczania akceptuje elementy
- Wizualne potwierdzenie operacji

---

### TC-05: Double Tap

| ID | TC-05 |
|----|-------|
| **Nazwa** | Gest podwójnego kliknięcia |
| **Priorytet** | P4 |
| **Content Descriptor** | `doubleTap` |
| **Warunki wstępne** | Użytkownik zalogowany |

**Kroki:**
1. Na liście Samples List znajdź opcję 'Double Tap'
2. Kliknij na 'Double Tap'
3. Wykonaj gest podwójnego kliknięcia na elemencie docelowym
4. Zweryfikuj reakcję na gest
5. Kliknij przycisk 'Back'

**Oczekiwany rezultat:**
- Gest podwójnego kliknięcia jest rozpoznany
- Oczekiwana akcja zostaje wykonana
- Pojedyncze kliknięcie nie wywołuje akcji double tap

---

### TC-06: Long Press

| ID | TC-06 |
|----|-------|
| **Nazwa** | Gest długiego naciśnięcia |
| **Priorytet** | P4 |
| **Content Descriptor** | `longPress` |
| **Warunki wstępne** | Użytkownik zalogowany |

**Kroki:**
1. Na liście Samples List znajdź opcję 'Long Press'
2. Kliknij na 'Long Press'
3. Wykonaj gest długiego naciśnięcia na elemencie
4. Zweryfikuj menu kontekstowe lub reakcję
5. Kliknij przycisk 'Back'

**Oczekiwany rezultat:**
- Gest długiego naciśnięcia wywołuje akcję
- Menu kontekstowe pojawia się (jeśli dotyczy)
- Czas naciśnięcia jest poprawnie wykrywany

---

### TC-07: Photo View

| ID | TC-07 |
|----|-------|
| **Nazwa** | Przeglądanie i manipulacja zdjęciami |
| **Priorytet** | P5 |
| **Content Descriptor** | `photoView` |
| **Warunki wstępne** | Użytkownik zalogowany |

**Kroki:**
1. Na liście Samples List znajdź opcję 'Photo View'
2. Kliknij na 'Photo View'
3. Wykonaj gest powiększenia (pinch to zoom)
4. Wykonaj gest przesuwania (pan)
5. Kliknij przycisk 'Back'

**Oczekiwany rezultat:**
- Obraz wyświetla się poprawnie
- Gest powiększenia działa
- Gest przesuwania działa
- Jakość obrazu zachowana podczas transformacji

---

### TC-08: Web View

| ID | TC-08 |
|----|-------|
| **Nazwa** | Wyświetlanie zawartości webowej |
| **Priorytet** | P5 |
| **Content Descriptor** | `webView` |
| **Warunki wstępne** | Użytkownik zalogowany |

**Kroki:**
1. Na liście Samples List znajdź opcję 'Web View'
2. Kliknij na 'Web View'
3. Poczekaj na załadowanie zawartości webowej
4. Zweryfikuj wyświetlanie treści
5. Wykonaj interakcję z elementami web (jeśli dostępne)
6. Kliknij przycisk 'Back'

**Oczekiwany rezultat:**
- WebView ładuje się poprawnie
- Zawartość webowa jest wyświetlana
- Brak błędów ładowania
- Elementy web są interaktywne

---

### TC-09: Carousel

| ID | TC-09 |
|----|-------|
| **Nazwa** | Nawigacja w karuzeli |
| **Priorytet** | P5 |
| **Content Descriptor** | `carousel` |
| **Warunki wstępne** | Użytkownik zalogowany |

**Kroki:**
1. Na liście Samples List znajdź opcję 'Carousel'
2. Kliknij na 'Carousel'
3. Przesuń w lewo (następny element)
4. Przesuń w prawo (poprzedni element)
5. Zweryfikuj wskaźnik aktualnego elementu
6. Kliknij przycisk 'Back'

**Oczekiwany rezultat:**
- Karuzela wyświetla elementy do przewijania
- Przesunięcie w lewo pokazuje następny element
- Przesunięcie w prawo pokazuje poprzedni element
- Płynne animacje przejścia

---

### TC-10: Wheel Picker

| ID | TC-10 |
|----|-------|
| **Nazwa** | Wybór wartości z koła wyboru |
| **Priorytet** | P5 |
| **Content Descriptor** | `wheelPicker` |
| **Warunki wstępne** | Użytkownik zalogowany |

**Kroki:**
1. Na liście Samples List znajdź opcję 'Wheel Picker'
2. Kliknij na 'Wheel Picker'
3. Przewiń koło wyboru, aby wybrać różne wartości
4. Zweryfikuj wybraną wartość
5. Kliknij przycisk 'Back'

**Oczekiwany rezultat:**
- Wheel picker reaguje na gesty przewijania
- Wybrana wartość jest podświetlona
- Wartość można odczytać programowo

---

## Podsumowanie

| Kategoria | Liczba testów |
|-----------|---------------|
| Autentykacja | 1 |
| Nawigacja | 10 |
| Gesty | 7 |
| Komponenty UI | 5 |
| **Razem** | **11** |

### Priorytety

| Priorytet | Opis | Liczba |
|-----------|------|--------|
| P0 | Krytyczny | 1 |
| P2 | Wysoki | 1 |
| P3 | Średni | 2 |
| P4 | Niski | 3 |
| P5 | Najniższy | 4 |

---

**Wersja dokumentu:** 1.0  
**Data aktualizacji:** 2025-12-11  
**Status:** Gotowy do implementacji

