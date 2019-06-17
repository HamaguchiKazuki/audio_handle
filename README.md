# audio_handle
音声初学用

## pyaudio 入れるためのチェックシート
- [ ] ``` sudo apt install libasound2 ``` のインストール終わってる？
- [ ] http://www.portaudio.com/download.html でPortAudioのソースコードをダウンロードする。
- [ ] tarファイルなので解凍してディレクトリ内に移動し``` ./configure && make ```
- [ ] ``` sudo make install ```してPortAudioをインストール
- [ ] ``` pip install pyaudio ```でエラーが出ないかを確認