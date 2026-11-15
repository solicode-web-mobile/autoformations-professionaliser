---
layout: tuto
title: "Prompts & Skills : Gouvernance Scrum Fil Rouge"
sous_titre: "Concevoir le prompt RIO réutilisable pour générer la charte d'équipe et la DoD Fil Rouge"
slug: "prompts-skills-gouvernance-scrum-fil-rouge"
permalink: /tutos/prompts-skills-gouvernance-scrum-fil-rouge/
tuto_id: "T.351.113"
version: "normal"
ua: "UA.351.11"
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
- Transposition de l'Étape 1.2 (Gouvernance d'Équipe Scrum) vers l'application métier Fil Rouge (ex : Plateforme Cinéma).

## 2. Travail à Faire
Concevoir dans `livrables/ia/prompts/prompt-gouvernance-scrum.prompt.md` le prompt d'ingénierie réutilisable permettant à un agent IA de générer une charte d'équipe adaptée au contexte spécifique du Projet Fil Rouge.

## 3. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle :** Scrum Master senior & coach agile spécialisé dans les équipes produit autonomes.
- **Instruction :** Générer les rôles, les règles de collaboration et la DoD adaptés au thème du Projet Fil Rouge à partir des variables `[THEME_PROJET]` et `[TAILLE_EQUIPE]`.
- **Output :** Document Markdown prêt à être intégré dans le dépôt Fil Rouge.
- **Contraintes Négatives :** Pas de rôles fantaisistes hors Scrum, pas de DoD invérifiable.

## 4. Critères de Validation
- [ ] Le prompt est testé avec l'agent IA sur le contexte de l'application Fil Rouge.
- [ ] Le résultat généré est cohérent et exploitable sans retouche manuelle majeure.
