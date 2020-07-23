import csv

from pathlib import Path

class DeniedPersonsCollection:
    def __init__(self):
        self.ids = []
        self.dpl = {}
        self.dpl_add = {}

    def load_lists(self):
        sdn_path = Path('./data/sdn-2020-07-08.csv')
        sdn_aka_path = Path('./data/sdn_aka-2020-07-08.csv')
        sdn_add_path = Path('./data/sdn_add-2020-07-08.csv')

        with open(sdn_path, 'r') as sdn_file:
            reader = csv.reader(sdn_file.readlines())

            for sdn in reader:
                if sdn[2] == 'individual':
                    sdn_id = sdn[0]
                    fname, lname = sdn[2].lower().split(',')

                    names_dict = {}

                    if lname in self.dpl:
                        names_dict[lname].append((fname, sdn_id))
                    else:
                        names_dict[lname] = [
                            (fname, sdn_id)
                        ]

                    self.ids.append(sdn_id)

        with open(sdn_aka_path, 'r') as sdn_aka_file:
            reader = csv.reader(sdn_aka_file.readlines())

            for aka in reader:
                aka_id = aka[0]
                fname, lname = aka[3].lower().split(',')

                names_dict = {}

                if lname in self.dpl:
                    names_dict[lname].append((fname, sdn_id))
                else:
                    names_dict[lname] = [
                        (fname, sdn_id)
                    ]


    def find_name(self, lastname: str, firstname: str):
        if lastname in self.dpl:
            tuple_list = self.dpl[lastname]

            for tup in tuple_list:
                fname, snid = tup

                if fname == firstname:
                    return True


        return False