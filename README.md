# Voter Model
![voter_model drawio](https://user-images.githubusercontent.com/52354163/148811506-0f7352c1-f587-4e90-8217-1c5c4869c8ef.png)

以上のようなネットワークを考える。

これは、Voter Model（投票者モデル）と呼ばれ、例えば賛成/反対のどちらの票を投票する人かを白塗り/黒塗りのノードで表す。ここで、賛成ノードは1、反対ノードは0であるとする。

また、周辺のノードによってノードの値は変わる。(自身を含む周辺のノードの値の総和)/(自身を含む周辺のノードの数)の確率でノードの値は1に変わる。

# Voter Art
以上のようなVoter Modelを参考にして、size×sizeのセルがどのように変化していくかを見てみたいと考え作成した。

![voter_model-Page-2 drawio](https://user-images.githubusercontent.com/52354163/148814072-62af6fed-ac72-4e27-9302-a142bb343376.png)

# 必要な追加ライブラリ
```
pip intsall numpy
pip install natsort
```

# 実行例
```
python main.py --size 100 --iter 100 --show False --save True
```

# 結果例
![animation](https://user-images.githubusercontent.com/52354163/148814456-fba2c488-761b-4cc3-8134-7385b54a952f.gif)
