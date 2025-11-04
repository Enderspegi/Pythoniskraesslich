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