from anki.collection import Collection

def load_character_meanings(file_path):
    meanings = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            # Skip comment lines
            if line.startswith('#') or line.startswith('!'):
                continue
            
            parts = line.split('/', 1)
            if len(parts) >= 2:
                # Extract character and meaning
                character = parts[0].split(' ')[1]
                meaning = parts[1].strip()
                if (len(character) == 1):
                    meanings[character] = meaning
    return meanings

col = Collection(
    "/Users/vinitmiranda/Library/Application Support/Anki2/User 1/collection.anki2"
)

character_meanings = load_character_meanings("cedict_ts.u8")
note_type = "Vocabulary"
note_model = col.models.by_name(note_type)
note_ids = col.models.nids(note_model)
for nid in note_ids:
    note = col.get_note(nid)
    simplified_word = note["Simplified"]
    
    # Split the word into individual characters
    morphemes = [char for char in simplified_word]
    
    # Get meanings for each character
    morpheme_meanings = [(char, character_meanings.get(char, "N/A")) for char in morphemes]
    morpheme_meaning_strings = [f"{char}: {meaning[:-1]}" for char, meaning in morpheme_meanings]
    note["Morphemes"] = '\n'.join(morpheme_meaning_strings)
    print(note["Morphemes"], "\n")
    note.flush()

