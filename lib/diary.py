
class Diary:
    def __init__(self):
        self.diaryentries = []

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        self.diaryentries.append(entry)

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self.diaryentries

    def count_words(self):
        word_count = [entry.count_words() for entry in self.diaryentries]
        return sum(word_count)

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        time = [entry.reading_time(wpm) for entry in self.diaryentries]
        return sum(time)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        pass
