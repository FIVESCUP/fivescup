<!DOCTYPE html><!--[if IE 8]>
		<html xmlns="http://www.w3.org/1999/xhtml" class="ie8" lang="ja">
	<![endif]--><!--[if !(IE 8) ]><!--><html xmlns="http://www.w3.org/1999/xhtml" lang="ja"><!--<![endif]--><head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>ログイン ‹ S5Projects | FIVESCUP — WordPress</title>
	<link rel="stylesheet" id="dashicons-css" href="wp-includes/css/dashicons.min.css" type="text/css" media="all">
<link rel="stylesheet" id="buttons-css" href="wp-includes/css/buttons.min.css" type="text/css" media="all">
<link rel="stylesheet" id="forms-css" href="wp-admin/css/forms.min.css" type="text/css" media="all">
<link rel="stylesheet" id="l10n-css" href="wp-admin/css/l10n.min.css" type="text/css" media="all">
<link rel="stylesheet" id="login-css" href="wp-admin/css/login.min.css" type="text/css" media="all">
	<meta name="robots" content="noindex,noarchive">
	<meta name="referrer" content="strict-origin-when-cross-origin">
		<meta name="viewport" content="width=device-width">
	<link rel="icon" href="wp-content/uploads/2020/04/cropped-fivescup_logo-1-32x32.png" sizes="32x32">
<link rel="icon" href="wp-content/uploads/2020/04/cropped-fivescup_logo-1-192x192.png" sizes="192x192">
<link rel="apple-touch-icon-precomposed" href="wp-content/uploads/2020/04/cropped-fivescup_logo-1-180x180.png">
<meta name="msapplication-TileImage" content="http://fivescup.jp/wp-content/uploads/2020/04/cropped-fivescup_logo-1-270x270.png">
	</head>
	<body class="login no-js login-action-login wp-core-ui  locale-ja">
	<script type="text/javascript">
		document.body.className = document.body.className.replace('no-js','js');
	</script>
		<div id="login">
		<h1><a href="https://ja.wordpress.org/">Powered by WordPress</a></h1>
	
		<form name="loginform" id="loginform" action="wp-login.php" method="post">
			<p>
				<label for="user_login">ユーザー名またはメールアドレス</label>
				<input type="text" name="log" id="user_login" class="input" value="" size="20" autocapitalize="off">
			</p>

			<div class="user-pass-wrap">
				<label for="user_pass">パスワード</label>
				<div class="wp-pwd">
					<input type="password" name="pwd" id="user_pass" class="input password-input" value="" size="20">
					<button type="button" class="button button-secondary wp-hide-pw hide-if-no-js" data-toggle="0" aria-label="パスワードを表示">
						<span class="dashicons dashicons-visibility" aria-hidden="true"></span>
					</button>
				</div>
			</div>
						<p class="forgetmenot"><input name="rememberme" type="checkbox" id="rememberme" value="forever"> <label for="rememberme">ログイン状態を保存する</label></p>
			<p class="submit">
				<input type="submit" name="wp-submit" id="wp-submit" class="button button-primary button-large" value="ログイン">
									<input type="hidden" name="redirect_to" value="https://fivescup.jp/wp-admin/">
									<input type="hidden" name="testcookie" value="1">
			</p>
		</form>

					<p id="nav">
									<a href="wp-login.php">パスワードをお忘れですか ?</a>
								</p>
					<script type="text/javascript">
			function wp_attempt_focus() {setTimeout( function() {try {d = document.getElementById( "user_login" );d.focus(); d.select();} catch( er ) {}}, 200);}
wp_attempt_focus();
if ( typeof wpOnload === 'function' ) { wpOnload() }		</script>
				<p id="backtoblog"><a href="index.html">
		← S5Projects | FIVESCUP に戻る		</a></p>
			</div>
	<script type="text/javascript" src="wp-includes/js/jquery/jquery.js"></script>
<script type="text/javascript" src="wp-includes/js/jquery/jquery-migrate.min.js"></script>
<script type="text/javascript">
/* <![CDATA[ */
var _zxcvbnSettings = {"src":"https:\/\/fivescup.jp\/wp-includes\/js\/zxcvbn.min.js"};
/* ]]> */
</script>
<script type="text/javascript" src="wp-includes/js/zxcvbn-async.min.js"></script>
<script type="text/javascript">
/* <![CDATA[ */
var pwsL10n = {"unknown":"\u30d1\u30b9\u30ef\u30fc\u30c9\u5f37\u5ea6\u4e0d\u660e","short":"\u975e\u5e38\u306b\u8106\u5f31","bad":"\u8106\u5f31","good":"\u666e\u901a","strong":"\u5f37\u529b","mismatch":"\u4e0d\u4e00\u81f4"};
/* ]]> */
</script>
<script type="text/javascript" src="wp-admin/js/password-strength-meter.min.js"></script>
<script type="text/javascript" src="wp-includes/js/underscore.min.js"></script>
<script type="text/javascript">
/* <![CDATA[ */
var _wpUtilSettings = {"ajax":{"url":"\/wp-admin\/admin-ajax.php"}};
/* ]]> */
</script>
<script type="text/javascript" src="wp-includes/js/wp-util.min.js"></script>
<script type="text/javascript">
/* <![CDATA[ */
var userProfileL10n = {"warn":"\u65b0\u3057\u3044\u30d1\u30b9\u30ef\u30fc\u30c9\u306f\u3001\u4fdd\u5b58\u3055\u308c\u3066\u3044\u307e\u305b\u3093\u3002","warnWeak":"\u8106\u5f31\u306a\u30d1\u30b9\u30ef\u30fc\u30c9\u306e\u4f7f\u7528\u3092\u78ba\u8a8d","show":"\u8868\u793a","hide":"\u975e\u8868\u793a","cancel":"\u30ad\u30e3\u30f3\u30bb\u30eb","ariaShow":"\u30d1\u30b9\u30ef\u30fc\u30c9\u3092\u8868\u793a","ariaHide":"\u30d1\u30b9\u30ef\u30fc\u30c9\u3092\u96a0\u3059"};
/* ]]> */
</script>
<script type="text/javascript" src="wp-admin/js/user-profile.min.js"></script>
	<div class="clear"></div>
	
	
	</body></html>