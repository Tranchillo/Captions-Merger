# Captions-Merger.py

Questo script Python unisce più file di testo (.txt) presenti nella cartella corrente in un unico file, mantenendo il nome del file originale come prefisso per ogni riga.

## Descrizione

Lo script esegue le seguenti operazioni:
1. Cerca tutti i file .txt nella cartella in cui viene eseguito
2. Crea un nuovo file chiamato `caption_list.txt` (o `caption_list_N.txt` se il file esiste già)
3. Per ogni file di testo trovato:
   - Legge il contenuto
   - Rimuove i ritorni a capo
   - Aggiunge una nuova riga nel file unificato con il formato: `[nome_file] [contenuto]`

## Requisiti

- Python 3.x
- I moduli utilizzati (`os` e `glob`) sono parte della libreria standard di Python, quindi non sono necessarie installazioni aggiuntive.

## Installazione

1. Clona questo repository:
```bash
git clone [URL_DEL_TUO_REPOSITORY]
```

2. Naviga nella directory del progetto:
```bash
cd [NOME_DIRECTORY]
```

## Utilizzo

1. Posiziona lo script nella cartella contenente i file .txt che vuoi unire
2. Esegui lo script:
```bash
python Captions-Merger.py
```

Il programma creerà un nuovo file `caption_list.txt` (o `caption_list_N.txt` se il file esiste già) contenente tutti i testi unificati.

## Output

- Il file di output avrà il nome `caption_list.txt`
- Se esiste già un file con questo nome, verrà creato un file con numerazione progressiva (es. `caption_list_1.txt`)
- Ogni riga del file di output avrà il formato: `[nome_file] [contenuto]`

## Gestione degli Errori

Lo script include la gestione degli errori per:
- Cartella senza file .txt
- Errori di lettura dei singoli file
- Errori generali durante l'esecuzione

## Contribuire

Sentiti libero di aprire issues o inviare pull requests per migliorare questo progetto.

## Licenza

MIT License
