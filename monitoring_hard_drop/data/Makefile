all: $(patsubst %.py,%.pdf,$(filter-out tsg_plot.py, $(wildcard *.py)))

%.pdf: %.py %.csv
	./$<

clean:
	rm *.pdf *.pyc
