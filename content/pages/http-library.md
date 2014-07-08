Title: HTTP Library
Date: 2013-09-19
Category: Pages
Tags: project
Slug: http-library
Author: Louie Dinh
Summary: Problem definition for a HTTP Library

HTTP Library
============

Motivation
----------

If you've been on The Internet for any amount of time at all, you've probably heard of HTTP. It's the protocol that powers the web.
Have you ever wondered why you have to type http://wwww.<insert your favourite website here>.com? That first little bit specifies
the protocol (i.e language) your web browser is going to use to talk to the web server. 

HTTP stands for Hyper Text Transfer Protocol. It is the language we use to transfer Hyper Text (e.g HTML) between computers. Once
the HTML has been transferred, it's up to your browser render it to you in a pretty way. 

By learning a bit about the protocol, you'll be able to understand the web a little better and also hop on the new RESTful bandwagon.
The whole REST movement is essentially telling people not to implement their own protocols on top of HTTP and just use it like
it was meant to be used in the first place. 


Problem Statement
-----------------

### The Protocol ###

I'm going to quickly explain the protocol without going into too much depth. For perspective, the full protocol is so complex that it took an entire group of the 
world's top engineers more than 9 years to _amend_ it (RFC 2616 - an clarification of HTTP/1.1)! 

In HTTP, there are two ideas you must grasp: resources and actions. 

Resources are the nouns of the Internet.  Here are examples of resources: a Wikipedia page, a picture of your friend eating an entire cupcake in one go, 
a video of cats backflipping. They are just objects that live on The Internet that you can interact with. Each resource lives at a Uniform Resource Locator(URL). 

You use HTTP Verbs to interact with a resource. For a language that powers The Internet, the core of HTTP is surprisingly small.
There are only four major verbs to know:

    GET - Retrieve a resource. GET should _never_ have any side effect. 

    POST - Store the attached data as a child resource at the specified URL. Think of this as posting to a forum thread or creating a file inside a folder.

    PUT - Store the attached data at the specified URL. If that URL already points to a resource, replace it; otherwise create it.

    DELETE - Remove the resource at the specified URL.

Keep in mind that not all servers support all verbs. The majority of your web surfing experience consists of GETs and POSTs.
Think of the havoc if you could DELETE random webpages on The Internet!

The other cool thing about HTTP is that it's completely plain text. You can actually read the conversation between your computer and a web server.
It looks a bit like simplified english. Here is an example GET to www.pythonpracticeprojects.com:

    My Computer:
        GET / HTTP/1.1
        User-Agent: curl/7.24.0 (x86_64-apple-darwin12.0) libcurl/7.24.0 OpenSSL/0.9.8y zlib/1.2.5
        Host: pythonpracticeprojects.com
        Accept: */*

    Web Server:
        HTTP/1.1 200 OK
        Server: pythonpracticeprojects.com
        Date: Mon, 09 Jun 2014 17:04:15 GMT
        Content-Type: text/html; charset=utf-8
        Content-Length: 10333
        Last-Modified: Mon, 02 Jun 2014 17:40:30 GMT
        Expires: Mon, 09 Jun 2014 17:14:15 GMT
        Cache-Control: max-age=600
        Vary: Accept-Encoding
        Accept-Ranges: bytes
        
        <html>
            ... The HTML for the site itself...
        </html>

Notice that each statement is terminated with a newline. When my computer finishes talking, it sends an empty line to let the server know.
The lines that look like XXX: YYYY, are called headers. They contain a bit of metadata about  the resource that is about to be
retrieved. Most of them are quite self-explanatory. Cache-Control tells the user's agent (usually a browser) what it is allowed to do
with the resource, once retrieved, to speed up performance. 

If you want to take a look at how your computer is talking with the rest of the world, just open up the debug console on your browser and 
hit the "Network" tab. It's pretty nifty.

### URL Encoding ###

In the above example, we're getting just a plain resource but how do we pass additional information to the webserver to narrow down our results? 
For example, we would like to search google for the top 10 restaurants in the Vancouver area. How would we do that?

URLs support an extra section called the query string. Within the query string, you can pass arbitrary information in a key-value format. 
To get the top 10 restaurants in Vancouver, we would want to pass information like the following:

    limit = 10
    location = "Vancouver"

When you URL encode this, it looks something like: limit%3D10%26location%3D%22Vancouver%22. So your full URL would be www.google.com?query=limit%3D10%26location%3D%22Vancouver%22.

We need URL encoding because there are characters (e.g. / : ?) which have special meaning. When we encode the query string, we replace each symbol with a special %XX code that represents it.
When the URL gets to the other side, the receiving server decodes it by doing the reverse operation and gets the orignal message. 

### Forms and POST'ing ###

Now that we can retrieve all the resources we could possibly want, let's talk about creation. A great example of this is POST'ing to a forum thread. Let's take a look.

    POST /posts HTTP/1.1
    Host: discourse.pythonpracticeprojects.com
    Accept:*/*
    Accept-Encoding:gzip,deflate,sdch
    Accept-Language:en-US,en;q=0.8
    Cache-Control:no-cache
    Connection:keep-alive
    Content-Length:113
    Content-Type:application/x-www-form-urlencoded; charset=UTF-8
    ...
    # Beginning of body.
    raw=Hello+to+this+wonderful+world!&topic_id=4&reply_to_post_number=&category=4&archetype=regular

    HTTP/1.1 200 OK
    Server: nginx/1.4.4
    Date: Sat, 14 Jun 2014 17:40:46 GMT
    Content-Type: application/json; charset=utf-8
    Transfer-Encoding: chunked
    Connection: keep-alive
    Status: 200 OK
    ...

