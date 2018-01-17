class sensors:
    '''a general class for sensors'''

    def __init__(self, n, s, wt, wr, cms, cds, nos, nd, sd):
        '''Intializes the Sensor'''
        self.name = n
        self.sensor = s
        self.wireless_tranceiver = wt
        self.wireless_reciever = wr
        self.carbon_monoxide_sensor = cms
        self.carbon_dioxide_sensor = cds
        self.nitric_oxide_sensor = nos
        self.nitrogen_dioxide_sensor = nd
        self.sulfure_dioxide_sensor = sd
        self.height = 10.0
        self.width = 1.0
        sensors.__init__(self, n, s, wt, wr, cms, cds, nos, nd, sd)



