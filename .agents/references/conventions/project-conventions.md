# Conventions Générales du Projet : Autoformations Solicode (Jekyll)

> **Document de Référence Local & Universel — Niveaux N1, N2, N3**  
> Ce document définit l'architecture et les conventions applicables à l'ensemble des plateformes d'autoformation Solicode basées sur Jekyll et le thème Just the Docs.

---

## 1. Philosophie Pédagogique & Niveaux de Formation

Les autoformations Solicode s'organisent en trois niveaux complémentaires :
- **Niveau 1 — Découvrir :** Acquisition guidée des fondamentaux pas-à-pas (autoformations, syntaxe de base).
- **Niveau 2 — Prototyper :** Structuration, POO, architecture 3-tiers, modélisation UML et prototypes dirigés.
- **Niveau 3 — Développer (ou Réaliser) :** Transposition, frameworks professionnels (Laravel, Alpine.js), méthodologie Scrum, TDD, principes SOLID et projets complets.

---

## 2. Architecture des Collections Jekyll

Le site s'appuie sur une structure de collections Jekyll organisée et standardisée :

```text
├── _missions/         # Grandes missions transversales de formation (M1 à M6)
├── _competences/      # Compétences du référentiel (ex: C.1xx, C.2xx, C.3xx)
├── _domaines/         # Domaines techniques rattachés aux compétences
├── _uas/              # Unités d'Apprentissage (UAs) regroupant les activités
├── _sessions/         # Fiches de cadrage des sessions de formation (S1 à S18)
├── _tutos/            # Guides d'autoformation et tutoriels techniques
├── _prototypes/       # Cahiers des charges des prototypes dirigés (N2)
├── _projets/          # Spécifications des mini-projets et projets d'intégration (N3)
├── _labs/             # Ateliers pratiques d'expérimentation
├── code/              # Code source d'accompagnement et démonstrateurs exécutables
├── images-tutos/      # Médias organisés par domaine et identifiant de tutoriel
└── assets/            # Feuilles de style CSS modulaires et scripts JavaScript
```

---

## 3. Règles d'Intégrité Front Matter & Liquid

1. **Format YAML Strict :** Chaque fichier de collection doit contenir un Front Matter YAML valide avec les métadonnées requises (`layout`, `title`, `nav_order`, `code`, etc.).
2. **Filtre `jsonify` :** Ne jamais entourer `{{ variable | jsonify }}` de guillemets dans le code HTML/JS (`jsonify` génère déjà les quotes nécessaires).
3. **Zéro CSS Inline :** Interdiction d'inclure des balises `<style>` ou du style inline dans les layouts ou composants Markdown. Tous les styles sont centralisés dans `assets/css/`.

---

## 4. Livrables et Traces d'Apprentissage

- **Livrables obligatoires :** Dépôt GitHub propre, fichier Markdown `.md` documenté, ou commits vérifiables.
- **Interdiction formelle de captures d'écran** comme preuve de validation ou livrable d'exercice.
- **Transparence de l'Agent IA :** Mentionner systématiquement les compétences mobilisées à la fin de chaque intervention.
