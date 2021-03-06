# download_images

**download_images** is a Python library for downloading images from google.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install download_images.

```bash
pip install download_images
```

Download download_images from [my github](https://github.com/Xarcrax/download_images) and use in your project

## Usage

```
import download_images

download_images.main(["-q", "<query>", <args>"]) searches google for images from args and downloads them
```

### Example
An example use is given on [my github](https://github.com/Xarcrax/download_images) in the examples repository

### Args

```python
usage: download_images.main([-h] -q QUERY [QUERY ...] [-l LIMIT] [-o OUTPUTDIR]
                          [-c CHROMEDRIVER] [-epq EXACTQUERY]
                          [-oq OPTIONALQUERY] [-eq EXCEPTQUERY]
                          [-cs CUSTOMSIZE | -sz {s,m,l,i,>2MP,>4MP,>6MP,>8MP,>10MP,>12MP,>15MP,>20MP,>40MP,>70MP,>400*300,>640*480,>800*600,>1024*768}]
                          [-ar {s,t,w,p}]
                          [-co {red,orange,yellow,green,teal,blue,purple,pink,white,gray,black,brown} | -ct {full-colour,black-and-white,transparent}]
                          [-it {face,photo,clipart,lineart,animated}]
                          [-ft {jpg,gif,png,bmp,svg,webp,ico,raw}] [-s SITE]
                          [-ss {True,False}] [-ur {CC,Commercial,Other}])

Get arguments for searching for images

optional arguments:
  -h, --help            show help message and exit
  -q QUERY [QUERY ...], --query QUERY [QUERY ...]
                        Query to search for
  -l LIMIT, --limit LIMIT
                        Max images to download
  -o OUTPUTDIR, --outputDir OUTPUTDIR
                        Full directory to store images in
  -c CHROMEDRIVER, --chromedriver CHROMEDRIVER
                        Full directory to the chromedriver
  -epq EXACTQUERY, --exactQuery EXACTQUERY
                        Words that must be included (e.g. bat under)
  -oq OPTIONALQUERY, --optionalQuery OPTIONALQUERY
                        Words that are optional (e.g. apple tree)
  -eq EXCEPTQUERY, --exceptQuery EXCEPTQUERY
                        Words that must not be included (e.g. cat vote)
  -cs CUSTOMSIZE, --customSize CUSTOMSIZE
                        Find image of specific size
  -sz {s,m,l,i,>2MP,>4MP,>6MP,>8MP,>10MP,>12MP,>15MP,>20MP,>40MP,>70MP,>400*300,>640*480,>800*600,>1024*768}, --size {s,m,l,i,>2MP,>4MP,>6MP,>8MP,>10MP,>12MP,>15MP,>20MP,>40MP,>70MP,>400*300,>640*480,>800*600,>1024*768}
                        Find images of specific size (s, m, l, icon, >x MP,
                        >x*y)
  -ar {s,t,w,p}, --aspectRatio {s,t,w,p}
                        Find images of specific aspect ratio (square, tall,
                        wide, panoramic)
  -co {red,orange,yellow,green,teal,blue,purple,pink,white,gray,black,brown}, --colour {red,orange,yellow,green,teal,blue,purple,pink,white,gray,black,brown}
                        Find images containing specific colour
  -ct {full-colour,black-and-white,transparent}, --colourType {full-colour,black-and-white,transparent}
                        Find images of specific type
  -it {face,photo,clipart,lineart,animated}, --imageType {face,photo,clipart,lineart,animated}
                        Type of image
  -ft {jpg,gif,png,bmp,svg,webp,ico,raw}, --fileType {jpg,gif,png,bmp,svg,webp,ico,raw}
                        Type of file
  -s SITE, --site SITE  Specific site or domain to search (e.g. example.com,
                        .org
  -ss {True,False}, --SafeSearch {True,False}
                        Should SafeSearch be on
  -ur {CC,Commercial,Other}, --usageRights {CC,Commercial,Other}
                        Filter by usage rights
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Disclaimer
This program lets you download images from Google. Please do not use any image in a way that violates its copyright terms. 

Google Images is a search engine that merely indexes images and allows you to find them. It does NOT produce its own images and, as such, it doesn't own copyright on any of them. The original creators of the images own the copyrights.

Images published in the United States are automatically copyrighted by their owners, even if they do not explicitly carry a copyright warning. You may not reproduce copyright images without their owner's permission, except in "fair use" cases, or you could risk running into lawyer's warnings, cease-and-desist letters, and copyright suits. Please be very careful before its usage! 

Use this code judiciously.

## Support Us
To show your support for this project you can [thank me](https://saythanks.io/to/akhilesh.chandorkar%40gmail.com) or [buy me a coffee](https://ko-fi.com/xarcrax)
