from anki.collection import Collection

col = Collection(
    "/Users/vinitmiranda/Library/Application Support/Anki2/User 1/collection.anki2"
)

note_type = ""
note_model = col.models.by_name(note_type)
note_ids = col.models.nids(note_model)

# Make sure all the fields are added in Anki
def modify_note(note):
    pass

note_type = "Vocabulary"
note_model = col.models.by_name(note_type)
note_ids = col.models.nids(note_model)
for index, nid in enumerate(note_ids):
    note = col.get_note(nid)
    modify_note(note)
    col.update_note(note)



