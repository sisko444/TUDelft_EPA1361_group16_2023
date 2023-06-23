# Structure
The work of group 16 has the following structure:

- The running of the model that resulted in used images and some if the analysis and interpretation is displayed in the "Group16_notebook_scenario_discovery.ipynb" and "Group16_notebook_MORDM.ipynb" notebook files in the root folder. The results of the scenario discovery are used in the MORDM notebook.
- Additions or changes to the model as delivered for this course are expressed below with reasoning in the changelog.
- For aesthetic reasons a lot of ugly code was put into the vis.py file as functions. These functions are only used in the notebooks.
- Some general conventions that were used in the notebook sare explained below
- Additionally to providing the virtual environment this code was ran in originally we also provide a requirements.txt to construct a virtual environment from in the root folder. This was generated in the end of the MORDM notebook.

### General conventions notebooks
In the notebooks the running of experiments is always done with an experiment name, and saving the results as a .pickle file in the archive/pickle_files folder.
When running a notebook cell with an experiment in it, it will check if an experiment with that experiment name was ran before. If so, it will load the results instead of generating and saving results.
This has a second purpose besides not needing to run experiments twice. The visualizations of the results load the dataset each time a visualization is done. This means only the results from one experiment is loaded into memory at a time, and a mixup of the variables is less likely to occur. If you want to check if experiments run you can change the name of the corresponding pickle file in archives/pickle_files directory before running the cell the experiment is in. All of the images that were eligible for use at any point during the course are still reproducible in the notebook. So there are some images that are not thoroughly analysed as that is not neccesary.


### Changelog
- The model was altered such that the dike_model_function.py DikeNetwork constructor takes a num_planning_steps parameter that is set to three by default. This allowed for setting the time steps to 1, which was neccesary because of computing constraints. The added complexity of three time steps made it impossible to execute the simulations on our laptops.
- The model files and data were put into a sub directory "model" and all changes to accomodate that change were made. This includes altering paths and dependencies.
- For clarity purposes we opted to do problem definition manually in the notebook, for this the sum_over and sum_over_time functions were placed in dike_model_function.py