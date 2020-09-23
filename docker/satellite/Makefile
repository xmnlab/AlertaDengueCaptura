# note: --env-file requires docker-compose>=1.25
#       ref: https://github.com/docker/compose/pull/6535

include $(ENVFILE)
export

compose_cmd = docker-compose -f docker/satellite/downloader-compose.yml --env-file docker/satellite/.env


build_satellite_app:
	$(compose_cmd) build

deploy_satellite_app: build_satellite_app
	$(compose_cmd) up

stop_satellite_app:
	$(compose_cmd) stop

install_alertadenguecaptura:
	pip install -e .['develop']

configure_ci_satellite_app:
	bash .github/scripts/update_credentials_environ.sh
	python satellite_app/ci/config.py

# TESTS

flake8_satellite_app:
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

test_satellite_app:
	pytest satellite_app/ -vv

clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
