import time
import subprocess


def download(command):
    try:
        # Downloading the file
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as err:
        # In case of download error
        print('ERROR:', err)


if __name__ == '__main__':
    start = time.perf_counter()
    size = 1000
    # Files to download
    urls = [
        'https://edutechlearners.com/download/Introduction_to_algorithms-3rd%20Edition.pdf',
        'https://www.appliedstemcell.com/pub/media/wysiwyg/dockerbook.pdf',
        'https://mirbozorgi.ir/books/Docker-in-Action.pdf'
    ]

    for i in range(size):
        # Accesing each element in urls
        for j in range(len(urls)):
            # Getting the command in order to run it
            command = ['curl', urls[j], '-o', 'output' + str(i) + '_' + str(j)]
            download(command)

        time.sleep(10)

    # Execution time
    finish = time.perf_counter()
    print(f'\nFinished in {round(finish - start, 2)} second(s)')
