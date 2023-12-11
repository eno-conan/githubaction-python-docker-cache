# Github Actionにキャッシュを適用する話
- 詳細は[こちらの記事](https://qiita.com/eno49conan/items/508bae516fa2ed089db9)で公開しています。

### 実装内容
FastAPIのコードに対して、以下workflowを作成
  - Linterツール（[ruff](https://github.com/astral-sh/ruff)）によるチェック
  - アプリケーションテスト
  - DockerイメージのBuild、ECRへPush、Lambda関数の更新
### キャッシュ適用
workflowの実行時間短縮のために、キャッシュ利用
  - Python自体のインストール
  - Pythonライブラリのインストール
  - DockerイメージのBuild
