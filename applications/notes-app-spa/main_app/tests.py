from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date

from .models import Note, MoodCheck, Photo, Reaction


class ModelsTest(TestCase):
    def setUp(self):
        # User
        self.user = User.objects.create_user(username='maha', password='12345')

        # Reactions (
        self.reaction1 = Reaction.objects.create(emoji='😊')
        self.reaction2 = Reaction.objects.create(emoji='😡')
        self.reaction3 = Reaction.objects.create(emoji='😭')

        # Notes 
        self.note1 = Note.objects.create(
            title='First Note',
            content='today was good',
            user=self.user,
        )
        self.note2 = Note.objects.create(
            title='Second Note',
            content='today was bad',
            user=self.user,
        )

        # ManyToMany:
        self.note1.reactions.set([self.reaction1, self.reaction2])

        # MoodChecks 
        self.moodcheck1 = MoodCheck.objects.create(
            date=date(2025, 1, 1),
            period='M',          # Morning
            note=self.note1
        )
        self.moodcheck2 = MoodCheck.objects.create(
            date=date(2024, 1, 1),
            period='A',          # Afternoon
            note=self.note1
        )
        self.moodcheck3 = MoodCheck.objects.create(
            date=date(2023, 1, 1),
            period='N',          # Night
            note=self.note2
        )

        # Photo 
        self.photo1 = Photo.objects.create(
            note=self.note1,
            url='http://img1.com',
            title='selfie'
        )
        self.photo2 = Photo.objects.create(
            note=self.note2,
            url='http://img2.com',
            title='mirror pic'
        )

    # -------------------
    # String Representations 
    # -------------------

    def test_user_create(self):
        self.assertEqual(str(self.user), "maha")

    def test_note_create(self):
        self.assertEqual(str(self.note1), "First Note")
        self.assertEqual(str(self.note2), "Second Note")

    def test_reaction_create(self):
        self.assertEqual(str(self.reaction1), "😊")
        self.assertEqual(str(self.reaction2), "😡")
        self.assertEqual(str(self.reaction3), "😭")

    def test_moodcheck_create(self):
        self.assertEqual(str(self.moodcheck1), "Morning on 2025-01-01")
        self.assertEqual(str(self.moodcheck2), "Afternoon on 2024-01-01")
        self.assertEqual(str(self.moodcheck3), "Night on 2023-01-01")

    def test_photo_create(self):
        self.assertEqual(
            str(self.photo1),
            f"Photo for note_id: {self.note1.id} @{self.photo1.url}"
        )
        self.assertEqual(
            str(self.photo2),
            f"Photo for note_id: {self.note2.id} @{self.photo2.url}"
        )

    # -------------------
    # Relationships
    # -------------------

    def test_note_reactions_relationship(self):
        self.assertEqual(self.note1.reactions.count(), 2)
        self.assertIn(self.reaction1, self.note1.reactions.all())
        self.assertIn(self.reaction2, self.note1.reactions.all())
        self.assertEqual(self.note2.reactions.count(), 0)

    def test_note_user_relationship(self):
        self.assertEqual(self.note1.user.username, "maha")
        self.assertEqual(self.note2.user, self.user)

    def test_note_moodcheck_relationship(self):
        self.assertEqual(self.moodcheck1.note, self.note1)
        self.assertEqual(self.moodcheck2.note, self.note1)
        self.assertEqual(self.moodcheck3.note, self.note2)

        self.assertEqual(self.moodcheck1.period, 'M')
        self.assertEqual(self.moodcheck2.period, 'A')
        self.assertEqual(self.moodcheck3.period, 'N')

    def test_note_photo_relationship(self):
        self.assertEqual(self.photo1.note, self.note1)
        self.assertEqual(self.photo2.note, self.note2)

    # -------------------
    # Model Methods / Ordering
    # -------------------

    def test_moodcheck_ordering(self):
        moodchecks_for_note1 = list(
            MoodCheck.objects.filter(note=self.note1)
        )
        self.assertEqual(moodchecks_for_note1[0].date, date(2025, 1, 1))
        self.assertEqual(moodchecks_for_note1[1].date, date(2024, 1, 1))

    # -------------------
    # Cascade Deletions
    # -------------------

    def test_delete_note_cascades(self):
        self.note1.delete()

        # note1 should be gone
        self.assertEqual(Note.objects.count(), 1)  

        self.assertEqual(
            MoodCheck.objects.filter(note=self.note1.id).count(),
            0
        )
        self.assertEqual(
            MoodCheck.objects.count(),
            1
        )

        self.assertEqual(
            Photo.objects.filter(note=self.note1.id).count(),
            0
        )
        self.assertEqual(Photo.objects.count(), 1)

        self.assertEqual(Reaction.objects.count(), 3)

    def test_delete_user_deletes_notes(self):

        self.user.delete()

      
        self.assertEqual(User.objects.count(), 0)

        self.assertEqual(Note.objects.count(), 0)

      
        self.assertEqual(Photo.objects.count(), 0)

    
        self.assertEqual(MoodCheck.objects.count(), 0)

       
        self.assertEqual(Reaction.objects.count(), 3)

