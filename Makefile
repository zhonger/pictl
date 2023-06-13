.PHONY: all

all: uninstall build install
build:
	poetry build
install:
	pip3 install dist/*.whl
uninstall:
	pip3 uninstall pictl -y
clean:
	rm -rf dist