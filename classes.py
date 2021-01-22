class RevenueCenter():
    def __init__(self, dataframe):
        self.dataframe = dataframe


    def print_stats(self):
        print(self.dataframe[['Charges', 'Cases w/Chgs', 'Billed', 'Cases Billed', 'Payments',
                    'Cases Paid', 'Balance', 'Cases']].sum())


    def visits_by_facility(self):
        print(self.dataframe['Facility'].value_counts())


    def visits_by_asu(self):
        print(self.dataframe['ASU SERVICE'].value_counts())

