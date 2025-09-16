list_of_profile = [
    {
        "name": "maha",
        "last_name": "alghuraibi"
    },
    {
        "name": "maha",
        "last_name": "alghuraibi"
    }
]
for el in list_of_profile:
    print(el)
print(list_of_profile)


class Cat:
    next_id = 1   # class attribute (مشترك بين كل القطط)

    def __init__(self, name, age=0):
        self.name = name        # خاصية خاصة بكل قطة
        self.age = age          # خاصية خاصة بكل قطة
        self.id = Cat.next_id   # تعيين رقم ID
        Cat.next_id += 1        # نزيد الرقم للقطة التالية

    def meow(self):             # method خاص بالقطة
        print(f"{self.name} says meow!")

    def __str__(self):          # نتحكم كيف يطبع الكائن
        return f"Cat #{self.id} named {self.name} is {self.age} years old."

    @classmethod
    def get_total_cats(cls):    # method خاص بالكلاس
        return cls.next_id - 1


# 🐱 إنشاء القطط
cat1 = Cat("miu", 8)
cat2 = Cat("lulu", 3)

# الطباعة
print(cat1)     # يستخدم __str__
print(cat2)

# استدعاء method من الكائن
cat1.meow()
cat2.meow()

# استدعاء method من الكلاس
print(Cat.get_total_cats())
