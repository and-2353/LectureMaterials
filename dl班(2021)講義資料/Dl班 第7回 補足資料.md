# Dl班 第7回 補足資料
###### tags: `DeepLearning班` `OSK`

## 7.2.2 畳み込み演算
### 畳み込み演算の流れ
入力データとフィルターの要素積(アダマール積)をとって、それを足し合わせる。その後、活性化関数を通す。

### フィルターと入力データの具体例
たとえば、フィルターが
$$
\begin{pmatrix}
0 & 0 & 1 \\
0 & 0 & 1 \\
0 & 0 & 1
\end{pmatrix}
$$

だとする。このフィルターは画像の中で、右のほうにバリューが大きい部分があると強く反応する。
入力データのウインドウが

$$
\frac{1}{255}
\begin{pmatrix}
5 & 5 & 255 \\
5 & 5 & 255 \\
5 & 5 & 255
\end{pmatrix}
$$

> 数値計算のため、データを読み込むときにデータの画素値を1/255にする処理はよく行われる(と思う)。
> 
> なので本当は入力データは0～1のバリューになってから入力されるのですが、それだと見づらいのでこのような表記にする

だとすると、フィルター適用後の計算結果は $3$ になる。これにより、「右のほうにバリューが大きい地域である」という情報が伝わる。
> まず、3×3で表されている情報が1つの数値になってる時点ですごいと思う。
 
逆に、入力データのウインドウが
$$
\frac{1}{255}
\begin{pmatrix}
255 & 255 & 5 \\
255 & 255 & 5 \\
255 & 255 & 5
\end{pmatrix}
$$

だと、フィルター適用後の計算結果は $0.058...$ になる。これにより「右のほうにバリューが大きい地域ではない」という情報が伝わる。(これも貴重な情報なはず。)

> まあまあフィルターと入力データが似ていれば、まあまあな値が出力される。(当たり前だけど)

### コサイン類似度との類似点

このように、行列と行列の近さを一つの値として出力する点で、畳み込み演算はコサイン類似度に似ている(と思う)。

計算結果はフィルターとの類似度みたいなものを表している。なお、計算結果はその後活性化関数に突っ込まれる。活性化関数がtanhだとすると、値は-1から1をとるので、コサイン類似度みたいに行列の近さを-1から1で表したものと解釈できるかもしれない。

