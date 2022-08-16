import time


class Person:

    def __init__(self, name, age, job):
        self.__job = job
        self.__name = name
        self.__age = age

    @property
    def job(self):
        return self.__job

    def set_job(self, job: str):
        if (len(job) < 3) or (job.isdigit()):
            raise Exception('Некорректная работа')
        self.__job = job

    def sleep(self, count_sec):
        for i in range(count_sec):
            print(f'До пробуждения {self.__name} осталось {count_sec - i - 1}')
            time.sleep(1)

    def __repr__(self):
        return f"""
        Name: {self.__name}\n
        Age: {self.__age}\n
        Job: {self.__job}\n
        """


# public
# protected
# private

person1 = Person('Dmitriy', '30', 'Drom.ru')
# person1.set_job('123')
print(person1.job)

print(person1)

person1.sleep(5)
