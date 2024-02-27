def paginate(items, per_page):
    pages = [items[i:i+per_page] for i in range(0, len(items), per_page)]
    return {
        'total': len(items),
        'pages_no': len(pages),
        'pages': pages
    }
