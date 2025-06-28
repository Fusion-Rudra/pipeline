import json

def parse_url_list(file):
    with open(file, 'r') as f:
        urls = [line.strip() for line in f.readlines()]
    return urls

def attack_surface_discovery(url):
    print(f"[+] Analyzing {url}")
    endpoints = [
        {"path": "/login", "params": ["username", "password"]},
        {"path": "/api/user/{id}", "params": ["id"]}
    ]
    print(f"[+] Discovered endpoints for {url}: {endpoints}")
    return endpoints

if __name__ == "__main__":
    urls = parse_url_list("url_list.txt")
    for url in urls:
        result = attack_surface_discovery(url)
        filename = f"{url.replace('https://','').replace('/','_')}_attack_surface.json"
        with open(filename, "w") as f:
            json.dump(result, f, indent=4)
        print(f"[+] Output written to {filename}")
