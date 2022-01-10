import argparse
from model import VoterArt

# コマンドライン引数の設定
parser = argparse.ArgumentParser()
parser.add_argument('--size', help='please model size', required=True, type=int)
parser.add_argument('--init_num', help='optional', type=int)
parser.add_argument('--r', help='optional', type=float, default=0.3)
parser.add_argument('--iter', help='optional', type=int)
parser.add_argument('--show', help='optional', type=bool, default=True)
parser.add_argument('--save', help='optional', type=bool, default=False)

# コマンドライン引数の処理
args = parser.parse_args()
size = args.size
init_num = args.init_num
r = args.r
iter = args.iter
show = args.show
save = args.save

# クラスのインスタンス化と実行
VA = VoterArt(size, init_num, r)
VA.run(iter, show, save)