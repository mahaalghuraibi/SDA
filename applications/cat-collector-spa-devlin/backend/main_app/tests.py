from django.test import TestCase
from django.contrib.auth.models import User
from .models import Cat, Feeding, Photo, Toy
from datetime import date
# Create your tests here.

class ModelsTest(TestCase):
    def setUp(self):
        # user;
        self.user = User.objects.create_user(username='testuser', password='12345')
        # toys;
        self.toy1 = Toy.objects.create(name='Mouse',   color='Gray')
        self.toy2 = Toy.objects.create(name='Ball',    color='Red')
        self.toy3 = Toy.objects.create(name='Feather', color='white')
        # cat; each related to user
        self.cat1 = Cat.objects.create(name='Felix',   breed='Tabby', description='Playful cat',   age=3, user=self.user)
        self.cat2 = Cat.objects.create(name='Whiskers',breed='Tabby', description='A playful cat.',age=5, user=self.user)
        # feeding; two related to cat1
        self.feeding1 = Feeding.objects.create(date=date(2025, 1, 1), meal='B', cat=self.cat1)
        self.feeding2 = Feeding.objects.create(date=date(2024, 1, 1), meal='L', cat=self.cat1)
        self.feeding3 = Feeding.objects.create(date=date(2023, 1, 1), meal='D', cat=self.cat2)
        # photo; each related to one cat
        self.photo1 = Photo.objects.create(cat=self.cat1, url='http://url1.com', title='First')
        self.photo2 = Photo.objects.create(cat=self.cat2, url='http://url2.com', title='First')
        # relate toy1 and toy2 to cat
        self.cat1.toys.set([self.toy1, self.toy2])

    # TESTS
    # tests start with "test_"
    # example

    def test_user_create(self):
        self.assertEqual(str(self.user), 'testuser')

    # -------------------
    # String Representations / creation (using __str__ to ensure property return)
    # -------------------

    def test_user_create(self):
        self.assertEqual(str(self.user), 'testuser')
    
    def test_cat_create(self):
        self.assertEqual(str(self.cat1), 'Felix')
        self.assertEqual(str(self.cat2), 'Whiskers')

    def test_toy_create(self):
        self.assertEqual(str(self.toy1), 'Mouse')
        self.assertEqual(str(self.toy2), 'Ball')
        self.assertEqual(str(self.toy3), 'Feather')

    def test_feeding_create(self):
        self.assertEqual(str(self.feeding1), 'Breakfast on 2025-01-01')
        self.assertEqual(str(self.feeding2), 'Lunch on 2024-01-01')
        self.assertEqual(str(self.feeding3), 'Dinner on 2023-01-01')

    def test_photo_create(self):
        self.assertEqual(str(self.photo1), 'http://url1.com')
        self.assertEqual(str(self.photo2), 'http://url2.com')

    # -------------------
    # Relationships
    # -------------------
    
    def test_cat_toys_relationship(self):
        self.assertEqual(self.cat1.toys.count(), 2)
        self.assertIn(self.toy1, self.cat1.toys.all())
        self.assertIn(self.toy2, self.cat1.toys.all())

    def test_cat_user_relationship(self):
        self.assertEqual(self.cat1.user.username, 'testuser')

    def test_cat_feeding_relationship(self):
        self.assertEqual(self.feeding1.cat, self.cat1)
        self.assertEqual(self.feeding1.meal, 'B')
        self.assertEqual(self.feeding2.cat, self.cat1)
        self.assertEqual(self.feeding2.meal, 'L')
        self.assertEqual(self.feeding3.cat, self.cat2)
        self.assertEqual(self.feeding3.meal, 'D')

    def test_cat_photo_relationship(self):
        self.assertEqual(self.photo1.cat, self.cat1)
        self.assertEqual(self.photo2.cat, self.cat2)

    # -------------------
    # Model Methods / Ordering
    # -------------------
    
    def test_feeding_ordering(self):
        feedings = list(self.cat1.feeding_set.all())
        self.assertEqual(feedings[0].date, date(2025, 1, 1))
        self.assertEqual(feedings[1].date, date(2024, 1, 1))

    # -------------------
    # Cascade Deletions
    # -------------------

    # 1 user, two related cats => 0 cats left after delete
    def test_deleting_user_cascades_to_cat(self):
        self.user.delete()
        self.assertEqual(Cat.objects.count(), 0)

    # cat2 had ONE feeding => should still be two in database related to cat1!
    def test_deleting_cat_cascades_to_feedings(self):
        self.cat2.delete()
        self.assertEqual(Feeding.objects.count(), 2)

    # cat1 had one photo out of two => 1 left over!
    def test_deleting_cat_cascades_to_photo(self):
        self.cat1.delete()
        self.assertEqual(Photo.objects.count(), 1)