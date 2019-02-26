from gist_search.utils import get_gists
# from utils import get_gists

def search_gists(username, description=None, file_name=None):
    if not description and not file_name:
        print("At least one search parameter must be specified")
        return
    
    gists = get_gists(username)
    results = []
    
    for gist in gists:
        if description and description not in gist['description'].lower():
            continue
        
        if file_name:
            matched = False
            for fname in gist['files']:
                if file_name in fname:
                    matched = True
                    break
            if matched == False:
                continue            
        
        results.append(gist)        
    
    return results
