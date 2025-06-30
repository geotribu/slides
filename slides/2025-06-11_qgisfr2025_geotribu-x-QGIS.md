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

:date: 11 juin 2025 16h30 - ~~16h55~~ 20h  
_(pour les correspondances SNCF, [cliquer ici](https://www.ter.sncf.com/sud-provence-alpes-cote-d-azur/se-deplacer/prochains-departs/avignon-centre-87765008))_  
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

Au menu :

1. Geotribu
1. QGIS dans les yeux de Geotribu
1. Perspectives et prospectives croisées

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

![logo Geotribu](https://cdn.geotribu.fr/img/internal/charte/geotribu_logo_rectangle_384x80.png)

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## Geotribu c'est quoi ?

> micro-quizz

1. un nom de domaine
1. une association
1. une société d'économie mixte
1. une SCOP
1. un regroupement spontané de personnes
1. une société écran
1. un media spécialisé

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

Notes:

- avec la disparition de medias spécialisés réellement indépendants

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## Geotribu c'est qui ?

- affiliée à aucune entreprise --> 100% temps libre
- un noyau de quelques personnes seulement
- une 10aine de satellites +/- réguliers
- bonne ambiance
- aucune obligation de résultat ou d'investissement

Notes:

- faire du travail sérieux sans se prendre au sérieux
- et moi ? je fais office de vieux de la vieille, un peu responsable de publication, support technique et ayatollah du Markdown

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## :handshake: Valeurs

- côté pile : la technique
- côté face : le libre
- une charte déontologique +/- définie : pas d'autopromo, pas de communiqués de presse ou de pseudos tutos copiés/collés depuis le blog d'entreprise, pas de contenu généré par IA
- relecture collaborative
- qualité > quantité
- ton libre en théorie mais la visibilité impacte la critique pour ménager les susceptibilités

Notes:

- la ligne éditoriale implique une gestion de ses identités. Par exemple, je n'écris jamais sur mes projet Oslandia. Ça me permet de répondre à des insinuations.

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## 🎯 Mission

<div style="display: flex; align-items: center; justify-content: space-between;">
  <div style="flex: 1; padding-right: 10px;">
    <ul>
      <li>francophone</li>
      <li>occuper l'espace informationnel</li>
      <li>valoriser</li>
      <li>géogeek --> "empowerement"</li>
      <li>structurer une culture du libre dans la géomatique</li>
      <li>accompagner les professionnel(le)s dans leur veille technologique</li>
    </ul>
  </div>
  <div style="flex: 1;">
    <img src="https://cdn.geotribu.fr/img/articles-blog-rdp/divers/mission.png" alt="Mission. Crédits : Metalus" style="max-width: 50%; height: auto;">
  </div>
</div>

Notes:

Rendre accessibles les évolutions de l’écosystème. En documentant, vulgarisant et analysant l’évolution de QGIS, Geotribu participe à sa diffusion et à l’appropriation des outils par la communauté.  

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

## Ligne de vie

![Ligne de vie Geotribu](https://cdn.geotribu.fr/img/articles-blog-rdp/geotribu/history/geotribu_frise_chrono_2006-2017.png)

Notes:

----

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

### Album photos 2008

![Geotribu en 2008](https://cdn.geotribu.fr/img/articles-blog-rdp/geotribu/history/web_timemachine_geotribu_2008.png)

----

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

### Album photos 2012

![Geotribu en 2012](https://cdn.geotribu.fr/img/articles-blog-rdp/geotribu/history/web_timemachine_geotribu_2012.png)

----

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

### Album photos 2020

![Geotribu tweet renaissance](https://cdn.geotribu.fr/img/articles-blog-rdp/geotribu/history/geotribu_tweet_renaissance_2020.png)

----

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

### Album photos 2020

![Geotribu en 2020](https://cdn.geotribu.fr/img/articles-blog-rdp/geotribu/history/geotribu_2020-04-30.png)

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
- du Python, du Material for Mkdocs
- de la CI/CD
- des bots

Notes:

- à titre de comparaison, le dépôt principal de QGIS c'est plus de 92 000 commits. Mais bon les nôtres sont des commits conventionnels 😁

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## Quelques chiffres

> 📊 côté fréquentation

<div style="display: flex; align-items: center; justify-content: space-between;">
  <div style="flex: 1; padding-right: 10px;">
    <ul>
  <li>Une année 2024 record</li>
  <li>Globalement une dynamique assez stable</li>
  <li>Un travail sur le référencement et le web sémantique</li>
  <li>Pas très algos friendly : articles longs = % de lecture complète faible</li>
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

## QGIS dans les yeux de Geotribu

![QMaro](https://cdn.geotribu.fr/img/articles-blog-rdp/memes/qmaro_fme_like_u_banner.png)

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## Une longue histoire

- premier article dédié en novembre 2008 sur le workshop Quantum GIS
- ~200 contenus directement liés à QGIS dont beaucoup sont des news
- environ autant où QGIS est secondaire

Notes:

- chiffres sur les contenus lié à QGIS :
  - distinguer ceux portant directement sur QGIS de ceux où il est simplement mentionné (par exemple comme outil de visuaisation)
  - progression sur la périoe 2008 - 2025 : nombre absolu, proportionnel
  - types de contenus : tutoriel, news

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## En synthèse

- du _sidekick_ au _protagoniste_ <!-- .element: class="fragment" -->
- gratuit = forte adoption : certes mais les autres aussi. <!-- .element: class="fragment" -->
- logiciel hégémonique dans l'écosystème open source : adios gvsig, ciao uDig, slurp SAGA... <!-- .element: class="fragment" -->
- logiciel "guichet unique" des principales solutions géospatiales : géocodage, GDAL, outils de géométrie, de topo, etc. <!-- .element: class="fragment" -->
- une documentation et une traduction qui n'ont eu de cesse de s'améliorer <!-- .element: class="fragment" -->
- mais une communication disparate et très technico centrée <!-- .element: class="fragment" -->

Notes:

- documentation --> du coup, valeur ajoutée moins évidente pour Geotribu et autres tutoriels : c'est très bien !

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## QGIS : 23 ans

![QGIS Splash Screens - Crédits : Thomas Gratier](https://raw.githubusercontent.com/webgeodatavore/qgis-splash-screens-birthday/master/qgis-splash-screens-no-text.gif)

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## Une très belle dynamique

![QGIS - Stats février 2025](https://geoobserver.de/wp-content/uploads/2025/02/2025_02_18_08_01_13_QGIS_Dashboard_Metabase.png)

Notes:

Ok mais au-delà des chiffres qui sont largement biaisés, what else ?

- une super évolution depuis Quantum GIS
- des virages pas toujours bien négociés comme le passage 2 --> 3. Le passage à la 4, ça
- enfin une vitrine web à la hauteur du projet

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

## Et maintenant ?

> Perspectives et prospectives

![Géo boule de cristal](https://cdn.geotribu.fr/img/internal/icons-rdp-news/globe_boule_cristal_divination.jpg)

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## Continuer de mûrir : sortir du garage

- assumer son rôle de logiciel leader <!-- .element: class="fragment" -->
- s'inspirer d'autres projets d'importance confrontés aux enjeux de l'utilisation à l'échelle industrielle <!-- .element: class="fragment" -->
- prendre le temps de faciliter, consolider les retours des utilisateurs et de les placer au coeur de la culture du projet <!-- .element: class="fragment" -->

![meme map is hard](https://cdn.masto.host/mapstodonspace/media_attachments/files/114/115/888/904/094/028/original/c35c9011391e9694.png) <!-- .element: class="fragment" -->

Notes:

- car c'est toujours dur de faire des cartes

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## Concilier les publics

- les dévs core
- les dév de plugins
- les contributeurs périphériques : documentation, traduction
- les utilisateurs avancés et réguliers
- les nouveaux venus
- les autres

> Le challenge est de les concilier voire de les réconcilier

Notes:

- renforcer la communication
- ajouter de l'animation de l'écosystème

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## Rôle de Geotribu là-dedans : la continuité

- continuer de communiquer et animer
- continuer de soutenir les acteurs institutionnels comme l'OSGeo FR <!-- .element: class="fragment" -->
- s'appuyer sur QGIS pour parler des autres briques de l'écosystème libre <!-- .element: class="fragment" -->

![QGIS 4 Star Wars](https://cdn.geotribu.fr/img/articles-blog-rdp/memes/qgis4_banner.png)

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## Rôle de Geotribu là-dedans : les changements

- moins d'articles techniques ?
- démystifier les dynamiques communautaires sous-jacentes au projet QGIS <!-- .element: class="fragment" -->
- valoriser les modes de financement  <!-- .element: class="fragment" -->

![Gouvernance association QGIS](https://qgis.org/community/organisation/QGIS-ORG_Organizational_structure.png)

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## Challenges à relever et dilemmes à résoudre : l'IA

![IA](https://cdn.masto.host/mapstodonspace/media_attachments/files/114/315/137/511/109/435/original/590330ddd0910be2.png)

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_slide_bg.png" data-background-size="cover" -->

## Lancez-vous

- rédiger des tutoriels et actualités
- nourrir la pompe d'échanges de savoirs avec vos retours d'expérience
- constituer et diffuser une veille
- relayer et vulgariser les nouveautés

> sur Geotribu ou ailleurs !

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

### Questions / réponses

<!-- .slide: data-background-video="https://video.osgeo.org/download/videos/generate/39101d03-465e-491c-8894-c5d1254e9b1d?videoFileIds=112228" data-background-video-loop="true" data-background-size="cover" data-background-video-muted="true" -->

---

<!-- .slide: data-background-image="https://cdn.geotribu.fr/img/slides/2025/qgisfr_geotribu-x-qgis/osgeo_qgis_rencontres_fr_2025_last_bg.png" data-background-size="cover" -->
