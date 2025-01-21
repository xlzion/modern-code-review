def is_win(game):
    """检查当前棋盘是否存在胜利条件"""
    # 检查行、列和对角线
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] and game[i][0] in ('X', 'O'):  # 检查行
            return True
        if game[0][i] == game[1][i] == game[2][i] and game[0][i] in ('X', 'O'):  # 检查列
            return True
    # 检查对角线
    if game[0][0] == game[1][1] == game[2][2] and game[0][0] in ('X', 'O'):
        return True
    if game[0][2] == game[1][1] == game[2][0] and game[0][2] in ('X', 'O'):
        return True
    return False


def print_board(game):
    """打印当前棋盘"""
    print("\n当前棋盘状态:")
    for row in game:
        print(" | ".join(row))
        print("-" * 9)


def main():
    # 初始化棋盘和玩家信息
    game = [[' ' for _ in range(3)] for _ in range(3)]  # 3x3 棋盘
    players = ['X', 'O']  # 玩家标志
    turn = 0  # 当前回合的玩家索引（0为玩家1，1为玩家2）

    print("欢迎来到井字棋游戏！")
    print("玩家1: X\n玩家2: O\n")

    for n in range(9):
        print_board(game)  # 打印棋盘
        print(f"轮到玩家{turn + 1} ({players[turn]}) 下棋。")
        
        # 输入并验证
        while True:
            try:
                i, j = map(int, input("请输入要标记的格子 (行 列) [1-3]: ").split())
                if i < 1 or i > 3 or j < 1 or j > 3:  # 检查范围
                    print("输入超出范围，请输入1到3之间的数字！")
                    continue
                if game[i-1][j-1] != ' ':  # 检查是否已经被占用
                    print("该格子已被占用，请选择其他格子！")
                    continue
                break
            except ValueError:
                print("输入无效，请输入两个数字，用空格分隔 (如: 1 2)。")

        # 更新棋盘
        game[i-1][j-1] = players[turn]

        # 检查胜利条件
        if is_win(game):
            print_board(game)
            print(f"恭喜玩家{turn + 1} ({players[turn]}) 获胜！")
            break

        # 检查平局
        if n == 8:
            print_board(game)
            print("平局！")
            break

        # 切换到下一个玩家
        turn = 1 - turn


if __name__ == "__main__":
    main()
    
