# Flaskでの静的ファイルの配信の挙動を確認する

## デフォルトのstatic

`app`を定義しているモジュールの隣に`static`というディレクトリを作り、その中に`xxx`というファイルを入れとくと、`/static/xxx`というURLでアクセスできる。

## 任意のフォルダをルートとしてアクセスしたい

```python
from pathlib import Path

PUBLIC_DIR = Path(os.getcwd()) / "public"

@app.route('/<path:path>')
def download_file(path: str) -> Response:
    items = path.split("/")  # todo: 雑実装
    d = "/".join(items[:-1])
    f = items[-1]
    return send_from_directory(PUBLIC_DIR / d, f)
```

上のようなrouteを定義しておけば、

http://localhost:20091/a/b/c.txt で `public/a/b/c.txt`にアクセスできる。

## デフォルトのstaticの場所を変えたい

`app`のプロパティ`static_folder`の値を変えておけば良い
