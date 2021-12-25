build:
	docker build -t kyokley/color_blame --target=base .

build-dev:
	docker build -t kyokley/color_blame --target=dev .

shell:
	docker run --rm -it -v $$(pwd):/app kyokley/color_blame /bin/sh
