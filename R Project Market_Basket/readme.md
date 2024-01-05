library('dplyr')
read.csv("C:/Users/sagar/Data sets/market_basket.csv")->market_basket
View(market_basket)
library(arules)
library(arulesViz)
library(ggplot2)
market_basket<-read.transactions(
              file='market_basket.csv',
              sep=',',
              quote="",
              format='basket',
              rm.duplicates=TRUE ,
              skip=1
              )

summary(market_basket)
#Total items are perchest
18440*549*0.0009914
# read the First five record
head(market_basket)

# plots point 
library(RColorBrewer)
  itemFrequencyPlot (x=market_basket,
                    topN=10,
                    type='absolute',
                    horiz=TRUE,
                    col=brewer.pal(10,'spectral')
                                       )
  
#Aprirori Algo
  rule1<-market_basket%>%
        apriori(parameter=list(supp=0.005,conf=0.8))%>%
         sort(by='confidence')
summary(rule1)

rule1 %>% head(n=5) %>% inspect

rule1 %>% tail(n=5) %>% inspect

rule1<-rule1 %>% sort(by='lift')
rule1 %>% head(n=5) %>% inspect
#plot rules
plot(rule1=engine("htmlweidget"))
plot(rule1,method="two-key",engine="htmlweidget")
plot(rule1,method="graph",engine="htmlweidget")
#_________________________

rule2<-market_basket %>%
  apriori(parameter=list(supp=0.009,conf=0.3))%>%
  sort(by='confidence')

summary(rule2)

rule2 %>% head(n=5) %>% inspect

rule2 %>% tail(n=5) %>% inspect

#plot rules2
plot(rule2=engine("htmlweidget"))
plot(rule2,method="two-key",engine="htmlweidget")
plot(rule2,method="graph",engine="htmlweidget")
#_________________________
# rule3

rule3<-market_basket %>%
  apriori(parameter=list(supp=0.02,conf=0.5))%>%
  sort(by='support')
summary(rule3)

rule3 %>% head(n=5) %>% inspect

rule3 %>% tail(n=5) %>% inspect

#plot rules3
plot(rule3=engine("htmlweidget"))
plot(rule3,method="two-key",engine="htmlweidget")
plot(rule3,method="graph",engine="htmlweidget")
#_________________________









