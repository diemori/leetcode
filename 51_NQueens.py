class Solution:
    def __init__(self):
        self.move_stack = list()
        self.table = list()
        self.answer_list = list()
        self.cnt = 0
        self.len_table = 0
        self.tried = list()

    def gen_table(self, n):
        self.len_table = n
        for x in range(n):
            row = [0 for y in range(n)]
            self.table.append(row)

    def print_table(self):
        for row in self.table:
            print(row)

        print("-" * 30)

    def set_queen(self, x, y):
        if self.table[y][x] != 0:
            # print("Already Possessed in %d, %d (%d)" % (x, y, self.table[x][y]))
            return False

        self.cnt += 1

        self.table[y][x] = -1

        self.side_effect(x, y, 1)

    def rem_queen(self, x, y):
        if self.table[y][x] != -1:
            # print("There is no Queen in %d, %d (%d)" % (x, y, self.table[x][y]))
            return False

        self.cnt -= 1

        self.side_effect(x, y, -1)

        self.table[y][x] = 0

    def side_effect(self, x, y, _val):
        for yp, row in enumerate(self.table):
            if self.table[yp][x] == -1:
                continue
            self.table[yp][x] += _val

        for xp, val in enumerate(self.table[y]):
            if self.table[y][xp] == -1:
                continue
            self.table[y][xp] = val + _val

        seed = max(x, y) - min(x, y)

        if x > y:
            seed = -seed

        table_len = len(self.table)

        for i in range(table_len):
            ip = i + seed
            if ip not in range(table_len):
                continue

            if self.table[ip][i] == -1:
                continue

            self.table[ip][i] += _val

        rx = table_len - x
        seed = max(rx, y) - min(rx, y)

        if rx > y:
            seed = -seed

        for i in range(table_len):
            ri = table_len - i
            rip = ri + seed

            if rip not in range(table_len):
                continue

            if self.table[rip][i] == -1:
                continue

            self.table[rip][i] += _val

        return True

    def search_table(self, _except=None):
        empty_list = list()

        for y, row in enumerate(self.table):
            for x, item in enumerate(row):
                if item != 0:
                    continue

                empty_list.append((x, y))

        return empty_list

    def solve(self):
        empty_list = self.search_table()

        el = sorted(empty_list)

        if el in self.tried:
            return False

        self.tried.append(el)

        for pos in el:
            self.set_queen(*pos)

            if self.cnt == self.len_table:
                table = self.change_table(self.table)
                if table not in self.answer_list:
                    self.answer_list.append(table)

            self.solve()

            self.rem_queen(*pos)

        return True

    def change_table(self, _table):
        result = list()

        for x in range(self.len_table):
            result.append("")
            for y in range(self.len_table):
                if _table[y][x] == -1:
                    result[x] += 'Q'
                else:
                    result[x] += '.'

        return result

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.gen_table(n)
        self.cnt = 0

        self.solve()
        return self.answer_list


s = Solution()

r = s.solveNQueens(5)

print(r)
print("\n")

for pos, ans in enumerate(r):
    print(pos+1, ans)

    print("-" * 30)
