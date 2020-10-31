import argparse
import sys
import os


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--board_grid', type=int, help='矩形区域边长像素数')
    parser.add_argument('--unit_grid', type=int, help='矩形组件分辨率')
    parser.add_argument('--unit_n', type=int, help='组件数')
    parser.add_argument('--positions', nargs='+', type=int, help='位置编号')
    parser.add_argument('--outdir', type=str, help='输出结果的目录')
    parser.add_argument('--file_name', type=str, help='输出文件名')
    args = parser.parse_args()
    b_n = (args.board_grid / args.unit_grid)**2
    isExists = os.path.exists(args.outdir)

    if (args.board_grid % args.unit_grid != 0):
        sys.exit(1)

    if (len(args.positions) < 1 or len(args.positions) > b_n):
        sys.exit(1)

    if (len(args.positions) != args.unit_n):
        sys.exit(1)

    if not isExists:
        os.makedirs(args.outdir)
        path = args.outdir + '/'
        file = open(path + args.file_name + '.mat', 'w')
        file = open(path + args.file_name + '.jpg', 'w')
        file.close()


if __name__ == "__main__":
    main()
