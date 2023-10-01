# Metaphor_Assessment

Name: Noel Zacharia
Email: noelzacharia8@gmail.com
Status (junior, senior, graduated): Senior

Link to Project Github: https://github.com/nz2000/Metaphor_Assessment

Project Name: Research Data Ranker

1. Brief Explanation of Project:

When researchers initially start familiarizing themselves with a new domain they usually perform a literature review. Often times when the researcher is new to the field parsing through the data becomes tough as there are multiple publications on each topic across various journals and due to unfamiliarity with the domain identifying the key links/papers becomes tough.

This project is built for new researchers performing literature reviews, it takes in the domain they are researching and along with searching for the best research papers it makes a parallel search to what the best journals in that field are. Then it ranks the research papers based on the results of the journal matches.

The quality of results should increase as the number of search responses increases and the output should provide researchers with a ranked list of matching & most relevant links to research papers in a particular subdomain. This essentially eliminates the learning curve all researches face in navigating & comparing data sources in new domains.

2. How you Built it:

The code makes use of threading and Semaphores (i'm aware that in Python the GIL prevents true concurrency, but I still used this as a tech demonstrator for what could be done to scale up the system) to make 2 requests to the API. The first request gets the raw data i.e., the links to relevant research papers. The second request retrieves matches for the best journals in that field.

Lastly, the raw data gets ranked against the journal data and the ranked list of links is presented to the user.

3. Challenges/Feedback on the API: I found the API to be straightforward & quite easy to use. One feedback I can think of is currently there is an option to only include/exclude domains, however many times we don't know beforehand all the domains that will be suggested. My project acts as a means to rank data when the domains are unknown by relying on the output of searches for best journals. This API could be expanded to include greater control over the parameters being used to rank/categorize results.

4. Why you’re interested in Metaphor : Metaphor works in an interesting problem domain & there is a lot of scope for learning and implementing cutting-edge features. I think I have the right skillset to work in this problem domain.
