url_to_code = {}
code_to_url = {}
counter = 1

def shorten(url):
    global counter

    if url in url_to_code:
        return url_to_code[url]

    code = str(counter)
    counter += 1

    url_to_code[url] = code
    code_to_url[code] = url

    return code

def resolve(code):
    return code_to_url.get(code, None)