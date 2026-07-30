export REPO

MARKERS.md: markers.csv markers.py
	python3 markers.py report

markers.csv: markers.py
	python3 markers.py scan

.PHONY: clean
clean:
	rm -f markers.csv MARKERS.md
