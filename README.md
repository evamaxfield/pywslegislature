# wa-legislature
Data grabbing and potential redesign of Washington State Legislative Web Services.

[Link to the WSLWebServices API](http://wslwebservices.leg.wa.gov/#Table1)

[Link to Python-Firebase Reference](https://pypi.python.org/pypi/python-firebase/1.2)

## About the Project:
I am starting up this project because I personally think the Washington Legislature website could use a bit of a UX makeover.
Additionally, from a data science perspective, I feel that there is a lot of valuable information present in the WSL databases that
could be utilized for interesting datasets and other projects. Making this information more easily accessible and putting it into the
hands of others I believe will help get people to actively engage with their state government.

## How to Contribute:
This is completely open to development from anyone who wants to help. Go ahead and clone or fork this repo and give it a go.
I have finished replicating and expanding the api's functionality. Currently I am working on getting an understanding of what data is available and how I can structure it in my own database. And before I actually store any data I will be building out a website that lets people retrieve datasets for specific targeted queries using my api and the functionality I have built out.

There is additionally an example of a chain api call in the allCalls.py file to understand how they can work together.

This is an update.

## Completed and Uncompleted API Calls:
*There are known issues with additional dictionaries being returned in an individual DataFrame/ csv cell. I am working on a patch. That addresses all use cases.*
- [x] Amendments
- [x] Committees
- [x] Committee Actions
- [x] Committee Meetings
- [x] Documents
- [x] Legislation
- [x] RCW Cite Affected
- [x] Session Law
- [x] Sponsors

## Timeline:
- [x] API Replication and Data Comprehension
- [ ] Fix any leftover bugs from returned objects
- [ ] Create web portal for retrieving datasets with specific targets
   - [ ] Design
   - [ ] Connection to my API
   - [ ] Potential short term storage database for datasets to reduce load
- [ ] Database (Firebase + Relational) Modeling
   - on hold
- [ ] Construct Datapiplines and Manipulation
   - on hold
- [ ] Mass Data Grab and Store
   - on hold
- [ ] Construct Front-End and Connect Services
   - Design Started
- [ ] Create Auto-Updating Scripts
- [ ] Create Exportable Datasets
