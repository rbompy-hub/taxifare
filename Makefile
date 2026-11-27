run-api:
		uv run uvicorn api.fast:app

docker_build_local:
		docker build \
				-t ${DOCKER_IMAGE_NAME}:dev .

docker-run :
		docker run -it -p 8080:8080 ${DOCKER_ID}
