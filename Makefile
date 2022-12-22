
lint:
	pylint *.py

sample:
	pandoc --filter=pandoc_jinja.py --metadata-file=weather.yml sample.md

docker_bash:
	docker run -it -v `pwd`:/pandoc --entrypoint=bash dalibo/pandocker:latest
