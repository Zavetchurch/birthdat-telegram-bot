import os
import zipfile

TEMP_DIR = "build_temp"


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), arcname=os.path.join(root.replace(path, ''), file))


if __name__ == '__main__':
    # TODO: Install Visual C++ 14
    # if not os.path.exists(TEMP_DIR):
    #     os.mkdir(TEMP_DIR)
    # os.system(f"pip install -r requirements.txt -t {TEMP_DIR}")

    zipf = zipfile.ZipFile('birthday-bot.zip', 'w', zipfile.ZIP_DEFLATED)

    zipdir('venv/Lib/site-packages', zipf)
    zipdir('src/', zipf)
    zipf.close()