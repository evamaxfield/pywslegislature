# wa-legislature
Data grabbing and potential redesign of Washington State Legislative Web Services.

###[Link to their WSLWebServices API](http://wslwebservices.leg.wa.gov/#Table1)

###About the Project
I am starting up this project because I personally think the Washington Legislature website could use a bit of a UX makeover.
Additionally, from a data science perspective, I feel that there is a lot of valuable information present in the WSL databases that
could be utilized for interesting datasets and other projects. Making this information more easily attainable and putting it into the
hands of others I believe will help get people to actively engage with their state government.

###How to Contribute
This is completely open to development from anyone who wants to help. Go ahead and clone or fork this repo and give it a go.
Currently I am working on getting an understanding of what data is available and how I can structure it in my own database.
The files currently in this repo aren't a completed list of API calls to WSLWebServices but it's a decent start.

There is additionally an example of a chain api call in the allCalls.py file to understand how they can work together.

######Completed and Uncompleted API Calls:
- [ ] Amendments
- [x] Committees
- [ ] Committee Actions
- [x] Committee Meetings
- [x] Documents
- [ ] Legislation
- [ ] RCW Cite Affected
- [ ] Session Law
- [x] Sponsors
