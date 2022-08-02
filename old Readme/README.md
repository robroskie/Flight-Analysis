[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=312174&assignment_repo_type=GroupAssignmentRepo)
# Group 325 - 

How Covid19 Has Affected Air Travel Around The World

## Milestones

Milestone I: + Created Github repository as per course specifications.
             + Selected dataset and had it approved by TA Amir. 
             + Introduced, described and imported dataset as a Pandas dataframe to Github repository using Python.
    **Completed: October 25, 2020**

Milestone II:+ Marked down all README files using different elements.
             + Wrote chained the data processing methods to make them more streamline.
             + Wrapped the newly written method chains in functions to make them reusable.
             + Moved function wrapped method chains to a separate .py file.
             + Conducted EDA on the dataset and revised research questions. 
             + Created plots to begin testing EDA hypotheses.
    **Completed: November 18, 2020**

Milestone III:+ Marked down all README files using different elements.
             + Wrote chained the data processing methods to make them more streamline.
             + Wrapped the newly written method chains in functions to make them reusable.
             + Moved function wrapped method chains to a separate .py file.
             + Conducted EDA on the dataset and revised research questions. 
             + Created plots to begin testing EDA hypotheses.
    **Completed: November 28, 2020**

Milestone IV:+ Project video complete and available at: https://www.youtube.com/watch?v=VluC2S7ztLs&feature=youtu.be
    **Completed: December 3rd, 2020**



## Describe your topic/interest in about 150-200 words

Using this data, I want to quantify and show visually just how much of an impact the COVID19 outbreak has had on the airline industry, since the beginning of the pandemic response back around March 2020. The data will be loaded and filtered to incorporate separate dataframes for passenger and cargo airlines. The overall change in daily flight volumes will be presented, with the **prediction being that a downward trend in passenger flights will be seen from March 2019 to present, while cargo flight volumes will have either stayed the same or increased slightly. I also anticipate that with a decrease in overall passenger flights from March onwards this year, the ratio of domestic to international flights will increase.**
This is of specific interest to me because I started a new job in aircraft maintenance just before the pandemic hit and have seen first-hand the impact of COVID19 on the aviation industry as a whole. There are more than enough data and parameters to build a dashboard with this dataset. 

## Describe your dataset in about 150-200 words

The dataset I am using for this project was retrieved from zenodo.org. It consists of crowdsourced flight data collected from OpenSky Network, which is a non-profit Swiss research organization founded to improve air travel. Each of the sets of data are taken in one-month intervals beginning January 2019 and include various metrics that track the what, where and when of both international and domestic flights. Those that are of most interest to me for the project include: the identifier that reveals which airline the flight is with, the aircraft model type, the departing airport name and time of departure, as well as the arrival airport name and time of arrival. The data, presented as compressed csv.gz files, will need to be prefiltered to include only 2 - 3 different passenger and cargo airlines before any other analysis is done, as the total volume around 4 Gb is far too large. The main purpose of selecting this data is to illustrate how air travel was impacted by the COVID19 pandemic and will be continually updated until the pandemic is declared over.

## Team Members

- Luke Roblesky: I was working in the aircraft maintenance industry just before the pandemic hit.

## References

Data retrieved from:
https://zenodo.org/record/4088202#.X5G_sEJKjOQ

Used as a reference:
https://traffic-viz.github.io/scenarios/covid19.html

Airport iata codes taken from this repository:
https://github.com/datasets/airport-codes.git

Credit to:
Matthias Schäfer, Martin Strohmeier, Vincent Lenders, Ivan Martinovic and Matthias Wilhelm.
"Bringing Up OpenSky: A Large-scale ADS-B Sensor Network for Research".
In Proceedings of the 13th IEEE/ACM International Symposium on Information Processing in Sensor Networks (IPSN), pages 83-94, April 2014.

Xavier Olive.
"traffic, a toolbox for processing and analysing air traffic data."
Journal of Open Source Software 4(39), July 2019.



