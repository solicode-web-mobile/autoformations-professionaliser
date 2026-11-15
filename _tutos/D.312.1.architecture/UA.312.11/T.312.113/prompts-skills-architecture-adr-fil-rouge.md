---
layout: tuto
title: "Prompts & Skills : Architecture et ADR Fil Rouge"
sous_titre: "Concevoir le prompt RIO réutilisable pour générer le dossier d'architecture et l'ADR du Projet Fil Rouge"
slug: "prompts-skills-architecture-adr-fil-rouge"
permalink: /tutos/prompts-skills-architecture-adr-fil-rouge/
tuto_id: "T.312.113"
version: "normal"
ua: "UA.312.11"
maturite: "UA-Lab"
nav_order: 3
simplified: true
en_construction: true
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Positionnement dans le Flux Fil Rouge
- Transposition de l'Étape 3.1 (Découplage Architectural & Décision ADR) vers l'application métier Fil Rouge (ex : Plateforme Cinéma).

## 2. Travail à Faire
Concevoir dans `livrables/ia/prompts/prompt-architecture.prompt.md` le prompt d'ingénierie réutilisable permettant à un agent IA de produire le dossier d'architecture découplée et l'ADR adapté au Projet Fil Rouge.

## 3. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle :** Architecte logiciel senior spécialisé en découplage d'applications web et Clean Architecture.
- **Instruction :** Prendre en entrée les contraintes du Projet Fil Rouge `[THEME_PROJET]` et formaliser la décision d'architecture 2 couches avec son ADR complet et le diagramme de séquence Mermaid associé.
- **Output :** Document Markdown prêt pour le dossier d'architecture du projet Fil Rouge.
- **Contraintes Négatives :** Pas de préconisation de micro-services disproportionnés, rester dans le cadre du socle 2 couches défini.

## 4. Critères de Validation
- [ ] Le prompt est testé sur l'application Fil Rouge.
- [ ] L'ADR généré est pertinent, argumenté et directement intégrable dans le dépôt.
