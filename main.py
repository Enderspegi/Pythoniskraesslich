class Graph:
    """
    Eine Klasse zur Darstellung eines ungerichteten, gewichteten Graphen
    unter Verwendung einer Adjazenzliste.
    """


def __init__(self):
    # Die Adjazenzliste wird als Dictionary gespeichert.
    # Schlüssel sind Knotennamen (Strings), Werte sind Listen von
    # Tupeln (Nachbarknoten, Gewicht).
    self.adj_list = {}


def addnode(self, node: str):
    """
    Fügt einen neuen Knoten zum Graphen hinzu.
    Ignoriert den Knoten, wenn er bereits existiert.
    """
    if node not in self.adj_list:
        self.adj_list[node] = []
        print(f"Knoten '{node}' hinzugefügt.")
    else:
        print(f"Knoten '{node}' existiert bereits.")


def addedge(self, node1: str, node2: str, weight: int):
    """
    Fügt eine gewichtete, ungerichtete Kante zwischen node1 und node2 hinzu.
    Erstellt die Knoten, falls sie noch nicht existieren.
    """
    # Stelle sicher, dass beide Knoten existieren
    if node1 not in self.adj_list:
        self.add_node(node1)
    if node2 not in self.adj_list:
        self.add_node(node2)

    # Die Kante für node1 hinzufügen (zum Nachbarn node2 mit Gewicht)
    # Überprüfe, ob die Kante bereits existiert, um Duplikate zu vermeiden
    if (node2, weight) not in self.adj_list[node1]:
        self.adj_list[node1].append((node2, weight))

    # Die Kante für node2 hinzufügen (zum Nachbarn node1 mit Gewicht)
    if (node1, weight) not in self.adj_list[node2]:
        self.adj_list[node2].append((node1, weight))

    print(f"Kante zwischen '{node1}' und '{node2}' mit Gewicht {weight} hinzugefügt.")


def get_neighbors(self, node: str) -> list[tuple[str, int]]:
    """
    Gibt eine Liste der Nachbarn des Knotens zurück,
    zusammen mit den Kantengewichten, in Form von
    [(Nachbarknoten, Gewicht), ...].
    Gibt eine leere Liste zurück, wenn der Knoten nicht existiert.
    """
    if node in self.adj_list:
        # Wenn der Knoten existiert, geben wir seine Liste der Nachbarn zurück.
        return self.adj_list[node]
    else:
        # Wenn der Knoten nicht existiert, informieren wir den Benutzer
        # und geben eine leere Liste zurück.
        print(f"Fehler: Knoten '{node}' existiert nicht im Graphen.")
        return []

    def print_nodes(self):
        """
        Gibt eine lesbare Darstellung der Adjazenzliste aus.
        """

    print("\n--- Adjazenzliste des Graphen ---")
    for node, neighbors in self.adj_list.items():
        # Erstellt eine String-Darstellung der Nachbar-Tupel: (Nachbar, Gewicht)
        neighbor_str = ", ".join([f"({n}, {w})" for n, w in neighbors])
        print(f"{node}: [{neighbor_str}]")
    print("----------------------------------\n")

    # --- Beispielhafte Verwendung ---


# 1. Graph-Instanz erstellen
my_graph = Graph()

# 2. Knoten hinzufügen
my_graph.add_node("A")
my_graph.add_node("B")
my_graph.add_node("C")
my_graph.add_node("D")

# 3. Kanten hinzufügen
my_graph.add_edge("A", "B", 4)
my_graph.add_edge("A", "C", 2)
my_graph.add_edge("B", "C", 1)
my_graph.add_edge("B", "D", 5)
my_graph.add_edge("C", "D", 8)

# 4. Adjazenzliste ausgeben (entsprechend der gewünschten Beispielausgabe)
my_graph.print_nodes()

# 5. Nachbarn abrufen
neighbors_of_B = my_graph.get_neighbors("B")
if neighbors_of_B:
    print(f"Nachbarn von B: {neighbors_of_B}")

neighbors_of_X = my_graph.get_neighbors("X")  # Nicht existierender Knoten
