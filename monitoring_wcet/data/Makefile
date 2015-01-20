all: wcet-sim.pdf sequential-wcet.pdf mon-none.pdf

wcet-sim.pdf: wcet-sim.py wcet-sim.csv
	./wcet-sim.py
sequential-wcet.pdf: sequential-wcet.py sequential-wcet.csv
	./sequential-wcet.py
mon-none.pdf: mon-none.py mon-none.csv
	./mon-none.py

clean:
	rm *.pdf *.pyc
