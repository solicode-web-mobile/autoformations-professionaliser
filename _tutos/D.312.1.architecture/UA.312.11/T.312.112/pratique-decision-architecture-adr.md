---
layout: tuto
title: "Pratique : Décision d'architecture (ADR)"
sous_titre: "Rédiger l'ADR-01 et modéliser le diagramme de séquence Mermaid de la requête HTTP"
slug: "pratique-decision-architecture-adr"
permalink: /tutos/pratique-decision-architecture-adr/
tuto_id: "T.312.112"
version: "normal"
ua: "UA.312.11"
maturite: "UA-Lab"
nav_order: 2
simplified: true
en_construction: true
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Livrable Attendu
- `livrables/architecture/architecture-sprint1.md` (contenant l'ADR-01 et le diagramme de séquence Mermaid).

## 2. Consignes & Jalons de Réalisation
Bâtir le livrable d'architecture en respectant ces 3 jalons :
1. **Rédaction de l'ADR-01 :** Documenter le choix de l'architecture 2 couches avec persistance tabulaire CSV (justifier le gain de temps pour l'amorçage et l'absence de configuration SGBD initiale).
2. **Analyse d'Impact & Conséquences :** Lister les bénéfices (rapidité, simplicité, testabilité) et les contraintes acceptées (pas de transactions, volumétrie limitée).
3. **Modélisation de la Séquence HTTP :** Rédiger le diagramme `sequenceDiagram` décrivant l'enchaînement : Navigateur $\to$ Route $\to$ `ArticleController` $\to$ `ArticleService` $\to$ Vue Blade $\to$ Réponse 200 (ainsi que la branche d'exception 404).

## 3. Points de Vigilance
- ⚠️ L'ADR doit exposer clairement les alternatives qui ont été rejetées (ex: monolithe sans service, ORM direct).
- ⚠️ Le diagramme de séquence doit refléter scrupuleusement les classes et méthodes réelles du code.

## 4. Critères de Validation
- [ ] Le fichier `livrables/architecture/architecture-sprint1.md` existe et adopte le formalisme canonique ADR.
- [ ] Le diagramme de séquence Mermaid est syntaxiquement valide.
- [ ] L'isolation entre couche de présentation et couche de données est formellement garantie.
