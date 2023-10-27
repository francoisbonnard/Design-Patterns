
# Modularity

Tools to analyze architecture : such as metrics, fitness functions, and visualizations

1. **Metrics (Métriques) :** Les métriques logicielles sont des mesures quantitatives qui aident à évaluer divers aspects de la qualité du code et de l'architecture. Parmi les métriques couramment utilisées, on trouve :
   - **Complexité Cyclomatique :** Mesure la complexité d'un programme en comptant le nombre de chemins d'exécution possibles à travers le code.
   - **Nombre de lignes de code (LOC) :** Compte le nombre total de lignes de code dans un programme.
   - **Nombre de méthodes ou fonctions :** Indique combien de fonctions ou de méthodes sont présentes dans le code source.
   - **Couverture de code (Code Coverage) :** Mesure le pourcentage de code source couvert par les tests.
   - **Taux d'instabilité :** Mesure le degré de dépendance d'un module par rapport à d'autres modules.
  
2. **Fitness Functions (Fonctions de fitness) :** Dans le contexte de l'architecture logicielle, les fonctions de fitness sont des critères utilisés pour évaluer à quel point une solution architecturale est bonne par rapport à un ensemble donné de besoins. Ces fonctions peuvent inclure des critères de performance, de sécurité, de maintenabilité, etc.

3. **Visualizations (Visualisations) :** Les visualisations architecturales sont des représentations graphiques de l'architecture logicielle. Cela peut inclure des diagrammes UML (comme les diagrammes de classes, de composants, et de séquence), des cartes de dépendances, des graphiques de flux de données, etc. Ces visualisations aident à comprendre la structure du système, les dépendances entre les composants, et les flux de données à travers l'application.

Chacun de ces outils joue un rôle important dans l'analyse de l'architecture logicielle en fournissant des données quantitatives, des critères d'évaluation et des représentations visuelles qui aident les architectes logiciels à comprendre, évaluer et améliorer l'architecture des systèmes informatiques.

## Definition 38

functions/methods

```python
    # Définition d'une fonction
    def fonction():
        print("Ceci est une fonction.")

    # Définition d'une méthode dans une classe
    class MaClasse:
        def methode(self):
            print("Ceci est une méthode.")

```

classes

```python
    class Voiture:
        def __init__(self, marque, modele):
            self.marque = marque
            self.modele = modele

        def afficher_details(self):
            print(f"Marque : {self.marque}, Modèle : {self.modele}")
```

packages/namespaces

```python
# Dans un fichier math_operations.py
def additionner(a, b):
    return a + b

# Dans un autre fichier main.py
import math_operations

resultat = math_operations.additionner(5, 3)

```

## Measuring Modularitxy 40

### Cohesion 40

functional, sequential, communicational, procedural, logical, coincidental

### Coupling 44

#### Abstractness, Instability, and Distance rom the Main Sequence 44
#### Distance from the Main Sequence 46

### Connascence 48

## Unifying Coupling and Connascence Metrics 52

## From Modules to Components 53

1. What is meant by the term connascence?
2. What is the difference between static and dynamic connascence?
3. What does connascence of type mean? Is it static or dynamic connascence?
4. What is the strongest form of connascence?
5. What is the weakest form of connascence?
6. Which is preferred within a code base—static or dynamic connascence?
