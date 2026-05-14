def extract_product_ids(products):

    return [
        product["id"]
        for product in products
    ]


def has_duplicates(items):

    return len(items) != len(set(items))