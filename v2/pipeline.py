
# pipeline_llama.py

import re

import requests

from SPARQLWrapper import SPARQLWrapper, JSON

import nltk

from nltk.corpus import stopwords



# ---------- CONFIG ----------

FUSEKI_URL = "Your fuseki endpoint"

LLAMA_API_URL = "Your llama endpoint"



# ---------- NLTK STOPWORDS SETUP ----------

nltk.download("stopwords")

STOPWORDS = set(stopwords.words("english"))



# ---------- FUNCTIONS ----------



def extract_university(user_query):

    universities = ["Air University", "FAST", "NUST", "National University"]

    for uni in universities:

        if uni.lower() in user_query.lower():

            return uni

    return None



def extract_keywords(user_query):

    """

    Tokenize, lowercase, and remove NLTK stopwords.

    """

    words = re.findall(r"\w+", user_query.lower())

    keywords = [w for w in words if w not in STOPWORDS]

    return keywords



def generate_sparql(user_query, university=None):

    """

    Generate SPARQL query using keywords from user query.

    If keywords are empty, no FILTER is added (returns all FAQs).

    """

    keywords = extract_keywords(user_query)

    

    sparql = f"""

PREFIX : <http://example.org/unifaq#>

SELECT ?question ?answer

WHERE {{

    ?faq a :FAQ ;

         :hasQuestion ?q ;

         :hasAnswer ?a .

    ?q :text ?question .

    ?a :text ?answer .

"""

    if keywords:

        filter_clauses = " || ".join([f'CONTAINS(LCASE(?question), "{k}")' for k in keywords])

        sparql += f"    FILTER ({filter_clauses})\n"



    if university:

        sparql += f'    ?faq :fromUniversity :{university.replace(" ","")} .\n'

    

    sparql += "}"

    return sparql.strip()



# ---------- RUN SPARQL ON FUSEKI ----------



def run_sparql(query):

    sparql = SPARQLWrapper(FUSEKI_URL)

    sparql.setQuery(query)

    sparql.setReturnFormat(JSON)

    results = sparql.query().convert()

    faqs = []

    for result in results["results"]["bindings"]:

        faqs.append({

            "question": result["question"]["value"],

            "answer": result["answer"]["value"]

        })

    return faqs

