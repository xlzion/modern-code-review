class TicTacToe:
    def __init__(self):
        """初始化游戏"""
        self.game = [[' ' for _ in range(3)] for _ in range(3)]  # 棋盘
        self.players = ['X', 'O']  # 玩家标志
        self.turn = 0  # 当前回合玩家索引
        self.history = []  # 记录历史操作（用于悔棋）

    def print_board(self):
        """打印当前棋盘"""
        print("\n当前棋盘状态:")
        print("  1   2   3")  # 显示列号
        for i, row in enumerate(self.game):
            print(i + 1, " | ".join(row))  # 显示行号
            if i < 2:
                print("  " + "-" * 9)

    def is_win(self):
        """检查胜利条件"""
        g = self.game
        for i in range(3):
            # 检查行
            if g[i][0] == g[i][1] == g[i][2] and g[i][0] in ('X', 'O'):
                return True, [(i, 0), (i, 1), (i, 2)]
            # 检查列
            if g[0][i] == g[1][i] == g[2][i] and g[0][i] in ('X', 'O'):
                return True, [(0, i), (1, i), (2, i)]
        # 检查对角线
        if g[0][0] == g[1][1] == g[2][2] and g[0][0] in ('X', 'O'):
            return True, [(0, 0), (1, 1), (2, 2)]
        if g[0][2] == g[1][1] == g[2][0] and g[0][2] in ('X', 'O'):
            return True, [(0, 2), (1, 1), (2, 0)]
        return False, []

    def get_input(self):
        """获取玩家输入并验证"""
        while True:
            try:
                i, j = map(int, input("请输入要标记的格子 (行 列) [1-3]，或输入-1悔棋: ").split())
                if i == -1:  # 悔棋逻辑
                    if not self.history:
                        print("当前无法悔棋，棋盘为空！")
                        continue
                    last_move = self.history.pop()
                    self.game[last_move[0]][last_move[1]] = ' '
                    self.turn = 1 - self.turn  # 切换回上一玩家
                    print("已悔棋！")
                    self.print_board()
                    continue
                if i < 1 or i > 3 or j < 1 or j > 3:  # 检查范围
                    print("输入超出范围，请输入1到3之间的数字！")
                    continue
                if self.game[i - 1][j - 1] != ' ':  # 检查格子是否被占用
                    print("该格子已被占用，请选择其他格子！")
                    continue
                return i - 1, j - 1
            except ValueError:
                print("输入无效，请输入两个数字，用空格分隔 (如: 1 2)。")

    def play(self):
        """运行游戏逻辑"""
        print("欢迎来到井字棋游戏！")
        print("玩家1: X\n玩家2: O\n")
        for n in range(9):
            self.print_board()
            print(f"轮到玩家{self.turn + 1} ({self.players[self.turn]}) 下棋。")
            
            i, j = self.get_input()
            self.game[i][j] = self.players[self.turn]  # 更新棋盘
            self.history.append((i, j))  # 记录历史操作

            win, winning_line = self.is_win()
            if win:
                self.print_board()
                print(f"恭喜玩家{self.turn + 1} ({self.players[self.turn]}) 获胜！")
                self.highlight_winning_line(winning_line)
                break

            if n == 8:  # 平局
                self.print_board()
                print("平局！")
                break

            self.turn = 1 - self.turn  # 切换到下一个玩家

        if input("是否重新开始游戏？(y/n): ").lower() == 'y':
            self.__init__()  # 重置游戏
            self.play()

    def highlight_winning_line(self, winning_line):
        """高亮显示胜利的连线"""
        for i, j in winning_line:
            self.game[i][j] = f"*{self.game[i][j]}*"
        print("\n胜利连线高亮:")
        self.print_board()


if __name__ == "__main__":
    game = TicTacToe()
    game.play()
