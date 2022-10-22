import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

trucks = pd.read_csv('C:/test.py/pyplot/BDS/examples/pickup.csv')

#ヒストグラム

plt.hist(trucks["price"], bins=5)
plt.xlabel("price", fontsize=10)           #x軸ラベル
plt.ylabel("frequency", fontsize=10)      #y軸ラベル
plt.savefig('histogram.png')

#データ加工
Dodge_df = trucks[trucks["make"] == "Dodge"]    #Dodge,Ford,GMCについてpriceをリストに格納
Dodge_list = list(Dodge_df["price"])            #もっと上手な加工法はありそう

Ford_df = trucks[trucks["make"] == "Ford"]
Ford_list = list(Ford_df["price"])

GMC_df = trucks[trucks["make"] == "GMC"]
GMC_list = list(GMC_df["price"])

#箱ひげ図
points = (Dodge_list, Ford_list, GMC_list)

fig, ax = plt.subplots()

bp = ax.boxplot(points,
           vert=True,  # 横向きにする
           patch_artist=True,  # 細かい設定をできるようにする
           widths=0.8,  # boxの幅の設定
           boxprops=dict(facecolor='lightgray',  # boxの塗りつぶし色の設定
                         color='black', linewidth=1),  # boxの枠線の設定
           medianprops=dict(color='black', linewidth=4),  # 中央値の線の設定
           whiskerprops=dict(color='black', linewidth=1, linestyle="--"),  # ヒゲの線の設定
           capprops=dict(color='black', linewidth=1),  # ヒゲの先端の線の設定
           flierprops=dict(markeredgecolor='black', markeredgewidth=1),# 外れ値の設定
           sym=""  # 外れ値を表示しない
           )
ax.set_xticklabels(['Dodge', 'Ford', 'GMC'])

plt.xlabel('make')
plt.ylabel('price')
plt.savefig('boxplot.png')

#散布図
trucks.plot.scatter(x='year', y='price')

plt.scatter(Dodge_df['year'],Dodge_df['price'],color='k',label="Dodge")
plt.scatter(Ford_df['year'],Ford_df['price'],color='r',label="Ford")
plt.scatter(GMC_df['year'],GMC_df['price'],color='g',label='GMC')
plt.legend()
plt.savefig('scatterplot.png')

#pointplot

browser = pd.read_csv('C:/test.py/pyplot/BDS/examples/web-browsers.csv')
plt.figure()

sns.pointplot(data=browser, x='race', y='spend', hue='broadband', errorbar='ci=99', join=False, capsize=.4)
plt.ylim(-500, 8500)

plt.savefig('bootstrapping.png')