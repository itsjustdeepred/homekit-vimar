# HomeKit Controller - Vimar Dimmer Patch

Questo repository contiene un fork automatizzato del componente core `homekit_controller` di Home Assistant, modificato specificamente per risolvere il problema del dimmeraggio delle luci e dei moduli connessi **Vimar** (serie Arké, Eikon, Plana con firmware HomeKit nativo).

## Il Problema Originale
I dispositivi Vimar soffrono di un bug nel firmware HomeKit: se ricevono il comando di accensione (`ON: True`) e il valore di luminosità (`BRIGHTNESS`) all'interno dello stesso pacchetto dati (payload), ignorano la luminosità e forzano la luce al 100%. All'atto pratico, muovendo il dimmer dall'interfaccia di Home Assistant, la luminosità si aggiorna per un istante e poi schizza immediatamente al 100%, rendendo impossibile la regolazione.

## La Soluzione
Sfruttando le specifiche del protocollo Apple HAP, questa patch rimuove l'invio del comando esplicito `ON` quando si invia una regolazione di luminosità. Questo forza il firmware Vimar a eseguire un'accensione implicita direttamente al livello di dimmer desiderato, ripristinando il perfetto funzionamento del cursore della luminosità.

Il fix è isolato e si applica **esclusivamente** se il produttore del dispositivo è valorizzato esattamente come `"Vimar"`, garantendo la totale assenza di regressioni o problemi per lampadine o accessori di altri marchi.

## Aggiornamenti Automatici
Questo repository viene sincronizzato automaticamente ogni notte con il ramo `main` ufficiale di Home Assistant Core. La patch viene riapplicata e iniettata sopra l'ultimo codice disponibile, garantendo un componente sempre aggiornato e compatibile con le ultime release di Home Assistant.

## Installazione tramite HACS
1. Apri **HACS** su Home Assistant.
2. Clicca sui tre puntini in alto a destra e seleziona **Repository personalizzati**.
3. Incolla l'URL di questo repository GitHub.
4. Seleziona **Integrazione** come categoria e clicca su **Aggiungi**.
5. Cerca l'integrazione appena aggiunta, clicca su **Installa** e riavvia Home Assistant.
