build:
	docker build --target=final -t kyokley/color_blame .

build-dev:
	docker build --target=dev -t kyokley/color_blame .

tests: build-dev
	docker run --rm -t -v $$(pwd):/app kyokley/color_blame pytest
