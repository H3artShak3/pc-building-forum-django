from django.db import models
from PIL import Image
from django.contrib.auth.models import User

# Create your models here.


class Cpu(models.Model):
    MANUFACTURER_LIST = (
        ('a', 'Amd'),
        ('i', 'Intel')
    )
    manufacturer = models.CharField(
        "Gamintojas",
        max_length=1,
        choices=MANUFACTURER_LIST,
        default='a'
    )
    model = models.CharField("Modelis", max_length=25)
    base_speed = models.CharField("Bazinis daznis", max_length=5)
    speed = models.CharField("Dažnis", max_length=5)
    cores = models.CharField("Branduolių kiekis", max_length=3)
    threads = models.CharField("Gijų kiekis", max_length=3)
    tdp = models.IntegerField("TDP")
    score = models.IntegerField('Skaičius palyginimui')

    def __str__(self):
        return f"{self.manufacturer} {self.model}"

    class Meta:
        verbose_name = 'Procesorius'
        verbose_name_plural = 'Procesoriai'


class Gpu(models.Model):
    MANUFACTURER_LIST = (
        ('a', 'Amd'),
        ('n', 'Nvidia'),
        ('i', 'Intel')
    )
    manufacturer = models.CharField(
        "Gamintojas",
        max_length=1,
        choices=MANUFACTURER_LIST,
        default='a'
    )
    model = models.CharField("Modelis", max_length=25)
    vram = models.CharField("Atminties kiekis", max_length=5)
    mem_type = models.CharField("Atminties tipas", max_length=7)
    POWER_OPTIONS = (
        ('n', 'Nereikalauja papildomo maitinimo'),
        ('6', '6 pinų'),
        ('8', '8 pinų'),
        ('6+6', '2 x 6 pinų'),
        ('8+6', '8 pinų + 6 pinų'),
        ('8+8', '2 x 8 pinų'),
        ('12', '12 pinų')
    )
    power_pins = models.CharField(
        "Reikalaujamas connectorius",
        max_length=3,
        choices=POWER_OPTIONS,
        default='n')
    tdp = models.IntegerField("TDP")
    score = models.IntegerField('Skaičius palyginimui')

    def __str__(self):
        return f"{self.model} {self.vram} GB"

    class Meta:
        verbose_name = 'Vaizdo plokštė'
        verbose_name_plural = 'Vaizdo plokštės'

class Ram(models.Model):
    MANUFACTURER_LIST = (
        ('k', 'Kingston'),
        ('cor', 'Corsair'),
        ('cru', 'Crucial'),
        ('a', 'Adata'),
        ('amd', 'AMD'),
        ('h', 'SK Hynix'),
        ('m', 'Micron'),
        ('s', 'Samsung'),
        ('p', 'Patriot')
    )

    manufacturer = models.CharField(
        "Gamintojas",
        max_length=3,
        choices=MANUFACTURER_LIST,
        default='k'
    )

    model = models.CharField("Modelis", max_length=25)
    TYPE_LIST = (
        ('2', 'DDR2'),
        ('3', 'DDR3'),
        ('4', 'DDR4'),
        ('5', 'DDR5')
    )
    type_ram = models.CharField(
        "Atminties tipas",
        max_length=1,
        choices=TYPE_LIST,
        default='4'
    )
    speed = models.CharField("Atminties greitis", max_length=4)
    size = models.IntegerField("Atminties dydis", null=True)

    def __str__(self):
        return f"{self.size}GB {self.model} {self.speed}"

    class Meta:
        verbose_name = 'Ram atmintis'
        verbose_name_plural = 'Ram atmintys'


class Profile(models.Model):
    picture = models.ImageField(upload_to='profile_pics', default='default-user.png')
    f_name = models.CharField("Vardas", max_length=30, null=True, blank=True)
    l_name = models.CharField("Pavardė", max_length=30, null=True, blank=True)
    reg_data = models.DateField("Registracijos data", auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} profilis'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # numatytieji Model klasės veiksmai suvykdomi
        img = Image.open(self.picture.path)
        thumb_size = (200, 200)
        img.thumbnail(thumb_size)
        img.save(self.picture.path)

    class Meta:
        verbose_name = 'Profilis'
        verbose_name_plural = 'Profiliai'


