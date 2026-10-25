---
author: Guilhem Allaman
date: 2026-1X-XX
language: en
tags: Geotribu,QChat,QGIS,QField
title: "QChat: let's chat with your QGIS mates!"
type: slide
revealjs:
  backgroundTransition: fade
  transition: slide
---

## QChat

:speech_balloon: Let's chat with your QGIS mates!

<img src="https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qchat/prez/cat.png" alt="Une photo de chat avec les logos de Geotribu et QGIS" style="height:250px;">

QGIS Open Day - October 2026 session

Guilhem Allaman - <img src="https://cdn.geotribu.fr/img/logos-icones/social/mastodon.png" alt="Logo Mastodon" style="height:40px;vertical-align:middle;"> [@guilhem_allaman@mapstodon.space](https://mapstodon.space/@guilhem_allaman)

*Somebody else* - <img src="https://cdn.geotribu.fr/img/logos-icones/social/mastodon.png" alt="Logo Mastodon" style="height:40px;vertical-align:middle;"> [@somebody_else@mapstodon.space](https://mapstodon.space/@guilhem_allaman)

[Geotribu](https://geotribu.fr/) - <img src="https://cdn.geotribu.fr/img/logos-icones/social/mastodon.png" alt="Logo Mastodon" style="height:40px;vertical-align:middle;">  [@geotribu@mapstodon.space](https://mapstodon.space/@geotribu)

----

### QChat : how it started

One day, in July 2024...

![A green garden with a dog](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qchat/prez/garden.jpeg)

----

### :iphone: Spontaneous phone call

With _GeoJulien_ (Geotribu):

- What about chatting in QField ?
- What about chatting in QField **and** QGIS ?
- Yeah... Why ?
- Why not ?

It's useless, so you absolutely need it!

----

### Let's start with a QGIS plugin

Initially: chat feature in [the already existing _QTribu_ plugin](https://plugins.qgis.org/plugins/qtribu/):

![QTribu on plugins.qgis.org](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qchat/prez/qtribu_qgis_plugin.png)

QTribu: news & blog posts from _Geotribu_ straight into QGIS.

----

### Then, one year later...

New QGIS plugin out there: [`QChat`](https://plugins.qgis.org/plugins/qchat/)!

![QChat on plugins.qgis.org](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/qchat_qod/qchat_qgis_plugin_screenshot.webp)

Currently: [`v1.8.1`](https://plugins.qgis.org/plugins/qchat/version/1.8.1/).

----

### How it was created

- Boilerplated with [the QGIS plugin templater](https://oslandia.gitlab.io/qgis/template-qgis-plugin/) - _credits to Oslandia_.

![Screen of the QGIS plugin templater doc by Oslandia](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/qchat_qod/qgis_plugin_templated_doc_screenshot.webp)

-> One command, a few prompts and you have a functional QGIS plugin with CICD and integrations.

----

### QChat: what's that!?

- have some fun in QGIS while chatting with other connected users
- as devs, have some fun developing this plugin
- meet new QGIS users & people, close or far away
- (maybe) some new useful outcomes ? eg. support, field <-> office communications ? TBD.

----

### QChat: at the beginning

- Study existing open chat protocols: IRC, jabber, matrix...
-> Let's start simple: "Keep it simple" a.k.a. [K.I.S.S.](https://en.wikipedia.org/wiki/KISS_principle) :kissing_heart:
- Open and accessible to anybody
-> You've got QGIS installed ? You can chat now, no need to register on an obscure server out there :)

----

### QChat: dev story

- Initially: PostgreSQL's [`LISTEN`](https://www.postgresql.org/docs/current/sql-listen.html) / [`NOTIFY`](https://www.postgresql.org/docs/current/sql-notify.html) mechanism considered
- Technical decision: HTTP _websocket_, since [`QtWebSockets`](https://doc.qt.io/qt-6/qtwebsockets-index.html) available in `pyqgis` :thumbsup:
- Plugin parameters, using teh boilerplate provided by the templater.
- `QgsDockWidget` -> parallel to what you're used to do in QGIS.

----

### QChat "features"

:point_up: Live demo a bit later :)

- Send some basic text messages
- Mention other users with `@jane_doe` / `@all`
- A few notifications in the QGIS Message Bar
- Share geographic things:
  - Light vector layers
  - Extents
  - Coordinates Reference Systems
  - Images and QGIS map screenshots
  - Graphical Models
  - Processing scripts
- And some funny stuff not listed there :smirk:

----

### QChat server: `gischat`

- On GitHub: [`gischat`](https://github.com/geotribu/gischat)
- Using python and _FastAPI_
- Websockets dispatcher based on _redis_
- No database: stateless websockets, only the last 5 messages are stored
- Docker image available on the [DockerHub](https://hub.docker.com/r/gounux/gischat) + [GHCR](https://github.com/geotribu/gischat/pkgs/container/gischat)
- You can deploy one instance pretty easily and quickly
-> 1 service + a few environment variables

----

### QChat in QField: _QfChat_

- Developed after the QGIS plugin
- Based on the QField plugins framework: QML + Javascript

*TODO: Add a screenshot of QChat in QField*

----

### QChat demo

Open your QGIS, let's chat!

:speech_balloon:

----

### QChat: what about now ?

- Some people on QChat, sometimes...
- We sometimes fix bugs and introduce new features
- Satisfying server test coverage, that said it's not a huge amount of code lines in `gischat`...
- Looking forward feedbacks from the users!

----

### Dev feedback

- Nice to experiment and see how QGIS / Qt are robust, with websockets and so on...
- Happy to chat and meet sometimes new QGIS people in QChat :)
- Discovery of the QField plugins framework
- Somehow feeling like having specified _yet another_ message protocol on our own...

-> Let's get more people joining QChat! :open_hands:

----

### What about next ?

- Create and implement compatibilities / "bridges" with `matrix` and `telegram`:

-> See the QGIS community telegram chat directly within QGIS ?

- Some other funny stuff: emojis, sounds, slash commands, easter eggs... :smirk:
- More fluent UI with QML -> sharing code across QGIS and QField plugins ?

-> What do you guys think ? Any ideas for QChat ? :)

----

### Thank you for your time and attention!

![A photo of a cow with the Geotribu and QGIS logo](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qchat/prez/cow.png)

Let's meet next time in QChat!
