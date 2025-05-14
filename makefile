html:
	pelican content -o output -s pelicanconf.py

serve:
	cd output && python3 -m http.server 8000