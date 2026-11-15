---
layout: tuto
title: "Prompts & Skills : Service métier et détail Fil Rouge"
sous_titre: "Concevoir le prompt RIO réutilisable pour générer la tranche verticale complète Fil Rouge"
slug: "prompts-skills-service-metier-et-detail-fil-rouge"
permalink: /tutos/prompts-skills-service-metier-et-detail-fil-rouge/
tuto_id: "T.321.133"
version: "normal"
ua: "UA.321.13"
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
- Transposition des Étapes 4.3 & 4.4 (Tranche Verticale Complète & Gestion d'Erreurs) vers le Projet Fil Rouge (ex : Consultation détaillée d'un Film).

## 2. Travail à Faire
Concevoir dans `livrables/ia/prompts/prompt-service-detail.prompt.md` le prompt d'ingénierie réutilisable permettant à un agent IA d'implémenter la tranche verticale complète d'une entité du Projet Fil Rouge (route dynamique, service, contrôleur, layout et gestion 404).

## 3. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle :** Architecte applicatif et développeur Laravel 12 senior.
- **Instruction :** Générer l'ensemble des fichiers de la tranche verticale pour l'entité métier `[ENTITE_METIER]` (ex : Film, Séance) en respectant l'architecture 2 couches (Contrôleur mince IoC + Service découplé), le layout Blade Tailwind et le traitement d'erreur 404.
- **Output :** Fichiers complets avec arborescence exacte et instructions de test.
- **Contraintes Négatives :** Zéro code manquant dans les méthodes de service, typage strict imposé.

## 4. Critères de Validation
- [ ] Le prompt est testé avec l'agent IA sur l'application Fil Rouge.
- [ ] La tranche verticale générée est immédiatement opérationnelle sur serveur local et conforme aux 7 critères de la DoD.
