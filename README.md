# Latin Text Dataset

28.7 million+ character dataset containing latin texts for machine learning, language generation  and analysation.

## About
This is a small snippet of what the dataset looks like:
```
Cum venisset accitus praedicto die, advocato omni quod aderat commilitio, tribunali ad altiorem
suggestum erecto, quod aquilae circumdederunt et signa, Augustus insistens eumque manu retinens
dextera, haec sermone placido peroravit: Adsistimus apud illos, optimi rei publicae defensores, 
causae communi uno paene omnium spiritu vindicandae, quam acturus tamquam apud aequos iudices.
```
As you can see it's all authentic latin written in the roman times by historic figures such as: [Ceasar](https://en.wikipedia.org/wiki/Julius_Caesar), [Augustus](https://en.wikipedia.org/wiki/Augustus) and many many more. 

There are still certain kinks I have not been able to resolve such as the occasional title or capitalised roman numeral, but because the dataset is so large it shouldn't make a difference as its result is diluted enough for LSTM's (or GRU's) not to pick up on them.

All data and text originates from [thelatinlibrary.com](https://www.thelatinlibrary.com/cred.html) which is to my knowledge in public domain.
## Getting Started

You can either use the pre-scraped and pre-processed file called `latincorpus.txt` or run / modify the `main.py` file and configure it to your liking! Scraping all the text data takes about 3-5 minutes on a computer with a moderately fast cpu and ethernet connection.

### Prerequisites

The following libraries are required to run `main.py`, to install these automatically go to <b>Installing</b> down below.

```
selenium==3.141.0
beautifulsoup4==4.7.1
tqdm==4.31.1
```

### Installing

To install the python libraries described above execute this command:
```
pip3 install -r requirements.txt
```

