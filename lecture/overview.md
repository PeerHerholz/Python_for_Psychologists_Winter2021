# Course overview & procedure

Since a good amount of years, the majority of experimental work within `Psychology` (and most other disciplines) requires the application of computers. No matter if `data acquisition` or `analyses`, computer-aided research is almost impossible to avoid and if done right, can be incredible helpful and even enable new types of `analyses` to obtain insights that are otherwise inaccessible. Rather surprisingly to most folks, the efficient utilization of `computers` within `research` also includes `programming` or even requires it. Besides making `research` faster, more streamlined, efficient, stable and less prone to errors, some parts of the  `research workflow` might actually require certain `programming skills`. This for example entails the generation of `experiments` and certain `analyses` of subsequently obtained `data`. While most thesis projects (undergrad and grad), PhD and other positions that actively work with `data` expect `programming` knowledge and/or experience, most programs however don't enable students to gather this skill set as their curricula don't include respective course. Obviously, we won't be able to turn you into expert programmers within one semester, but this course is intended to provide you with a good basic understanding of and capabilities with the [Python](https://www.python.org/) [programming language](https://en.wikipedia.org/wiki/Programming_language). Specifically, this course should build the basis for further endeavors, setting you up with everything you need to know for that.    

### TL;DR

Within this course we will explore the [Python programming language](https://en.wikipedia.org/wiki/Python_(programming_language)), specifically how it can be and why it should be utilized within experimental
psychology. To do so, we will follow a "learning by doing" approach in a tripartite manner. Starting from a basic introduction into `programming` and `python` (Block I), we will evaluate how `python` can be used to run `experiments` (Block II) and `analyze` the resulting `data` (Block III). Thus, we actively seek out `realistic examples` and `workflows`, trying to solve problems with `python`.  Along this way we will also talk about important adjacent topics such as `computing environments` and `IDE`s. For a rather precise outline of the course, please consult the [respective section](https://peerherholz.github.io/Python_for_Psychologists_Winter2021/setup.html).

### How to reach the person in the front

The contact information of the instructor are as follows:

- [Peer Herholz (he/him)](https://peerherholz.github.io/)
- Office hours: [by arrangement via this webpage](https://peerherholz.github.io/contact/)
- E-mail: Herholz@psych.uni-frankfurt.de
- preferred mode of contact: usually online to save time and effort for everyone

<iframe src="https://giphy.com/embed/U6GunJi6B1o7ecMfKc" width="240" height="136" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/justviralnet-funny-mistake-spelling-U6GunJi6B1o7ecMfKc">via GIPHY</a></p>

### Gimme the details

Below you will find important details regarding the course summarized in a compact form. Please consult and familiarize yourself with the information presented there prior to and/or within the first few days of the course. 

#### When and where

The course will run from October 28th, 2021 till February 10th, 2022, every Thursday from 4:15 - 5:45 PM CEST at [PEG 5.G 056](https://qis.server.uni-frankfurt.de/qisserver/rds?state=verpublish&status=init&vmfile=no&moduleCall=webInfo&publishConfFile=webInfoRaum&publishSubDir=raum&keep=y&raum.rgid=7008&noDBAction=y&init=y), Theodor-W.-Adorno-Platz 6, 60323, Frankfurt am Main. Please note that there will be "winter holidays" from December 18th, 2021 - January 13th, 2022 and no classes will take place within this time period.

<iframe width="425" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.openstreetmap.org/export/embed.html?bbox=8.661464452743532%2C50.12589530933526%2C8.67423176765442%2C50.130778644149046&amp;layer=mapnik&amp;marker=50.12833703902714%2C8.667848110198975" style="border: 1px solid black"></iframe><br/><small><a href="https://www.openstreetmap.org/?mlat=50.12834&amp;mlon=8.66785#map=17/50.12834/8.66785">View Larger Map</a></small>

#### What about the pandemic? 

Until further notice, it is assumed that the course will take place in person. This is of course very likely to change given everything we experienced and learned in the last 1 1/2 years. Thus, the course is setup in a way that would allow both in person and virtual meetings. If you want to attend in person, please note that the [3G rule](https://www.bundesregierung.de/breg-en/news/federal-regional-consultation-coronavirus-1949666) applies, meaning that you either have to show _proof_ of _full vaccination_, that you have _recovered from COVID-19_ or provide a _negative antigen test_. Without any of these things you won't be allowed within the University buildings and room where we will meet. Please note that might not be asked when you enter the building but definitely before you enter the room. If you feel uncomfortable doing a busy commute to sit in a room with several other people, please let me know and I'll give my best to come up with a hybrid format. However, based on current regulations there won't be any recordings. Just in case: yes, everyone should wear a mask at all times!

<iframe src="https://giphy.com/embed/opPuISKbzCXAFHhZFJ" width="280" height="280" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/opPuISKbzCXAFHhZFJ">via GIPHY</a></p>



#### Can I use my calculator?

For this class you will need frequent access to a computer that can run Python. None of the analyses that we will be doing will be very intensive, so this does not need to be a modern or "fast" computer. Still, it will need to be running a standard operating system like Windows, Mac OS X, or Linux. Unfortunately, tablets running mobile operating systems (iOS, Android) probably won't work for this purpose. If this is an issue for you, please get in touch with the instructor as soon as possible so that we can try to figure out a solution. Regarding software and installation thereof, please check the next section.

<iframe src="https://giphy.com/embed/DHqth0hVQoIzS" width="240" height="103" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/maths-DHqth0hVQoIzS">via GIPHY</a></p>

#### How do I get all the software and do I have to apply for a loan to get it?

Don't worry at all. First, in order to help you get all the software required for the course, a [comprehensive installation instruction](https://peerherholz.github.io/Python_for_Psychologists_Winter2021/setup.html) was compiled. In a step-by-step manner it guides you through the installation process, covering several `OS`: `windows`, `macos` and `linux`. Second, everything will be completely free of charge as we will only use publicly available [open-source software](https://en.wikipedia.org/wiki/Open-source_software). Why? Because teaching students via [proprietary software](https://en.wikipedia.org/wiki/Proprietary_software) is just not fair and won't help anyone: students have to obtain licenses or use those from the university (which usually doesn't have enough for everyone), leading to tremendous problems regarding inequity now and in the future. Additionally, [opens-source software](https://en.wikipedia.org/wiki/Open-source_software) can do everything, if not more, what [proprietary software](https://en.wikipedia.org/wiki/Proprietary_software) can and is furthermore usually better supported, tested and documented, creating a fantastic sense of community. 

<iframe src="https://giphy.com/embed/CTX0ivSQbI78A" width="240" height="177" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/internet-computer-technology-CTX0ivSQbI78A">via GIPHY</a></p>

#### Where is everything?

All course materials (lecture slides, lecture demo notebooks, lab notebooks, homework assignments, etc.) will be available on the [course website](https://peerherholz.github.io/Python_for_Psychologists_Winter2021/index.html), i.e. the one you're looking at right now. Everything will be completely open and free to use, thus constituting an [open educational resource](https://en.wikipedia.org/wiki/Open_educational_resources) you are free to explore, enhance and share. Thus, this website and all materials will also remain up for the entire duration of the course and beyond, ideally to end of the internet. The usage of this resource and the materials therein will be explained at the beginning and throughout the course.  

<iframe src="https://giphy.com/embed/c20UV66B7zCWA" width="240" height="155" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/superman-phone-looking-c20UV66B7zCWA">via GIPHY</a></p>

#### Syllabus and Text

As noted above, this page serves as the syllabus for this course, with the precise outline indicated in the [respective section](https://peerherholz.github.io/Python_for_Psychologists_Winter2021/outline.html). This syllabus is subject to change; students who miss class are responsible for learning about any changes to the syllabus.

The course has several textbooks, all of which are online and free:

https://www.inferentialthinking.com/

https://jakevdp.github.io/PythonDataScienceHandbook/

Additional reading material might be added but will always be open & free with students being informed about any addition.

<iframe src="https://giphy.com/embed/9dFvgd4ID6ne0" width="240" height="135" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/community-nbc-ken-jeong-9dFvgd4ID6ne0">via GIPHY</a></p>

#### How to get those credits?

##### Exams and Assignments

There will be a `take-home, open book final exam` at the end of the course. It will entail the generation of an `analysis pipeline` `documented` and `run` within a `jupyter notebook`. There will be __no midterm exam__.

There will be `10 homework assignments`. Assignments will be posted as the semester progresses after each meeting.

##### Grading

Your final grade will be based on a `weighted combination` of `homework assignments`, the `final exam` and `class participation`:

- `homework assignments` (50%): There will be `10 homework assignments`. Each `assignment` is worth `5%` of your grade.
- `Final exam` (40%): There will be a `take-home, open book final exam`.
- `Class participation` (10%): Showing up for class, demonstrating preparedness (i.e., doing the readings), contributing to class discussions, and doing the in-class labs. Students who are unable to regularly attend synchronous online class should contact the instructor.

<iframe src="https://giphy.com/embed/yFHkrrbfITemc" width="240" height="173" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/exams-yFHkrrbfITemc">via GIPHY</a></p>

##### Late Homework & Extension Policy

`Homework assignments` are due `5 days` after a given class. `Homework assignments` must be turned in on the due date in order to receive full credit. `Homework assignment` turned in less than 1 week late will be accepted but the score will be penalized by `10%`. `Homework assignments` later than 1 week will _not_ be accepted.

Late `homework assignments` will also be accepted under _exceptional circumstances_ (e.g., medical or family emergency) and at the discretion of the instructor (e.g. exceptional denotes a rare event) with no penalty. This policy allowing for exceptional circumstances is definitely a right, but courtesy to be used when needed and not abused. Should you encounter such circumstances, simply email assignment to instructor and note "late submission due to exceptional circumstances". You do not need to provide any further justification or personally revealing information regarding the details.

##### Academic Honor Code

You are encouraged to discuss problem sets with classmates and work on them together, but certain written submissions must reflect your own, original work. If you worked with other students on a problem set, please include their names in a statement like "I worked on this homework with XX and YY" on the assignment. If in doubt, ask the instructor.

##### Notice about missed work due to religious holy days

Please notify the instructor of your pending absence at least fourteen days prior to the date of observance of a religious holy day. If you must miss a class, an examination, a work assignment, or a project in order to observe a religious holy day, I will give you an opportunity to complete the missed work within a reasonable time after the absence.

### Student Accommodations

- Please request a meeting as soon as possible to discuss any accommodations.
- Please notify me as soon as possible if the material being presented in class is not accessible.
- Please notify me if any of the physical space is difficult for you.

### Code of conduct

This course has a `Code of conduct`. Please inform yourself about the specifics by carefully reading through the [respective section](https://peerherholz.github.io/Python_for_Psychologists_Winter2021/CoC.html).

<iframe src="https://giphy.com/embed/l5s71uAp3CzKwxwkoZ" width="240" height="200" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/theoffice-nbc-the-office-tv-l5s71uAp3CzKwxwkoZ">via GIPHY</a></p>

### Acknowledgements

Several parts of this section are directly taken or adapted from [Alexander Huth's Neuro Data Analysis in Python syllabus](https://github.com/alexhuth/ndap-fa2020) licensed under a [BSD-3-Clause License](https://github.com/alexhuth/ndap-fa2020/blob/master/LICENSE). 