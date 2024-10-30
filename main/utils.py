    

def get_articles_by_year(articles):
    year2articles = {}
    for art in articles:
        year = art.created_at.year
        if year not in year2articles:
            year2articles[year] = []
        year2articles[year].append(art)
    sorted_articles = sorted(year2articles.items(), key=lambda x: x[0], reverse=True)
    return sorted_articles 
