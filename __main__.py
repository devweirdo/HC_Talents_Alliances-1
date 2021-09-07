from predefine import *

class AlliancesView:
    def __init__(self, tank_num: int, mage_num: int, arch_num: int) -> None:
        self.tank_num = tank_num
        self.mage_num = mage_num
        self.arch_num = arch_num
        self.max_total = tank_num + mage_num + arch_num

    def get_possible_alliances(self) -> list:
        alli_list = []
        for i in range(self.tank_num + 1):
            for j in range(self.mage_num + 1):
                for k in range(self.arch_num + 1):
                    comb = [i, j, k]
                    if sum(comb) <= self.max_total and sum(comb) >= 2:
                        alli_list.append(tuple(comb))
        return alli_list

    def get_alliances_combination(self):
        
        pass

def main():
    test = AlliancesView(1, 2, 3)
    print(test.get_possible_alliances())

if __name__ == '__main__':
    main()