---
author: Julien Moura
date: 2025-06-11
language: fr
tags: Geotribu, QGIS, open source, écosystème, contribution
title: "Contribuer à la culture de l'écosystème sur QGIS : l'expérience Geotribu"
type: slide
revealjs:
  backgroundTransition: fade
  transition: slide
---

<!-- Export en PDF :

docker run --name decktape --rm  -v "./:/slides" astefanutti/decktape --pdf-author "Julien Moura (Geotribu)" --pdf-title "Contribuer à la culture de l'écosystème sur QGIS : l'expérience Geotribu" --pdf-subject "Support de la conférence de Geotribu à l'édition 2025 des Rencontres des utilisateurs francohones de QGIS" https://slides.geotribu.net/2025-06-11_qgisfr2025_geotribu-x-QGIS.html QGISFR2025_Geotribu_QGIS_2025-06-11.pdf

-->

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_cover_bg.png" data-background-size="cover" -->

## Contribuer à la culture de l'écosystème sur QGIS : l'expérience Geotribu

:date: 11 juin 2025 16-30 - 20h  
🎙️ Julien Moura  
:billed_cap: Geotribu

> Rencontres des utilisateurs francophones de QGIS

Notes:

- présenter geotribu assez rapidement
- chiffres sur les contenus lié à QGIS :
  - distinguer ceux portant directement sur QGIS de ceux où il est simplement mentionné (par exemple comme outil de visuaisation)
  - progression sur la périoe 2008 - 2025 : nombre absolu, proportionnel
  - types de contenus : tutoriel, news
- analyse lexicométrique

Pitch :

