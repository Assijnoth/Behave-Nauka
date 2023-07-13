1. CHANGELOG:

Wersja 0.9 Atreides
===================

Lista scenariuszy obsługiwanych przez testy automatyczne PWA:

Czy homepage nie zwraca 404                                       done -> pwa_homepage_status
Czy kategoria wyłączona zwraca homepage 404                       done -> pwa_is_off_category_404
Czy kategoria włączona odpowiada produktami                       done -> pwa_does_on_category_gives_items
Czy kategoria włączona jest widoczna w menu                       done -> pwa_is_on_category_visible_in_megamenu
Czy można dodać produkt do koszyka                                done -> pwa_add_then_remove_from_cart
Czy można usunąć produkt z kozsyka                                done -> pwa_add_then_remove_from_cart
Czy mogę zalogować się na konto testowe                           done -> pwa_signin
Czy mogę edytować adresy                                          done -> pwa_add_edit_adress
Czy mogę dodawać adresy                                           done -> pwa_add_edit_adress
Czy wyszukiwarka prawidłowo zwraca konkretną frazę testową        done -> pwa_search_engine
Czy wyszukiwarka prawidłowo nie zwraca nic nie dziwne frazy       done -> pwa_search_engine
Czy filtry i sortowanie zwracają prawidłowe dane
Czy nie zwracają zdublikowanych SKU w ramach zapytania
Czy mogę złożyć zamówienie:
   per metody płatności PayU, COD, PayU Card                      done -> pwa_dpd_order, pwa_inpost_order
   per metody shippingu Inpost, DPD                               done -> pwa_dpd_order, pwa_inpost_order
Czy mogę założyć nowego usera na wylosowany ciąg znaków           done -> pwa_new_user

Czy homepage nie jest blank page                                  Do przegadania - po czym interpretować blank page (moduły cms na stronie głównej)
Czy mogę wyłować email z przypominaniem hasła                     Do przegadania - skąd łowić meila?


2. STAŁE ELEMENTY TESTÓW:

1. Megamenu
2. Koszyk
3. Moje konto / zaloguj / przypomnij hasło / wyloguj
4. Dodaj do koszyka
5. Filtrowanie/sortowanie
6. Box z potwierdzeniem dodania do koszyka
7. Napis 404
8. Checkout - pola z placeholderami Imię, Nazwisko, Adres itd.)

Oraz XPATH input dla danych logowania
