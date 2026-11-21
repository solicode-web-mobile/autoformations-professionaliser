# Skill : agent-communication

## Description
Le skill **`agent-communication`** gouverne et outille le protocole de communication formelle inter-agents entre l'**Agent Rédacteur d'Autoformation** (`redacteur-autoformation`) et l'**Agent Réalisation de Sprint** (`realisation-sprint`).

Il garantit la traçabilité des directives, l'alignement des découpages didactiques et l'intégrité des échanges grâce à un système de fichiers physiques émetteurs reliés par liens symboliques (symlinks).

---

## 1. Rôle & Responsabilités
- **Gouvernance des Canaux :** Normalisation du nommage `[agent-emetteur]-to-[agent-recepteur].md`.
- **Gestion des Liens Symboliques :** Création et maintien du symlink dans le dépôt récepteur pointant vers le dépôt émetteur.
- **Templates Structurés :** Fourniture de gabarits rigoureux pour les demandes de cadrage, notifications de livraison et arbitrages techniques.

---

## 2. Prompts Types pour l'Invoquer
- *« Émets une note de cadrage vers l'Agent Réalisation de Sprint pour lui demander d'adopter le nouveau découpage de S0. »*
- *« Crée le canal de communication entre l'Agent Rédacteur et l'Agent Réalisation avec le lien symbolique. »*
- *« Vérifie l'état des demandes en attente dans le canal inter-agents. »*

---

## 3. Mise en Œuvre Pratique du Canal EFP N3

### Initialisation du Symlink sous Windows PowerShell :
```powershell
New-Item -ItemType SymbolicLink `
  -Path "d:\labs-web\projet-imiation-n3\.agents\communication-agents\redacteur-autoformation-to-realisation-sprint.md" `
  -Target "d:\solicode-web-mobile\autoformations-professionaliser\.agents\communication-agents\redacteur-autoformation-to-realisation-sprint.md" `
  -Force
```

En cas d'absence de privilèges développeur pour la création de liens symboliques Windows, un lien dur (`HardLink`) est utilisé comme fallback transparent.