Depuis plus de 15 ans, le collectif [Geotribu](https://geotribu.fr/) anime un espace collaboratif dédié au partage des connaissances sur la géomatique libre et ouverte, avec une attention particulière aux logiciels FOSS4G et notamment QGIS. Cet engagement s'est traduit par la publication d'environ 200 articles et actualités sur QGIS, soit une moyenne d’un contenu par mois.  

Dans l’univers du logiciel libre, la contribution est souvent associée au développement de code. Pourtant, l’expérience Geotribu montre qu’au-delà de l’écriture de lignes de code, il est important de structurer une culture numérique, d’accompagner les professionnel(le)s dans leur veille technologique et de rendre accessibles les évolutions de l’écosystème. En documentant, vulgarisant et analysant l’évolution de QGIS, Geotribu participe à sa diffusion et à l’appropriation des outils par la communauté.  

Cette présentation reviendra sur l’histoire de Geotribu et les enseignements tirés en matière de stratégie éditoriale, de choix des formats et d’évolution des thématiques abordées. Elle proposera également une analyse de l’évolution de QGIS à travers le prisme des articles et des actualités publiées au fil des ans sur Geotribu et ailleurs. Quels grands jalons ont marqué l'évolution du projet QGIS ? Quelles tendances se dégagent pour l’avenir ?

Une occasion de prendre du recul et d’échanger sur le rôle de la documentation et de la communication dans l’écosystème QGIS.

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## Geotribu c'est qui ?

- affiliée à aucune entreprise --> 100% temps libre
- une charte déontologique +/- définie : pas d'autopromo, pas de communiqués de presse ou de pseudos tutos copiés/collés  de promotion,
- relecture collaborative
- bonne ambiance
- qualité > quantité

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## Geotribu c'est quoi ?

> micro-quizz

1. un nom de domaine
1. une association
1. une société d'é associationconomie mixte
1. une SCOP
1. un regroupement spontané de personnes
1. une société écran
1. un media spécialisé :grey_exclamation:

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## Geotribu c'est quoi ?

1. un nom de domaine :white_check_mark:
1. une association ❌ <!-- .element: class="fragment" -->
1. une société d'économie mixte ❌ <!-- .element: class="fragment" -->
1. une SCOP  ❌ <!-- .element: class="fragment" -->
1. un regroupement spontané de personnes :white_check_mark: <!-- .element: class="fragment" -->
1. une société écran  ❌ <!-- .element: class="fragment" -->
1. un media spécialisé :grey_exclamation: <!-- .element: class="fragment" -->

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## Geotribu c'est combien ? :moneybag:

- un coût de **15€**/mois hors extras (besoins ponctuels, goodies, délires) <!-- .element: class="fragment" -->
- une [cagnotte Tipeee](https://fr.tipeee.com/geotribu) qui a récolté 619€ depuis sa création, principalement abondée par les membres <!-- .element: class="fragment" -->
- une [cagnotte LiberaPay](https://liberapay.com/Geotribu/) qui récolte 1€/mois <!-- .element: class="fragment" -->
- un soutien sans faille, c'est le seul qui aille : [GeoRezo](https://georezo.net/) 💞 <!-- .element: class="fragment" -->
- un soutien ponctuel : [Oslandia, mon employeur](https://oslandia.com/2023/03/27/linvestissement-open-source-doslandia/), m'a accordé 7 jours de travail en 2023 dans le cadre des grants open source internes. Merci aux collègues pour le vote 🫶. <!-- .element: class="fragment" -->

Notes:

Étant donné notre non statut d'association, nous ne pouvons avoir de compte bancaire et c'est donc sur mon compte perso que les cagnottes sont versées.  
🐍 Aie confiiiiiiiiiiiiiance 🐍

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## historique Geotribu

Notes:

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## Quelques chiffres

> 🌐 interfaces

- ⛺ 1 site principal
- 🪞 1 miroir du site principal au cas où
- 🇬🇧 1 site anglophone
- 📚 1 site guide de contribution
- 🖼️ 1 pseudo-cdn (~4 900 images)
- 👩‍💻 1 outil en ligne de commandes
- 🗨️ 1 plugin pour QGIS
- ~~1 plugin pour ArcGIS~~
- 📱 1 plugin pour QField
- 📫 1 newsletter
- 📢 3 réseaux sociaux

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## Quelques chiffres

> 🧑‍💻 côté technique

- ~10 de dépôts Git actifs
- 9 500 commits sur le site principal, environ 13 000 en tout
- quelques dizaines de forks

Notes:

- à titre de comparaison, le dépôt principal de QGIS c'est plus de 92 000 commits. Mais bon les nôtres sont des commits conventionnels 😁

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## Quelques chiffres

> 📊 côté fréquentation

<div style="display: flex; align-items: center; justify-content: space-between;">
  <div style="flex: 1; padding-right: 10px;">
    <ul>
  <li>Une bien belle année 2024</li>
  <li>Globalement une dynamique assez stable</li>
  <li>Un travail sur le référencement et le web sémantique</li>
  <li>Pas très algos friendly : articles longs, </li>
  <li>Énormément d'URLs et un historique qui grève les résultats (404, redirections...)</li>
</ul>
  </div>
  <div style="flex: 1;">
    <img src="https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/bilan_2024_voeux_2025/geotribu_referencement_cap_2500_clics_mois_2024-12.webp" alt="Google Search Console Insights - Cap des 2500 clics mensuels" style="max-width: 50%; height: auto;">
  </div>
</div>

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## Quelques chiffres

> ⚽ côté communauté

- 434 commentaires
- +90 personnes ont déjà contribué au site principal
- réseaux sociaux : pas mal d'abonnés (+1600 sur LinkedIn, +500 sur Mastodon)
- 400 abonnés à la newsletter

Notes:

- concernant les RS mais engagement assez inégal voire faible

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## Un exemple parmi d'autres

Notes:

- il y a déjà plein de contenus

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## QGIS dans Geotribu

Notes:

- chiffres sur les contenus lié à QGIS :
  - distinguer ceux portant directement sur QGIS de ceux où il est simplement mentionné (par exemple comme outil de visuaisation)
  - progression sur la périoe 2008 - 2025 : nombre absolu, proportionnel
  - types de contenus : tutoriel, news

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## Objectifs

Notes:

- occuper l'espace informationnel
- francophone
- géogeek --> empowerement

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## Que peut on en dire du projet QGIS

- du sidekick au protagoniste ?
- gratuit = forte adoption : certes mais les autres aussi.
- modularité et facilité de développement de plugins (même si rappelez-vous : les plugins tuent encore des sessions QGIS. Soyez prudents sur la route du développement)
- logiciel hégémonique dans l'écosystème open source : adios gvsig, ciao uDig, slurp SAGA...
- logiciel "guichet unique" des principales solutions géospatiales : géocodage, GDAL, outils de géométrie, de topo, etc.

Notes:

- mature
- communication disparate
- une documentation qui n'a de cesse de s'améliorer cf Harissou et Lova

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## Modularité et facilité de développement des plugins

- pas besoin d'être un développeur pour démarrer et même aboutir
- peu de freins à la publication
- énormément de ressources disponibles
- 👋 le [tutoriel de Geotribu sur Plugin Builder de mars 2010](https://geotribu.fr/articles/2010/2010-09-23_creer_ses_propres_plugin_qgis/)
- 💯 le [support complet et à jour de Nicolas Roelandt](https://roelandtn.frama.io/cours_pyqgis/cr%C3%A9er-une-extension-plugin.html)

Notes:

Bien évoqué ce matin par le laboratoire LETG (vous savez le plugin pour le trait de côte)

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## Modularité et facilité de développement des plugins

> Rappelez-vous : toutes les 5 minutes, une session QGIS est tuée à cause d'un plugin mal développé ⚰️

![Mème QGIS minidumped par le plugin QTribu](https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/meme_qgis_minidumped_qtribu.png)

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## Les publics de QGIS

- les dévs core
- les dév de plugins
- les contributeurs périphériques : documentation, traduction
- les utilisateurs avancés et réguliers
- les nouveaux venus

Le challenge permanent est de les concilier voire de les réconcilier

---

## Des contenus très techniques

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

---

<!-- .slide: data-background-video="https://video.osgeo.org/download/videos/generate/39101d03-465e-491c-8894-c5d1254e9b1d?videoFileIds=112228" data-background-video-loop="true" data-background-size="cover" data-background-video-muted="true" -->

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## Libre comme l'air du houblon

Ce support est sous [licence Beerware](https://fr.wikipedia.org/wiki/Beerware) :

- Sources : <https://github.com/geotribu/slides/>
- Publié sur <https://slides.geotribu.net/>

![licence beerware](https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/licence_beerware.png)

👉 RDV à l'apéro ce soir :wink:

Notes:

Je finirai en vous rappelant qu'à l'instar de nombreux contenus publiés sur Geotribu, ce support est sous licence Beerware. À bon entendeur...

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## Suivre et soutenir Geotribu

![Suivre et/ou soutenir Geotribu](https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/geotribu_suivre-soutenir.png)

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_last_bg.png" data-background-size="cover" -->
