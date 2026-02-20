class Spaceship:

    __instance = None

    @classmethod
    def get_instance(cls):
        if cls.__instance == None:
            cls.__instance = Spaceship()
            return cls.__instance 
        return cls.__instance


if __name__ == '__main__':
    a = Spaceship.get_instance()
    b = Spaceship.get_instance()

    assert a == b 