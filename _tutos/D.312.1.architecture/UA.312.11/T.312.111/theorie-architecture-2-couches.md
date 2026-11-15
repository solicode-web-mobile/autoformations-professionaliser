---
layout: tuto
title: "Théorie : Architecture 2 couches"
sous_titre: "Comprendre la séparation des responsabilités, les contrôleurs minces, les classes services et le formalisme ADR"
slug: "theorie-architecture-2-couches"
permalink: /tutos/theorie-architecture-2-couches/
tuto_id: "T.312.111"
version: "normal"
ua: "UA.312.11"
maturite: "UA-Lab"
nav_order: 1
simplified: true
en_construction: true
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase 3 — Conception & Architecture Logicielle / Étape 3.1 — Découplage Architectural & Décision ADR.
- **Stack mobilisée :** Principes SOLID (Single Responsibility), patrons d'architecture MVC et Services, formalisme ADR.

## 2. Travail à Faire (Ce que l'Apprenant Doit Produire)
Effectuer les recherches nécessaires et concevoir une présentation synthétique (support visuel ou mémo écrit) expliquant le principe de séparation des responsabilités, les dangers des « contrôleurs obèses » (*Fat Controllers*), l'intérêt du patron Classe Service pour isoler l'accès aux données et la méthodologie de traçabilité des choix par les ADRs.

## 3. Notions Clés du Sprint à Ne Pas Oublier
- Le principe SoC (Separation of Concerns).
- Le rôle précis d'un contrôleur mince (recevoir la requête HTTP, appeler le service, retourner la réponse Blade).
- Le rôle d'une classe Service comme frontière métier indépendante du protocole web.
- La structure formelle d'un ADR et les critères d'une décision d'ingénierie traçable.

## 4. Points de Réflexion & Auto-Évaluation
- *Pourquoi est-il stratégique de démarrer le Sprint 1 avec une classe Service lisant un CSV plutôt que de coder des requêtes SQL directes dans le contrôleur ?*
- *Quand nous remplacerons le CSV par une base relationnelle au Sprint 2, quel composant sera modifié et quel composant restera intact ?*
