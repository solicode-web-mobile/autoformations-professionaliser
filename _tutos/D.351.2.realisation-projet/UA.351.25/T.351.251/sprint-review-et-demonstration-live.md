---
layout: tuto
title: "Sprint Review et dÃ©monstration live"
sous_titre: "Conduire la dÃ©monstration de l'incrÃ©ment fonctionnel et valider la Definition of Done"
slug: "review-demonstration"
slug_domaine: "realisation-projet"
slug_ua: "cloture-sprint"
permalink: /tutos/review-demonstration/
tuto_id: "T.351.251"
version: "normal"
ua: "UA.351.25"
maturite: "projet"
type: "tuto-tache"
nav_order: 1
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Objectif OpÃ©rationnel & PrÃ©requis
- **Position dans le flux :** Phase D â€” ClÃ´ture de Sprint, RÃ©trospective & Bilan / Ã‰tape 12.1 â€” DÃ©monstration Live.
- **Branche Git :** `sprint1`
- **Fichiers modifiÃ©s ou crÃ©Ã©s :** `scrum/revue-s1.md`.
- **Objectif :** Conduire la dÃ©monstration live de l'incrÃ©ment dÃ©ployable du *Blog des LaurÃ©ats* face au Product Owner et valider critÃ¨re par critÃ¨re les 7 Ã©lÃ©ments de la Definition of Done (DoD).
- **PrÃ©requis :** Tranche verticale complÃ¨te Laravel stabilisÃ©e (`UA.321.13`) sur la branche `sprint1`.

## 2. DÃ©roulement Pas-Ã -Pas de la TÃ¢che

1. **Ã‰tape 1 â€” PrÃ©paration de l'Environnement de DÃ©monstration :**  
   DÃ©marrez le serveur local et prÃ©parez les jeux d'essais :

```bash
cd src
php artisan serve
```

   VÃ©rifiez que le fichier de donnÃ©es tabulaires `src/database/data/articles.csv` contient au moins 3 articles complets pour la dÃ©monstration.

2. **Ã‰tape 2 â€” Conduite de la DÃ©monstration Fonctionnelle en Direct :**  
   Sous la conduite du Product Owner (formateur) :
   - PrÃ©sentez la page d'accueil responsive (`/`).
   - AccÃ©dez Ã  la liste des articles (`/articles`).
   - Cliquez sur un article et dÃ©montrez l'affichage complet de sa vue dÃ©taillÃ©e (`/articles/1`).
   - Modifiez manuellement l'URL avec un identifiant inexistant (`/articles/999`) et dÃ©montrez l'interception propre par la page d'erreur 404 personnalisÃ©e.

3. **Ã‰tape 3 â€” Ã‰margement et Validation Formelle de la DoD :**  
   Renseignez le procÃ¨s-verbal `scrum/revue-s1.md` en auditant les 7 critÃ¨res bloquants :
   - [x] Code source versionnÃ© sur la branche de sprint active (`sprint1`).
   - [x] Architecture 2 couches respectÃ©e (ContrÃ´leur mince $\to$ Classe Service).
   - [x] Gabarit Blade responsive sous Tailwind CSS sans CSS inline.
   - [x] ScÃ©nario nominal (HTTP 200) fonctionnel en direct.
   - [x] ScÃ©nario d'exception (HTTP 404) gÃ©rÃ© de maniÃ¨re rÃ©siliente.
   - [x] Code conforme aux standards PSR-12 et sans warning.
   - [x] Prompts d'ingÃ©nierie rÃ©utilisables opÃ©rationnels.

4. **Ã‰tape 4 â€” Journalisation des commandes :**  
   Consignez la commande de dÃ©marrage dans `tutoriels/realisation-projet/cloture-sprint/review-demonstration/review-demonstration.command.md` :

```bash
cd src
php artisan serve
```

## 3. Livrables & CritÃ¨res de RÃ©ussite
- **Livrables attendus :**
  - ProcÃ¨s-verbal de dÃ©monstration : `scrum/revue-s1.md` sur la branche `sprint1`.
  - Journal des commandes : `tutoriels/realisation-projet/cloture-sprint/review-demonstration/review-demonstration.command.md`.
- **CritÃ¨res de validation :**
  - [ ] L'incrÃ©ment logiciel fonctionne en dÃ©monstration rÃ©elle sans anomalie bloquante.
  - [ ] Les 7 critÃ¨res de la DoD sont formellement validÃ©s avec le Product Owner dans `scrum/revue-s1.md`.
  - [ ] Le journal consigne fidÃ¨lement les commandes opÃ©rationnelles exÃ©cutÃ©es.
