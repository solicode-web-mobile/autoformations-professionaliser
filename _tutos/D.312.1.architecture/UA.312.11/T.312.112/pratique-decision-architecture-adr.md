---
layout: tuto
title: "Pratique : Décision d'architecture (ADR-01) & Diagramme de séquence"
sous_titre: "Formaliser le choix d'architecture 2 couches avec persistance CSV et modéliser le flux HTTP sous Mermaid"
slug: "decision-adr-sequence"
slug_domaine: "architecture"
slug_ua: "deux-couches"
permalink: /tutos/decision-adr-sequence/
tuto_id: "T.312.112"
version: "normal"
ua: "UA.312.11"
maturite: "UA-Lab"
nav_order: 2
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Travail à faire
Formaliser la décision stratégique d'architecture logicielle pour le premier sprint du *Blog des Lauréats* sous le formalisme standardisé ADR-01, et modéliser le parcours complet de la requête HTTP en syntaxe déclarative Mermaid.js (`sequenceDiagram`).

Vous devez concevoir :
1. Le document d'architecture opposable : `adr-01-architecture-2-couches.md`.
2. Le fichier source Mermaid de séquence HTTP : `sequence-http.mmd`.
3. Le diaporama Marp de restitution technique : `presentation-decision-adr-sequence.md`.

## 2. Consignes & Spécifications de Réalisation

1. **Jalon 1 — Rédaction de l'ADR-01 :**  
   Rédigez l'Architecture Decision Record en appliquant la structure canonique à 6 sections :
   - *Titre :* ADR-01 — Architecture découplée en 2 couches et persistance tabulaire transitoire CSV.
   - *Statut :* Accepté.
   - *Contexte :* Objectif d'amorçage rapide du Sprint 1, livraison prioritaire de la consultation sans dépendance d'infrastructure SGBD.
   - *Décision :* Découplage strict entre `ArticleController` (orchestrateur HTTP mince) et `ArticleService` (extraction des données depuis `database/data/articles.csv`).
   - *Conséquences :* Testabilité unitaire immédiate, légèreté du projet, absence de migrations relationnelles en S1, transition transparente vers MySQL au Sprint 2.
   - *Alternatives écartées :* Justification de l'abandon du modèle monolithique ("Fat Controller") et de l'installation prématurée d'une base MySQL.

2. **Jalon 2 — Modélisation du Flux HTTP en Diagramme de Séquence :**  
   En syntaxe déclarative Mermaid `sequenceDiagram`, modélisez les deux scénarios d'exécution :
   - *Scénario nominal (HTTP 200) :* Navigateur $\to$ `routes/web.php` $\to$ `ArticleController::show($id)` $\to$ `ArticleService::find($id)` $\to$ lecture CSV $\to$ retour tableau associatif $\to$ contrôleur instancie la vue Blade $\to$ retour page HTML 200 au navigateur.
   - *Scénario d'exception (HTTP 404) :* `ArticleService::find($id)` renvoie `null` $\to$ `ArticleController` déclenche `abort(404)` $\to$ Kernel intercepte l'exception $\to$ rendu de `errors/404.blade.php` $\to$ réponse HTTP 404 au navigateur.

3. **Jalon 3 — Restitution Marp :**  
   Concevez `presentation-decision-adr-sequence.md` au format Marp Markdown pour présenter oralement l'arbitrage architectural et le diagramme de séquence aux parties prenantes.

## 3. Livrables & Critères de validation
- **Livrables attendus :**
  - Document ADR : `tutoriels/architecture/deux-couches/decision-adr-sequence/adr-01-architecture-2-couches.md` sur la branche `sprint1`.
  - Diagramme Mermaid : `tutoriels/architecture/deux-couches/decision-adr-sequence/sequence-http.mmd` sur la branche `sprint1`.
  - Diaporama Marp : `tutoriels/architecture/deux-couches/decision-adr-sequence/presentation-decision-adr-sequence.md` sur la branche `sprint1`.
- **Critères de validation :**
  - [ ] Le document ADR-01 respecte la structure à 6 sections sans omission.
  - [ ] Le diagramme de séquence Mermaid compile sans avertissement et explicite le cas nominal ainsi que l'interception de l'erreur 404.
  - [ ] L'isolation entre le contrôleur mince et la classe service est formellement démontrée.
  - [ ] Le diaporama Marp respecte les règles didactiques (zéro tableau Markdown).
