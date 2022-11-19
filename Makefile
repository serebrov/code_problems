# make init_hr P=example_name
init_hr:
	mkdir hackerrank_$(P)
	touch hackerrank_$(P)/solution.py
	mkdir hackerrank_$(P)/input
	mkdir hackerrank_$(P)/output

# make run_hr F=example_folder
run_hr:
	cd $(F) && python3 ../hrtool.py
