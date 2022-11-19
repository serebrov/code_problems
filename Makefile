# make init_hr P=example_name
init_hr:
	mkdir hackerrank_$(P)
	touch hackerrank_$(P)/solution.py
	mkdir hackerrank_$(P)/input
	mkdir hackerrank_$(P)/output

# make run_hr P=example_name
run_hr:
	cd hackerrank_$(P) && python3 ../hrtool.py
