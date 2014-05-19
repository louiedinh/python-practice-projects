Title: Static Site Generator
Date: 2014-05-15
Category: Pages
Tags: project
Slug: static-site-generator
Author: Louie Dinh
Summary: Problem definition for a static site generator

Motivation
----------

In the good old days of the WWW, an elite webpage had a bit of text sprinkled with images. 
Here, [take a look at a top internet destination in 1998](https://web.archive.org/web/19981212032831/http://www.slashdot.org/). Nowadays,
you need a constantly updating stream of tidbits, an extensive link profile, social plugins to Twitter and Facebook, and a dedicated community 
of readers. Blogs have dethroned the static homepage and taken the web presence crown.

The web is aesthetically a much nicer place now, but this comes with the cost of great complexity.
Building a great web presence from scratch isn't easy. To save you from the endless pit that is
tweaking your personal web presence, a whole host of companies began offering canned options. We call it the social web.
In terms of customizability, the solutions ranges from strait-jacket-esque monocultures
(Facebook, Twitter, Pinterest, Linkedin) to theme-based customizable (Wordpress, Blogger, Typepad) to 
you-are-god-don't-mess-up (Heroku, Amazon Web Services, Digital Ocean).

Each solutions lives on the Easy-Custom continuum. Unusually user-friendly sites like Facebook
and Twitter cannot offer ridiculous power user features. Conversely, Wordpress cannot offer a
super simple way to get your completely unique snowflake-of-a-web presence online.  

The solution all have drawbacks: paying to attach a custom domain name, limited selection
of themes, cannot modify the site from the comfort of your own server and having to work through their clunky UI. Ideally,
we would have a framework that takes in plain-text and just spits out an awesome looking plain HTML site. 
That way, you can take that site and throw it onto any old web hosting company or an old server running in your closet.

Enter the static site generator. 

The static site generator is a framework that allows you to quickly push _content_ to your site. It's Wordpress on command line crack.
If havn't yet understood the power of the command line, I recommend you checkout the 
[Command Line Parser](|filename|/pages/command-line-parser.md) project. 

Here's how you would create a new post in a site generator:

    1. Create a new file
    2. Fill it with text or optionally HTML, depending on your mood
    3. Hit "Go"

The generator will pick up your changes, convert all text into HTML and upload a shiny new version to your web host. 


Problem Statement
-----------------

For this example, we will be using Jinja2 for templating and Markdown with the meta extension for content. Both are available
for installation via pip.

### Architectural Concerns ###

Fundamentally, a static site generator is quite straight forward. You take all the files in a directory, you pass it through a few utilities
that convert a file of one type (reStructured Text, asciiDoc, Markdown) into HTML, then you spit those files into an output directory.

Our site generator will support two types of documents: pages and articles. Articles are like blog posts, you'll update them frequently
and they should automagically appear on our index.html Pages are long lived content that have permanent homes on our site 
(e.g. about, contact, FAQs).

The valuable lesson here is to design for extensibility. How will you support new file formats like RSS), or a 
new publishing option like direct upload to web host?


### Command Line Interface ###

A barebones CLI needs to support two commands: bootstrap and make.

Bootstrap sets up the general directory structure with the appropriate stubs.

Make will do the following:

    1. Go into the input directory and retrieve all files.
    2. Parse metadata from the file.
    3. Convert the rest of the file into HTML
    4. Output into another directory, respecting their metadata.


### Directory Layout ###

Like Git, we will consider a directory a project. Our directory layout must encourage 
decoupling of presentation from content.  Here is an example of how you would structure your directory.

    ~/simple-blog
        settings.py
        /static                   # Holds your static assets. Images, javascript and css
            jquery.js
            bootstrap.css
        /templates
            /base.html            # A nice base template that carries common elements like headers, navigation and sidebars
            /entry.html           # Template for a blog entry
            /page.html            # Template for a static page
        /content
            /entries              # Blog entries
            /pages                # Static pages like about, contact, index
        /output
    

### Writing ###

You don't want to write your entires in pure HTML, instead you want to use something closer to plain text.
Markdown is a nice compromise between unstructured text and HTML. You get to write what looks like a nicely
organized email and it all gets nicely decorated with <br>'s and <p>'s for you. Your static generator
will take all the text that is markdown (indicated with .md) and put it in their appropriate place.
If you want to write pure HTML then use .html ending. Everything just gets slotted into your themes.

Each file will need a bit of metadata at the top. You can use this to specify date of publication, author,
title. A bunch of hooks that you want to modify on the site itself, but not exactly part of the content. 
Maybe each author will have their own column. You must parse metadata in it's own step.

Here is an example file that can be parsed with the Python package Markdown (with the meta extension).

    Title: My First Blog Post
    Date: 2013-08-19
    Author: Louie Dinh
    Summary: Saying Hi To The World

    My First Blog Post
    ----------

    Just saying hi to the world!

### Configuration ###

You'll need a way to do site-specific configuration. A few things you might want to configure include: domain, twitter handle, and email address.
Your generator will load this settings file to be included during the generation phase. 

Example setings.py:

    EMAIL = "me@pythonpracticeprojects.com"
    DOMAIN = "pythonpracticeprojects.com"

### BONUS: Development Server ###

Ideally, you would have a simple daemon that watches your content directory for changes.
When a file is touched, the daemon will re-run your site generator and keep your output
folder up-to-date. The daemon also runs a simple HTTP server that hosts your file so you can
view your site through a web browser.

### Your Task ###

Create a static site generator. Here is what an example session would look like.

    # Bootstrap
    $ mkdir ~/simple-blog
    $ cd ~/simple-blog
    $ python ~/Code/bloggy.py bootstrap

    # Go add some static stuff like jquery, bootstrap
    ... 

    # Directory Structure
    $ ls
    ~/simple-blog
        settings.py
        /static
            jquery.js
            bootstrap.css
        /templates
            /base.html            # A nice base template that carries common elements like headers, navigation and sidebars
            /entry.html           # Template for a blog entry
            /page.html            # Template for a static page
        /content
            index.md
            /entries              # Blog entries
            /pages                # Static pages like about, contact, index. Right now these are just empty stubs.
                about.md          
                contact.md
        /output

    # Write your first post. Something like "My First Blog Post" described in the section Writing.
    $ vim content/entries/my-first-blog-post 

    # Make
    $ python ~/Code/bloggy.py generate
    
    # Output
    $ cd output
    $ ls
        ~/simple-blog
            ...             # Omitted for clarify
            /output
                index.html  # Contains a link to my-first-blog-post.html
                /static
                    jquery.css
                    bootstrap.css
                /entries
                    my-first-blog-post.html
                /pages
                    about.html
                    contact.html



Now you can just go upload the content of your output directory to any web host.  


References
-----------

* [Pelican](http://blog.getpelican.com/)
* [Nikola](http://getnikola.com/)
* [Hyde](http://hyde.github.io/)
* [Sphinx](http://sphinx-doc.org/)

