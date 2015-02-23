all: sw_drop_wcet.pdf umc_sweep.pdf dift_sweep.pdf flex_umc_sweep.pdf flex_dift_sweep.pdf

sw_drop_wcet.pdf: sw_drop_wcet.py sw_drop_wcet.csv
	./sw_drop_wcet.py
umc_sweep.pdf: umc_sweep.py umc_sweep.csv
	./umc_sweep.py
dift_sweep.pdf: dift_sweep.py dift_sweep.csv
	./dift_sweep.py
flex_umc_sweep.pdf: flex_umc_sweep.py flex_umc_sweep.csv
	./flex_umc_sweep.py
flex_dift_sweep.pdf: flex_dift_sweep.py flex_dift_sweep.csv
	./flex_dift_sweep.py

clean:
	rm *.pdf *.pyc
