def domain_name(url):
    prefixes = ["http://www.", "http://", "https://", "www."]

    for prefix in prefixes:
        if url.startswith(prefix):
            url = url[len(prefix):]
    domain = ""
    for char in url:
        if char == ".":
            break
        domain += char

    return domain





    # domain = ""
    # if url.startswith("http://www."):
    #     new_url = url.lstrip("http://www.")
    #     for char in new_url:
    #         if char == ".":
    #             break
    #         domain += char
    # elif url.startswith("http://"):
    #     new_url = url.lstrip("http://")
    #     for char in new_url:
    #         if char == ".":
    #             break
    #         domain += char
    # elif url.startswith("https://"):
    #     new_url = url.lstrip("https://")
    #     for char in new_url:
    #         if char == ".":
    #             break
    #         domain += char
    # elif url.startswith("www."):
    #     new_url = url.lstrip("www.")
    #     for char in new_url:
    #         if char == ".":
    #             break
    #         domain += char
    # else:
    #     for char in url:
    #         if char == ".":
    #             break
    #         domain += char
    # return domain

print(domain_name("hyphen-site"))
