from lib.diary_entry import*
from lib.diary import*

"""add an entry"""
def test_add_entry():
    diaryentry = Diary()
    week1 = DiaryEntry("monday","today was a good day")
    week2 = DiaryEntry("tuesday","today was not a good day")
    diaryentry.add(week1)
    diaryentry.add(week2)
    assert diaryentry.all() == [week1, week2]

"""count words of entries in Diaryentry class
"""
def test_count_entries_from_DiaryEntry_class():
    diaryentry = Diary()
    week1 = DiaryEntry("monday","today was a good day")
    week2 = DiaryEntry("tuesday","today was not a good day")
    diaryentry.add(week1)
    diaryentry.add(week2)

    assert week1.count_words() == 5
    assert week2.count_words() == 6
    
"""count words of entries in Diary class
"""
def test_count_entries_from_Diary_class():
    diaryentry = Diary()
    week1 = DiaryEntry("monday","today was a good day")
    week2 = DiaryEntry("tuesday","today was not a good day")
    diaryentry.add(week1)
    diaryentry.add(week2)

    assert diaryentry.count_words() == 11
    
"""calculate estimate reading time in minutues of contents from DiaryEntry Class
"""
def test_estimate_reading_time():
    diaryentry = Diary()
    week1 = DiaryEntry("monday","today was a good day")
    diaryentry.add(week1)
    wpm = week1.reading_time(1)
    
    assert wpm == 5

"""calculate estimate reading time in minutues of contents from DiaryEntry Class
"""
def test_estimate_reading_time_of_two_entries():
    diaryentry = Diary()
    week1 = DiaryEntry("monday","today was a good day")
    week2 = DiaryEntry("tuesday","today was not a good day")
    diaryentry.add(week1)
    diaryentry.add(week2)
    wpm = diaryentry.reading_time(2)
    
    assert wpm == 5.5

def test_reading_chunk_on_entry():
    week1 = DiaryEntry("monday","today was a good day")
    assert week1.reading_chunk(1, 3) == 'today was a'

def test_recall_reading_chunk_on_entry():
    week1 = DiaryEntry("monday","today was a good day")
    assert week1.reading_chunk(1, 3) == 'today was a'
    assert week1.reading_chunk(1, 2) == 'good day'
    assert week1.reading_chunk(1, 2) == 'today was'