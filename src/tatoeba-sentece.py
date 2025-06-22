from anki.collection import Collection
import csv

def load_sentences(file_path):
    sentences = []
    with open(file_path, "r", encoding="utf-8") as tsv_file:
        reader = csv.reader(tsv_file, delimiter="\t")
        for row in reader:
            if len(row) >= 4:
                chinese_sentence = row[1]
                english_translation = row[3]
                sentences.append((chinese_sentence, english_translation))
    return sentences


def fetch_example_sentences(word, sentences_list, max_matches=5):
    matches = []
    for chinese_sentence, english_translation in sentences_list:
        if word in chinese_sentence:
            matches.append((chinese_sentence, english_translation))
        if len(matches) >= max_matches:
            break
    return matches


sentences_list = load_sentences(
    "/Users/vinitmiranda/Documents/GitHub/anki-addon/sentences-no-duplicates.tsv"
)
col = Collection(
    "/Users/vinitmiranda/Library/Application Support/Anki2/User 1/collection.anki2"
)
note_type = "Vocabulary"
note_model = col.models.by_name(note_type)
note_ids = col.models.nids(note_model)

for index, nid in enumerate(note_ids):
    note = col.get_note(nid)
    simplified_word = note["Simplified"]
    example_sentences = fetch_example_sentences(
        simplified_word, sentences_list, max_matches=5
    )

    # Add the sentences and translations to the note fields
    for i, (chinese_sentence, english_translation) in enumerate(example_sentences):
        note[f"Sentence {i + 1}"] = chinese_sentence
        note[f"Translation {i + 1}"] = english_translation

    # Fill remaining fields with empty strings if fewer than 5 matches are found
    for i in range(len(example_sentences), 5):
        note[f"Sentence {i + 1}"] = ""
        note[f"Translation {i + 1}"] = ""

    # print(f"Word: {simplified_word}, Sentences: {example_sentences}")
    col.update_note(note)
