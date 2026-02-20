class Vaisseau:
    def __init__(self, name, color, speed, acceleration):
        self.name = name
        self.color = color
        self.speed = speed
        self.acceleration = acceleration  
        self.distance_parcourue = 0

    def avance(self):
        self.distance_parcourue += self.speed


class Circuit:
    def __init__(self, distance, nb_tour):
        self.distance = distance
        self.nb_tour = nb_tour


class Simulation:
    def __init__(self, circuit: Circuit, vaisseaux: list):
        self.circuit = circuit
        self.vaisseaux = vaisseaux
        self.tick_actuel = 0   
        self.classement = []

    def tick(self):
        self.tick_actuel += 1
        print(f"\nTick : {self.tick_actuel}")

        for vaisseau in self.vaisseaux:
            if self.tick_actuel >= vaisseau.acceleration:
                vaisseau.avance()

            distance_totale = self.circuit.distance * self.circuit.nb_tour
            if vaisseau.distance_parcourue >= distance_totale and vaisseau not in self.classement:
                self.classement.append(vaisseau)
                print(f" {vaisseau.name} arrive en position {len(self.classement)}")

        self.afficher_position()

    def afficher_position(self):
        for vaisseau in self.vaisseaux:
            print(f"  {vaisseau.name} ({vaisseau.color}) : {vaisseau.distance_parcourue} metre")

    def course_terminee(self):
        distance_totale = self.circuit.distance * self.circuit.nb_tour
        return all(vaisseau.distance_parcourue >= distance_totale for vaisseau in self.vaisseaux)

    def lancer(self):
        print("Départ")
        while not self.course_terminee():
            self.tick()

        print("\nClassement final :")
        for i, vaisseau in enumerate(self.classement, 1):
            print(f"  {i}. {vaisseau.name} ({vaisseau.color})")





if __name__ == "__main__":
    circuit = Circuit(distance=100, nb_tour=3)

    vaisseaux = [
        Vaisseau("Nebula-X",    "Rouge",  30, acceleration=3),  # démarre au tick 3
        Vaisseau("StarCruiser", "Bleu",   25, acceleration=1),  # démarre au tick 1
        Vaisseau("PhoenixDawn", "Vert",   28, acceleration=5),  # démarre au tick 5
        Vaisseau("VoidRunner",  "Violet", 22, acceleration=2),  # démarre au tick 2
    ]

    sim = Simulation(circuit, vaisseaux)
    sim.lancer()



    




    