from pybites_search.all_content import AllSearch

def search_for_content(extracted_subject):
    # Instantiate bob's object
    searcher = AllSearch()
    results = searcher.match_content(extracted_subject)
    return results

