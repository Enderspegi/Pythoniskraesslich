import unittest
from Graph import Graph
class TestGraph(unittest.TestCase):
    
    def setUp(self):
        """Wird vor jedem Test ausgeführt, um einen neuen, sauberen Graphen zu erstellen."""
        self.graph = Graph()

    # --- Tests für add_node ---

    def test_add_single_node(self):
        """Testet das Hinzufügen eines einzelnen neuen Knotens."""
        self.graph.add_node("A")
        self.assertIn("A", self.graph.adj_list)
        self.assertEqual(self.graph.adj_list["A"], [])

    def test_add_duplicate_node(self):
        """Testet das Hinzufügen eines bereits existierenden Knotens (sollte ignoriert werden)."""
        self.graph.add_node("A")
        initial_size = len(self.graph.adj_list)
        # Die add_node Methode sollte hier False zurückgeben
        self.assertFalse(self.graph.add_node("A")) 
        self.assertEqual(len(self.graph.adj_list), initial_size)

    # --- Tests für add_edge ---

    def test_add_edge_new_nodes(self):
        """Testet das Hinzufügen einer Kante zwischen zwei neuen Knoten."""
        self.graph.add_edge("A", "B", 5)
        self.assertIn("A", self.graph.adj_list)
        self.assertIn("B", self.graph.adj_list)
        self.assertEqual(self.graph.adj_list["A"], [("B", 5)])
        self.assertEqual(self.graph.adj_list["B"], [("A", 5)])

    def test_add_edge_existing_nodes(self):
        """Testet das Hinzufügen einer Kante zwischen bereits existierenden Knoten."""
        self.graph.add_node("X")
        self.graph.add_node("Y")
        self.graph.add_edge("X", "Y", 10)
        self.assertEqual(self.graph.adj_list["X"], [("Y", 10)])
        self.assertEqual(self.graph.adj_list["Y"], [("X", 10)])
    
    def test_add_duplicate_edge(self):
        """Testet das Hinzufügen einer duplizierten Kante (sollte ignoriert werden)."""
        self.graph.add_edge("A", "B", 4)
        # add_edge sollte False zurückgeben, wenn die Kante bereits existiert
        self.assertFalse(self.graph.add_edge("A", "B", 4)) 
        self.assertEqual(len(self.graph.adj_list["A"]), 1)
        self.assertEqual(len(self.graph.adj_list["B"]), 1)

    def test_add_edge_different_weight(self):
        """Testet das Hinzufügen einer Kante mit gleichem Knotenpaar, aber anderem Gewicht (wird hinzugefügt)."""
        self.graph.add_edge("A", "B", 4)
        self.graph.add_edge("A", "B", 8)
        self.assertEqual(len(self.graph.adj_list["A"]), 2)
        self.assertEqual(len(self.graph.adj_list["B"]), 2)
        self.assertIn(("B", 4), self.graph.adj_list["A"])
        self.assertIn(("B", 8), self.graph.adj_list["A"])
        self.assertIn(("A", 4), self.graph.adj_list["B"])
        self.assertIn(("A", 8), self.graph.adj_list["B"])

    # --- Tests für get_neighbors ---

    def test_get_neighbors_existing_node(self):
        """Testet das Abrufen der Nachbarn eines Knotens mit Kanten."""
        self.graph.add_edge("A", "B", 4)
        self.graph.add_edge("A", "C", 2)
        neighbors = self.graph.get_neighbors("A")
        # Da ein Dictionary keine garantierte Reihenfolge hat, prüfen wir die Menge
        expected_neighbors = [("B", 4), ("C", 2)]
        self.assertCountEqual(neighbors, expected_neighbors)

    def test_get_neighbors_isolated_node(self):
        """Testet das Abrufen der Nachbarn eines Knotens ohne Kanten."""
        self.graph.add_node("Z")
        self.assertEqual(self.graph.get_neighbors("Z"), [])

    def test_get_neighbors_non_existent_node(self):
        """Testet das Abrufen der Nachbarn eines nicht existierenden Knotens."""
        self.assertEqual(self.graph.get_neighbors("NichtDa"), [])
        
    # --- Integrationstest (überprüft das Beispiel) ---
    def test_example_usage(self):
        """Überprüft das Verhalten des bereitgestellten Beispielcodes."""
        
        # Knoten hinzufügen
        self.graph.add_node("A")
        self.graph.add_node("B")
        self.graph.add_node("C")
        self.graph.add_node("D")

        # Kanten hinzufügen
        self.graph.add_edge("A", "B", 4)
        self.graph.add_edge("A", "C", 2)
        self.graph.add_edge("B", "C", 1)
        self.graph.add_edge("B", "D", 5)
        self.graph.add_edge("C", "D", 8)

        # Nachbarn von B abrufen
        neighbors_of_B = self.graph.get_neighbors("B")
        expected_B = [("A", 4), ("C", 1), ("D", 5)]
        self.assertCountEqual(neighbors_of_B, expected_B)
        
        # Testet die print_nodes Ausgabe
        # Beachten Sie, dass die Reihenfolge der Nachbarn in der Ausgabe von print_nodes 
        # aufgrund der Dictionary-Iteration von Python 3.7+ deterministisch ist, 
        # die Reihenfolge der Einträge innerhalb der Liste ist jedoch die Einfügereihenfolge.
        output = self.graph.print_nodes()
        self.assertIn("A: [(B, 4), (C, 2)]", output)
        self.assertIn("B: [(A, 4), (C, 1), (D, 5)]", output)
        self.assertIn("C: [(A, 2), (B, 1), (D, 8)]", output)
        self.assertIn("D: [(B, 5), (C, 8)]", output)
        
        # Testet den nicht existierenden Knoten aus dem Beispiel
        neighbors_of_X = self.graph.get_neighbors("X")
        self.assertEqual(neighbors_of_X, [])


if __name__ == '__main__':
    unittest.main()