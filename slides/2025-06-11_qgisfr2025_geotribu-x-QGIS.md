---
author: Julien Moura
date: 2025-06-11
tags: Geotribu, QGIS, open source, écosystème
title: "Contribuer à l'écosystème FOSS4G : l'exemple de QGIS dans Geotribu"
type: slide
slideOptions:
  theme: geotribu
  transition: 'fade'
---

<!-- Fichier rédigé sur Hedgedoc dans la syntaxe de reveal-md.

Export en PDF :

docker run --name decktape --rm  -v "./:/slides" astefanutti/decktape --pdf-author "**Julien** Moura (Geotribu)" --pdf-title "" --pdf-subject "Support de la conférence de Geotribu à l'édition 2025 des Rencontres des utilisateurs francohones de QGIS" https://slides.geotribu.net/ QGISFR2025_Geotribu_QGIS_2025-06-11.pdf

-->

## Geotribu x QGIS

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_cover_bg.png" data-background-size="cover" -->

:date: 11 juin 2025 16-30 - 20h  
🎙️ Julien Moura  
:billed_cap: ~~Oslandia~~ Geotribu

##### Rencontres des utilisateurs francophones de QGIS

Notes:

- présenter geotribu assez rapidement
- chiffres sur les contenus lié à QGIS :
  - distinguer ceux portant directement sur QGIS de ceux où il est simplement mentionné (par exemple comme outil de visuaisation)
  - progression sur la périoe 2008 - 2025 : nombre absolu, proportionnel
  - types de contenus : tutoriel, news
- analyse lexicométrique

---

## Geotribu c'est qui ?

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

- affiliée à aucune entreprise --> 100% temps libre
- une charte déontologique +/- définie : pas d'autopromo, pas de communiqués de presse ou de pseudos tutos copiés/collés  de promotion,
- relecture collaborative
- bonne ambiance
- qualité > quantité

---

## Geotribu c'est quoi ?

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

- un regroupement spontané de personnes
- un soutien de GeoRezo depuis 2016

---

## Geotribu c'est comment ?

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

- un budget de ... €

---

## historique Geotribu

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

---

## Un exemple parmi d'autres

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

Notes:

- il y a déjà plein de contenus

---

## QGIS dans Geotribu

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

Notes:

- chiffres sur les contenus lié à QGIS :
  - distinguer ceux portant directement sur QGIS de ceux où il est simplement mentionné (par exemple comme outil de visuaisation)
  - progression sur la périoe 2008 - 2025 : nombre absolu, proportionnel
  - types de contenus : tutoriel, news

---

## Objectifs

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

Notes:

- occuper l'espace informationnel
- francophone
- géogeek --> empowerement

---

## Que peut on en dire du projet QGIS

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

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

## Les publics de QGIS

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

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

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

Ce support est sous licence Beerware.

![licence beerware](https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/licence_beerware.png)

👉 RDV à l'apéro ce soir :wink:

---

<!-- .slide: data-background-video="" data-background-video-loop="true" data-background-size="cover" data-background-video-muted="true" -->

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_last_bg.png" data-background-size="cover" -->
