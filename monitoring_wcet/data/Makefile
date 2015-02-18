all: wcet-sim.pdf wcet-sequential.pdf mon-none.pdf

wcet-sim.pdf: wcet-sim.py wcet-sim.csv
	./wcet-sim.py
wcet-sequential.pdf: wcet-sequential.py sequential-wcet.csv
	./wcet-sequential.py
mon-none.pdf: mon-none.py mon-none.csv
	./mon-none.py

clean:
	rm *.pdf *.pyc
