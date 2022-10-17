# build_files.sh
python3.9 -m pip install --upgrade pip
pip install -r requirements.txt
python3.9 manage.py makemigrations
python3.9 manage.py migrate
python3.9 manage.py collectstatic --noinput