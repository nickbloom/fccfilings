library('tm')
library('topicmodels')
library('ggplot2')
library('reshape2')
library('dplyr')
library('igraph')

# Make Corpus
fcc<-Corpus(DirSource("PATH TO FOLDER WITH TEXT FILES",encoding="UTF-8"), readerControl = list(language = "lat"))
fcc <- tm_map(fcc, tolower)

# Remove stopwords
fcctm <- tm_map(fcc, removeWords, stopwords("en"))

# Create the term-document matrix
fcctm<- DocumentTermMatrix(fcctm)

# If you want to de-sparsify it:
fcctm.sp<-removeSparseTerms(fcctm, 0.85)



