Title: On The Importance of Side Projects
Date: 2013-08-18
Category:
Tags: learning
Slug: learning-by-projects
Author: Louie Dinh
Summary: Learning progresses one side project at a time.


I asked Zed Shaw, a guru programmer and author of Learn Python The Hard Way, which 5 books to read to master programming. He replied,

    "5 books to master programming?  There's no such list.  To master anything you have to do a hell of a lot of it for years." 
    - Zed Shaw

##
At first I was annoyed at the seemingly flippant answer. Then it hit me. Zed wasn't being flippant, he was telling it like it is. It just sounded
cryptic because a) it was via Twitter and b) there is deep wisdom is platitudes. 
##

The only way to "do a hell of a lot of it for years" is to keep it fun. Your brain isn't wired to willingly labour at a task that has no reward day in and day out. Our brains
crave novelty and fun. If we are to convince ourselves to tackle a task with enthusiasm after failure over and over again, we must learn to work with our biological programming rather than against it.

Paul Buchheit, the creater of Gmail, puts it best in his essay [The Two Paths to Success](http://paulbuchheit.blogspot.ca/2011/02/two-paths-to-success.html):

    My strategy [for success] can be reduced to two rules: 1) Find a way to make it fun and 2) If that fails, find a way to do something 

One of my ways to "do a hell lot of it" is work on side projects. Side projects are not the be-all and end all because you still need to learn
how to work on large legacy code bases, coordinate with others, get buy-in from your team, set and meet deadlines, along with a whole host of other skills. However, I believe that side projects hold a special 
place in the education of a great programmer. Side projects are crucial because they give you a safe haven within which you get to play, experiment and learn from your mistakes. 

There are several principles that I revisit over and over again when I work on side projects. If I forget these principles the project stops being fun, which means that I stop working on the side project.

Your main task while working on side project is to maintain an environment of productive play. 

Keep Side Projects Simple And Stupid
------------------------------------

    “When you treat something like it’s stupid, you have fun with it, you don’t put too much structure around it. You can enjoy different types of success.”
    - Tobias van Schneider 

Doesn't that sound like a a wonderful way to learn? Having fun. Working on a side project should feel a bit like doodling, or singing to yourself in the shower. You're just fooling around and having a good time. 
To keep motivated, one must occassionally experience flow. Flow is where you have to stretch your skills slightly for achieving the task at hand. Since you are setting your own task,
you have a full control over how difficult you want the task to be and keep pushing yourself to find your own flow boundary. 

The other reason for keeping it simple and stupid is efficienty. Side projects are efficient because you have to think of the next tinest step that you can move it forward. What is the next step you can take in the 30 minutes between finishing breakfast and starting your commute to work? The constant crunching in your head actually makes for better work because your subconscious is chewing on it the entire time. 

Learn From Mistakes
-------------------

Children learn faster than nobody else. You go from knowing 0 words to knowing 10,000 by the time you are 6; that is learning to use 5 words every single day. The difference, that I can see, between a child learner and adult learner is that adults get mad at themselves for not achieving perfection right away. When a child falls, it's usually the adult that is much more concerned. All kids know that falling (e.g "failing") only stings for a little. They don't tend to beat themselves up over it.

    "A specific mistake is an excellent source of insight, because a
    mistake gives you something specific to think about. This shifts your
    thinking from coming up with a correct solution (hard), to correcting
    a specific mistake (easy)"
    -Starbird and Burger in The 4 Elements of Effective Thinking

Let yourself make mistakes. One of the great liberations of working on a side project is that you get to be a beginner again. You have no expectations. You get to fail and learn to your heart's content. It's only when you make those mistakes that you viscerally know how to not do it the next time around. 

According to X's hierarchy of learning, you only retain 20% of what you read/hear but 90% of what you do. This is probably because the higher level of engagement and the mistake feedback loop allows you to truly flesh out the nooks and crannies of the problem for yourself. No description can be detailed enough to explain every single aspect of completing even teh simplest of side projects. Only by sitting down and navigating the maze of microdecisions will you actually learn the real texture of the problem. 

Kill the Boring Bits
------------------------

You want to make working on your side project to be as fun as possible. Are there any things that annoy you while working on your side project? Build environment sucks? Editor highlighting is lame? Deploying is a pain in the butt?
Take the time to automate it away.

A specific examples from my own life.

I found that I think about my side projects a lot and it's hard for me to capture it all in one place. I have a personal organization system that makes extensive use of Org Mode (a feature of Emacs). Org Mode is like
a todo list took a hit of cocaine and decided to bootstrap itself into an Operating System. Really, it's amazing. Anyways, I tried a mobile client for OrgMode but it was incredibly painful. I realized that
I ended up defaulting to emailing myself tasks and then just using that as my todo list.  So I wrote a little cronjob that would examine my email and fetch all my tasks, and move it into my organization system
automatically every night. That fun little exercise really showed me the extensibility of Emacs. 

If worst comes to worst, and you can't automate away your pain, just give up and don't do that bit. Anything that feels vaguly like pulling teeth will drive your brain
away from it and you won't want to work on the side project anymore. You must keep it fun.


Go Big or Not
--------------

Some of the most successful projects (Gmail, .....), started out as side projects. You never know where they are going to lead. However, this doesn't have to be the case. My computer is littered with half baked ideas and empty directories that were created in moments of inspiration. It's up to you. You're in full control. If you want to get big, go for it. If you want to keep it small and run it for friends and family, go for it. You are a god (with respect to your side projects). Being the one in charge has the happy side benefit of giving you confidence in your own judgement. See how it didn't turn out horrible.

If you're starting to feel restless or don't want to work on that project anymore, archive it, write a blog post, put it on github or just mentally flag it as complete because you learned what you wanted. 

You are the captain of your own ship and the master of your own destiny (where side projects are concerned). 

    “When you’re working on a side project, you have the time and the choice to invest in learning new things ... You can also be choosier about the feedback you take. When you do take it, it’s because you truly want to get better at something.”
    - Tobias van Schneider



Tutorials, books and lectures are great when you're starting out because they give you a mental framework to hang your hat on. After though, side projects become much much more efficient. 

If you're looking for good side project ideas, just take a look at my [Python Practice Projects](http://pythonpracticeprojects.com) for Python specific projects or
[Karan's Side Project Ideas](https://github.com/karan/Projects) for language agnostic ones.