class UserRig(models.Model):
    profilis = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    procesorius = models.ForeignKey(Cpu, on_delete=models.CASCADE, blank=True)
    vaizdo_plokste = models.ForeignKey(Gpu, on_delete=models.CASCADE, blank=True)
    ram_kiekis = models.CharField("RAM  plokštelių kiekis", max_length=2, blank=True)
    ramai = models.ForeignKey(Ram, on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name = 'Naudotojo kompiuteris'
        verbose_name_plural = 'Naudotojų kompiuteriai'


class Postai(models.Model):
    CATEGORY_LIST = (
        ('s', 'Pagalba surinkime nuo nulio'),
        ('a', 'Atnaujinimas seno kompiuterio'),
        ('p', 'Problemos su kompiuteriu'),
        ('k', 'Kiti įrenginiai'),
        ('r', 'Tematiški renginiai')
    )
    category = models.CharField(
        "Kategorija",
        max_length=1,
        choices=CATEGORY_LIST,
        default='s'
    )

    STATUS_LIST = (
        ('a', 'Aktyvi'),
        ('u', 'Uždaryta'),
        ('p', 'Paslėpta'),
        ('d', 'Ištrinta'),
        ('v', 'VIP')
    )

    status = models.CharField(
        "Statusas",
        max_length=1,
        choices=STATUS_LIST,
        default='a',
        blank=True,
        null=True
    )
    theme = models.CharField("Tema", max_length=150)
    description = models.CharField("Aprašymas", max_length=5000)
    ft_1 = models.ImageField("Paveiksliukas Nr. 1", upload_to='post_pics', default='no_photo.jpg')
    ft_2 = models.ImageField("Paveiksliukas Nr. 2", upload_to='post_pics', default='no_photo.jpg')
    ft_3 = models.ImageField("Paveiksliukas Nr. 3", upload_to='post_pics', default='no_photo.jpg')
    ft_4 = models.ImageField("Paveiksliukas Nr. 4", upload_to='post_pics', default='no_photo.jpg')
    ft_5 = models.ImageField("Paveiksliukas Nr. 5", upload_to='post_pics', default='no_photo.jpg')
    create_data = models.DateTimeField("Sukurimo data", auto_now_add=True, null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # numatytieji Model klasės veiksmai suvykdomi
        img = Image.open(self.ft_1.path)
        img.save(self.ft_1.path)
        img = Image.open(self.ft_2.path)
        img.save(self.ft_2.path)
        img = Image.open(self.ft_3.path)
        img.save(self.ft_3.path)
        img = Image.open(self.ft_4.path)
        img.save(self.ft_4.path)
        img = Image.open(self.ft_5.path)
        img.save(self.ft_5.path)


    class Meta:
        verbose_name = 'Postas'
        verbose_name_plural = 'Postai'

class PostaiReview(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField('Komentaras postui', max_length=2000)
    postas = models.ForeignKey(Postai, on_delete=models.CASCADE, blank=True)
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    ft = models.ImageField('Komentaro paveiksliukas', upload_to='review_pics', default='no_photo.jpg')

    def __str__(self):
        return f"{self.date_created}, {self.reviewer}, {self.postas}, {self.content[:50]}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # numatytieji Model klasės veiksmai suvykdomi
        img = Image.open(self.ft.path)
        img.save(self.ft.path)

    class Meta:
        verbose_name = 'Posto komentaras'
        verbose_name_plural = 'Posto komentarai'

class Advertisements(models.Model):
    kaina = models.FloatField(blank=True, null=True)
    telefonas = models.CharField(blank=True, default='+370', max_length=13)
    tema = models.CharField(blank=True, null=True, max_length=150)
    aprasymas = models.CharField('Aprašymas', blank=True, null=True, max_length=2500)
    cpu_kiekis = models.IntegerField(blank=True, default=0, null=True)
    cpu_modelis = models.ForeignKey(Cpu, on_delete=models.CASCADE, blank=True, null=True)
    gpu_kiekis = models.IntegerField(blank=True, default=0, null=True)
    gpu_modelis = models.ForeignKey(Gpu, on_delete=models.CASCADE, blank=True, null=True)
    ram_kiekis = models.IntegerField(blank=True, default=0, null=True)
    ram_modelis = models.ForeignKey(Ram, on_delete=models.CASCADE, blank=True, null=True)
    useris = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    STATUS_LIST = (
        ('a', 'Aktyvus'),
        ('p', 'Paslėptas'),
        ('d', 'Ištrintas'),
        ('v', 'VIP')
    )

    status = models.CharField(
        "Statusas",
        max_length=1,
        choices=STATUS_LIST,
        default='a',
        blank=True,
        null=True
    )

    ft_1 = models.ImageField("Paveiksliukas Nr. 1", upload_to='advertisement_pics', default='no_photo.jpg')
    ft_2 = models.ImageField("Paveiksliukas Nr. 2", upload_to='advertisement_pics', default='no_photo.jpg')
    ft_3 = models.ImageField("Paveiksliukas Nr. 3", upload_to='advertisement_pics', default='no_photo.jpg')
    ft_4 = models.ImageField("Paveiksliukas Nr. 4", upload_to='advertisement_pics', default='no_photo.jpg')



    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # numatytieji Model klasės veiksmai suvykdomi
        img = Image.open(self.ft_1.path)
        img.save(self.ft_1.path)
        img = Image.open(self.ft_2.path)
        img.save(self.ft_2.path)
        img = Image.open(self.ft_3.path)
        img.save(self.ft_3.path)
        img = Image.open(self.ft_4.path)
        img.save(self.ft_4.path)

    class Meta:
        verbose_name = 'Skelbimas'
        verbose_name_plural = 'Skelbimai'

class AdvertisementReview(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField('Komentaras skelbimui', max_length=2000)
    advert = models.ForeignKey(Advertisements, on_delete=models.CASCADE, blank=True)
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.date_created}, {self.reviewer}, {self.advert}, {self.content[:50]}"

    class Meta:
        verbose_name = 'Skelbimo komentaras'
        verbose_name_plural = 'Skelbimų komentarai'
