import datetime

# Store the next available id for all the new note
last_id = 0


class Note:
    """
    Represent a note in the notebook. Match against a string in searches
    and stores tags for each note.
    """

    def __init__(self, memo, tags=''):
        '''
        initialize a note with memo and optional
        space-separated tags. Automatically set the note's
        creation date and a unique id.
        '''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        '''
        Determine if this note matches the filter
        text. Return True if it matches, False otherwise .
        Search is case sensitive and matches both text and
        tags.
        '''
        return filter in self.memo or filter in self.tags


class Notebook:
    """
    Representation of a group of notes that can be searched, tagged and modified.
    """

    def __init__(self):
        """
        Initializes the repository with an empty list of notes.
        """
        self.notes = []

    def new_note(self, memo, tags=''):
        """
        Creates and add new notes to the notebook.
        """
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        """
        Find the note with the given note_id
        """
        for note in self.notes:
            if note_id == note.id:
                return note
        return None

    def modify_memo(self, note_id, memo):
        """
        Searches for the note with the note_id and updates the memo.
        """
        note = self._find_note(note_id)
        note.memo = memo

    def modify_tags(self, note_id, tags):
        """
        Find the note with the given id and change its
        tags to the given value.
        """
        note = self._find_note(note_id)
        note.tags = tags

    def search(self, filter):
        """
        Find all notes that match the given filter string.
        """
        return [note for note in self.notes if note.match(filter)]
