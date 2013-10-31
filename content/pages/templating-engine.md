Title: Templating Engine
Date: 2013-08-19
Category: Pages
Tags: templating-engine
Slug: templating-engine
Author: Louie Dinh
Summary: Problem definition for a templating engine.

Motivation
----------

A templating engine combines templates and data models to produce result documents. A good analogy
is baking cookies. You have a cookie cutter(template) and your dough(the data model). You take
your cookie cutter and, depending on the dough, you will stamp out cookies that are clearly
related but are not identical.

Templating engines allows you to seperate logic from presentation in a program. By splitting these two
concerns you are free to modify each piece relatively independently. The split between logic and presentation is
well explored and serves as the primary motivation behind the popular Model-View-Controller
design pattern driving many web and mobile applications today.

In this practice problem, we will try to build a templating engine with a specialized syntax. Some
templating engines allow you to execute normal python code, but that dangles the carrot of model 
data mutation a little too close for my liking.


Prerequisites
-------------

It would be helpful to have some experience with a templating engine before you start this project.
You can download one of the engines below to start experimenting. However, almost everybody has
used a basic templating engine before. What do you think string formatting is?

    name = <insert your name here>
    "Hello %s, I hope you're well today" % name


Problem Statement
-----------------

We will use the jinja2/django syntax because that is what people are most familiar with. 
If you're feeling adventerous, feel free to invent your own syntax.

The rendering of a template should be fairly easy. The template
should take in a dictionary that provides all the data required
to render it.

Here is an example of what our template should be able to do.

    >>template = Template(open("our_template.tmpl", "r"))
    >>data = {"name": "Eva", "age": 23, "apple_count": 5}
    >>output = template.render(data_model=data)
    >>print output

    Hello Eva, what a fine age, 23, to be baking apple pies. You need 7 more apples until you have a dozen. Come back when you're ready!

    >>data = {"name": "Eva", "age": 23, "apple_count": 12, "friends": ["Billy", "John", "Emily"]}
    >>output = template.render(data_model=data)
    >>print output

    Hello Eva, what a fine age, 23, to be baking apple pies. It looks like you've got a round dozen. I'll just go preheat the oven now. 
    After, you can call Billy, John, Emily to help us eat.

### String Interpolation ###

This is just a direct substitution of the string.

    "Hello {{name}}, what a fine age, {{age}}, to be baking apple pies"

### Conditionals and Comparisons ###
    Conditionals allow you to make presentation decisions based on your data.

    {% if apple_count >= 12 %}
        ...
    {% else %}
        ...

### Calculations ###

Simple arithmetic should be supported within your template delimiters.

    "You need {{12 - apple_count}} until you have a round dozen"

### Loops ###
You should be able to loop through lists (and maybe even dictionaries!) to show collections of data.

    "After, you can call {% for friend in friends %}{{friend}},{% endfor %} to help us eat."

That's it for your simple template engine! This is just scratching the surface, feel free to
dig into production templating engines and see how far you can take it.


References
-----------

* [Toy Templating Engine](http://alexmic.net/building-a-template-engine/) - Alex Michael
* [Jinja](http://jinja.pocoo.org/docs/) - Armin Ronacher
* [Django Templates](https://www.djangoproject.com/) - Django Project
* [Pyratemp](http://www.simple-is-better.org/template/pyratemp.html) - Roland Koebler
* [Evoque](https://pypi.python.org/pypi/evoque/) - Mario Ruggier

