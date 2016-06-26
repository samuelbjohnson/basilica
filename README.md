# Basilica

A CMS for medium-sized websites, built on the Django framework, intended to permit (and require) focus on the *structure* of the content, not just the design of the site and the content itself.

## Philosophy and Intent

### Background

Most systems for authoring websites seem to focus so much on democratizing the creation and curation of content, allowing anyone to put together a website with a professional look and feel with a few clicks of a mouse. This is okay if the site consists of a few static pages, or a single blog. But when the amount and variety of information grows, this approach falls short. (Witness the large number of websites for organizations that have decent content but are completely unusable, despite looking flashy.) 

Basilica is not intended for use by amateurs. The name refers to the idea that while many homeowners can paint, fix broken windows, install kitchen cabinets, or even build a new deck, to build and maintain something larger requires the skills of both a professional architect and a good general contractor. It's not targeted at the simple blogs or sites with a few static pages (the single family domiciles or the web) but the sites of larger organizations who have a plethora of content but not the budget for a full-time web developer.

In ancient Rome, [basilicas](https://en.wikipedia.org/wiki/Ancient_Roman_architecture#Basilica) were the centers of public life--the town halls of their time. Not as large or glamorous as a colliseum or ampitheatre, but nonetheless important infrastructure and deserving of professional attention.

### Goals

The primary goal of Basilica is to provide a framework for organizing the content of the site. Its focus is on the *Information Architecture* rather than its design or content alone. The resulting site will not be one where new structural elements (whether pages, menus, or even an additional column or different position for an image) can be updated by a normal user. The process of authoring and updating content will be kept distinct from changes to the site's structure, which will be kept distinct from the site's look and feel.

We chose Django because it's a stable platform, and its approach dovetails nicely with the above goal. Content can be easily updated via the admin interface. Design can be accomplished through a collection of templates. Basilica shuns the idea of themes, because the look and feel of a website can't easily be divorced from its information architecture, and we don't want to accommodate that idea. Creation of new types of content, as well as additional menus and pages, will require a code change, rather than allowing ad-hoc changes on the fly.

Python is also widely available on most web hosting platforms, meaning that a Basilica site can be deployed on a wide number of environments.

## Concepts

At its core, a Basilica site is a collection of "Pages." Each page is rendered by a template, and that template defines what content is on the page (both its rendered type and its semantic type). For example, a home page might have a menu, a summary, business hours, and a business location. While the summary, business hours, or even location could be updated via the admin interface, the actual content of the home page could not be.

## Setup

We recommend you use [VirtualEnv](https://virtualenv.pypa.io/en/stable/) in order to create a python environment with the correct dependencies. After you've installed it, run

```
virtualenv <env>
source <env>/bin/activate

pip install django
```

where `<env>` is the name you'd like for your virtual environment.
