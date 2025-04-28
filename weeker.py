class WeekDayError(Exception):
    pass

class Weeker:
    __week_days = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']

    def __init__(self, day):
        if day not in self.__week_days:
            raise WeekDayError("Día inválido")
        self.__current_day_index = self.__week_days.index(day)

    def __str__(self):
        return self.__week_days[self.__current_day_index]

    def add_days(self, n):
        self.__current_day_index = (self.__current_day_index + n) % 7

    def subtract_days(self, n):
        self.__current_day_index = (self.__current_day_index - n) % 7

# Ejemplo de uso:
try:
    week = Weeker('Lun')
    print(week)              # Lun
    week.add_days(1)
    print(week)              # Mar
    week.subtract_days(3)
    print(week)              # Dom
    invalid = Weeker('XXX')  # Lanza WeekDayError
except WeekDayError:
    print("Lo siento, no puedo atender tu solicitud.")