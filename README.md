# AUTOZOOM2

## AUTOZOOM2 とは

AUTOZOOM2 は，クリックするだけでその曜日のその時間に入らなければならない ZOOM ミーティングへと繋いでくれるアプリです．

特に，オンライン授業を受ける大学生の強い味方になるかと思います．

## 必要環境

- Mac,Linux 環境(Linux は Ubuntu のみ動作確認済み)
- **Python3 が使える**
- **tkinter がインストールしてある**(python のライブラリなので，python3 が入っている人はとりあえず無視してください．なければインストーラーが怒る仕様になっています．)
- bash が使える(Mac,Ubuntu の方は気にしなくて大丈夫です．)

## インストール方法

autozoom2 を任意の場所に落としてきて，installer をダブルクリックします．
(実行できなければ，autozoom2 ディレクトリにて`bash installer`とします．)

> home/autozoom2 にインストールされるので，別の自前ディレクトリを autozoom2 という名でそこに配置している場合は削除されますので注意してください

```
Welcome "自分の名前"
successfully installed
```

と表示されれば OK です．

Mac ならデスクトップに実行ファイルが，Ubutntu ならアプリケーション内に AUTOZOOM2 が配置されていると思います．(Linux の場合は autozoom2 コマンドも登録されています．)

### インストール時に想定されるエラーと対処法

Mac だと，「開発元が不明なため開けません」というエラーが出る可能性があります.
この場合は，システム環境設定から許可を出してください．

参考:

- https://support.apple.com/ja-jp/guide/mac-help/mh40616/mac
- https://support.apple.com/ja-jp/guide/mac-help/mh40596/12.0/mac/12.0

Mac にて，Operation not premitted と表示された場合は，Mac が Terminal へディスクフルアクセス権限を付与していないのが原因なので，

1. システム環境設定を開く
1. セキュリティとプライバシーを開く
1. プライバシー欄からフルディスクアクセスをターミナルに許可する．

としてください．

## 使い方

autozoom2 を起動すると，

- Add URL
- Join The Meeting
- Delete URL

と表示されると思います．
書いてある通り，Add URL 　で ミーティング を登録，
Delete URL で登録されたミーティング を削除，Join The Meeting でミーティングに参加できます．

> Linux では，ターミナルにて`autozoom2`と入力することでも起動できます．

### Mac 用アイコンについて

デスクトップの autozoom2 はあまりにも無骨なので，

1. 右クリックして情報を見るを選択
2. autozoom2/icon/icon.icns を左上の方にドラッグ&ドロップするとアイコンが変えられます．

参考:

https://support.apple.com/ja-jp/guide/mac-help/mchlp2313/mac

### ターミナルについて

シェルスクリプトを実行している関係で GUI とは別窓でターミナルが立ち上がると思いますが，無視してください．

## 終わりに

kakekakemiya による個人開発です．以前から自分用に作成して使っていたものを友達に見せたところ意外と好評だったので正式にリリースしようと思って作りました．(なので AUTOZOOM2 になっています．)

いいなと思った方は是非ご利用ください．

ご意見・修正依頼もお待ちしております．
