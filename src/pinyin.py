from anki.collection import Collection
import pinyin_jyutping

col = Collection(
    "/Users/vinitmiranda/Library/Application Support/Anki2/User 1/collection.anki2"
)
pinyin_jyutping_module = pinyin_jyutping.PinyinJyutping()
note_type = "Vocabulary"
note_model = col.models.by_name(note_type)
note_ids = col.models.nids(note_model)

# Make sure all the fields are added in Anki
def modify_note(note):
    for i in range(5):
        if note[f"Sentence {i + 1}"] is not "":
            note[f"Pinyin {i + 1}"] = pinyin_jyutping_module.pinyin(note[f"Sentence {i + 1}"])
            
note_type = "Vocabulary"
note_model = col.models.by_name(note_type)
note_ids = col.models.nids(note_model)
for index, nid in enumerate(note_ids):
    note = col.get_note(nid)
    modify_note(note)
    col.update_note(note)



