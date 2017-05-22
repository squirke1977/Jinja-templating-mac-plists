Learning about Jinja
---

Apple configuration profiles and Munki manifests are structured XML.

[Jinja](http://jinja.pocoo.org/) is a Python templating engine. You provide a template, and in my basic example I'm marking the tags I want to change  

`{{ Like_This }}`  

And letting the python csv libraries and a handy for loop do the rest...

You'll need to install the Jinja libraries to use this code. This can be done using python easy_install...

`sudo easy_install jinja2`

To use, run `python JinjaMobileconfig.py list_of_computers.csv`

There's no proper error handling I'm afraid, it was just designed to be a quick and dirty fix for a problem I needed to solve!

This code is for the creation of `mobileconfig` files to configure [Fuze for Rooms](https://www.fuze.com/products/fuze-rooms) on Mac clients at ThoughtWorks where I work.
