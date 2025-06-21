from flask import Flask

# インスタンスの生成
app = Flask(__name__)

# ルーティングの設定
@app.route('/')

# ルートURLにアクセスしたときの処理
def home():
    return "Welcome to Qiita!"

# ファイルが直接実行されたときの処理
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)