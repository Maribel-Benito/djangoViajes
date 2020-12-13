from django.db import models


# Create your models here.
class Branch_office(models.Model):
    code = models.CharField(verbose_name="Código", max_length=6, unique=True)
    name = models.CharField(verbose_name='Nombre', max_length=40)
    address = models.CharField(verbose_name='Dirección', max_length=60)
    phone = models.CharField(verbose_name='Telefono', max_length=10, unique=True)

    def __str__(self):
        return "Código: {0}  -  Nombre: {1}  -  Dirección: {2}".format(self.code, self.name, self.address)

    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"


class Hotel(models.Model):
    code = models.CharField(verbose_name='Código', max_length=6, unique=True)
    name = models.CharField(verbose_name='Nombre', max_length=40)
    address = models.CharField(verbose_name='Direccion', max_length=60)
    city = models.CharField(verbose_name='Ciudad', max_length=30)
    phone = models.CharField(verbose_name='Telefono', max_length=10, unique=True)
    square = models.PositiveIntegerField(verbose_name='Plaza')

    def __str__(self):
        return "Código: {0}  -  Nombre: {1}  -  Dirección: {2}  -  Ciudad: {3}".format(self.code, self.name, self.address, self.city)

    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hoteles"


class Tourist(models.Model):
    code = models.CharField(verbose_name='Código', max_length=6, unique=True)
    name = models.CharField(verbose_name='Nombre', max_length=40)
    last_name = models.CharField(verbose_name='Apellido', max_length=50)
    address = models.CharField(verbose_name='Direccion', max_length=60)
    phone = models.CharField(verbose_name='Telefono', max_length=10, unique=True)

    def __str__(self):
        return "Código: {0}   -  Nombre: {1} {2}  -   Telefono: {3}".format(self.code, self.name, self.last_name, self.phone)

    class Meta:
        verbose_name = "Turista"
        verbose_name_plural = "Turistas"


class Flight(models.Model):
    number = models.CharField(verbose_name='Número de vuelo', max_length=6, unique=True)
    date = models.DateField(verbose_name='Fecha de vuelo')
    time = models.TimeField(verbose_name='Hora de vuelo')
    origin = models.CharField(verbose_name='Origen', max_length=40)
    destination = models.CharField(verbose_name='Destino', max_length=40)
    total_square = models.PositiveIntegerField(verbose_name='Plaza Total')
    tourist_square = models.PositiveIntegerField(verbose_name='Plaza Turista')

    def __str__(self):
        return "Vuelo: {0}  -  Fecha: {1}  -  Hora: {2}".format(self.number, self.date, self.time)

    class Meta:
        verbose_name = "Vuelo"
        verbose_name_plural = "Vuelos"


class Stay(models.Model):
    code = models.CharField(verbose_name='Código', max_length=8, unique=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='Hotel')
    pension = models.CharField(verbose_name='Pension', max_length=50)
    entry_date = models.DateField(verbose_name='Fecha Entrada')
    departure_date = models.DateField(verbose_name='Fecha Salida')

    def __str__(self):
        return "Código: {0}  -  Pension: {1} -   Entrada: {2}".format(self.code, self.pension, self.entry_date)

    class Meta:
        verbose_name = "Estancia"
        verbose_name_plural = "Estancias"


class Reserve(models.Model):
    code = models.CharField(verbose_name='Código', max_length=8, unique=True)
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE, verbose_name='Turista')
    branch_office = models.ForeignKey(Branch_office, on_delete=models.CASCADE, verbose_name='Sucursal')
    stay = models.ForeignKey(Stay, on_delete=models.CASCADE, verbose_name='Estancia')

    def __str__(self):
        return "Código: {0}  -  Turista: {1}".format(self.code, self.tourist)

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"


class Tourist_flight(models.Model):
    code = models.CharField(verbose_name='Código', max_length=8, unique=True)
    DICT_PASSENGER = [
        ('Primera clase', 'Pimera clase'), ('Business', 'Clase ejecutiva o business'),
        ('Premium', 'Clase premium economy'), ('Económica', 'Clase turista o económica')
    ]
    passenger = models.CharField(choices=DICT_PASSENGER, default='Primera clase', max_length=100)
    reserve = models.ForeignKey(Reserve, on_delete=models.CASCADE, verbose_name='Reserva')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, verbose_name='Vuelo')

    def __str__(self):
        return "Código: {0}  -  Cabina: {1} -   Reserva: {2}".format(self.code, self.passenger, self.reserve)

    class Meta:
        verbose_name = "Vuelo de Turista"
        verbose_name_plural = "Vuelos de Turistas"
