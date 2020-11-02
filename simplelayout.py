import argparse
import sys
from pathlib import Path


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

    if (args.board_grid % args.unit_grid != 0):
        sys.exit(1)

    if (len(args.positions) < 1 or len(args.positions) > b_n):
        sys.exit(1)

    if (len(args.positions) != args.unit_n):
        sys.exit(1)

    if not Path(args.outdir).exists():
        Path(args.outdir).mkdir(parents=True, exist_ok=True)
        path1 = args.outdir + '/' + 'example'
        Path(path1 + '.mat').open('w')
        Path(path1 + '.jpg').open('w')


if __name__ == "__main__":
    main()
