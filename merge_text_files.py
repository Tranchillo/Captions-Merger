import os
import glob

def merge_text_files():
    try:
        # Ottieni il percorso della cartella in cui si trova lo script
        current_folder = os.getcwd()

        # Trova tutti i file di testo nella cartella
        text_files = glob.glob(os.path.join(current_folder, "*.txt"))

        if not text_files:
            print("Nessun file di testo trovato nella cartella.")
            return

        # Determina il nome del file unificato
        output_file = os.path.join(current_folder, "caption_list.txt")
        counter = 1
        while os.path.exists(output_file):
            output_file = os.path.join(current_folder, f"caption_list_{counter}.txt")
            counter += 1

        # Crea il file unificato
        with open(output_file, "w", encoding="utf-8") as unified:
            for file in text_files:
                try:
                    file_name = os.path.splitext(os.path.basename(file))[0]  # Nome del file senza estensione
                    with open(file, "r", encoding="utf-8") as f:
                        content = f.read().strip().replace("\n", " ")  # Rimuove i ritorni a capo
                        unified.write(f"{file_name} {content}\n")
                        print(f"Contenuto di '{file}' aggiunto come '{file_name}'.")
                except Exception as e:
                    print(f"Errore durante la lettura del file '{file}': {e}")

        print(f"File unificato creato con successo: {output_file}")

    except Exception as e:
        print(f"Errore generale: {e}")

if __name__ == "__main__":
    merge_text_files()
