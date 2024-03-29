from logic import Logic
from menu import UX

# import modułów 

def main():
    char_set = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    scale_factor = 0.5
    one_char_width = 10
    one_char_height = 18
    font_path = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
    font_size = 15

    menu = UX(char_set, scale_factor, one_char_width, one_char_height, font_path, font_size)
    menu.root.mainloop()

# wywołanie programu
if __name__ == "__main__":
    main()



# ''''''''''''''''''''''''''''''''`'`'```^,"``''''''`'''''''`'''''''''`''`'''''''''''''''```'''''''''''''''''''''''''''''''''''''
# '''''''''''''''''''''''''''''''''''``'''''`'`?``'`'''''''''''''''''''''''''`''''''''''''```''''''''''''''''''''''''''''''''''''
# '''''''''''''''''''''''''''''''''''''''`''`''>^'`'`:.'''''''''''''''''''''''''''''''''''``'''''''''''''''''''''''''''''''''''''
# ''''''''''''''''''''''''''''''''''''''''''` 'I,,(+!^^`'"';`'''''`''''''''^I`'''''''''''''`'''''''''''''''''''''''''''''''''''''
# ''''''''''''''''''''''''''''''''''''''''',,i.:lf+I?];:t^>i`~`''.;.'`''''<f:+i.'''''''''''''''''''''''''''''''''''''''''''''''''
# ''''''''''''''''''''''''''''''''''''''''^il^:!,:ii!+{{}-i|:I''>:'''`''`r"'i?];'';'`''''''''`'''''''''''''''''''''''''''''''''''
# ''''''''''''''''''''''''''''''''''''''; <^;! ^i,i^?zvv{{crY_+Xi"`''''^I'If~~]<``n-?.`'''``.^`''''''''''''''''''''''''''''''''''
# '''''''''''''''''''''''''''''''''''''',..'`^ ,l;nzvUn)cmm0LxU0\?^'^''_`j?mfj}I`zpC)l^^'^I,I"^``''''''''''''''''''''''''''''''''
# ''''''''''''''''''''''''''''''''''''+<`.`<":^+)fzvJLOUZdQwCw0nLn[-II_+u1CtmZt>]U00O/_}l(~l!n1I`'`''''''''''''''''''''''''''''''
# ''''''''''''''''''''''''''''''''''''>:^^',<>>xfrLCQ0QOpwhhhpUparjU+--cOm*QdUxjXkdqq0zzY/r)_^<"]`'''''''''''''''''''''''''''''''
# '''''''''''''''''''''''''''''''''''':''!`.>i~tzYOOQqddpkhohOk#od*#LuZ#ao*bdkYLapkphhmw1f/f\;.'`>'''''''''''''''''''''''''''''''
# '''''''''''''''''''''''''''''''''``;`~.i;;~[iXcLCQ0QObhhaa*o*ahMWhmpp0#*okahhhoohakoakQ\]/vi'`'_`''''''''''''''''''''''''''''''
# '''''''''''''''''''''''''''''''''''"`,^:"i~/nQYCJ0mpqhhkooa##W*&&8haW&MM#MMWMoo**booahpOUxuj,.^``''''''''''''''''''''''''''''''
# '''''''''''''''''''''''''''''''''''`:-:..I_tfLUQOCmphaoo**#WM&&&8WW&WW&#M&&WWMW#o*ohhdbwQCrc?l]'l''''''''''''''''''''''''''''''
# '''''''''''''''''''''''''''''''''''^'`:l>-(tvX0O00wdahaoM*W&&8&M&8&&&&&W&&&&&&WM#W#*hbbpw0cc|>>^^''''''''''''''''''''''''''''''
# ''''''''''''''''''''''''''''''''''''`'"^li(uuOQwJ0dqhkh#*o&WW8&8&88&&W8&8&8W&W&WM#M*okhkp0cU\:i+'''''''''''''''''''''''''''''''
# ''''''''''''''''''''''''''''''''''''`I' ;_>fYCZwZQwhaaoW#*MWW&&&W#&&8M&&&&W&WWWW##*#*hhkqcLC\^]l,`'''''''''''''''''''''''''''''
# '''''''''''''''''''''''''''''''''''''^^I<i[czCmhmpqaao#o##*&WW&&&W&WWWW&WW&&&W#M#M#*okhapUOQ}?I}`''''''''''''''''''''''''''''''
# ''''''''''''''''''''''''''''''''''''.:'^;~rU0QZOqmOpbh*M*##MWWWW8&8&MWW8&&8&WWMM#**oh*omQQLc]:'`^``,,lI"^`'`'''''''''''''''''''
# '''''''''''''''''''''''''''''''''``'``;:!~vC0OmmQOmbkh**#*#WM8W&&&88WWM&8W&&8&WWM#*#*adqQJUY<i;!`"l>-?+i~!!:"''''''''''''''''''
# '''''''''''''''''''''''''''''''.~YwO.I<Ili1Orm0ZO0mwhahZdbpooWW&WMWW&8&&&8W&WWWW#aMW*odbwUzc}>Ii',i-}1?-_>>I"''''''''''''''''''
# '''''''''''''''''''''''''''''''`dh?k#O}]:+<Y0wwpwqLwJmC0zxm<)1rJwq*MM&W&W#M#WWWM#oMoohkqOLJL[^^''`"I>!iII::^`''''''''''''''''''
# '''''''''''''''''''''''''''''''fk*z(doa';.~1`\qp0ux1uY[zo*q?cUf(YZo*M&WWMhd0L\r{vX0LJYmpuCQn?'^''`'```'''''''''''''''''''''''''
# '''''''''''''''''''''''''''''''Ophw#[wb:`I0J0mY~`U%uw0CY/){{[zcC1"dh#&&W#kpbphz_~[?];^?JCUJJ_}mu''```''''''''''''''''''''''''''
# '''''''''''''''''''''''''''''''{djbkwXJ:I[CJQZhkdwxYjfuj?^+*MaqvOp1:O_&qiYb)YUQnzYjwdpt[vzcJkdk^.'````'''''''''''''''''''''''''
# '''''''''''''''''''''''''''''''`on#*o]Lt]nXJOpkkhhqOXzzvOOwmm0UJQYZCw#M*b?|ch-`i_#Z:|ZJ/zzI1}xa}'''''''''''''''''''''''''''''''
# ''''''''''''''''''''''''''''''''kvMMZwp|{\xYCwpdhkm0mm00mO00ZUZqQmf`k*MMd|^UzZ_[oo0JjYJwOXnUzoo`'''''''''''''''''''''''''''''''
# '''''''''''''''''''''''''''''''.0dhm|aC|]rncO0khkrhmkdmbkbbkbpwdpwX{dM#WaJ:wOUQO0OQz0UdqwY|.*hd'`''''''''''''''''''''''''''''''
# '''''''''''''''''''''''''''''''.,b#zakL)t|jjcOppddldhahddhkkdo#hqqbwqaaohOfwbbbwpmmZpdmwm<p&ph^''''`'''''''''''''''''''''''''''
# ''''''''''''''''''''''''''''''''.{hvk#o)|xjtn0dkdphlmbaaaooo**kv"0Qwao#MomX<hokdphhkdpOOwjLahx'''''''''''''''''''''''''''''''''
# '''''''''''''''''''''''''''''''''`cCk*q?fjr/nYpphhkhhp_cbakpU}WpccYOb*M**pCo*{aohhokkdb|XxkLb.`'''`''''''''''''''''''''''''''''
# `'''''''''''''''''''''''''''''''''.Xbb#)tfr/fxZmaahOkk#MaWMWWMU0mJQmao**akwZW&#MI,uc(!oaXnkac''''''''''''''''''''''''''''''''''
# '''''''''''''''''''''''''''''''''''''..^)ctntcLqdhoph*o*WWWMMWJmOmZka&%%*hpLd&WMWdkhdokOuoqL.''''''''''''''''''''''''''''''''''
# "`'''''''''''''''''''''''''''''''''''.]`]fvv(nzOdddkoo#W#WWMWWoQdY-Cha**aqpcMWWWMMahhqL0fkC`''`'``'''''''''''''''''''''''''''''
# "`''''''''''''''''''''''''''''''''''`Q8~ |cuxucL0wwa*oM#MMMM**aJ-[))zdx]YkbMWW&8Mo*obq0(b!''`````'`''''``'`''''''''''''''''''''
# ^``''''''''''''''''''''''''''''''''.Y8%O'(rntvuUZaodaoWMk*bOCr1I>!n~dr1>)1L**#WMWModdZc''''''''`'`'''''``''''''''''''''''''''''
# `''''''''''''''''''''''''''''''''''vW%W[?'1xfrcUL0haM*Qb1Y?\^<+xzCv[v))??!~/da**#oqkZU~'`''````````''`'```'''''''''''''''''''''
# '''''''''''''''''''''''''''''''''.z*8%o}}'}\jruLfLb#kmCOl-+jcUdoa0Qdhakaw-]?)zz#ohobJf'''''`'````'`'''```'``'''''''''''''''''''
# '''''''''''''''''''''''''''''''`IJ#88BY(-]I\ttvY0wmUkOMrnqZXzjQYz?|vnrJvmhx1/|0dk*wCv''``''`''''''`'''`'``'''''''''''''''''''''
# ''''''''''''''''''''''''''''''+/QMo8%%k?)<?^jxjtczr\cumf+UOdw?fLO00QJYLxYcvOc}{~0dvv@\","""`''``''`'''````'`'''''''''''''''''''
# ''''''''''''''''''''''''''''[zwYo#88BBWt?]1?'j\fUC(\xu/(hokhapmwmwmmmQOwOwZwm!Q(z<rBBW~I,:,^`'''`''''`````'``''''''''''''''''''
# '''''''''''''''''''''''''',q*owooW8%%BW/1{<[('f)zY~1~i/YdobhaakkYjctcZokdppdLr0r)'%BB%#,I;^`'`''`''''`'``````''''''''''''''''''
# '''''''''''''''''''''''`'!dM##op*W8%B%8M1_![x_11))'"["{<~Xnp*oabkX/cwCaabddff(}+:}%B%%%t:"``'`'''''''''''`'''`'''''''''''''''''
# '''''''''''''''''''''..liM88&Mb#&8%%BB%W|11\<n-,'_>:++>+rnt/hUkd0pdO#*dhhc\_>l`[1&%BBB%&+`"'`'``''''''`'````'''''''''''''''''''
# '''''''''''''`'''.?{}}[:aMW&*oo&88%BBB8&->)<+|f}/.`"^li]+;:jxMLbkMukpZmcZUi]'`:rU&%%@B%%8^^,"^``````'``''`''`''''''''''''''''''
# ''''''''''''`^?[}?[][1tpM88&&M#W88%BBB%&()r+I>i{ff+^^I^^\!?>?|tfYYCU/0\in~:`~]1(L8%BBB%%8{I:,"^,^,^"`'''``''''''''''''''''''''`
# `''''`'`??[1})n/((\|\/QMW888WW&&8BBB%B%8J)i)-/iiI<}}>'^l;':l_]_-[<]]I]?II._"(jj|C%%BBB@%%8>+II,i>Il:^``'''```'''''''''''''''''`
# \|1|fjt(\f())))\)|\/rz*88888888%8%BBBB%8h/<+j<+{ili<:._^^I'__I`>,-""!~I\^i{(tf/\z%%BBBBB%BaoJu{<iil:"`'`''''''''''''''''''''''`
# //f/\ttf||||(\\|t\frIM&88%888888B%BBBB%&#l-<-{~){\~[i_!>!i`~'!I.l:^^>:+I-_)r\)f]x8%BB@BBB%%M&bvtjf(I;,^`''''''''''''''''''''''`
# \tf/\//t/\/\/|\|tft_*&888888%8%8%B%%BBB%&?(>:~!1-)/!);}I}<l!<!ii!+,:+[}f/t1|[{~>>&%@BBBB%BBWM&Waunf\/j+'`''''''''''''''''''''``
# tjt/\/\/||///\||t//h888%8%%%8%8%%BBBBB%8&l?>}];;>i}[)|n|{[I+][);),i1t]\t[)+11-{)>M%BBBBB%%%BoM8%kcrfrtjr\f)}'`'''''''''''''''``
# tjtjtf\/t/((/fft\jbW8%8%%8%%888%BBBB%%B%8(?{;i>1I;^_t)[(]?][?}(f{[>|-|}1|:)))}(/[M%%B%%BBB%B8oM&&kJjxxfxrfjjr\<''''''''''''''``
# fttjftrtt//t(//t/UW88%888%8%%%%B%B%B@%B%&ll)!!(xII]+-\1v  `+>:<^("^I]1>[>)[x|{|{+#8%BBBBB%%B%boWW8&Qvcvznxxrx/xf/>'.''''''''''`
# fjjxj/trfttt\rfrbW8%88%8%8%%%%B@B@@BBBBB&x]!;;ll,;~?],>!fr(?~[[])'11l[[[?r?{}]~?iM%@@BBBBB%BBMpaMW88pvrvxrrrxjjrjnt>'''''''''''
# jjrjfftfrfjtt//w8888%88%%B%%BBBBBBBBBBB%8Xr<!l/[>?||}{+_/<!+f|[)f-?(?>)1)t|[t)I--d%BBBBBBBBB@%obkMW88aUucvrjxfvjrjxf/.'''''''''
# jrfjjjtfjtjtjth8M8888%%%%%BBBBBBB@%B@B%%8ju|+~|?{}ru/uu\nffu}[[)+?|~/xf]!r[1-~[<]Q%%BBBB%%%%B@8M*b#W8%#vrxnnnrnrnjrjn\'''''''''
# frxjxnff/f/jftQ8%%%8%%%88%B%BBBBB@BBBBBB&v-|)+\_<"|r~rr~>1I>|}1{f([(>I}1rjf1_i|\?O8BBB@B%%%BBB%8&Ma#M&%&Qrxnrr\frftrnr)''''''''
# rjrtfjtttfttrf&%88%%8%%8%BBBB%BB@@BBBBBB8utC/}l<-1)[^}+,+i~(--<]}}1!{fu/(+~)fr-}\U8%BBBB%@BBBBB8%8M*#&88%krrrxuxtrftjjf`'''''''
# tjfjjtjftftj\x%B%%%88%%%%BBBBB@BBB@@BBB%8b+tnnj\rf>+->+{/tufrutnu-_j[-}{rjx-<<r}jf8B%B@BBBB%BBB%%88W##W88%dxrxxxrj\ntfj(.''''''
# trtftrj/jfrxfzW%%%8%%B%%%%BBBBB%B@@@B%%B%&|"".j)v/ccXfuv}uxt/<l+}iI;]|(/{+</?f}|]i&B%@BBBB%%%%@%W%%8&##&88%hvtjrrjnx/jr\`''''''
# nfrrfjxttnjtncWB%88%88%BBBBBBB@B@@@BBBB%%Wrrt1+~IIli</ti.+[(l:]/[|c(r|\![uv?tf1]fI&%B@BBBB8%%@BB%%888WMW&&8%ovrjnjrjjftr;''''''
# frjt/fnrfjtxffW%%%888%@%BB@@B@@B@B@@@BBB%8>[-)?[uj)ff':~rt1\{zu~t/)j[]lf[!(x~i+f_:W%BB@B%%%%%BBBB%%88&&WMWW8&wjrnxnrtt/n|''''''
# tjtrrjnjjrjrjxdB%8%8%%BBB@BBB@@@@@B@B@@@B8t]-{f/_izj{Yuj-nf[|i:+~)\}fvY}1xn>zn)_tiW%BB@@B%%%%BBBBW8%8%8&&&888%Jnuuuunjtjt.'''''
# rjrtnnrrjffrf|k%8&88%BBBB@B@@@B@@@@@@B@@%8~)fj^' :{1{>l"i[<[,~Xtut>t:^-rx^i/}_(f+;WBBB@BB%%%%%BBB%%%%B%8888888avrrcjjtjnj''''''
# xxjftrunxrxjnj#%%888%%BBBB@@BB@@@@@@@@BBB%I>i{ujnt]nu+<)Uzf[ru)~?,?-jrfinuf}(fv~\lWBB@@BBBBBB%B@B%M888%88888888wcnuxttt/r:.''''
# ujrr/\rjrxnxj)w8888%B%B@B@B@@@@@B@@$@B@@BBz)[[\[|>\||XX-^}]||/r[]Ixf?|</);-ft1I[f{&%B@@BBB%%%BBBBB8888888&88888*cvuvu/t\j<l''''
# nunf//jjxnnxr/o%%%88BBB@B@B@@@@@B@@B@@@@BBwctxI-+!?<[.`)Ynf1zf|_?+\1Jft{t(ui!~jf(!8%B@@BB%B%%B%B@B%%8%%%88888&88Lvuxnnrfx?+"'''
# uujt/tfjrxnrjr888&8%BBB@BBBB@@@B@BB@@@@BBBLUx]Xvxx_|vYY1.+>|[xr|~!]-fc/\_{~jzv|]r}&B@@@BBB%B%%%BBB@M%%%%%8888&&%8Ynuvr\rf{+i"''
# nrn////jrrrxrjbo%88%@BB@@@@@BB@@@@@@@@B@BBhJYt.' ;z{_i"+Yx|}Uft)/|fu?{?f)'<i]it|!]&@B@@BBB%B%%%BBBB%8%%%B888&&&8&Oxvurrtj[<-i^'
# curt/t\ffncrnuW&&88%%BBB@@@@@@@@@@@@@@@BBBWYnvcuf)!-v|z(!)[f\cf/}/[)1(x-)Ynnn|[[f}8BB@@BBBBB%B%BB@BB%8%88888&&8&8qrnnrr|f[[-+I'
# uxr/f||furnnvtk%88%@%@@@@@@@@$@@@B@B@@@@BB8Lvzc>lvUz1(^_Jxx[\)?]?!}?]t1}Il"-t|jj?>8BBB@@@B%B%%%B@@BBM%88%8%88&&W88zxvnrjt[[[}_'
# uuxf|\fjrxnru|a8%%%%B@BB@@B@B@@B@B%@@BBBB%&zzzj|[I;I>-i<-i``.:'"!1Ou)f|u|+|i:"?1\I%@BB@BB%%BB%%%BBBB%%%%8888%WM&8%rjuurr/(-(11'
# xxj\(t\frvcuj(o%88%BBBB@@@@@@B@B@B@@dw0%#0&pvt))\|jz$zt$\}{1{}~1(//\&Ir1)0nUtt{\[>8B@@$@@%@B%%%B%@B@888888888&WW88%ucrr\){(}}{'
# {vx/\\|trrxru]#&8%BBBB@@@@@@@@@@@@@@*W%8&qBk|xrvU|p8@oYv\)]I{+?crfnnonCrt)+nrUcY}>%@@@BBB%%B%%8BB%B@@M%8888%8&&&&&8mvxxr??){}}'
# +}f/t\/jffnfvcp88BB@B@@@BB@@@BB@@@@@%8BB%hBMxtnunXdBBcwttx+I[}?vc\|qY]/t_!{+r/|r\l%B@@@BB%%%%%%%%B@BB&8%888888W&&88ovnrr(1{)[)`
# \{x\\\|tjtjrrJ%8%%BB@@@B@@@@@@@@@B@@@W%%%b@#Y/tjuUd@WQnt))l>+?+YQc)#{\?1}||_]i`{fl%@@@BBBB%BB%8BBBB@B%888&8%88W&W&&8crfx1{}{}{'
# _[]/|\\\jjfjjj&%%%BB@@@@@@@B@@@@@@@B@M&W8p8Bq)jfuXW@&mY(\{i!I!}u|rj*rrUf1tf];}<((UBB@@@B@%%%B%%BBB@%@%o%%8%8%88M&&&8mx/r11[)}[`
# ,/>t(|)/\ftfr}oB%%B@@@@@@@@@B@@@@B@@Baaa8m#Wj{/tzCW@WCYf{-i:^~i/(\}%uwfYJj|z-?)jrw%B@@@BBB@B%%%8%BBBBB88888888&8W&&8*vnr({(()?!
# l>~|||||/tftjj*%%BB@@@B@@@@@@@@@@@BBBaddWwuJ|fnrrwB@%Wfj-?>l,l>/|[)%I;,;|z/cfrvnjMB@@@@BBB%%B%%%%%BBB@%88%88888&W8&&8ztj))1){1-
# ,>!/|1)(\/\ft>*%BBBB@@@@@@@@B@@@@WUntxrYQdahhaoooohbdpZZYtiI:i]fv-Y*f[tt+vn/r|/UYW%@@@@BB@@%%%888BB%BB%W8888888&&&&&8*nf|}1][[[
# <??/))|\\(tf/r&BBBBB@@@@@@@@@B@8x}_tu00Od*MMMWW&WM*##*kobopoU\~vf)-*fr[jf?f|_[~{}8%@B@BBB%BBB%%@%%BB@@BM8%88%88&88&8&MJt/|1{?][
# i[>|((\/|)t\t~MBBBBB@@@@@@BB@Wj}fvvYCZOwkaWWWWMWWMWMWMa8&W*qujacr{Ob_<jnv~,t_}i+l&B@@$B@B%BB%888%%%BBB@&888%88888&&W&8wt\}[)({[
# <-\|)(/|)|\\)MW%B@@@@B@@@@B&(?(v0OZC0mwkahbbakdkqZwdkkhhkhknzbwfz]ZuzvYuu11\x|[i^%@B@BBB%B%%8%%B%%BBBB@8&%8%8%8888&888kt/?[[{_}
# +\)|||||1|)ffZ&%BB@@@@@@@@&)_{Yqdkkbqwqpqpd0([]O]zlxn1jOXXUnYoLffvQ])f~)juc~f11?-8@@@@@@%B%%888%BBBB@BBBW888%%8WB8&&888uf}1{[][
# l(|11/)(t\\(\^8MB@B@@@@@%t]t|zLk##M*hqwmq/{U(|!Cc~l?tnvn|(J}|\)!Uxk+;]+lU1v{<-{{d%@@@@B%BBBB%%%%B%%BB@B%#888%888888888WO/[[1?{]
# {t\1|1|\\\\\|"#8BB@@B@B&\}1)ncmh#WMWWWWW#XXvzcYuztjn}-cQn+[}n]{`/tqfnrt~-f}x<({|&B@@@@@BBB%88%8%BBBBB@B%o&%8%%888&8888Wbt))}+}1
# //t/))1\f\\/t^b&@8@@B%tu]|1\rC0kkhaoooddbqkhohhbhbdpwqdpOCurjZ/]UXk(nJu\"rJxn|?cM%@@@BB%%%%B%8%%BB%%B@%B8M8%888888&8888qf11}}]}
# /t|\|t\|))\\;'1/|?<fr\|1)1tjjXmbhoaookkpko*MM*o*o##WWMWMMoahh##MW*Mw|nrn-1\|uu)(8%@B@@@BBB88%88%8%%B@@B@%*88%888888%B&8WL}}]){}
# 'l:II\)/{,']-,[+<{xunf//f\tfjUpo*#**oaohoa***h**MMMW&&&&&WM*MW#M%@%WX<1\r(){?jn:8BB@@BBBB%%%8&8BB%BB@B@B%h888%88%88888&&C}}+{[1
# -][<i~?~i}-_ii/(jQXUvjuxxjrjn0ho#*##*obddm***ohh**MMMMWW&Mo*hobo**ohY[u((n_11jn08@@@@B@BB%%%8&88BB@B@BB@B*&8888888%8888%C11~[}|
# ??~<+~?>(,~"l{_)rCJUrruxccxvYUho*#opkqmw0ZZwhbaokaabbhkdkd000mmObQv~|1]u1j_|[jta%B@@BBB%B%%B%88%%BB%BBB@BWW&%8%8&888%88&ot??}11
# ~>}l[>}:|l,l>((1vLmjjnrxYXY0UYq*#W&&&8&&&W8WWWWWW&WM*#*WohbhkmOQf(}^i+`}xrf\tn)#BB@@@@%BB8BB%%88%%B@B@BBBB#888888%88%888*x~}]1)
# {]<:)1>?i"!<_[+]JUULXzunJXzJCCYb###MWW&W&&&&&W&WMWM*a#o#abmqOJCi_l,[+.<ix|z{[\o8B@BB@@@BB%%88%88%%B%BBB@B%*8%88%%%%8888&Mu?}{1[
# !!"{!_?III!<}]1)/COULUUXzXYXYXcbMWWW&&W&&WWWWW*M###hwhaopL}:]t/_(}<[\?v-(\r+ff&%B@BBBBB%%%%B88888%%%B@@@%Ba&&8W88888%%88#\)?[{l
# il<i/{i->!"i}[]-1Xm00ZJUJCCYUcuYwbho*oaaoaadpqmmwOLCX0Zncx-1t1n|11\)fj}(t_\}fr&%BB@@@B@%%88%%%8&B%@B@@BBBB*8%&8&8888%8&88w[}1?`
# _?+;~[-?i;+l}__~iLmdmzQYUL0Q0Q0cXLdoa#MM#MWWWM#oa*hhzzvxnu(1tu)tU|n[1c])[f1+c(8BBB@@B@%B%B%%%%8%88BBBBBBBBW#&&&%888%888W8a[}-I'

# Bogusław Bagsik -  Właściciel i założyciel spółki Art-B.
