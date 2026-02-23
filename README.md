# FIVESCUP

S5Works が運営する CS2/VALORANT イベント「FIVESCUP」のサイトです。  
WordPress から GitHub Pages（Hugo）へ移行しました。

- **サイト**: https://fivescup.github.io/fivescup/
- **リポジトリ**: https://github.com/FIVESCUP/fivescup

## 開発

### 必要なもの

- [Hugo](https://gohugo.io/installation/)（extended 推奨）

### ローカルでプレビュー

```bash
hugo server
```

ブラウザで http://localhost:1313 を開きます。

### ビルド

```bash
hugo --minify
```

生成された静的ファイルは `public/` に出力されます。

## GitHub Pages の設定

1. リポジトリの **Settings** → **Pages**
2. **Build and deployment** の **Source** で **GitHub Actions** を選択

`master` ブランチへ push（またはマージ）すると、GitHub Actions が Hugo をビルドし、GitHub Pages にデプロイします。

## ディレクトリ構成

- `content/` - 固定ページ（`pages/`）と投稿（`posts/`）の Markdown
- `layouts/` - Hugo テンプレート
- `static/` - 静的ファイル（画像など）
- `hugo.toml` - Hugo 設定
- `docs/` - コンテンツ一覧・マッピング（`content-map.json`）
- `output/` - WordPress エクスポートから生成した Markdown（参照用・Phase 8 で削除予定）
- `waybackmachine/` - Wayback Machine 取得データ（参照用・Phase 8 で削除予定）

## PR の出し方（移行時）

- 初回コミット（`master`）はエクスポートデータのみ。
- サイト構成は `feature/gh-pages-site` ブランチで実施。このブランチを push し、**Pull Request** を `master` 向けに作成。
- マージ後、**Settings → Pages → Source** で **GitHub Actions** を選択すると、次回の push から自動でビルド・デプロイされます。
- `master` が更新された場合は `git fetch origin master && git rebase origin/master` で追従。`master` への force-push は行わないこと。

## 移行について

- 元データ: `s5worksfivescup.WordPress.2026-02-23.xml` を wordpress-export-to-markdown で `output/` に展開
- 不足分は wayback-machine-downloader で取得した HTML を `waybackmachine/old`, `waybackmachine/new` に保存
- 初回コミットで上記エクスポートをそのまま保存し、その上に Hugo サイト構成とコンテンツ統合を追加

## ライセンス

コンテンツの利用については S5Works / FIVESCUP にご確認ください。
