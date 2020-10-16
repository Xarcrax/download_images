from download_images import download_images

download_images.main(["-q", "Elon Musk", "-l", "10", "-ar", "t", "-it", "face", "-ur", "CC", "-c", "c:/bin/chromedriver.exe"])

params = ["-q", "Butterfly", "-co", "black", "-it", "photo", "-ft", "png", "-c", "c:/bin/chromedriver.exe"]
download_images.main(params)
