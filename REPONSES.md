# Réponses aux Questions - Devoir UML & Paradigmes

## Partie 1 — UML & Approche Orientée Objet

**Q1.** Une classe est un modèle (blueprint) qui définit la structure et le comportement. Un objet est une instance concrète de cette classe.  
Exemple : La classe `Copy` est le modèle, tandis qu’un exemplaire spécifique avec `numero="C001"` est un objet.

**Q2.** L'encapsulation consiste à cacher les détails internes d’une classe et à exposer uniquement une interface publique. Dans la classe `Loan`, on rendrait `dateRetour` et `penalite` privés et on fournirait des méthodes comme `enregistrerRetour()` et `calculerPenalite()`.

**Q3.** 
- **Association** : relation faible (un Member peut avoir plusieurs Loans).  
- **Agrégation** : relation "a un" (un Cart contient des Products).  
- **Composition** : relation forte où la partie ne peut exister sans le tout (un Loan est détruit si le Member est supprimé).

**Q4.** L’héritage permet à une classe d’hériter des attributs et méthodes d’une autre. Oui, une classe abstraite `Person` dont héritent `Member` et `Librarian` est pertinente (nom, email communs).

**Q5.** Le polymorphisme permet à des objets de différentes classes d’être traités de manière uniforme via une interface commune. Exemple : Plusieurs formes géométriques (`Circle`, `Rectangle`) implémentant une méthode `calculateArea()`.

**Q6.** Le diagramme de cas d’utilisation montre **quoi** fait le système (fonctionnalités et acteurs). Le diagramme de séquence montre **comment** (échanges de messages dans le temps).

**Q7.** `<<include>>` = réutilisation obligatoire (ex : "Valider emprunt" inclus dans "Emprunter un livre"). `<<extend>>` = comportement optionnel (ex : "Enregistrer pénalité" étend "Retourner un livre" en cas de retard).

**Q8.** Il permet de visualiser clairement les états et transitions d’un objet. Il rend plus visible les règles métier complexes que du texte seul.

**Q9.** La multiplicité indique combien d’instances d’une classe peuvent être liées à l’autre. Entre `Member` et `Loan` : **1..*** (un membre peut avoir 0 à plusieurs emprunts, max 3 simultanés selon règle métier).

**Q10.** L’approche OO organise le système autour d’objets avec état + comportement, favorisant la modularité et la réutilisation, contrairement à l’approche procédurale qui sépare données et fonctions.

## Partie 2 — Paradigmes de Programmation

**Q1.** L’impératif dit **comment** faire (étapes détaillées). Le déclaratif dit **quoi** faire (résultat souhaité sans préciser les étapes).

**Q2.** Une fonction pure retourne toujours le même résultat pour les mêmes entrées et n’a pas d’effets de bord (ne modifie rien à l’extérieur). On évite les effets de bord pour plus de prévisibilité et testabilité.

**Q3.** Meilleure organisation du code, extensibilité (nouveaux types de réductions via nouvelles méthodes), encapsulation, et maintenance plus facile quand le système grossit.

**Q4.** 
- Impératif : C, Python (style procédural)
- Orienté Objet : Java, Python, JavaScript
- Fonctionnel : Haskell, Scala, Python/JS (avec map/reduce)
- Déclaratif : SQL, HTML, CSS

**Q5.** Non. Python et JavaScript sont multi-paradigmes : ils supportent l’impératif, l’OO et le fonctionnel.

**Q6.** Pour le traitement de données (data pipelines, transformations massives, parallélisme) comme dans le calcul de statistiques ou le traitement de logs.

**Q7.** Les classes créées en Partie 2 (Product, Cart) correspondent directement aux classes modélisées dans le diagramme de classes UML (Book/Copy, Loan, etc.).

**Q8.** Django repose principalement sur le paradigme **Orienté Objet**. Exemple : les Models sont des classes Python (`class Book(models.Model):`), et les QuerySets permettent une approche déclarative.

