build: clean generate-svg build-font install-font

install-font:
	rm -rf "~/Library/Fonts/Aurebesh Code.ttf"
	cp "build/Aurebesh Code.ttf" ~/Library/Fonts/

build-font:
	rm -rf build
	mkdir -p build
	python3 src/generate.py

generate-svg:
	rm -rf src/svg
	mkdir -p src/svg
	~/Applications/Sketch\ Old.app/Contents/MacOS/sketchtool export artboards "src/Aurebesh Code Source.sketch" --output="src/svg"

clean:
	git clean -Xdff
