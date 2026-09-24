class Command():
    
    def __init__(self):
        self._section = None;
        self._step = None;
        self._inputs = [];
        self._workflow = [];
    
    @property
    def section(self)->str|None:
        return self._section;
    
    @property
    def step(self)->str|None:
        return self._step;
    
    @property
    def inputs(self)->list:
        return self._inputs;
    
    @property
    def workflow(self)->str|None:
        return self._workflow;
    
    @section.setter
    def section(self, new_section:str):
        self._section = new_section;
    
    @step.setter
    def step(self, new_step:str):
        self._step = new_step;
    
    @inputs.setter
    def inputs(self, new_inputs:str):
        self._inputs.append(new_inputs);
    
    @workflow.setter
    def workflow(self, new_workflow:str):
        self._workflow.append(new_workflow);