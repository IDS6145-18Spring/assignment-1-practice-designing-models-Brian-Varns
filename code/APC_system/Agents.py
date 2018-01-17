class agents:
    ''' A general agent class '''

    def __init__(self, cm, cd, nc, nd, sd, pollute):
        '''initializes the agent'''
        self.carbon_monoxide = cm
        self.carbon_monoxide.frequency = 25
        self.carbon_dioxide = cd
        self.carbon_dioxide.frequency = 25
        self.nitric_oxide = nc
        self.nitric_oxide.frequency = 20
        self.nitrogen_dioxide = nd
        self.nitrogen_dioxide.freqency = 15
        self.sulfur_dioxide = sd
        self.nitrogen_dioxide.freqency = 15
        self.pollute_content = pollute
        agents.__init__(self, cm, cd, nc, nd, sd, pollute)

    def normal_pollution():
         pollute_content -= 15
         return 15.0

    def medium_pollution():
         pollute_content -= 25
         return 25.0

    def heavy_pollution():
         pollute_content -= 35
         return 35.0