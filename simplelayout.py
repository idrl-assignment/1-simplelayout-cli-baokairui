import argparse
import sys
import os


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-bg', '--board_grid', metavar='', type=int, help='矩形区域的边长像素数')
    parser.add_argument('-ug', '--unit_grid', metavar='', type=int, help='矩形组件分辨率')
    parser.add_argument('-un', '--unit_n', metavar='', type=int, help='组件数')
    parser.add_argument('-p', '--positions', metavar='', type=int, help='每个组件的位置编号')
    parser.add_argument('-o', '--outdir', metavar='', type=str, help='输出结果的目录')
    parser.add_argument('-fn', '--file_name', metavar='', type=str, help='输出文件名')
    args = parser.parse_args()
    b_n = (args.board_grid/args.unit_grid)**2
    isExists = os.path.exists(args.outdir)

    if (args.board_grid//args.unit_grid == 0):
        sys.exit(0)

    if (args.positions < 1 & args.positions >= b_n):
        sys.exit(0)

    if not isExists:
        os.makedirs(args.outdir)
        path = args.outdir + '/'
        file = open(path + 'example' + '.mat', 'w')
        file = open(path + 'example' + '.jpg', 'w')
        file.close()


if __name__ == "__main__":
    main()
