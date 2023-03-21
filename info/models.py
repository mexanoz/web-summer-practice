from django.db import models


class Position(models.Model):
    name = models.CharField("название", max_length = 50, unique = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "должность"
        verbose_name_plural = "должности"


class Education(models.Model):
    level = models.CharField("степень", max_length = 15)
    field = models.CharField("область", max_length = 50)

    def __str__(self):
        return self.level + " " + self.field

    class Meta:
        verbose_name = "учёная степень"
        verbose_name_plural = "учёные степени"


class Room(models.Model):
    ROOM_TYPES = [
        ("TE", "Преподавательская"),
        ("LE", "Учебная"),
        ("AD", "Администрация"),
        ("OF", "Служебное помещение")
    ]

    number = models.CharField("номер", max_length = 10, unique = True)
    room_type = models.CharField("тип", max_length = 2, choices = ROOM_TYPES, default = "TE")

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "аудитория"
        verbose_name_plural = "аудитории"


class Discipline(models.Model):
    name = models.CharField("название", max_length = 50, unique = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "дисциплина"
        verbose_name_plural = "дисциплины"


class LessonType(models.Model):
    name = models.CharField("вид", max_length = 15)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "вид занятия"
        verbose_name_plural = "виды занятий"


class Lesson(models.Model):
    lesson_type = models.ForeignKey(LessonType, verbose_name = "вид занятия", on_delete = models.RESTRICT)
    discipline = models.ForeignKey(Discipline, verbose_name = "дисциплина", on_delete = models.CASCADE)

    def __str__(self):
        return str(self.discipline) + ", " + str(self.lesson_type)

    class Meta:
        verbose_name = "занятие"
        verbose_name_plural = "занятия"


class Teacher(models.Model):
    TEACHER_POSITIONS = [
        ("AS", "ассистент"),
        ("DC", "доцент"),
        ("PR", "преподаватель"),
        ("PF", "профессор"),
        ("SP", "старший преподаватель"),
        ("ST", "стажёр"),
    ]

    name = models.CharField("ФИО", max_length = 50)
    position = models.ForeignKey(Position, verbose_name = "должность", on_delete = models.RESTRICT)
    education = models.ForeignKey(Education, verbose_name = "учёная степень", on_delete = models.SET_NULL, null = True, blank = True)
    photo = models.ImageField("фотография", blank = True, upload_to = "photos")
    room = models.ForeignKey(Room, verbose_name = "аудитория", on_delete = models.SET_NULL, limit_choices_to = {"room_type": "TE"}, blank = True, null = True)
    additional_work = models.TextField("дополнительная деятельность", blank = True, default = "")
    lessons = models.ManyToManyField(Lesson, verbose_name = "занятия", blank = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "преподаватель"
        verbose_name_plural = "преподаватели"