![](https://i.imgur.com/D8XXYB8.png)


### 畳み込みにおけるReLUが果たす機能の考察
でも、魚本ではReLUが使われてる。理由はたぶんReLUの性能がいいからだと思う。(そもそも、類似度を表すために-1から1じゃないといけない道理はない)

ReLUは1以上の値をとるので、コサイン類似度みたいに解釈することはできない。
![](https://i.imgur.com/K7RnIwG.png)

sigmoid(やtanh)は全部0～1(-1～1)の間に丸め込まれるから、「4」(結構似てる)と「100」（めちゃめちゃ似てる）がほとんど同じになってしまう欠点がありそう

![](https://i.imgur.com/JDaG3ZT.png)

ReLUはその点をクリアする。値域に上限がないので、「4」(結構似てる)と「100」（めちゃめちゃ似てる）が明確に区別される。これによって、「めちゃめちゃ反応する場所がどこにあるか」みたいな情報を伝えるのには適しているかもしれない。逆に、0以下が全部0になるから、「-100」(全然似てない)と「-1」(あんまり似てない)が同じになってしまう欠点がありそう

ReLUはあまり反応しない部分は全部0になるが、フィルターはいっぱいあるから、ほかのフィルターから出力されるfeature mapでその地域がどんな形状・色になっているのかは伝わる気もする。

> ~~っていうか、活性化関数通す前の計算結果が0未満になることってあるの？~~ → **なるらしい 畳み込み層も重みと同様更新対象で、負の数になるので要素積の和も負になりうる**
> 
> ~~あと、フィルターって具体的にはどのくらいの値になるのが普通なんですか？ わかる人いれば教えてください。(本質的な問いは、畳み込み層に限らない重みの平均や分散)~~ → **正則化するかどうかによっても結構変わるみたい 参考：[Deep Learningをkerasで可視化したい](https://recruit.gmo.jp/engineer/jisedai/blog/deep-learning-keras/)**

### 畳み込み演算でやろうとしていること・お気持ち

同じフィルターをスライドさせて1枚の画像を全部通るので、画像の中のどこに反応する地域があるかという情報がくみ取られる。
これによって、明るい部分・暗い部分がどこに位置しているのかなどの情報はもちろん、縦線がどこにあるかとか輪郭/エッジがどこにあるか(エッジは、画素値が急激に変化する部分)などの情報が抽出される。

なお、7.2.6 とかをよく読んだらわかるけど、フィルターは複数ある。
> 1つのフィルターで1枚の画像を通るのは変わらない(正確には1つのフィルターで画像内の1つのチャンネルを全部通る)。
> 1つのフィルターから出力されるfeature mapは1枚になる。

たとえば、フィルターが
$$
\begin{pmatrix}
0 & 0 & 0 \\
1 & 1 & 1 \\
0 & 0 & 0
\end{pmatrix}
$$

であるなら、横棒に反応すると思われる。
:::info
正確に言うと、横棒以外にも反応する。たとえば、フィルターが
$$
\begin{pmatrix}
0 & 0 & 0 \\
1 & 1 & 1 \\
0 & 0 & 0
\end{pmatrix}
$$
なら、入力データが
$$
\frac{1}{255}
\begin{pmatrix}
0 & 0 & 0 \\
255 & 255 & 255 \\
0 & 0 & 0
\end{pmatrix}
$$
でも、
$$
\frac{1}{255}
\begin{pmatrix}
255 & 255 & 255 \\
255 & 255 & 255 \\
255 & 255 & 255
\end{pmatrix}
$$
でも、フィルターとの計算結果は一緒になる。その意味で横棒以外にも反応するけど、別のフィルター
$$
\begin{pmatrix}
1 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & 1
\end{pmatrix}
$$
みたいなものが仮にあれば、計算結果は明確に異なるものになるので、2つの入力データの違いは次の層に伝えられるはず。
:::



画像全体を通したときに出力されるfeature mapは、「画像の中で横棒がどこにあるか」を反映したものかもしれない。

このように、フィルターを通った後のfeature mapは「あるフィルターから見たもとの画像」で、反応する地域がどこにあるかを表したもの。まさにfeature mapって感じがする。

ちなみに人の脳にも縦棒に反応するニューロンや横棒に反応するニューロンがあるらしいので、それとも似ているのかも。

## 7.6.2 階層構造による情報抽出
これは僕の推測です。

1層目の畳み込み層では「縦棒に反応するfeature map」が作られて、2層目の畳み込み層ではそれをもとに、「縦棒が集まってるということは毛皮っぽいな」みたいなことが推測される。そして、毛皮っぽさのfeatume map(毛皮っぽい部分はどこにあるか)が作成される。
さらに、3層目の畳み込み層では、毛皮っぽい部分が四角く集まっていたらそれはタオルっぽいし、ネコ型に集まっていたら猫っぽい。みたいな感じで、エッジ→テクスチャ→物体のパーツ みたいな情報の変化が起こるのかなと思った。
人間もこのような認識を行っているのかな？どう思いますか？

## その他CNN関係の資料

- [CNNは本当にテクスチャ好きなのか？](http://ai-scholar.tech/image-recognition/texture)

- [Convolutionの可視化集](https://github.com/vdumoulin/conv_arithmetic#transposed-convolution-animations)

![](https://github.com/vdumoulin/conv_arithmetic/blob/master/gif/same_padding_no_strides.gif?raw=true)

- [【深層学習】畳み込み層の本当の意味、あなたは説明できますか？【ディープラーニングの世界 vol. 5 】](https://youtu.be/vU-JfZNBdYU)

    <iframe width="560" height="315" src="https://www.youtube.com/embed/vU-JfZNBdYU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    
    



