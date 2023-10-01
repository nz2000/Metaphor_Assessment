from metaphor_python import Metaphor
from threading import *

metaphor = Metaphor("INSERT API KEY HERE")

print("Welcome, this program is meant to help researchers performing literature reviews\n")

semaphore = Semaphore(2)
data_store = []
journal_store = []

#Acquires raw data relevant to search
def raw_data(rfield):
    with semaphore:
        papers = metaphor.search(
            f"best research papers in {rfield}",
            num_results=10,
            use_autoprompt=True,
        )
        response = papers.get_contents()
        for content in response.contents:
            data_store.append((content.title, content.url))
    return

#Acquires top journals related to research field
def journal_filter(rfield):
    with semaphore:
        journal = metaphor.search(
            f"best research journals in {rfield}",
            num_results=10,
            use_autoprompt=True,
        )
        response = journal.get_contents()
        for content in response.contents:
            start = content.url.find("https://") + len("https://")
            end = content.url.find("/", start)
            journal_store.append(content.url[start:end])
    return

#Searchs for links & ranks the data
def search():

    rfield = input(
        "Please enter the specific research topic you are performing a literature review on (examples include topics like Deep Learning, Biochemistry, etc.):\n")

    # Create thread objects
    thread1 = Thread(target=raw_data(rfield))
    thread2 = Thread(target=journal_filter(rfield))

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for all threads to finish
    thread1.join()
    thread2.join()

    result = []

    for i in journal_store:
        for j in data_store:
            if i in j[1]:
                result.append(j)
    for i in data_store:
        if i not in result:
            result.append(i)
    return result


ranked_result = search()

for i in ranked_result:
    print("\n")
    print(i[1])
