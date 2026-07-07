# Diagrammes UML - Système de Gestion de Bibliothèque

Ce document présente la structure et le fonctionnement de notre système de gestion de bibliothèque à l'aide de différents diagrammes UML.

---
## 1. Diagramme de Cas d'Utilisation

![Diagramme de cas d'utilisation](uml/Diagramme%20de%20cas%20d'utilisation2.png)

Ce diagramme décrit les fonctionnalités du système du point de vue des acteurs (**Membre** et **Bibliothécaire**). Les cas principaux incluent : rechercher/réserver/emprunter/retourner un livre, gérer le catalogue, valider les opérations, enregistrer des pénalités et envoyer des notifications.

## 2. Diagramme de Classe

![Diagramme de classe](uml/Diagramme%20de%20classe.png)

Ce diagramme présente la structure statique du modèle de données. Il inclut les classes principales (**Personne**, **Membre**, **Librarian**, **Book**, **Copy**, **Reservation**, **Loan**) avec leurs attributs, méthodes et les relations (héritage, associations et cardinalités).

---

## 3. Diagramme de Séquence (Processus d'Emprunt)

![Diagramme de séquence](uml/Diagramme%20de%20séquence.png)

Ce diagramme montre l'interaction chronologique entre le **Membre**, le **Système**, la **Bibliothèque**, l'**Exemplaire** et l'**Emprunt**. Il détaille les étapes de validation (nombre d'emprunts, statut adhérent), la création de l'emprunt et la confirmation au membre.

---

## 4. Diagramme d'État-Transition (Exemplaire de Livre)

![Diagramme d'état de transition](uml/Diagramme%20etat%20transistion.drawio.png)

Ce diagramme illustre les différents états possibles d'un exemplaire de livre dans le système. Les états principaux sont : **Disponible**, **Réservé**, **Emprunté** et **Perdu**. Les transitions sont déclenchées par des événements tels que l'emprunt, le retour, la réservation, l'annulation ou la déclaration de perte.

---


