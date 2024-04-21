get-requirements: 
	poetry export --without-hashes --without-urls | awk '{ print $1 }' FS=';' > requirements.txt 
build-base:
	docker build --platform linux/amd64 --tag kohonen-base:latest -f kohonen/docker/base.Dockerfile .
build-test: build-base
	docker build --platform linux/amd64 --tag kohonen-test:latest -f kohonen/docker/test.Dockerfile .