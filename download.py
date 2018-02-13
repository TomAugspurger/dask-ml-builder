import requests
from bs4 import BeautifulSoup


def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)

    return local_filename


def main(version):
    r = requests.get("https://anaconda.org/TomAugspurger/dask-ml/files")

    soup = BeautifulSoup(r.content, "lxml")

    hrefs = soup.find_all("a", href=True)
    wheel_hrefs = [x.attrs['href'] for x in hrefs
                   if '0.4.1' in x.attrs['href'] and
                   x.attrs['href'].endswith(".whl")]
    urls = ['https://anaconda.org' + href for href in wheel_hrefs]
    n = len(urls)
    for i, url in enumerate(urls, 1):
        download_file(url)
        print(f"Downloaded {url} [{i}/{n}]")


if __name__ == "__main__":
    import sys

    version = sys.argv[1]
    main(version)
