import sys

# Setze eine große Zahl für "Unendlich"
INF = float('inf')

class Graph:
    """
    Eine einfache Graphenklasse zur Speicherung von gewichteten, gerichteten Kanten.
    Die Adjazenzliste ist ein Dictionary, wobei jeder Knoten auf eine Liste
    von Tupeln (Nachbar, Gewicht) verweist.
    """
    def __init__(self):
        # Struktur: {Knoten: [(Nachbar, Gewicht), ...]}
        self.adj = {}

    def add_edge(self, u, v, weight):
        """Fügt eine gerichtete Kante zum Graphen hinzu."""
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []

        self.adj[u].append((v, weight))

    def get_nodes(self):
        """Gibt alle eindeutigen Knoten zurück."""
        nodes = set(self.adj.keys())
        for neighbors in self.adj.values():
            for neighbor, _ in neighbors:
                nodes.add(neighbor)
        return list(nodes)

class Dijkstra:
    """
    Implementiert den Dijkstra-Algorithmus unter Verwendung einer
    zweidimensionalen Array-Struktur (Liste von Listen) als Warteschlange
    anstelle eines Heaps.
    """

    def __init__(self, graph):
        self.graph = graph

    def _get_min_distance_node(self, unvisited_queue):
        """
        Wählt den Knoten mit der kleinsten Distanz durch lineare Suche
        im 2D-Array (Schritt 3). Simuliert "extract_min" in O(V).
        """
        if not unvisited_queue:
            return None, None, -1

        min_dist = INF
        min_node = None
        min_index = -1

        for i, [node, dist] in enumerate(unvisited_queue):
            if dist < min_dist:
                min_dist = dist
                min_node = node
                min_index = i

        return min_node, min_dist, min_index

    def find_shortest_paths(self, start_node):
        """
        Berechnet die kürzesten Wege vom Startknoten zu allen anderen Knoten.
        :param start_node: Der Startknoten (String).
        :return: Ein Dictionary der kürzesten Distanzen {Knoten: Distanz}.
        """
        nodes = self.graph.get_nodes()
        
        # 1. Initialisieren Sie Distanzen mit ∞ und Startknoten mit 0
        distances = {node: INF for node in nodes}
        distances[start_node] = 0
        
        # 2. Fügen Sie alle Knoten in die 2D-Array-Warteschlange ein: [[Knoten, Distanz], ...]
        unvisited_queue = [[node, distances[node]] for node in nodes]
        
        visited = set()

        print(f"--- Starte Dijkstra-Algorithmus von Knoten '{start_node}' ---")

        while unvisited_queue:
            # 3. Wähle den Knoten mit der kleinsten Distanz (Lineare Suche)
            current_node, current_dist, min_index = self._get_min_distance_node(unvisited_queue)

            if current_node is None or current_dist == INF:
                # Alle verbleibenden Knoten sind nicht erreichbar
                break

            # 5. Entferne den besuchten Knoten in der Warteschlange
            unvisited_queue.pop(min_index)
            visited.add(current_node)
            
            print(f"\nBesuche Knoten: {current_node} (Distanz: {current_dist if current_dist != INF else '∞'})")

            # Entspanne Kanten zu den Nachbarn
            for neighbor, weight in self.graph.adj.get(current_node, []):
                # Prüfe nur unbesuchte Nachbarn
                if neighbor in visited:
                    continue

                new_dist = current_dist + weight
                
                # 4. Aktualisiere Distanzen, wenn ein kürzerer Weg gefunden wurde
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    print(f"  Aktualisiere Distanz zu {neighbor}: {new_dist}")
                    
                    # WICHTIG: Die Distanz muss auch in der 2D-Array-Warteschlange aktualisiert werden,
                    # da sonst die lineare Suche in zukünftigen Iterationen den alten, falschen Wert findet.
                    for i, [node, dist] in enumerate(unvisited_queue):
                        if node == neighbor:
                            unvisited_queue[i][1] = new_dist
                            break

        return distances

