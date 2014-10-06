function goCR (o, l, p, t) {
	var u = o.href ; 
	tt_sub_disable(o) ; 
	var m = g_D>1 
		&& (u && u.indexOf("://")>=0 
		&& u.search(/^\w*: \/\/([^:/?]*\.|)*(?!(ad)?cr\.)[^.:/?]+\.+naver\.com(:\d*)?(\/|$)/)<0) ? 2 : o.ownerDocument==document 
		&& o.target 
		&& o.target!="_self" 
		&& o.target!="_parent" 
		&& o.target!="_top" ? 0 : 1;
	var cr = getCRRanking(p) ; 
	if (cr > 0) p = p + "&cr=" + cr ;  
	if (p.indexOf("u=javascript") >= 0) t = true ; 
	if (t) m = 0 ; 
	if (!(u && u.indexOf("http://cr.naver.com/")==0)) {
		if (0 && u && u.indexOf("/search.naver?") >= 0) { 
			var str = "" ; 
			if (0) u += "&crcp=1", str += urlencode("&crcp=1") ; 
			if (0) u += "&rule=1", str += urlencode("&rule=1") ; 
			if (0) u += "&debug=1", str += urlencode("&debug=1") ; 
			p = p.replace(/(((?: ^|&)u=).*\/search.naver%3F[^&]*)/, '$1' + str);
		}

		u = "http://cr.naver.com/"+(g_D ? "nr" : l)+"?m="+m+"&"+cpip()+"&"+nxGetCommonCRParam()+"&"+p ;
	}

	if (m && u) {
		var a = o.innerHTML ; 
		o.href = u ; 
		if (o.innerHTML != a) o.innerHTML = a ;
	}

	else if (document.images) (new Image()).src = u ; return true ;
}

function getCRRanking (p) {
	var cr = 0 ;
	if (typeof nx_cr_area_info != 'undefined') cr = getCRRankingByParam(p, nx_cr_area_info) ;
	if (cr) return cr ;
	if (typeof nx_cr_right_area_info != 'undefined') cr = getCRRankingByParam(p, nx_cr_right_area_info) ;
	return cr ;
}

function getCRRankingByParam (p, info) {
	if (typeof info == 'undefined' || info == null) return 0 ; 
	var cr = 0 ; 
	try { 
		var y, z ; 
		var y = p.split('&') ; 
		for (var i = 0; i < y.length; i++) { 
			if (z = y[i].split('=')) { 
				if (z[0] == 'a') { 
					for (var j = 0; j < info.length; j++) { 
						if (z[1].substr(0, info[j].n.length) == info[j].n) { 
							cr = info[j].r ; 
							break ;
						} 
					}
					break ;
				}
			}
		}
	}

	catch (e) {
	}

	return cr ;
}
