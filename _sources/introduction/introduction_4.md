# Introduction IV

Within the fourth session we'll finish the `virtualization` section, that is exploring one aspect that might seem adjacent to utilizing `python` within research workflows but is actually a crucial component: `computing environments`. Don't worry: this will also entail hands-on programming, just not directly in `python`. The things covered in this section will introduce central concepts for our subsequent endeavors in this session. More precisely, we'll explore `jupyter notebooks` as one form of interacting with your computer, specifically `python`. Getting a good hang of this will be important as most of our `python` endeavors will happen within `jupyter notebooks` and they are a staple in research workflows.

## Topics 💡👨🏻‍🏫 

In the following you'll find the `objectives` and `materials` for each of the topics we'll discuss during this session.

### Computing environments
You might think: "why do we have to talk about computing environments & reproducibility? I just to code.". 
Fair enough but as hinted at during the introduction, knowing a bit more about this thing called the "computer" and how your code is run will be tremendously helpful and important going further. The sooner you can utilize the respective tools/resources the better as quite a bit, actually all, of your coding will depend on it. We usually trust our machines to do what we ask them to do and while quite often we get the desired output, there's a fair chance that the same task will lead to a different outcome on a different OS, using a different version, etc. . However, what outcomes do we "trust" and why does it converge? All of this relates to "reproducibility" and within this section we'll briefly explore underlying problems and potential (partial) solutions via `python`.    

#### Objectives 📍
- get to know problems wrt computational analysis & reproducibility
- learn about virtualization and its different options
- experiment with python virtualization options
- Ask and answer questions
- Have a great time


#### Materials 📓
Please download the example script [fancy_analyzes.py](https://www.dropbox.com/s/52q11h8r5oj8ocg/fancy_analyzes.py?dl=1).

**Warning**: there will be sounds in the presentation, so might you want to lower the volume on your machine.

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vT1EWyFjE6jxvPhGJ70wK1scXkKgPmVQzYCFVk0CO0fQ0RV0QBVIovOQYAEek2rMuzyVIGLdR_90wB_/embed?start=false&loop=false&delayms=3000" frameborder="0" width="600" height="370" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

### Jupyter notebooks
During the previous session we had a look at different ways of communicating with our computers. Generally speaking we could either use a `GUI` or a `CLI`. In more detail we also have different options to utilize the same `programming language` to communicate with our `computer`, e.g. the `shell`, `jupyter notebooks` and `IDE`s. After we already explored the `shell` a bit, we'll now spend a closer look at `jupyter notebook` and how we can work with them. This is a central topic as the `python introduction` and `data analyzes` parts of the course will be conducted via `jupyter notebook` and you'll have to hand in most assignments via them as well.  

#### Objectives 📍

- learn basic and efficient usage of the jupyter ecosystem & notebooks
    - what is Jupyter & how to utilize jupyter notebooks
- Ask and answer questions
- Have a great time

#### Materials 📓

Please see the rendered version of the `jupyter notebook` [Introduction IV - jupyter notebooks](https://peerherholz.github.io/Python_for_Psychologists_Winter2021/introduction/intro_jupyter.html) in the `ToC` on the left.

## Project related work 🥼🧑🏿‍🔬👩🏻‍🔬

Not applicable, as project related work didn't start yet.

## tasks for subsequent meeting 🖥️✍🏽📖

Your first homework assignment will entail the generation of a `conda environment` called  `bb8` with `python 3.9` and `pandas`, `nilearn`, `jupyter` & sending us the corresponding `environment.yml` via e-mail. 

Your second homework assignment will entail the generation of a `jupyter notebook` with
- **mandatory**: 3 different cells:
  - 1 rendered markdown cell within which you name your favorite movie and describe why you like it via
    max. 2 sentences
  - 1 code cell with an equation (e.g. `1+1`, `(a+b)/(c+d)`, etc.)
  - 1 raw cell with your favorite snack 
- **optional**: a picture of your favorite animal
Once you have everything, save the notebook and e-mail it to Peer.

Please note that the deadline for both assignments is: 24/11/2021, 11:59 PM EST.

### optional/reading/further materials

`Fernando Perez`' presentation on `From interactive exploration to reproducible data science: Jupyter` from [NeuroHackademy](https://neurohackademy.org/) 2020.

<iframe width="560" height="315" src="https://www.youtube.com/embed/nXA39_eW3Q4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>