# --- Unit Tests und Ausführung ---

def run_tests():
    """Führt Unit Tests für den Dijkstra-Algorithmus durch."""
    print("==============================================")
    print("             UNIT TEST START")
    print("==============================================")

    # 1. Testfall: Korrekte Berechnung der kürzesten Wege
    # Erwartete Ergebnisse vom Startknoten A: A->A=0, A->C=2, A->D=5, A->B=4, A->E=10, A->F=12
    graph1 = Graph()
    graph1.add_edge('A', 'B', 4)
    graph1.add_edge('A', 'C', 2)
    graph1.add_edge('B', 'C', 5)
    graph1.add_edge('B', 'D', 10)
    graph1.add_edge('C', 'D', 3)
    graph1.add_edge('D', 'E', 7)
    graph1.add_edge('C', 'E', 8)
    graph1.add_edge('E', 'F', 2)

    dijkstra1 = Dijkstra(graph1)
    results1 = dijkstra1.find_shortest_paths('A')

    expected1 = {
        'A': 0, 'B': 4, 'C': 2, 'D': 5, 'E': 10, 'F': 12
    }
    
    print("\n--- TEST 1: Kürzeste Wege (A nach allen) ---")
    print("Erwartet:", expected1)
    print("Erhalten:", {k: v if v != INF else '∞' for k, v in results1.items()})

    test1_passed = all(results1.get(node) == dist for node, dist in expected1.items())
    print(f"-> Test 1 {'BESTANDEN' if test1_passed else 'FEHLGESCHLAGEN'}.")


    # 2. Testfall: Richtiges Verhalten bei unverbundenen Knoten
    graph2 = Graph()
    graph2.add_edge('X', 'Y', 5)
    graph2.add_edge('Z', 'W', 1) # Z und W sind isoliert
    
    dijkstra2 = Dijkstra(graph2)
    results2 = dijkstra2.find_shortest_paths('X')

    expected2 = {
        'X': 0, 'Y': 5, 'Z': INF, 'W': INF
    }

    print("\n--- TEST 2: Unverbundene Knoten (X nach allen) ---")
    print("Erwartet: X=0, Y=5, Z=∞, W=∞")
    print("Erhalten:", {k: v if v != INF else '∞' for k, v in results2.items()})

    test2_passed = True
    for node, expected_val in expected2.items():
        actual_val = results2[node]
        # Überprüfung, ob INF korrekt gehandhabt wird
        if (expected_val == INF and actual_val != INF) or (expected_val != INF and actual_val != expected_val):
            test2_passed = False
            break

    print(f"-> Test 2 {'BESTANDEN' if test2_passed else 'FEHLGESCHLAGEN'}.")
    
    print("\n==============================================")
    print("              UNIT TEST ENDE")
    print("==============================================")
    
    return results1 # Gebe das erste Ergebnis für die finale Konsolenausgabe zurück


def print_distance_table(distances):
    """Gibt die Distanztabelle formatiert in der Konsole aus (Schritt Ausgabe)."""
    print("\n\n##############################################")
    print("         FINALE DISTANZTABELLE")
    print("##############################################")
    
    # Sortieren nach Knotenname für eine saubere Ausgabe
    sorted_distances = dict(sorted(distances.items()))
    
    # Header
    print(f"{'Knoten':<10}{'Min. Distanz':>15}")
    print("-" * 25)
    
    # Daten
    for node, dist in sorted_distances.items():
        # Formatieren Sie Unendlich als '∞'
        dist_str = f"{dist}" if dist != INF else "∞"
        print(f"{node:<10}{dist_str:>15}")
    print("-" * 25)


# Hauptausführung
if __name__ == '__main__':
    # Führt die Tests aus und speichert das Ergebnis des Haupt-Testgraphen
    final_results = run_tests()
    
    # Ausgabe der Distanztabelle in der Konsole
    if final_results:
        print_distance_table(final_results)