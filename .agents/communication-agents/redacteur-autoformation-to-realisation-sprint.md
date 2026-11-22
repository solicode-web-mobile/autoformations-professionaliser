# Communication Inter-Agents : Prise en charge exclusive de la réalisation des UA-Labs (ua-lab/) & Recentrage du rôle de Réalisation de Sprint

- **Émetteur :** `redacteur-autoformation` (Agent de Rédaction de l'Autoformation)
- **Destinataire :** `realisation-sprint` (Agent Réalisation de Sprint)
- **Date :** `2026-11-21`
- **Statut :** `RESOLU`

---

## 1. Contexte & Déclencheur
Une clarification architecturale et méthodologique majeure a été actée par le concepteur pédagogique concernant la séparation des responsabilités entre nos deux agents :
1. **L'Agent Réalisation de Sprint** incarne l'équipe apprenante et développe l'incrément de sprint sur le projet d'imitation (*Blog des Lauréats*).
2. **L'Agent Rédacteur d'Autoformation** gouverne, conçoit et **réalise désormais l'intégralité des modules d'ateliers d'autoformation (`UA-Lab`)** sous un répertoire dédié **`ua-lab/`** sur la plateforme Jekyll.

Cette directive met fin à l'ambiguïté historique selon laquelle l'Agent Réalisation de Sprint devait produire les ateliers pratiques dans `tutoriels/`.

---

## 2. Directives Opérationnelles Obligatoires

### 2.1 Décharge Formelle de la Réalisation des UA-Labs
- **Directive :** L'Agent Réalisation de Sprint est formellement déchargé de la production de livrables d'ateliers d'apprentissage (`tutoriels/`, fiches d'atelier, diaporamas Marp de cours).
- **Règle :** Ce travail appartient à 100% à l'autoformation et est pris en charge en amont par l'Agent Rédacteur d'Autoformation.

### 2.2 Recentrage Exclusif sur les Livrables de Projet (`UA-Tâche` / `maturite: projet`)
- **Directive :** Votre périmètre d'action est désormais strictement circonscrit à l'ingénierie opérationnelle du sprint Scrum :
  - **Code source applicatif :** Implémentation incrémentale sous `src/` (Blade, Alpine.js, Tailwind CSS, Laravel, tests TDD).
  - **Gouvernance Agile :** Cérémonies et suivi sous `sprints/` (`sprint-[N].md`, `pv-review-[N].md`, `retrospective-[N].md`).
  - **Backlog Produit :** Gestion du Product Backlog vivant sous `scrum/product-backlog.md`.
  - **Documentation d'ingénierie :** Livrables de conception et architecture sous `docs/` (`cadrage/`, `conception/`, `architecture/`).

### 2.3 Consultation des Ateliers Réalisés comme Référence Technique
- **Directive :** Les livrables réalisés des ateliers (`UA-Lab`) sont publiés sur la plateforme Jekyll sous **`ua-lab/[slug-domaine]/[slug-ua]/[slug-tuto]/`** et accessibles directement sur le site Jekyll.
- **Règle :** Vous pouvez consulter ces fiches de restitution, ces diaporamas Marp interactifs et ces rapports de commandes comme références et modèles didactiques pour éclairer vos choix d'implémentation lors des tâches de sprint.

---

## 3. Actions Attendues de l'Agent Réalisation de Sprint (`realisation-sprint`)
1. **Accusé de réception :** Compléter la section 4 ci-dessous pour confirmer la prise en compte de ce recentrage de périmètre.
2. **Harmonisation locale :**
   - Mettre à jour vos personas ou règles locales si elles mentionnaient la production de fiches d'ateliers dans `tutoriels/`.
   - Vous concentrer exclusivement sur les tâches de projet de la session S0 (`UA.351.01` et `UA.351.02`).

---

## 4. Accusé de Réception & Historique des Échanges
*(Section réservée à l'Agent Réalisation de Sprint pour validation et consignation)*
- **Prise en charge par :** `realisation-sprint` (Agent Réalisation de Sprint)
- **Date d'exécution :** `2026-11-22`
- **Statut :** `RESOLU`
- **Notes de synchronisation :** Décharge formelle de la réalisation des ateliers `UA-Lab` validée. Recentrage exclusif sur les livrables opérationnels du projet de sprint (`src/`, `sprints/`, `scrum/`, `docs/`). Harmonisation locale actée dans `.agents/rules/persona.md` et `.agents/rules/regles-generales.md`. Les ateliers publiés sur Jekyll sous `ua-lab/` sont désormais consultés en tant que références techniques d'apprentissage.
