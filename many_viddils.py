import viddil
import pr_v3_defs

class Many_viddils:
    def __init__(self, viddils=[]):
        self.viddils = viddils

    def add_item(self, vid):
        if pr_v3_defs.check_viddil(vid) == True:
            self.viddils.append(vid)
        return

    def __str__(self):
        s=''
        for item in self.viddils:
            s+= f'\n{item.__str__()}'
        return s

    def delete_elem(self, index):
        if index < len(self.viddils) and index > -1:
            self.viddils.pop(index)
        else: print("does not exist such index")

    def edit_viddil(self, old_data, new_data):
        ind = self.find_in_collection(old_data, 2)
        if ind != -1:
            for pole in self.viddils[ind].__dir__():
                if pole.startswith('__') == False and pole.startswith('set') == False and pole.startswith(
                        'get') == False:
                    try:
                        if str(old_data) in self.viddils[ind].__getattribute__(pole):
                            self.viddils[ind].__setattr__(pole, new_data)
                    except:
                        print("зловилась помилка")

    def find_in_collection(self, smth, chys):
        index = i = - 1
        for v in self.viddils:
            i += 1
            for pole in v.__dir__():
                if pole.startswith('__') == False and pole.startswith('set') == False and pole.startswith(
                        'get') == False:
                    try:
                        if chys == 1:
                            if str(smth) in v.__getattribute__(pole):
                                print(v)
                                index = i
                        else:
                            if v.__getattribute__(pole) == str(smth):
                                index = i
                    except:
                        print("Зловилась помилка")
        return index

    def sort_in_collection(self, atr):
        try:
            print(sorted(self.viddils, key=lambda x: x.__getattribute__(atr)))
        except:
            print("does not exist atribute")

    def write_in_file(self, str):
        file_ = open(str, 'a')
        for viddil in self.viddils:
            print(viddil, file=file_)
        file_.close()

    def read_from_file(self, str):
        try:
            with open(str, 'r') as f:
                for line in f:
                    temp = viddil.Viddil()
                    l = line.split()
                    temp.set_with_list(l)
                    self.add_item(temp)
            f.close()
        except IOError:
            print("this file does not exist")
            return