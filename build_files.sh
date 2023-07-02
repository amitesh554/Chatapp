echo " BUILD START"
python3.11 -m pip install -r requirement.txt
python3.11 manage.py collectstatic --noinput --clear
echo " BUILD END"