Looks quite a bit like the GET huh? The only difference is that instead of all the information going into the url, a POST actually has a body. Coincedentially enough,
we already know how to encode the body, it's just the same URL Encoding that we used in the GET! 

### Your Task ###

I've been generating all these examples using the curl tool with the -v option. I highly recommend you go play with it just to get a feeling for what you
will be building. Your task is to build a rudimentary version of the curl tool. It should support at least GET and POST, printing out the interaction as it occurs.


Here is a sample interaction of our HTTP library.

    $ purr -v httpie.org
    GET / HTTP/1.1
    Accept: */*
    Accept-Encoding: gzip, deflate
    Host: httpie.org
    User-Agent: HTTPie/0.8.0

    HTTP/1.1 302 Found
    Cache-Control: max-age=1800
    Content-Length: 223
    Content-Type: text/html; charset=iso-8859-1
    Date: Sat, 14 Jun 2014 21:41:41 GMT
    Expires: Sat, 14 Jun 2014 22:11:41 GMT
    Location: https://github.com/jakubroztocil/httpie
    Server: Apache
    X-Awesome: Thanks for trying HTTPie :)

    <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
    <html><head>
    <title>302 Found</title>
    </head><body>
    <h1>Found</h1>
    <p>The document has moved <a href="https://github.com/jakubroztocil/httpie">here</a>.</p>
    </body></html>

    $ purr -m POST api.example.org/person/1 name='John Smith' email=john@example.org cv=@~/Documents/cv.txt
    POST /person/1 HTTP/1.1
    Content-Type: application/x-www-form-urlencoded; charset=utf-8

    name=John+Smith&email=john%40example.org&cv=John's+CV+...

You now know (basically) how the internet works! Pretty cool right?

### Considerations ###

This project can be completed at different layers of abstraction. You should choose the level of difficulty based on what
you want to learn/accomplish by completing this project.

Difficulty Levels:

Easy: Use an existing library to do the actual server communication. Libraries like requests will do the vast majority of the heavy lifting for you. 
      Just parse the command line, and pass on the data appropriately, adding some print statements so you can see what's going on.

Medium: Use Python's provided web libraries like httplib2, urllib3. You get a bit more control over the interaction but you don't need to deal too much 
        with encodings and sockets.

Hacker: Use raw sockets to build your library. Your client will open and close raw internet sockets and then just read and write text to the streams. This is
        a hairy task and should only be attempted by the bravest (and time abundant) of hackers.  

References
-----------

* [httpie](https://github.com/jkbr/httpie) - Jakub Roztočil
* [requests](http://docs.python-requests.org/en/latest/) - Kenneth Reitz
* [httplib](http://docs.python.org/2/library/httplib.html) - Standard Library
* [urlib3](https://github.com/shazow/urllib3) - Andrey Petrov

