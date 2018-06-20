HackSoc.org rewrite
===

This build system is based on [Node.js][nodejs] and [Handlebars]. It replaces the previous system ([Hackyll]), which used Haskell.

## Writing content

### 'Regular' pages
These can be found in `regular/`, and consist of a YAML header and a HTML body, which is inserted into the template `wrapper.handlebars`.

#### YAML fields
 - **title**: put into the `<title>` element of the page.

### News articles
<!-- TODO document when this section is finished -->

### Minutes
For the moment, minutes are in PDF form and are put into `minutes/`. These are copied into the web directory, along with an index page which lists all the minutes in the directory.

### Templates
Most of the site is generated through the `wrapper.handlebars` template. This takes the content of the page, the title, plus some global values found in `templates/context.yaml`:

 - `servers`: controls the list of servers on the website banner
    - `name`: name of this server (capitalised, hostname only)
    - `href`: link to this server's README (typically just `http://<hostname>.hacksoc.org/`).
 - `nav`: links for navbar
    - `text` and `href`: fairly self-explanatory


### Server READMEs
Written in [Markdown]. Like regular pages, has a YAML header:
 - `hostname`: lowercase hostname of the server
 - `fqdn`: full domain of the server, typically `hostname.hacksoc.org`
 - `name`: purpose/subtitle of the server (eg "shell server")

Don't worry about a H1/title, it's generated by the template. All headings should be H2 or below (`##`).

## Installation

## Adding features

[nodejs]: https://nodejs.org/en/
[Handlebars]: https://handlebarsjs.com/
[Markdown]: https://daringfireball.net/projects/markdown/syntax
[Hackyll]: https://github.com/HackSoc/hacksoc.org/tree/master
<!-- TODO add tag before migration and link here -->