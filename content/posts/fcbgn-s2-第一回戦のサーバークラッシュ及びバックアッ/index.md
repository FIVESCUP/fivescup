---
title: "FCBGN S2 第一回戦で発生したトラブルについて"
slug: "fcbgn-s2-第一回戦のサーバークラッシュ及びバックアッ"
date: 2017-10-09
categories:
  - "news"
tags:
  - "event"
---

[FIVESCUP BEGINNING Season2](../../)の第一回戦 “Astonish Gaming Integral” VS “MISO”

第4ラウンド途中に”override caster”機能の暴走によるサーバークラッシュが発生し、

その後の全試合に30分近いタイムロスが発生しました。

参照動画:[[CS:GO] FIVESCUP BEGINNING Season2 初戦~第２回戦](https://www.youtube.com/watch?v=Yr8Yl7TB5_0)

40:35~ 第4ラウンドクラッシュ

1:02:02~ 第6ラウンド 再度クラッシュ

1:17:08~ 復旧

AstonishGamingIntegralの選手の皆様,MISOの選手の皆様,視聴者の皆様にお詫び申し上げます。

大変申し訳ありませんでした。

 

クラッシュ発生時のDEMO・復旧後の試合DEMOはアーカイブ参照のため、当サイトではリンクを掲載しておりません。

実際に使用したバックアップファイル (backup_round05.txt) はアーカイブ参照。

 

 

(埋め込み)

 

上記不具合は、本大会にて初めて使用する”override caster”機能の不具合による物と判断しており、

試合再開後本機能を無効化し、”backup round”機能によるラウンドの復元を行い試合を再開しました。

本不具合により皆様に多大なご迷惑をお掛けした事をお詫びします。

 

(2017/10/09 19:17 追記)demoを確認した所、本来のバックアップより2ラウンド先のファイルが読み込まれていました。

これにより、2回目のクラッシュが発生したラウンド(第6ラウンド)をテロリスト側(MISO)が取得した扱いとなり、

その次のラウンド(第7ラウンド)はバックアップの影響によりCT側(ANG)が取得した事になり、

この影響により両チームのマネーが増加し、スコアボード上の試合スコアも僅かに増加する結果となりました。

運営チームの度重なるミスにより選手の皆様に多大な迷惑をお掛けした事を深くお詫び申し上げます。

 

 

		
## サーバークラッシュの原因

上に記した通り、日本国内では初めて使用される”override caster”という機能の暴走だと判断しています。

本機能は”interactive caster”という第一カメラマンが行った操作を上書きし、

より優れたカメラワークを提供するシステムです。

 

このシステム提供に伴い、通常なら1つしか存在しない

“GOTVインスタンス”を同時に二つ起動しており、これが暴走の原因になったと判断しています。

復旧後は”override caster”を無効化しキャスター１人カメラ操作をしていた為、

見にくい視点になってしまった事が多々ありました。大変申し訳ありませんでした。

今後運営チームにてより詳しい原因の究明と解決方法の模索を行い、

より優れたカメラワークを提供するように努力して参ります。

 

 

## BACKUP ROUNDとは？

今回のトラブルより復旧する際に使用した機能の解説です。

本機能はサーバークラッシュ等の試合中にトラブルが発生した際に使用されるCS:GO標準の機能です。

csgoフォルダにbackup_roundXX.txtというファイルを作成し、以下の情報を自動的に保存するシステムです。

 

- 現在の獲得ラウンド数,連取ラウンド数

- ゲーム中ユーザーのID

- 獲得したキル数,デス数,アシスト数,HS数,MVP数

- プレイヤー全員の武器,ベスト,投げ物等の装備品情報

- プレイヤーが所持して居るマネー情報

 

この機能は主にメジャー大会やオフライン大会でのトラブル発生時に使用されています。

参照動画:[EliGE TK’S 2 of TeamLiquid CSGO ESL Cologne 2016 Full Round 29](https://www.youtube.com/watch?time_continue=96&v=U-LyvuyyVPA)

(埋め込み)

 

運営チームは障害が発生した5ラウンド目のバックアップファイルを別サーバーへアップロードし、

ファイルを遠隔操作でロードする事で上記情報の読み出し・復元を行いました。

復元を行った際に実行したコマンドは以下の通りです。

sm_rcon sm plugins unload lo3_matchplugin.smx //マッチ管理プラグインの強制アンロード

sm_rcon mp_backup_restore_load_file backup_round05.txt //クラッシュ直前の第5ラウンドの状態まで復元

sm_rcon mp_t_default_primary “”;//マッチプラグインの影響により初期武器がAK47だった為修正

sm_rcon mp_ct_default_primary “”; //マッチプラグインの影響により初期武器がM4A4だった為修正

sm_say ready? //選手にポーズの解除確認

sm_rcon mp_match_unpause //ポーズ解除実行

 

実際に使用したバックアップファイル (backup_round05.txt) はアーカイブ参照。

 

今後運営チームでより詳しい原因の究明,トラブルの対処能力の向上,選手の皆様が快適にプレイ出来る環境づくりを進めて参ります。

この度は大変申し訳ありませんでした。

      
	        
      
      
      
	        
        

	  
	  

      

      
	        
            
      

      

	  
	        
	  
	    
	      		  ![ FlowingSPDG ]
		  	        

	      
	  	    	      
  
	    
	    
	      Author：FlowingSPDG            投稿一覧
          
	      OWNER          配信・技術周り Project GIARS dev
	    
	  
      
	  	  

	  
	        
	  関連する記事	      
	        
					      ![ FIVESCUP BEGINNING SEASON6 ]
			  		    	        
	        
	          [FIVESCUP BEGINNING SEASON6](../fivescup-beginning-season6/)
	                        2020.05.05
              	        
	        2020年5月24日に**FIVESCUP BEGINNING SEASON6 **を開催します。[…]

	      
	  		      
	        
			              ![ NO IMAGE ]
			  		
		    	        
	        
	          [FIVES CUP BEGINNING Season3 概要](../fives-cup-beginning-season3-概要/)
	                        2017.10.26
              	        
	        目次 0.0.1. —この大会は終了しました。—1. 概要2. 参加資格3. 試合形式4. MAP VETO5. 使用マップ6[…]

	      
	  		      
	        <a class="related__imgLink" href="../fives-cup-xxxx-参加フォーラム/in