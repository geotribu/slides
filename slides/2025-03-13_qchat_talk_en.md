---
date: 2025-03-13
title: Let's chat in QGIS with QChat!
transition: slide
theme: dark
---

## QChat

:speech_balloon: Let's chat in QGIS!

![cat](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qchat/prez/cat.png)

Lightning Talk - March 2025  
Guilhem Allaman - OPENGIS.ch - Geotribu

----

### How it started

One day... In July 2024...

![a nice sunny garden with a dog](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qchat/prez/garden.jpeg)

Thanks, QField plugins framework :sunglasses: !

----

### :phone: Phone call with Julien Moura (Geotribu&Oslandia)

- Hey! Why not chatting in QField ?
- Hey! Why not chatting in QField **and** QGIS ?
- Hey! Why, actually !?
- Hey! Why not ??

:copyleft: Geotribu :tm::registered::copyright:

----

### Let's start with a QGIS plugin

[QTribu](https://plugins.qgis.org/plugins/qtribu/) QGIS plugin:

- already set up
- registered on plugins.qgis.org
- functional and running GitHub CI

![QTribu on plugins.qgis.org](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qchat/prez/qtribu_qgis_plugin.png)

----

### QChat Philosophy

- Let's study existing open chat protocols (IRC, jabber, matrix... :crying_cat_face:)
-> Let's actually [K.I.S.S.](https://en.wikipedia.org/wiki/KISS_principle) :kissing_heart:
- Let's make it open and accessible to anybody
-> You have a QGIS installed -> You can chat :speech_balloon:

----

### QTribu QGIS plugin dev

- At the beginning: postgres's `LISTEN` / `NOTIFY` mechanism considered
- Choice: websocket connections to server -> `QtWebSockets` available in `pyqgis` :thumbsup:
- Settings [using the QGIS plugin templater](https://oslandia.gitlab.io/qgis/template-qgis-plugin/)
- `QgsDockWidget` -> keep it fluid and parallel

----

### :speech_balloon: In the meantime, somewhere

![dog](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qchat/prez/dog.png)

----

### Main features

- Send text messages to other users
- Embody a _fancy_ avatar (native QGIS icons)
- Ping other users with `@jane_doe` / `@all`
- Notifications: QGIS message bar, sounds...
- Like messages :thumbsup:
- Share vector layers via `geojson`
- Share images and QGIS map canvas screenshots
- Share CRS / extents

----

### QChat Backend

- "gischat": [hosted on GitHub](https://github.com/geotribu/gischat) #gischat #yay
- Written in python - FastAPI
- Websockets dispatcher
- No database: just _stateless_ websockets :kissing_heart:
- Docker image on [DockerHub](https://hub.docker.com/r/gounux/gischat) and [GHCR](https://github.com/geotribu/gischat/pkgs/container/gischat)
- Deployable on a server using a KISS :kiss: `compose` stack
-> 1 single service + a few env variables

----

### QChat ops :metal:

3 server instances running at the moment:

- `gischat.geotribu.net`
-> everybody welcome, please speak :uk:
- `gischat.geotribu.fr`
-> everybody welcome, please speak :fr:
- `staging.gischat.geotribu.net`: staging

Also: :phone: [instances directory](https://github.com/geotribu/gischat/blob/main/instances.json) on GitHub repository (JSON file)

----

### :speech_balloon: Demo

![Snoop Dogg](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qchat/prez/snoopdogg.gif)

----

### What about now ?

- Some random people sometimes use it
- Some bug fix, sometimes...
- Backend test coverage: `93.7%` :smirk: :sunglasses:
- QTribu plugin test coverage: `NaN%` (...) :yum:

----

### What about later ?

- Create some compats through bridges with `matrix` servers (complex)
- Create a specific `"QChat"` QGIS plugin on plugins.qgis.org
- Implement more funny stuff: emojis, sounds, threads, easter eggs...
- QField plugin, of course :smirk:

----

### A bottle in the sea

Feel free to spread the word about the QChat in your upcoming QGIS talks and teachings :wink:

Could be nice to bring even more emulation in the QGIS users community!

----

### Thank you for your time

![cow](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qchat/prez/cow.png)

:question::cow::question: any questions :question::cow::question:
