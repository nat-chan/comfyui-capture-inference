## OBSを介してペイントソフトをキャプチャする方法

### Chrome側の設定

起動して `http://localhost:7860/` に初めてアクセスするとカメラへのアクセス権限を求められると思います。

![image](https://github.com/nat-chan/comfyui-capture-inference/assets/18454066/38ae0290-b4c8-497f-990d-30ec309b4090)



「許可する」を押した場合、大抵のPCではセンターカメラが入力ソースになるため、これをOBSの提供する仮想カメラに変更する方法を述べます。

ChromeのURL欄から`chrome://settings/content/camera`にアクセスしてください。

![image](https://github.com/nat-chan/comfyui-capture-inference/assets/18454066/6d246a65-b0cb-4eeb-901c-505f040a271c)


すると上記のような入力ソースを選ぶ欄があるため、この入力ソースを"OBS Virtual Camera"に変更してください。
これによって画像入力コンポーネントにOBS仮想カメラを入力することができます。

ペイントソフトをキャプチャする方法に関しては後述

### OBS側の設定

OBSのインストールがまだな方は`https://obsproject.com/ja/download`にアクセスからインストーラをダウンロードし、インストールしてください。

OBSを起動し、ソースからペイントソフトをキャプチャしてから「仮想カメラ開始」ボタンを押すことでペイントソフトをキャプチャした内容を入力することができます。

![image](https://github.com/nat-chan/comfyui-capture-inference/assets/18454066/bc276d56-efdf-442d-90e9-fdf0e1ce5d46)