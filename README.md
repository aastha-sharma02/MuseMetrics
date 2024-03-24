# MuseMetrics
# README

## Packages needed:

Joblib
Flask
Numpy
Pandas

## Credits:

Kaggle
https://www.kaggle.com/datasets/mateibejan/multilingual-lyrics-for-genre-classification
OpenAI

## File Descriptions
 
model.joblib: Assigns weights to words based on genre and rarity
vectorizer.joblib: Transforms word data into vectors that interact with model
placeholder.txt: 

MuseMetricsSite_test.html: The webpage that the user interacts with and connects to 
MuseApp.py: Flask file to connect python script to html webpage

MuseMetrics_Background.jpeg: background for html webpage
MuseMetrics_Logo.png: musemetrics logo

## Inspiration
Poetry has the power to enrich human perspective, increase empathy and allows writers to express themselves in the purest form. However, the influx of technology in society in recent decades has resulte in a drastic decrease in the value of poetry in our world, along with opportunities for poets to make a living. We wanted to provide a unique opportunity to integrate poetry with an art we engage with frequently - music.

## What it does
MuseMetrics provides poets with insights about what genre of music their poem would fit into as song lyrics. Additionally, it provides similar songs to the poem provided to view for stylistic inspiration. This provides them with the opportunity to reach out to songwriters and artists in the genre, specifically the artists of the most similar songs, to collaborate and produce a song from the poem. 

## How we built it
MuseMetrics working model was built using Python’s Pandas and local HTML. Specifically, we used Term Frequency-Inverse Document Frequency to build a categorization model that takes in lyrics/poems and outputs genres and inspiration to further poet’s careers. This model is trained off of song’s Lyrics where every word is directly related to a genre based on how often it appears in that genre and how rare that word tends to be. 

## Challenges we ran into
While building MuseMetrics, we faced many roadblocks we had to consider and work around. For example, we had to consider many different methods of implementation for suggesting the genre. Among the ideas we had were: building a parser that would break down poems and identify key "genre" words, building a recurrent neural networks to generate similar lyrics, searching through dictionaries of genre-identifying words for words in the poem etc.. We decided on a TF-IDF (Term Frequency - Inverse Document Frequency), which works well becaue it is made for natural language processing. Additionally, we struggled with finding a dataset composed of song lyrics through a variety of genres, simply due to the number of songs that exist, but we were able to find one after searching through Kaggle.

## Accomplishments that we're proud of
We were most proud of being able to fully understand and utilize a TF-IDF vectorization, due to its utility in understanding categorical natural language processing. Additionally, we were proud of being able to create a webpage, as prior to the hackathon no one on our team was familiar with html and css. Our initial plan didn't even include the possibility of creating a webpage, so being able to pull that together was something we all had to work hard to do. 
Additionally, we believe MuseMetrics has the potential to significantly change the projected career gorwth for poets. MuseMetrics allows poets to fully understand their place in the music industry by directly handing them an AI tool that can expand their reach in mainstream society. Poetry is a crucial art, but one that is frequently overlooked, so MuseMetrics will truly allow poets to reach their full potential, and we are proud of creating a product that helps them do that.

## What we learned
Through this project, we were able to expand our skillsets by exploring brand-new concepts as well as refining our existing skills by implementing them in a new way. Going into the project, none of us had experience with TF-IDFs, html or css. We were able to learn how to quickly look through documentation, identify what would apply to our project and implement it in a time-efficient manner. Additionally, facing challenges such as what framework to use to implement the project allowed us to think critically while facing the pressure of time.

## What's next for MuseMetrics
We believe the possibilites for MuseMetrics are endless. In the future, we hope for MuseMetrics to not only become a hub for poets, but also become a platform for singers and songwriters to search for potential collaborators, review poets work and directly reach out to work with them. Additionally, we hope to add features such as suggested keys, suggested lyrics and the option to create an AI-generated demo of the song for poets, allowing them greater control of how their work is used. Another feature we hope to incorporate is developing grammars to parse lyrics so we can look at things such as the phoneme breakdown and analyze meter and rhyme scheme By doing so, we can reincorporate a timeless art in a modern way to continue engaging critically with it.
