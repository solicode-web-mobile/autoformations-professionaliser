---
layout: tuto
title: "Cadrer le projet et définir le périmètre (In-Scope / Out-of-Scope)"
sous_titre: "Délimiter les objectifs SMART, les contraintes et la matrice de périmètre du Blog des Lauréats"
slug: "cadrer-projet"
slug_domaine: "realisation-projet"
slug_ua: "UA.351.21"
permalink: "/tutos/cadrer-projet/"
tuto_id: "T.351.212"
version: "normal"
ua: "UA.351.21"
maturite: "projet"
type: "tuto-tache"
etape: 2
nav_order: 2
simplified: true
en_construction: false
branche: "sprint0"
sprint: "Sprint 0"
statut_realisation: "a_realiser"
livrables:
  - chemin: "docs/cadrage/note-cadrage.md"
    version: "0.1.0"
---

## 1. Travail à faire
Formalisez la note de cadrage du *Blog des Lauréats* en collaboration étroite avec le **Groupe 1** (Product Owner) :
1. **Étape 1 — Recueillir les besoins initiaux :** Échangez avec le Product Owner pour comprendre les finalités de la solution multiplateforme : valoriser les réussites des anciens apprenants, diffuser des retours d'expérience via le web et assurer un accès nomade dédié à la consultation d'articles sur mobile.
2. **Étape 2 — Formuler les objectifs SMART :** Définissez des objectifs Spécifiques, Mesurables, Atteignables, Réalistes et Temporellement définis pour le projet (web et mobile).
3. **Étape 3 — Construire la matrice de périmètre :** Délimitez strictement ce qui sera développé au fil des sprints (*In-Scope* : plateforme web complète et application mobile de consultation) et ce qui est explicitement exclu pour éviter toute dérive (*Out-of-Scope* : administration sur mobile, messagerie, etc.).
4. **Étape 4 — Recenser les contraintes majeures :** Identifiez les contraintes techniques, temporelles, juridiques (RGPD) et d'accessibilité numérique sur les supports web et mobile.
5. **Étape 5 — Rédiger la note de cadrage :** Formalisez le document dans `docs/cadrage/note-cadrage.md` et faites-le valider par le Product Owner.

## 2. Consignes de Réalisation
- Créez le fichier de la note de cadrage :
  ```bash
  echo "" > docs/cadrage/note-cadrage.md
  ```
- Structurez le document selon le plan suivant :
  - **1. Présentation du Projet & Contexte Institutionnel :** Contexte de l'EFP, mission de valorisation des lauréats et double canal de diffusion (plateforme web et application mobile de lecture).
  - **2. Objectifs Stratégiques & SMART :** Indicateurs de réussite quantifiables pour le web et l'accès mobile nomade.
  - **3. Matrice de Périmètre :**
    - *In-Scope (Périmètre inclus) :*
      - *Plateforme Web :* Consultation des articles par catégorie, recherche d'articles, espace d'administration, authentification sécurisée, gestion des statuts de publication, profils lauréats.
      - *Application Mobile :* Affichage du catalogue des articles et lecture complète des articles (mode consultation / lecture seule pour les apprenants et visiteurs en déplacement).
    - *Out-of-Scope (Périmètre exclu) :*
      - *Sur l'application mobile :* Rédaction, modification, modération et administration des articles (réservées exclusivement à la plateforme web).
      - *Globalement :* Messagerie instantanée en direct, paiement en ligne, fonctionnalités de réseau social complexe.
  - **4. Parties Prenantes :** Product Owner (Groupe 1), Développeurs (Web et Mobile), Formateurs référents, Visiteurs et apprenants publics (sur ordinateur et smartphone).
  - **5. Risques Identifiés & Stratégies d'Atténuation :** Disponibilité des contenus, respect des délais de sprint, cohérence de l'API de consultation entre web et mobile.

## 3. Livrable attendu
- **Fichier de projet :** `docs/cadrage/note-cadrage.md`.
- **Critère de conformité :** La matrice In-Scope / Out-of-Scope délimite explicitement le périmètre web complet et le périmètre mobile (limité à l'affichage et la lecture des articles), validée par le Product Owner.
