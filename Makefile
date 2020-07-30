build:
	docker build --target=final -t kyokley/color_blame .

build-dev:
	docker build --target=dev -t kyokley/color_blame .

publish: build
	docker push kyokley/color_blame

tests: build-dev
	docker run --rm -t kyokley/color_blame pytest
