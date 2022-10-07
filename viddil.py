import pr_v3_defs
from math import log10

class Viddil:
    def __init__(self, id_=0, tit=0, dir_='', ph='', mo=0, ye=0, we=''):
        self.ID = id_
        self.title = tit
        self.director_name = dir_
        self.phone_number = ph
        self.monthly_budget = mo
        self.yearly_budget = ye
        self.website_url = we

    def set_with_list(self, l):
        self.ID, self.title, self.director_name, self.phone_number, self.monthly_budget, self.yearly_budget, self.website_url = l

    @property
    def get_iD(self):return self.ID
    @property
    def get_title(self):return self.title
    @property
    def get_director_name(self):return self.director_name
    @property
    def get_phone_number(self):return self.phone_number
    @property
    def get_mont_budget(self):return self.monthly_budget
    @property
    def get_yea_budget(self):return self.yearly_budget
    @property
    def get_website(self):return self.website_url

    def __str__(self):
        f = []
        for pole in self.__dir__():
            if pole.startswith('__') == False and pole.startswith('set') == False and pole.startswith('get') == False:
                f.append(self.__getattribute__(pole))
        return f'{f}'

    def __repr__(self):
        return '\n'+self.__str__()


    def set_with_keyboard(self):
        self.ID = pr_v3_defs.input_number_lenght("ID (lenght=6): ", 6)
        self.title = pr_v3_defs.input_word("title: ")
        self.director_name = pr_v3_defs.input_word("name: ")
        self.phone_number = pr_v3_defs.input_number_lenght("phone number (lenght=12) 380... : ", 12)
        self.monthly_budget = pr_v3_defs.input_number("monthly budget: ")
        self.yearly_budget = pr_v3_defs.input_number("yearly budget: ")
        self.website_url = pr_v3_defs.input_with_smth("url-site with .com: ", '.com')
        return

    def he(self):
        print("hello")

    # def check_viddil(self):
    #     result = True
        # if not str(self.ID).isdigit(): result = False
        # if not str(self.title).isalpha(): result = False
        # if not str(self.director_name).isalpha(): result = False
        # size_phone = int(log10(int(self.phone_number))) + 1
        # if not str(self.phone_number).isdigit() or size_phone != 12: result = False
        # if not str(self.monthly_budget).isdigit(): result = False
        # if not str(self.yearly_budget).isdigit(): result = False

        #return result









