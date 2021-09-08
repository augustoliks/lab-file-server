venv:
	virtualenv venv
	./venv/bin/pip3 install -r requirements.txt

pull:
	./venv/bin/docker-compose --project-name=web-server-files pull

up:
	./venv/bin/docker-compose --project-name=web-server-files up -d

down:
	./venv/bin/docker-compose --project-name=web-server-files down

ps:
	./venv/bin/docker-compose --project-name=web-server-files ps
