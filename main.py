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
def add_node(self, node: str):
        """
        Fügt einen neuen Knoten zum Graphen hinzu.
        Ignoriert den Knoten, wenn er bereits existiert.
        """
        if node not in self.adj_list:
            self.adj_list[node] = []
            print(f"Knoten '{node}' hinzugefügt.")
        else:
            print(f"Knoten '{node}' existiert bereits.")
def add_edge(self, node1: str, node2: str, weight: int):
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